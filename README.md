# Phishing Detection System

## Overview

The Phishing Detection System uses machine learning to analyze and detect phishing emails or URLs. The system stores email data and detection results in an SQL database for further analysis and reporting. The project integrates Python for machine learning and email processing, while SQL is used for managing the database.

## Features

- **Phishing Detection:** Detect phishing emails or URLs using a machine learning model.
- **Database Integration:** Store email data and detection results in a MySQL database.
- **Email Processing:** Extract features from email content for analysis.
- **Model Training:** Train a machine learning model to classify emails as phishing or legitimate.

## Technologies

- **Python:** Programming language used for machine learning and email processing.
- **MySQL:** SQL database for storing email data and detection results.
- **Scikit-learn:** Machine learning library used for training and prediction.
- **Joblib:** Library for saving and loading the machine learning model.
- **Pandas:** Data manipulation library for handling email features.

## Project Structure

- **`config.py`**: Configuration file for database connection details.
- **`email_processing.py`**: Script for processing and extracting features from emails.
- **`model.py`**: Script for training and saving the machine learning model.
- **`detection.py`**: Script for detecting phishing emails using the trained model.
- **`database.py`**: Script for interacting with the SQL database.
- **`main.py`**: Main script to run the detection process and manage the workflow.

## Installation

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/yourusername/phishing-detection-system.git
   cd phishing-detection-system
   ```

2. **Set Up MySQL:**

   - Install MySQL according to your operating system (refer to [MySQL Installation Guide](https://dev.mysql.com/doc/refman/8.0/en/installing.html)).
   - Update `DATABASE_CONFIG` in `config.py` with your MySQL credentials.
   - Create a database named `phishing_detection` using MySQL Workbench or the MySQL command line.

3. **Install Dependencies:**

   Create a virtual environment (optional but recommended):

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

   Install the required Python libraries:

   ```sh
   pip install pandas scikit-learn joblib mysql-connector-python
   ```

## Usage

1. **Create Database Table:**

   Run the following command to create the necessary table in the MySQL database:

   ```sh
   python database.py
   ```

2. **Train the Model:**

   Update `main.py` with sample email texts and their labels, then run:

   ```sh
   python main.py
   ```

   This will train the machine learning model using the provided email data.

3. **Detect Phishing Emails:**

   Add new email texts to the `new_email_texts` list in `main.py` and run the script again to detect phishing:

   ```sh
   python main.py
   ```

   Detection results will be stored in the MySQL database.

## Files

- **`config.py`**: Contains database connection configuration.
- **`email_processing.py`**: Functions for extracting features from email texts.
- **`model.py`**: Contains code for training and saving the machine learning model.
- **`detection.py`**: Functions for detecting phishing emails using the trained model.
- **`database.py`**: Functions for database operations.
- **`main.py`**: Main script for running the entire process.
