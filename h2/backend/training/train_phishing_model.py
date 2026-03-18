import pandas as pd
import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

def train():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, "..", "data", "emails.csv")
    models_dir = os.path.join(current_dir, "..", "models")
    
    os.makedirs(models_dir, exist_ok=True)
    
    print(f"Loading dataset from {data_path}...")
    df = pd.read_csv(data_path)
    
    X = df['email_text']
    y = df['label']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Training model...")
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(stop_words='english', max_features=5000)),
        ('clf', LogisticRegression(random_state=42))
    ])
    
    pipeline.fit(X_train, y_train)
    
    score = pipeline.score(X_test, y_test)
    print(f"Model trained with accuracy: {score:.4f}")
    
    model_path = os.path.join(models_dir, "phishing_model.pkl")
    with open(model_path, 'wb') as f:
        pickle.dump(pipeline, f)
        
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train()
