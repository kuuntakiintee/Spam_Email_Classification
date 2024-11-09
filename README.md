# Spam Email Detection
This project is a simple web application built using Streamlit, which uses a machine learning model to predict whether an email is spam or not spam. The model was trained using a dataset of labeled emails and applies Natural Language Processing (NLP) techniques to classify emails.

# Demo
You can access streamlit here : https://spam-email-model.streamlit.app/

# Project Overview
The goal of this project is to demonstrate the use of machine learning and NLP for text classification. It uses a Naive Bayes model trained on email data to determine if a given email is spam or not. The application also provides additional features such as sentiment analysis and a word cloud to give deeper insights into the email text.

# Features
Spam Detection: Predicts if the email is spam or not.
Sentiment Analysis: Analyzes the sentiment (positive, negative, or neutral) of the email.
Word Cloud: Visualizes the most common words in the email text.

# How It Works
Input: Insert the text of an email in the provided text box.
Prediction: Click the Predict button to get the result.
Output: The app will display:
- Whether the email is spam or not.
- Sentiment of the email (positive, negative, neutral).
- A word cloud showing the most frequent words in the email.
- Probability of the email being spam or not.

# Model
The model used in this project is a Multinomial Naive Bayes classifier trained on a dataset of emails labeled as spam or not spam. The email text is transformed into numerical features using CountVectorizer, which converts the text into a bag-of-words representation. The model is then used to predict the classification of new email text.

# How to Use
Open the Spam Email Detection Web App.
Type or paste an email message into the Insert Email Text box.
Click the Predict button to see if the email is spam or not.
The sentiment of the email (positive, negative, or neutral) will be displayed along with a word cloud of the email's content.
The model will also provide the probability of the email being spam or not.
