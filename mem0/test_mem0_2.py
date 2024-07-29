from mem0 import Memory
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize the Memory class
memory = Memory()

# Function to add a memory
def add_memory(data, user_id, metadata):
    response = memory.add(data=data, user_id=user_id, metadata=metadata)
    print(f"Memory added: {response}")
    return response[0]['id'] if response else None

# Function to retrieve a memory
def get_memory(memory_id):
    retrieved_memory = memory.get(memory_id)
    print(f"Retrieved memory: {retrieved_memory}")
    return retrieved_memory

# Function to search memories
def search_memories(query, user_id):
    related_memories = memory.search(query=query, user_id=user_id)
    print(f"Related memories: {related_memories}")
    return related_memories

# Main execution
if __name__ == "__main__":
    if os.getenv('OPENAI_API_KEY'):
        # Add a memory
        user_id = "test_user_123"
        data = "This is a test memory for Mem0."
        metadata = {"type": "test", "importance": "high"}
        memory_id = add_memory(data, user_id, metadata)

        if memory_id:
            # Retrieve the memory
            get_memory(memory_id)

            # Search for memories
            search_query = "Tell me about test memories"
            search_memories(search_query, user_id)
    else:
        print("OPENAI_API_KEY is not set. Please set it in your .env file.")