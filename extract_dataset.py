# extract_dataset.py
import os, random, pandas as pd

def generate_dummy_dataset(root_dir, files_per_class=50, bytes_per_file=500, classes=[2,7]):
    data_dir = os.path.join(root_dir, "dataSample")
    os.makedirs(data_dir, exist_ok=True)

    ids, labels = [], []
    for cls in classes:
        for i in range(files_per_class):
            file_id = f"{cls}_dummy_{i}"
            file_name = os.path.join(data_dir, f"{file_id}.bytes")
            content = ''.join(random.choices('0123456789ABCDEF', k=bytes_per_file))
            with open(file_name, 'w') as f:
                f.write(content)
            ids.append(file_id)
            labels.append(cls)

    labels_path = os.path.join(root_dir, "trainLabels.csv")
    pd.DataFrame({"Id": ids, "Class": labels}).to_csv(labels_path, index=False)
    return data_dir, labels_path


