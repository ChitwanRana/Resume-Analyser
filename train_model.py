import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import pickle

# Sample dataset (expand with more data)
data = {
    "Resume_Text": [
        "Python, Machine Learning, Pandas, SQL",
        "HTML, CSS, JavaScript, React, Django",
        "Recruitment, Payroll, Employee Relations",
        "Python, Data Analysis, SQL, Statistics"
    ],
    "Career_Field": [
        "Data Science",
        "Web Developer",
        "HR",
        "Data Science"
    ]
}

df = pd.DataFrame(data)

# TF-IDF
vectorizer = TfidfVectorizer(stop_words='english', max_features=500)
X_vect = vectorizer.fit_transform(df["Resume_Text"])

# Train model
model = MultinomialNB()
model.fit(X_vect, df["Career_Field"])

# Save model & vectorizer
pickle.dump(model, open("career_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model and vectorizer saved successfully!")
