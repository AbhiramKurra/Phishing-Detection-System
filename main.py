from email_processing import email_to_dataframe
from model import train_model
from detection import detect_phishing
from database import create_table, insert_email
import pandas as pd

def main():
    # Create table
    create_table()
    
    # Example email texts and labels
    email_texts = [
        "Congratulations! You've won a $1,000 gift card. Click here to claim.",
        "Hello, just checking in to see how you are doing.",
    ]
    labels = [1, 0]  # 1 for phishing, 0 for legitimate
    
    # Convert email texts to dataframe and train model
    data = email_to_dataframe(email_texts)
    train_model(data.to_dict(orient='records'), labels)
    
    # Example new email texts
    new_email_texts = [
        "Get your free trial now! Limited time offer!",
        "Meeting scheduled for next Monday at 10 AM.",
    ]
    
    # Detect phishing
    predictions = detect_phishing(new_email_texts)
    
    # Insert results into database
    for email, prediction in zip(new_email_texts, predictions):
        insert_email(email, None, prediction)  # `is_phishing` is unknown for new emails
    
    print("Detection completed and results saved to database.")

if __name__ == "__main__":
    main()
