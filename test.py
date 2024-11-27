from deepface import DeepFace

# Path to your image
img_path = "download.jfif"

# Perform emotion analysis
result = DeepFace.analyze(img_path=img_path, actions=["emotion"])
print("Emotion Analysis Result:", result)
