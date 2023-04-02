#Input the relevant libraries
import streamlit as st
import altair as alt
import nltk
import nltk.corpus
from nltk.tokenize import word_tokenize
nltk.download('punkt')


# Define the Streamlit app
def app():
    
    st.title("Welcome to the NLP Demo App")     
    st.subheader("(c) 2023 Louie F. Cervantes M. Eng.")
                 
    st.write("The NLP Demo App demonstrates various concepts in Natural Language Processing")
                 
    st.write("Natural Language Processing (NLP) is a subfield of artificial intelligence that deals with the interaction between computers and human languages. NLP involves the use of various computational techniques to enable machines to process, analyze, and understand natural language data such as text, speech, and other forms of communication. NLP can be used for a wide range of applications, including language translation, sentiment analysis, speech recognition, and chatbots. Some of the key techniques used in NLP include text preprocessing, machine learning, deep learning, and statistical analysis. Overall, NLP aims to bridge the gap between human communication and machine understanding, enabling machines to interact with humans in a more natural and intuitive way.")

 
# run the app
if __name__ == "__main__":
    app()
