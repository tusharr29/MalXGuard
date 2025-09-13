import os
from inference import predict_new_file

# Path to the folder containing new .bytes files
NEW_FILES_DIR = r"C:\Users\Tushar Deshmukh\OneDrive\Desktop\MalXGuard\dataSample"

# Get all .bytes files in the folder
bytes_files = [f for f in os.listdir(NEW_FILES_DIR) if f.endswith(".bytes")]

print(f"🔹 Found {len(bytes_files)} files for inference.\n")

# Predict each file
for f in bytes_files:
    file_path = os.path.join(NEW_FILES_DIR, f)
    predicted_class = predict_new_file(file_path)
    print(f"File: {f}  →  Predicted class: {predicted_class}")
