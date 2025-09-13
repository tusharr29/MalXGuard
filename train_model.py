# train_model.py
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, StratifiedKFold

def train_model(X, y, cv_folds=5):
    clf = RandomForestClassifier(n_estimators=300, random_state=42)
    
    # Cross-validation
    skf = StratifiedKFold(n_splits=cv_folds, shuffle=True, random_state=42)
    cv_scores = cross_val_score(clf, X, y, cv=skf, scoring='accuracy')
    print(f"✅ {cv_folds}-Fold CV Accuracy: {cv_scores.mean():.4f} ± {cv_scores.std():.4f}")

    # Train final model
    clf.fit(X, y)
    print("✅ Final model trained.")

    # Save model
    joblib.dump(clf, "random_forest_model.pkl")
    print("✅ Model saved as random_forest_model.pkl")

    return clf



