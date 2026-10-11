from fastapi import FastAPI
from pydantic import BaseModel
from fastembed.rerank.cross_encoder import TextCrossEncoder

app = FastAPI()

reranker = TextCrossEncoder(model_name="BAAI/bge-reranker-base")

class RerankInput(BaseModel):
    query: str
    documents: list[str]

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/rerank")
def rerank(input: RerankInput):
    scores = list(reranker.rerank(input.query, input.documents))
    ranked = sorted(
        zip(input.documents, scores),
        key=lambda x: x[1],
        reverse=True
    )
    return {"ranked_results": [{"text": doc, "score": float(score)} for doc, score in ranked]}