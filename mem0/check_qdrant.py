from qdrant_client import QdrantClient

client = QdrantClient("localhost", port=6333)
collection_name = "mem0"

# Get collection info
collection_info = client.get_collection(collection_name)
print(f"Collection info: {collection_info}")

# Get total points count
count = client.count(collection_name=collection_name)
print(f"Total points: {count}")

# Sample a few points
sample_size = min(5, count.count)
points = client.scroll(collection_name=collection_name, limit=sample_size, with_payload=True)[0]

print(f"\nSample of {sample_size} points:")
for point in points:
    print(f"ID: {point.id}, Payload: {point.payload}")