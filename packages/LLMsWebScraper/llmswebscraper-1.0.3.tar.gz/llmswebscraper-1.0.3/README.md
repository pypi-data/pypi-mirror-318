# LLMs Web Scraper

**LLMs Web Scraper** is an innovative Python library designed to simplify the process of extracting structured data from web pages using a generative AI model. Traditional web scraping methods often rely on fixed selectors, which can become outdated or broken due to frequent updates on websites. This can lead to significant maintenance challenges for developers and data analysts.

To address this issue, LLMs Web Scraper leverages advanced AI capabilities to intelligently identify and extract relevant data, adapting to changes in web page structures without the need for constant manual adjustments. This dynamic approach not only saves time and effort but also enhances the reliability of data extraction processes. With LLMs Web Scraper, users can efficiently gather and utilize web data, ensuring that their projects remain up-to-date and functional in the face of evolving web content.

## **Key Features**

### **1\. Multi-Model Support**

* Use various language models for structured data extraction:
  * **Gemini (Google Generative AI)**: Powerful for extracting and analyzing large-scale content.
  * **OpenAI (ChatGPT)**: Supports models like GPT-4 and GPT-3.5 for natural language understanding.
  * **Groq**: Integrates Groq models for specialized data extraction tasks.
  * **Ollama**: Runs locally, suitable for privacy-focused use cases without relying on external APIs.

### **2\. Structured Data Extraction**

* Uses advanced language models to extract specific data from web pages based on user instructions.
* **Customizable Instructions**: Users can provide detailed prompts like:
  * Example 01:

    ```markdown
        Extract the relevant data from the following HTML and format it as a JSON object. 
        The data to extract includes the title (h1), the paragraphs (p), and the link (a) 
        with its URL and text.

        Example:
        {
            "title": "title",
            "paragraphs": [
                "This paragraph contains...",
                "second paragraph...",
            ],
            "link": {
                "url": "https://example.com/",
                "text": "More information..."
            }
        }
    ```
  * Example 02:

    ```markdown
        Extract the following information:
        1. Titles of all blog posts on the page.
        2. Author names for each blog post.
        3. Publication dates of each blog post.

        Please provide the extracted information in a structured JSON format.
        Expecting property name enclosed in double quotes and values in string format.
        Example:
        {
        "blog_posts": [
                {
                    "title": "Blog Post 1",
                    "author": "Author 1",
                    "publication_date": "2022-01-01"
                },
                {
                    "title": "Blog Post 2",
                    "author": "Author 2",
                    "publication_date": "2022-01-02"
                }
            ]
        }
    ```

### **3\. Retry Logic**

* Built-in retry mechanism ensures resilience:
  * Retries model invocations up to 3 times in case of failures.
  * Uses exponential backoff to avoid overloading servers.

### **4\. JSON Parsing**

* Automatically extracts and parses structured JSON data from AI model outputs.
* Ensures users get clean, machine-readable results.
  ```python
  data = scraper.toJSON(url, instructions)
  ```

### **5\. Save Data to File**

* Provides functionality to save extracted data to JSON files:
  ```python
  data = scraper.toJSON(url, instructions)
  scraper.toFile(data, "output/extracted_data.json")
  ```
* Useful for saving results for future use, analysis, or sharing.

### **6\. Flexible Model Configuration**

* **Model Name Selection**: Choose specific models like `"gpt-4o-mini"` for OpenAI or `"gemini-2.0-flash-exp"` for Gemini.
* **Custom API Keys**: Use different API keys for multiple platforms.
* **Temperature Control**: Adjust model randomness for predictable or creative outputs.
  Examples:
  ```python
  scraper = LLMsWebScraper(model_type="gemini", model_name="gemini-2.0-flash-exp", api_key=os.getenv("Gemini_API_KEY"))
  # scraper = LLMsWebScraper(model_type="groq", model_name="llama-3.3-70b-versatile", api_key=os.getenv("Groq_API_KEY"))
  # scraper = LLMsWebScraper(model_type="openai", model_name="gpt-4o-mini", api_key=os.getenv("OpenAI_API_KEY"))
  # scraper = LLMsWebScraper(model_type="ollama", model_name="llama3.2", base_url="http://localhost:11434", api_key="")
  
  ## If you want to add a API that is compatible with the OpenAI API, then:
  # scraper = LLMsWebScraper(model_type="other", model_name="your-model", base_url="if-have-url", api_key="your-key") # Value of 'model_type' should be 'other'. Don't change that.
  ```

