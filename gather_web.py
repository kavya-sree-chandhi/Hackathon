from ddgs import DDGS

def search_web(query, max_results=3):
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            results.append({
                'title': r.get('title'),
                'url': r.get('href'),
                'snippet': r.get('body')
            })
    return results

if __name__ == "__main__":
    print("Testing search_web()...")
    query = "Has AI improved diagnostic accuracy in healthcare?"
    results = search_web(query)
    if results:
        for idx, r in enumerate(results, 1):
            print(f"\nResult {idx}:")
            print(f"Title: {r['title']}")
            print(f"URL: {r['url']}")
            print(f"Snippet: {r['snippet']}")
    else:
        print("No results found.")
