AI Spam Message Detector

A beginner-friendly Natural Language Processing (NLP) project that classifies text messages as spam or normal using TF-IDF feature extraction and Machine Learning.

Project Overview

This project demonstrates an end-to-end text classification workflow:

Raw Text
   ↓
TF-IDF Vectorization
   ↓
Machine Learning Model
   ↓
Prediction
   ↓
Evaluation

Two models are compared:

Multinomial Naive Bayes

Logistic Regression

The project also supports custom message prediction.

Dataset

The project uses:

day40_spam_dataset_1000_unique.csv

Dataset details:

1,000 messages

500 spam messages

500 normal messages

0 duplicate text rows

Columns:

text — message content

label — spam or normal

The dataset is synthetic and is intended for educational and portfolio practice.

Requirements

Python 3.9 or newer is recommended.

Install the required libraries:

pip install pandas scikit-learn

Or install from requirements.txt if it is included:

pip install -r requirements.txt

Project Files

A recommended repository structure is:

Project-4-ai-spam-message-detector/
│
├── text.csv
├── spam_detector.py
├── README.md
└── requirements.txt

How to Run

1. Clone the repository

git clone https://github.com/thilak091/Ai-Engineer-journey/tree/main/Projects
cd project-4-ai-spam-message-detector

2. Install dependencies

pip install -r requirements.txt

3. Make sure the CSV file is in the same project folder

Your Python program should reference:

pd.read_csv("day40_spam_dataset_1000_unique.csv")

4. Run the program

python spam_detector.py

What the Program Does

1. Loads and inspects the dataset

The program displays:

Dataset shape

Class distribution

Training accuracy

Testing accuracy

Cross-validation accuracy

2. Splits the data

The dataset is divided into training and testing sets using a stratified split.

Example:

train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

3. Converts text into numerical features

The project uses:

TfidfVectorizer()

TF-IDF converts text into numerical features based on the importance of words within documents and across the corpus.

4. Trains Multinomial Naive Bayes

The first model uses:

MultinomialNB()

combined with TF-IDF using a Scikit-learn pipeline.

5. Evaluates the model

The program reports:

Accuracy

Precision

Recall

F1-score

Confusion matrix

5-fold cross-validation accuracy

6. Compares Logistic Regression

A second pipeline is created using:

TfidfVectorizer()
+
LogisticRegression()

The two models are compared using the same dataset and evaluation approach.

7. Predicts custom messages

After training, the program asks:

Enter the Message to be Predicted:

Example:

Congratulations! You have won a free prize.

Possible output:

Prediction: SPAM
Confidence: 98.20%

Another example:

Please submit the project report before Friday.

Possible output:

Prediction: NORMAL
Confidence: 96.10%

The exact predictions and confidence values depend on the trained model.

Important Notes

Why Pipeline is Used

The project uses a Scikit-learn pipeline so that text vectorization and model training remain together:

Text
 ↓
TfidfVectorizer
 ↓
Classifier

This makes the workflow cleaner and helps prevent preprocessing leakage during cross-validation.

Why Accuracy Alone Is Not Enough

For classification projects, accuracy should not be considered by itself. Precision, recall, F1-score, and the confusion matrix provide additional information about model behavior.

About the Dataset

This dataset is synthetic and created for learning purposes. A high score on this dataset should not be interpreted as proof of real-world spam detection performance.

Real-world spam detection would require a larger and more diverse dataset containing naturally occurring messages.

Technologies Used

Python

Pandas

Scikit-learn

TF-IDF

Multinomial Naive Bayes

Logistic Regression

Machine Learning

Natural Language Processing

Learning Outcomes

This project demonstrates practical understanding of:

Text classification

TF-IDF vectorization

Sparse text features

Train/test splitting

Stratified sampling

Scikit-learn pipelines

Multinomial Naive Bayes

Logistic Regression

Cross-validation

Classification metrics

Confusion matrices

Custom model prediction


Author:-

Thilak

Project developed as part of Ai Engineering Journey — Day 40.