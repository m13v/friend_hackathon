from mem0 import Memory
import os
from dotenv import load_dotenv
import json
from hosted_mem0 import PersonalAITutor
ai_tutor = PersonalAITutor()

load_dotenv()

# Temporarily set the API key directly (for testing purposes only)

# Initialize the Memory class
memory = Memory()

# Add a new memory
raw_data = """
Bobak T.
  2nd degree connection2nd
CEO at Brilliant Labs | ex

Brilliant Labs  
University of Cambridge
Singapore 

"""  # Truncated for brevity

user_id = "BobakT"

# Add Nik's profile to the memory
memory_response = ai_tutor.add_profile(raw_data, user_id)
print(f"Memory response: {memory_response}")

# Retrieve and print Nik's profile
bobak_memories = ai_tutor.get_memories(user_id=user_id)
print("\Bobak's profile:")
for memory in bobak_memories:
    print(memory['text'])
# New memory data
# new_memory = {
#     "text": "Matt and Nik discussed hackathon at the AGI house that is happening on July 28 Matthew Diakonov 3:42 PM: Yo yo, is the hackathon at AGI house SF?\nNik Shevchenko  9:02 PM\nyes",
#     "tags": ["recent conversations"]
# }

# # Add the new memory to Nik's profile
# add_memory_response = ai_tutor.add_memory(new_memory["text"], user_id=user_id, metadata={"tags": new_memory["tags"]})
# print(f"Add memory response: {add_memory_response}")


# # Retrieve and print Nik's updated profile
# nik_memories = ai_tutor.get_memories(user_id=user_id)
# print("\nNik's profile:")
# for memory in nik_memories:
#     print(memory['text'])

# Search for specific information about Nik
# search_query = "Any hackathons?"
# search_results = ai_tutor.search_memories(search_query, user_id=user_id)
# print("\nSearch: ", search_query)
# for result in search_results:
#     print(f"Text: {result['text']}")
#     if 'similarity' in result:
#         print(f"Similarity: {result['similarity']}")
#     print("---")
