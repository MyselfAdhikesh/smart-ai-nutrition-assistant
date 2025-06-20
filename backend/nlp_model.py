import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Load training data
data_path = os.path.join("data", "nutrition_faq.csv")
df = pd.read_csv(data_path)

# Features and labels
X = df["question"]
y = df["answer"]

# Train TF-IDF model
vectorizer = TfidfVectorizer()
X_vect = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vect, y)

# Save trained model
joblib.dump(model, "backend/nlp_model.pkl")
joblib.dump(vectorizer, "backend/vectorizer.pkl")

# Load + Predict function for chatbot
def predict_answer(question):
    model = joblib.load("backend/nlp_model.pkl")
    vectorizer = joblib.load("backend/vectorizer.pkl")
    vect = vectorizer.transform([question])
    return model.predict(vect)[0]
