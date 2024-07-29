from openai import OpenAI
from mem0 import Memory
import os
from qdrant_client import QdrantClient

# Set the OpenAI API key
os.getenv('OPENAI_API_KEY')
# Initialize the OpenAI client
client = OpenAI()

# Add this before instantiating PersonalAITutor
try:
    qdrant_client = QdrantClient("localhost", port=6333)
    qdrant_client.get_collections()
    print("Successfully connected to Qdrant")
except Exception as e:
    print(f"Failed to connect to Qdrant: {e}")
    exit(1)

class PersonalAITutor:
    def __init__(self):
        """
        Initialize the PersonalAITutor with memory configuration and OpenAI client.
        """
        config = {
            "vector_store": {
                "provider": "qdrant",
                "config": {
                    "host": "localhost",
                    "port": 6333,
                }
            },
        }
        self.memory = Memory.from_config(config)
        self.client = client
        self.app_id = "app-1"

    def ask(self, question, user_id=None):
        """
        Ask a question to the AI and store the relevant facts in memory

        :param question: The question to ask the AI.
        :param user_id: Optional user ID to associate with the memory.
        """
        # Start a streaming chat completion request to the AI
        stream = self.client.chat.completions.create(
            model="gpt-4o",
            stream=True,
            messages=[
                {"role": "system", "content": "You are a personal AI Tutor."},
                {"role": "user", "content": question}
            ]
        )
        # Store the question in memory
        self.memory.add(question, user_id=user_id, metadata={"app_id": self.app_id})

        # Print the response from the AI in real-time
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="")

    def get_memories(self, user_id=None):
        """
        Retrieve all memories associated with the given user ID.

        :param user_id: Optional user ID to filter memories.
        :return: List of memories.
        """
        return self.memory.get_all(user_id=user_id)

    def search_memories(self, query, user_id=None, limit=5):
        """
        Search for memories based on a query.

        :param query: The search query.
        :param user_id: Optional user ID to filter memories.
        :param limit: Maximum number of results to return.
        :return: List of relevant memories.
        """
        return self.memory.search(query, user_id=user_id, limit=limit)

    def add_profile(self, profile_data, user_id):
        """
        Add a user profile to the memory.

        :param profile_data: The profile data to store.
        :param user_id: The user ID to associate with the profile.
        :return: The response from the memory addition.
        """
        metadata = {"type": "profile", "app_id": self.app_id}
        return self.memory.add(data=profile_data, user_id=user_id, metadata=metadata)


    def add_memory(self, memory_text, user_id, metadata=None):
        """
        Add a general memory to the memory store.

        :param memory_text: The memory text to store.
        :param user_id: The user ID to associate with the memory.
        :param metadata: Optional metadata to associate with the memory.
        :return: The response from the memory addition.
        """
        if metadata is None:
            metadata = {}
        metadata["app_id"] = self.app_id
        return self.memory.add(data=memory_text, user_id=user_id, metadata=metadata)

    def get_user_profile(self, user_id):
        """
        Retrieve the user profile from memory.

        :param user_id: The user ID to retrieve the profile for.
        :return: The user profile data, or None if not found.
        """
        profile_memories = self.memory.search(
            query="",
            user_id=user_id,
            metadata={"type": "profile", "app_id": self.app_id},
            limit=1
        )
        
        if profile_memories:
            return profile_memories[0]['text']
        return None

def create_tutor():
    return PersonalAITutor()

def example_usage(ai_tutor):
    # Define a user ID
    user_id = "john_doe"

    # Ask a question
    ai_tutor.ask("I am learning introduction to CS. What is queue? Briefly explain.", user_id=user_id)

    memories = ai_tutor.get_memories(user_id=user_id)
    print('\nAll memories:')
    for m in memories:
        print(m['text'])

if __name__ == "__main__":
    ai_tutor = create_tutor()
    # example_usage(ai_tutor)