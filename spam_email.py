import streamlit as st
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from textblob import TextBlob

# Load model and vectorizer
model = pickle.load(open('spam_email.pkl', 'rb'))
cv = pickle.load(open('cv.pkl', 'rb'))

# Add sidebar instructions
st.sidebar.title("How to Use")
st.sidebar.markdown("""
    1. Insert the text of an email in the provided text box.
    2. Press the **Predict** button.
    3. The model will predict if it's spam or not.
""")

st.markdown('<h1 style="color:green; text-align:center;">Spam Email Detection App</h1>', unsafe_allow_html=True)

# Initialize session state for email text if it doesn't exist
if 'email_text' not in st.session_state:
    st.session_state.email_text = ""

# Email input area
email_text = st.text_area("Insert Email Text", st.session_state.email_text)

# Update session state when the text is entered
st.session_state.email_text = email_text

# Prediction Button
if st.button("Predict"):
    if email_text:
        # Sentiment analysis
        sentiment = TextBlob(email_text).sentiment.polarity
        sentiment_label = "Positive" if sentiment > 0 else "Negative" if sentiment < 0 else "Neutral"
        st.write(f"Sentiment of the email: {sentiment_label}")

        # Show word cloud
        wordcloud = WordCloud(stopwords='english').generate(email_text)
        plt.figure(figsize=(6, 4))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        st.pyplot(plt)

        # Transform the email text using the fitted vectorizer and make the prediction
        email_predict = cv.transform([email_text])  
        prediction = model.predict(email_predict)
        
        if prediction[0] == 1:
            st.markdown('<h2 style="color:red;">This email is a SPAM!</h2>', unsafe_allow_html=True)
        else:
            st.markdown('<h2 style="color:green;">This email is not a SPAM!</h2>', unsafe_allow_html=True)
        
        # Show confidence
        prediction_prob = model.predict_proba(email_predict)[0]
        st.write(f"Probability of being SPAM: {prediction_prob[1]:.2f}")
        st.write(f"Probability of being NOT SPAM: {prediction_prob[0]:.2f}")
    else:
        st.write("Please insert an email text.")

# Footer
st.markdown("""
    <footer style="text-align:center; margin-top:50px;">
        <p>Created by Hans Santoso</p>
        <p><a href="https://www.linkedin.com/in/hans-santoso/" target="_blank">Connect with me on LinkedIn</a></p>
    </footer>
""", unsafe_allow_html=True)
