import joblib
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def train_model(data, labels):
    vectorizer = DictVectorizer()
    X = vectorizer.fit_transform(data)
    X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.3, random_state=42)
    
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    print(classification_report(y_test, predictions))
    
    # Save the model and vectorizer
    joblib.dump(model, 'model.pkl')
    joblib.dump(vectorizer, 'vectorizer.pkl')

def load_model():
    model = joblib.load('model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
    return model, vectorizer
