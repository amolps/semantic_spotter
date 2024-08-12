from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embeddings(text_chunks):
    return [model.encode(chunk) for chunk in text_chunks]
