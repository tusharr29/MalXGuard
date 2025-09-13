import os
import random
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib

def run_pipeline_pro(data_dir, labels_path, max_features=2000):
    # === Load labels ===
    labels_df = pd.read_csv(labels_path)

    # === Load .bytes files ===
    texts, y = [], []
    for root, dirs, files in os.walk(data_dir):
        for fname in files:
            if fname.endswith(".bytes"):
                file_id = fname.split('.')[0]
                label_row = labels_df[labels_df['Id'] == file_id]
                if label_row.empty:
                    continue
                file_path = os.path.join(root, fname)
                try:
                    with open(file_path, "r", errors="ignore") as f:
                        content = f.read()
                        content = re.sub(r'[^0-9A-Fa-f]', '', content)
                        if content:
                            texts.append(content)
                            y.append(label_row['Class'].values[0])
                except Exception as e:
                    print(f"⚠️ Skipping {fname}: {e}")

    print(f"✅ Loaded {len(texts)} files for feature extraction")

    # === TF-IDF feature extraction ===
    vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(3,6), max_features=max_features)
    X = vectorizer.fit_transform(texts)
    print("✅ Feature matrix shape:", X.shape)

    # === Encode labels ===
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)
    print("✅ Labels encoded. Classes:", le.classes_)

    # === Train/test split ===
    if len(texts) > 2:
        test_size = max(1, int(0.2 * len(texts)))
        X_train, X_test, y_train, y_test = train_test_split(
            X, y_encoded, test_size=test_size, random_state=42
        )
    else:
        X_train, y_train = X, y_encoded
        X_test, y_test = X, y_encoded

    print("✅ Train shape:", X_train.shape, y_train.shape)
    print("✅ Test shape:", X_test.shape, y_test.shape)

    # === Train Random Forest ===
    clf = RandomForestClassifier(n_estimators=200, random_state=42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    # === Evaluate ===
    print("\n=== Classification Report ===")
    print(classification_report(
        y_test, y_pred, labels=le.transform(le.classes_),
        target_names=[str(c) for c in le.classes_], zero_division=0
    ))
    print("\n=== Confusion Matrix ===")
    print(confusion_matrix(y_test, y_pred, labels=le.transform(le.classes_)))

    # === Save artifacts ===
    joblib.dump(X, "X_features.pkl")
    joblib.dump(y_encoded, "y_labels.pkl")
    joblib.dump(clf, "random_forest_model.pkl")
    joblib.dump(le, "label_encoder.pkl")
    joblib.dump(vectorizer, "tfidf_vectorizer.pkl")

    print("\n✅ Pipeline complete. Everything saved.")
    
    return X, y_encoded, vectorizer, le, clf

