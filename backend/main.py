from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer, util
import json

app = FastAPI(title="Intelligent Enterprise Assistant")

# Load the policy data
with open("../data/sample_policies.json", "r") as f:
    policies = json.load(f)

# Create model and embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')
policy_texts = [p["content"] for p in policies]
policy_embeddings = model.encode(policy_texts, convert_to_tensor=True)

class Query(BaseModel):
    text: str

@app.post("/api/query")
async def query_ai(q: Query):
    query_embedding = model.encode(q.text, convert_to_tensor=True)
    scores = util.cos_sim(query_embedding, policy_embeddings)
    best_idx = int(scores.argmax())
    best_policy = policies[best_idx]
    return {
        "query": q.text,
        "answer": best_policy["content"],
        "source": best_policy["title"]
    }

@app.get("/")
def root():
    return {"message": "Intelligent Enterprise Assistant API is running"}
