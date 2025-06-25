# app/train_model.py

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import pickle
import os

# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model to 'model' folder
os.makedirs("model", exist_ok=True)
with open("model/iris_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved in app/model/iris_model.pkl")
