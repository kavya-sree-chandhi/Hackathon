# agent/citations.py

def extract_sources_from_chunks(chunks):
    """
    Collects all unique sources (URLs, DOIs, arXiv IDs, etc.) from chunk metadata.
    Returns a list of unique sources.
    """
    sources = set()
    for chunk in chunks:
        # Standardize: your chunk metadata should include 'source'
        source = chunk.metadata.get('source') if hasattr(chunk, 'metadata') else None
        if source:
            sources.add(source)
    return list(sources)

def render_citations(sources):
    """
    Formats a list of sources as a citation section (Markdown or plain text).
    """
    if not sources:
        return "No citations found."
    out = "## References\n"
    for idx, source in enumerate(sources, 1):
        out += f"[{idx}]: {source}\n"
    return out


# # Example usage
# if __name__ == "__main__":
#     # Fake chunks with metadata for demonstration
#     class DummyChunk:
#         def __init__(self, meta):
#             self.metadata = meta
#     chunks = [DummyChunk({'source': 'https://arxiv.org/abs/2007.07892'}),
#               DummyChunk({'source': 'https://pubmed.ncbi.nlm.nih.gov/123456/'}),
#               DummyChunk({'source': 'https://arxiv.org/abs/2007.07892'})]  # duplicate
#     sources = extract_sources_from_chunks(chunks)
#     print(render_citations(sources))
