from extract_dataset import generate_dummy_dataset
from feature_extraction import run_pipeline_pro
from train_model import train_model

ROOT_DIR = r"C:\Users\Tushar Deshmukh\OneDrive\Desktop\MalXGuard"

# Optional: generate dummy dataset
data_dir, labels_path = generate_dummy_dataset(ROOT_DIR, files_per_class=50)

# Feature extraction
X, y_encoded, vectorizer, le, _ = run_pipeline_pro(data_dir, labels_path, max_features=2000)

# Train model
clf = train_model(X, y_encoded)


