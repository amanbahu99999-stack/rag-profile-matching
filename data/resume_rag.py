import os
import chromadb
from sentence_transformers import SentenceTransformer

# -------------------------
# SETTINGS
# -------------------------
RESUME_FOLDER = "data/resumes"
DB_PATH = "vector_db"

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create ChromaDB client
client = chromadb.PersistentClient(path=DB_PATH)

collection = client.get_or_create_collection("resumes")


# -------------------------
# READ TEXT FILE
# -------------------------
def load_resume(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


# -------------------------
# EXTRACT NAME
# -------------------------
def get_name(text):
    return text.split("\n")[0].strip()


# -------------------------
# STORE RESUME
# -------------------------
def process_resume(file, idx):
    path = os.path.join(RESUME_FOLDER, file)

    text = load_resume(path)

    name = get_name(text)

    embedding = model.encode(text).tolist()

    collection.add(
        ids=[str(idx)],
        documents=[text],
        embeddings=[embedding],
        metadatas=[{
            "name": name,
            "file": file
        }]
    )

    print(f"Indexed: {name}")


# -------------------------
# MAIN
# -------------------------
def main():
    files = os.listdir(RESUME_FOLDER)

    for idx, file in enumerate(files):
        if file.endswith(".txt"):
            process_resume(file, idx)

    print("All resumes indexed successfully!")


if __name__ == "__main__":
    main()