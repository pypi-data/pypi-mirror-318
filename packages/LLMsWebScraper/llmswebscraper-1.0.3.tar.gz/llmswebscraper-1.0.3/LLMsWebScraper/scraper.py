import requests
from bs4 import BeautifulSoup
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI, ChatOllama
from langchain_groq import ChatGroq
import json
import re
import logging
import os
from typing import Optional, Dict, Any, Literal
from markdownify import markdownify as md
from retrying import retry

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

ModelType = Literal["gemini", "openai", "groq", "ollama"]


class LLMsWebScraper:
    def __init__(
        self,
        api_key: str = "",
        model_type: ModelType = "gemini",
        model_name: str = "gemini-2.0-flash-exp",
        base_url: Optional[str] = None,
        temperature: float = 0.7,
    ):
        """Initialize the scraper with API key and model."""
        self.api_key = api_key
        self.model_type = model_type

        if not self.api_key and model_type != "ollama":
            raise ValueError(f"API key is not set for {model_type}.")

        if model_type == "gemini":
            self.model = ChatGoogleGenerativeAI(
                google_api_key=self.api_key,
                model=model_name,
                temperature=temperature,
                convert_system_message_to_human=True,
            )
        elif model_type == "openai":
            self.model = ChatOpenAI(
                api_key=self.api_key, model_name=model_name, temperature=temperature
            )
        elif model_type == "groq":
            self.model = ChatGroq(
                api_key=self.api_key, model_name=model_name, temperature=temperature
            )
        elif model_type == "ollama":
            self.model = ChatOllama(
                model=model_name,
                base_url=base_url or "http://localhost:11434",
                temperature=temperature,
            )
        elif model_type == "other":
            self.model = ChatOpenAI(
                base_url=base_url,
                api_key=self.api_key,
                model_name=model_name,
                temperature=temperature,
            )

        self.prompt_template = PromptTemplate(
            input_variables=["html", "instructions"],
            template="""
You are a data extraction expert. I will provide you with raw HTML content of a webpage, 
and you need to extract specific information based on my instructions.

HTML Content:
{html}

Extraction Instructions:
{instructions}

Please extract the information in a structured JSON format. No want any extra words or sentences. Only give json Code.
""",
        )

    def __fetch_webpage(self, url: str) -> str:
        """Fetch HTML content from a given URL, extracting metadata and body."""
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            logging.info("Webpage HTML content fetched successfully!")

            # Extract body content only
            soup = BeautifulSoup(response.text, "html.parser")

            TCIPatterns = {
                "nav",
                "menu",
                "navbar",
                "sidebar",
                "drawer",
                "breadcrumb",
                "side-nav",
                "sidenav",
                "header",
                "footer",
                "bottom-bar",
                "top-bar",
                "ad-",
                "ads-",
                "advertisement",
                "banner",
                "promo",
                "sponsored",
                "ads",
                "popup",
                "modal",
                "overlay",
                "dialog",
                "toast",
                "alert",
                "notification",
                "tracking",
                "analytics",
                "pixel",
                "beacon",
                "tag-manager",
                "disclaimer",
                "newsletter",
                "subscribe",
                "signup",
                "mailing-list",
                "search",
                "login",
                "register",
                "sign-in",
                "cookie",
                "gdpr",
                "consent",
                "privacy",
                "terms",
                "copyright",
                "hidden",
                "display-none",
                "invisible",
                "spacer",
                "gap",
                "background",
                "decoration",
                "ornament",
                "pattern",
                "gradient",
                "carousel",
                "slider",
                "lightbox",
                "tooltip",
                "dropdown",
                "skeleton",
                "placeholder",
                "loading",
                "shimmer",
                "spinner",
            }

            # Iterate in a while loop to handle tag decomposition correctly
            tags_to_remove = soup.find_all()
            while tags_to_remove:  # Keep looping as long as there are elements left
                tag = tags_to_remove.pop(
                    0
                )  # pop() so we only address one tag and keep the structure consistent

                if any(
                    pattern in soup.find_all().pop(0).get("class", [])
                    for pattern in TCIPatterns
                ):
                    tag.decompose()
                    continue  # Move to next tag

                if any(
                    pattern in soup.find_all().pop(0).get("id", "")
                    for pattern in TCIPatterns
                ):
                    tag.decompose()
                    continue  # Move to next tag

                if tag.name in TCIPatterns:
                    tag.decompose()
                    continue  # Move to next tag

            body = str(soup.find("body"))

            # Combine patterns to remove unwanted tags
            patterns = [
                r"<script.*?>[\s\S]*?</script>",
                r"<!--.*?-->",
                r"<style.*?>[\s\S]*?</style>",
                r"<meta.*?>",
                r"<link.*?>",
                r"<title.*?>[\s\S]*?</title>",
                r"<noscript.*?>[\s\S]*?</noscript>",
            ]
            combined_pattern = "|".join(patterns)
            body = re.sub(combined_pattern, "", body)

            extracted_content = f'<a href="{url}">This WebPage URL</a>{body}'

            # self.toFile(extracted_content, "output/webpage.html")
            return extracted_content
        except requests.RequestException as e:
            logging.error(f"Failed to fetch webpage: {e}")
            raise

    # Optimize the input data which is used on the model to generate the output. these input data are the html content and instructions.
    def __optimize_input_data(self, input_data: str) -> str:
        """Optimize input data for the model."""
        # Remove extra spaces and newlines
        input_data = re.sub(r"\s+", " ", input_data)
        input_data = input_data.strip()
        # convert html to markdown
        input_data = md(input_data)
        # self.toFile(input_data, "output/webpage.md")
        return input_data

    @retry(stop_max_attempt_number=3, wait_exponential_multiplier=1000)
    def __generate_output(self, input_data: str) -> str:
        """Generate content using the selected model with retry logic."""
        try:
            response = self.model.invoke(self.__optimize_input_data(input_data))
            # print(response.content)
            return response.content
        except Exception as e:
            logging.warning(
                f"Error during content generation with {self.model_type}: {e}"
            )
            raise

    def __extract_data(self, html_content: str, instructions: str) -> str:
        """Generate a structured response by passing HTML content and instructions to the language model."""
        formatted_prompt = self.prompt_template.format(
            html=html_content, instructions=instructions
        )
        return self.__generate_output(formatted_prompt)

    def __extract_json(self, md_code: str) -> Optional[Dict[str, Any]]:
        """Extract and parse JSON from markdown-style code."""
        match = re.search(r"```(?:[a-zA-Z]+)?\s*({[\s\S]*?})\s*```", md_code)
        # print(match)
        if match:
            try:
                return json.loads(match.group(1))
            except json.JSONDecodeError as e:
                logging.error(f"Failed to parse JSON: {e}")
                return None
        logging.error("No JSON code block found in the response.")
        return None

    def toJSON(self, url: str, instructions: str) -> Optional[Dict[str, Any]]:
        """Extract data from a given URL using provided instructions."""
        try:
            html_content = self.__fetch_webpage(url)
            extracted_md = self.__extract_data(html_content, instructions)
            return self.__extract_json(extracted_md)
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            return None

    def toFile(self, data: Dict[str, Any], file_path: str) -> None:
        """Save the extracted data to a JSON file."""
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
        logging.info(f"Data saved to {file_path}")