### **7\. Local Model Support (Ollama)**

* Works with local language models via Ollama, which eliminates dependency on external APIs.
* Perfect for secure and private data extraction.

### **8\. Advanced Logging**

* Detailed logging for every step:
  * Successful webpage fetching.
  * Errors during HTML processing or model invocation.
  * JSON parsing errors.
* Useful for debugging and monitoring.

## **Example Use Cases**

1. **Content Scraping**:

   * Extract the main content of an article, blog, or news page.
   * Identify and collect headings, subheadings, and text.
2. **Data Extraction for Research**:

   * Extract tables, product descriptions, or customer reviews from e-commerce websites.
   * Collect structured data for analysis or training machine learning models.
3. **Knowledge Graphs**:

   * Scrape and structure data from various sources to build knowledge graphs.
4. **Privacy-Friendly Data Processing**:

   * Use Ollama or Groq for private, local processing without sending data to the cloud.

## How to Use

1. **Install the pip Library**: Use the `pip install` command.

   ```cmd
   pip install LLMsWebScraper
   ```
2. **Test the Installed Library**
   After the library is installed, you can import and use it in your Python projects just like any other library.

   Create a Python File to Test It: Create a new Python file or open a Python REPL to use your library.

   For example:

   ```python
   from LLMsWebScraper import LLMsWebScraper  
   import os
   from dotenv import load_dotenv
   import logging

   # Load environment variables
   load_dotenv()

   # Initialize the scraper
   scraper = LLMsWebScraper(model_type="gemini", model_name="gemini-2.0-flash-exp", api_key=os.getenv("Gemini_API_KEY"))
   # scraper = LLMsWebScraper(model_type="groq", model_name="llama-3.3-70b-versatile", api_key=os.getenv("Groq_API_KEY"))
   # scraper = LLMsWebScraper(model_type="openai", model_name="gpt-4o-mini", api_key=os.getenv("OpenAI_API_KEY"))
   # scraper = LLMsWebScraper(model_type="ollama", model_name="llama3.2", base_url="http://localhost:11434", api_key="")


   # Define instructions
   instructions = """
   Extract the following information:
   1. Titles of all blog posts on the page.
   2. Author names for each blog post.
   3. Publication dates of each blog post.

   Please provide the extracted information in a structured JSON format.
   Expecting property name enclosed in double quotes and values in string format.
   Example:
   {
   "blog_posts": [
           {
               "title": "Blog Post 1",
               "author": "Author 1",
               "publication_date": "2022-01-01"
           },
           {
               "title": "Blog Post 2",
               "author": "Author 2",
               "publication_date": "2022-01-02"
           }
       ]
   }
   """

   # URL of the webpage to scrape
   url = "https://chirpy.cotes.page/"

   # Extract data
   blog_data = scraper.toJSON(url, instructions)

   # Print the data
   print(blog_data)

   # If need to save like as json file
   if blog_data:
       scraper.toFile(blog_data, "output/data.json")
   else:
       logging.warning("No blog data to save.")
   ```

---

## Consider:

### Supported Models when use Groq API

The following models are available for use with the Groq API key. Please note the intended usage and stability of each model:


| Model Type | Model Name                     | Notes                                                                      |
| ------------ | -------------------------------- | ---------------------------------------------------------------------------- |
| Production | `llama-3.3-70b-versatile`      | Stable for production use                                                  |
| Preview    | `llama-3.3-70b-specdec`        | Intended for evaluation, may be discontinued                               |
| Preview    | `llama-3.2-1b-preview`         | Intended for evaluation, may be discontinued                               |
| Preview    | `llama-3.2-3b-preview`         | Intended for evaluation, may be discontinued                               |
| Preview    | `llama-3.2-11b-vision-preview` | Intended for evaluation, may be discontinued, includes vision capabilities |
| Preview    | `llama-3.2-90b-vision-preview` | Intended for evaluation, may be discontinued, includes vision capabilities |

#### Usage Guidelines

- **Production Model**: Use `llama-3.3-70b-versatile` for stable and reliable performance in production environments.
- **Preview Models**: The preview models are primarily for evaluation purposes. They may be subject to discontinuation, so use them with caution in critical applications.

Make sure to select the appropriate model based on your project requirements and stability needs.

## License

This pip library is available under the [GPLv3](LICENSE) License.

## Contact

- **Author**: KSDeshappriya
- **Email**: ksdeshappriya.official@gmail.com

## Contribution

If you find any bugs or want to suggest improvements, feel free to open an issue or pull request on the GitHub repository.
