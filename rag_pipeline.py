import os
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load documents
def load_documents(folder="documents"):
    texts = []
    for file in os.listdir(folder):
        with open(os.path.join(folder, file), "r", encoding="utf-8") as f:
            texts.append(f.read())
    return texts

documents = load_documents()

# Create embeddings
doc_embeddings = model.encode(documents)

# Store embeddings in FAISS
dimension = doc_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(doc_embeddings))

def get_answer(query):
    query_embedding = model.encode([query])
    _, indices = index.search(query_embedding, 2)

    context = " ".join([documents[i] for i in indices[0]])

    return f"Based on the documents, the answer is:\n{context}"