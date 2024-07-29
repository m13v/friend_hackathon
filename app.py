from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import os
from datetime import datetime
from compare_faces import compare_faces
from pydantic import BaseModel
from typing import List, Optional
from PIL import Image
from io import BytesIO

app = Flask(__name__)
CORS(app)  # Enable CORS

class MemoryPhoto(BaseModel):
    base64: str
    description: str

class Memory(BaseModel):
    createdAt: datetime
    startedAt: Optional[datetime] = None
    finishedAt: Optional[datetime] = None
    transcript: str = ''
    transcriptSegments: List[str] = []
    photos: Optional[List[MemoryPhoto]] = []
    recordingFilePath: Optional[str] = None
    recordingFileBase64: Optional[str] = None
    structured: dict
    pluginsResponse: List[dict] = []
    discarded: bool

def decode_base64_image(base64_string, output_path):
    # Decode the base64 string
    image_data = base64.b64decode(base64_string)
    image = Image.open(BytesIO(image_data))

    # Rotate the image clockwise
    rotated_image = image.rotate(-90, expand=True)

    # Ensure the directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    rotated_image.save(output_path)

@app.route('/compare', methods=['POST'])
def compare():
    # Print the full request data
    print("Headers:", request.headers)
    # print("Body:", request.get_data(as_text=True))

    data = request.json
    if not data:
        print("No JSON data received")
        return jsonify({"error": "No JSON data received"}), 400

    try:
        memory = Memory(**data)
    except Exception as e:
        print(f"Error parsing JSON data: {e}")
        return jsonify({"error": "Invalid JSON data"}), 400

    if not memory.photos or len(memory.photos) == 0:
        print("No photos provided in the request")
        return jsonify({"error": "No photos provided"}), 400

    reference_image_path = "/Users/matthewdi/Desktop/screenpipe/do-i-know-you/Nik/image.png"
    results = []

    for photo in memory.photos:
        base64_image = photo.base64

        # Create a unique filename for the received image
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
        received_image_path = os.path.join("received_images", f"received_image_{timestamp}.jpeg")

        # Save the decoded image to the received_images directory
        decode_base64_image(base64_image, received_image_path)

        # Call compare_faces with the reference image and the received image
        result = compare_faces(reference_image_path, received_image_path)
        results.append({"result": result, "saved_image_path": received_image_path})

        # Print the result instead of the image
        print("Comparison result:", result)

    # Return the results
    return jsonify({"results": results})

if __name__ == '__main__':
    app.run(debug=True, port=8080)