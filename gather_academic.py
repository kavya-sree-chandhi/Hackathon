# agent/gather_academic.py

from langchain_community.document_loaders import ArxivLoader
import requests
from bs4 import BeautifulSoup

def search_arxiv(query, max_results=3):
    """
    Search arXiv for papers. Returns a list of LangChain Documents.
    """
    loader = ArxivLoader(query=query, load_max_docs=max_results)
    docs = loader.load()
    return docs

def get_pubmed_abstracts(query, max_results=3):
    """
    Search PubMed for abstracts. Returns a list of dicts: [{'title': ..., 'abstract': ...}, ...]
    """
    search_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmax={max_results}&term={query}&retmode=json"
    ids = requests.get(search_url).json()['esearchresult']['idlist']
    fetch_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={','.join(ids)}&retmode=xml"
    res = requests.get(fetch_url)
    soup = BeautifulSoup(res.content, "xml")
    abstracts = []
    for article in soup.find_all('PubmedArticle'):
        title = article.ArticleTitle.get_text() if article.ArticleTitle else ""
        abstract = article.AbstractText.get_text() if article.AbstractText else ""
        if abstract:
            abstracts.append({'title': title, 'abstract': abstract})
    return abstracts

# # Example usage (for testing)
# if __name__ == "__main__":
#     print("Arxiv results:")
#     for doc in search_arxiv("AI healthcare diagnostics", max_results=2):
#         print(doc.page_content[:200], "\n---")
#     print("\nPubMed abstracts:")
#     for ab in get_pubmed_abstracts("AI healthcare diagnostics", max_results=2):
#         print(ab['title'])
#         print(ab['abstract'][:200])
#         print("---")
