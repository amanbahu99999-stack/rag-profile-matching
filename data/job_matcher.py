import chromadb
from sentence_transformers import SentenceTransformer

# -------------------------
# SETTINGS
# -------------------------
DB_PATH = "vector_db"

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path=DB_PATH)

collection = client.get_collection("resumes")


# -------------------------
# SEARCH FUNCTION
# -------------------------
def search_candidates(job_description):
    query_embedding = model.encode(job_description).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=5
    )

    print("\nTop Matching Candidates:\n")

    docs = results["documents"][0]
    metas = results["metadatas"][0]

    for i in range(len(docs)):
        name = metas[i]["name"]
        file = metas[i]["file"]

        print(f"{i+1}. {name}")
        print(f"Resume File: {file}")
        print("-" * 40)


# -------------------------
# MAIN
# -------------------------
if __name__ == "__main__":
    jd = input("Enter Job Description: ")
    search_candidates(jd)