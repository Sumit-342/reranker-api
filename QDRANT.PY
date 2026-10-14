from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from dotenv import load_dotenv
import os

load_dotenv()

# Environment variables se read karo
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)

client.create_collection(
    collection_name="syllabus_chunks",
    vectors_config=VectorParams(size=384, distance=Distance.COSINE)
)

print("Collection created successfully!")
print(client.get_collections())
