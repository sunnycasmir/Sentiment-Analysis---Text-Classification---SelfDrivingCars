import pandas as pd
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import streamlit as st

#load the trained model
model = load_model('lstm_model.h5')

#load the tokenizer
with open('tokens.pk1', 'rb') as tk: 
    tokenizer = pickle.load(tk)

#Define the function to preprocess the user text input
def preprocess_text(text):
    # Tokenize the text
    tokens = tokenizer.texts_to_sequences([text])

    # pad the sequence to a fix lenght
    padded_tokens = pad_sequences(tokens, maxlen=20)
    return padded_tokens[0]

# Create the app
st.title('Sentiment Analysis App')

#Create text input widget for user input
user_input = st.text_area('Enter text for Sentiment Analysis', ' ')

# Create a button to trigger the sentiment analysis
if st.button('Predict sentiment'):
    # process the user input
    processed_input = preprocess_text(user_input)

    #Make prediction using the load model
    prediction = model.predict(np.array([processed_input]))
    st.write(prediction)
    sentiment = 'Negative' if prediction[0][0] > 0.5 else 'Positive'

    # Display the sentiment
    st.write(f'Sentiment: {sentiment}')