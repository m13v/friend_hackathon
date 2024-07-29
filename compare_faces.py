import face_recognition

def compare_faces(image_path1, image_path2):
    # Load the images
    image1 = face_recognition.load_image_file(image_path1)
    image2 = face_recognition.load_image_file(image_path2)

    # Get the face encodings for the first image
    face_encodings1 = face_recognition.face_encodings(image1)
    if len(face_encodings1) == 0:
        return "No faces found in the first image."
    face_encoding1 = face_encodings1[0]

    # Get the face encodings for the second image
    face_encodings2 = face_recognition.face_encodings(image2)
    if len(face_encodings2) == 0:
        return "No faces found in the image."
    face_encoding2 = face_encodings2[0]

    # Compare the faces
    results = face_recognition.compare_faces([face_encoding1], face_encoding2)

    if results[0]:
        return "The image contains the face of Nik Shevchenko"
    else:
        return "The images are of different people."
gi
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python compare_faces.py <path_to_image1> <path_to_image2>")
        sys.exit(1)

    image_path1 = sys.argv[1]
    image_path2 = sys.argv[2]

    result = compare_faces(image_path1, image_path2)
    print(result)