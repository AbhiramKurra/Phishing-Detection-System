from model import load_model
from email_processing import extract_features
import pandas as pd
import numpy as np

def detect_phishing(email_texts):
    model, vectorizer = load_model()
    features = [extract_features(email) for email in email_texts]
    X = vectorizer.transform(features)
    predictions = model.predict(X)
    return predictions
