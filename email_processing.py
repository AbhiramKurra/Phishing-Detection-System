import re
import pandas as pd

def extract_features(email_text):
    features = {}
    
    # Basic features
    features['length'] = len(email_text)
    features['num_links'] = len(re.findall(r'http[s]?://', email_text))
    features['num_exclamation'] = email_text.count('!')
    features['num_question'] = email_text.count('?')
    
    # More sophisticated features can be added here
    
    return features

def email_to_dataframe(email_texts):
    data = [extract_features(email) for email in email_texts]
    return pd.DataFrame(data)
