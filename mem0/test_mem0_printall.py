from mem0 import Memory
import os
from dotenv import load_dotenv

load_dotenv()

def get_all_memories():
    memory = Memory()
    all_memories = memory.get_all()
    return all_memories

def print_memories(memories):
    for mem in memories:
        print(f"ID: {mem['id']}")
        print(f"Text: {mem['text']}")
        print(f"Metadata: {mem['metadata']}")
        print("-" * 50)

if __name__ == "__main__":
    if os.getenv('OPENAI_API_KEY'):
        memories = get_all_memories()
        if memories:
            print(f"Total memories: {len(memories)}")
            print_memories(memories)
        else:
            print("No memories found.")
    else:
        print("OPENAI_API_KEY is not set. Please set it in your .env file.")