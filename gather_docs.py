# agent/gather_docs.py

from langchain_community.document_loaders import PyMuPDFLoader, TextLoader
from bs4 import BeautifulSoup
import requests
import urllib3

# Suppress insecure HTTPS warnings (since we use verify=False)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def extract_pdf(pdf_path):
    """
    Extracts text from a PDF file using PyMuPDFLoader.
    Returns a list of LangChain Documents (usually one per page).
    """
    loader = PyMuPDFLoader(pdf_path)
    docs = loader.load()
    return docs


def extract_text_file(path):
    """
    Loads a plain text file.
    Returns a list with a single LangChain Document.
    """
    loader = TextLoader(path)
    docs = loader.load()
    return docs


def extract_web_page(url):
    """
    Scrapes main text content from a web page using requests and BeautifulSoup.
    Returns a string (all paragraphs joined).
    """
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0 Safari/537.36"
        )
    }
    try:
        print(f"Fetching: {url}")
        response = requests.get(url, headers=headers, verify=False, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        paragraphs = [p.get_text() for p in soup.find_all("p")]
        return "\n".join(paragraphs)
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None


# # Example usage (for testing only)
# if __name__ == "__main__":
#     url = "https://en.wikipedia.org/wiki/Artificial_intelligence_in_healthcare"
#     print(extract_web_page(url)[:500])
