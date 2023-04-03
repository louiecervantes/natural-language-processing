#Input the relevant libraries
import streamlit as st
import altair as alt
import nltk
import nltk.corpus
nltk.download('punkt')
nltk.download('wordnet')

# Define the Streamlit app
def app():
    
    st.title("Welcome to NLP in a Nutshell")     
    st.subheader("(c) 2023 Louie F. Cervantes M. Eng.")
                 
    st.write("This App demonstrates various concepts in Natural Language Processing")
                 
    st.write("Natural Language Processing (NLP) is a subfield of artificial intelligence that deals with the interaction between computers and human languages. NLP involves the use of various computational techniques to enable machines to process, analyze, and understand natural language data such as text, speech, and other forms of communication. NLP can be used for a wide range of applications, including language translation, sentiment analysis, speech recognition, and chatbots. Some of the key techniques used in NLP include text preprocessing, machine learning, deep learning, and statistical analysis. Overall, NLP aims to bridge the gap between human communication and machine understanding, enabling machines to interact with humans in a more natural and intuitive way.")
    st.subheader('Tokenizer')
    st.write('Copy the sample sentence and paste in the input box.')
    st.write('Example 1')
    st.write('From a dream a university grew, Stirring hearts with a heroes refrain. \
            Out of darkness faith renew That our toils should not fade in vain. \
            West Visayas State University, Hold thy banner high, \
            Let genius bridge the earth And boundless sky. \
            Set the youth to task half begun, \
            Seek their rightful place ‘neath the sun.')
    st.write('Example 2')
    st.write('Python is an interpreted, high-level, general-purpose programming language. \
              It was created by Guido van Rossum and first released in 1991. \
              Python is designed to be easy to read and write, with clear syntax and code \
              that is easy to understand. It supports multiple programming paradigms, \
              including procedural, object-oriented, and functional programming')
    
    # Create a multiline text field
    user_input = st.text_area('Paste the block of text here', height=20)
    
    if st.button('Submit'):    
        with st.echo(code_location='below'):
            #Tokenizing
            st.write('The list of tokens')
            from nltk.tokenize import word_tokenize   
            sentence_tokens = word_tokenize(user_input)
            st.write(sentence_tokens)
            

            #checking the type and number of tokens
            output = type(sentence_tokens), len(sentence_tokens)
            st.write(output)
            
            st.write('frequency of tokens')
            #freuency of tokens
            from nltk.probability import FreqDist
            fdist = FreqDist()
            
            for i in sentence_tokens:
                fdist[i] = fdist[i] + 1
            st.write(fdist)    
          
            st.write('The top 10 most frequent tokens')
            #Ten most common token
            top_10 = fdist.most_common(10)
            st.write(top_10)

    st.subheader('tokens, bigrams, trigrams and ngrams')
    st.write('In natural language processing (NLP), bigrams and trigrams refer to sequences of two and three consecutive words in a text, respectively.  A bigram model considers the frequency of each pair of adjacent words in a corpus of text, while a trigram model considers the frequency of each triplet of adjacent words. These models are commonly used in tasks such as language modeling, where the goal is to predict the likelihood of a given sequence of words.')
    with st.echo(code_location='below'): 
        if st.button('bigrams, trigrams. ngrams'):
            #Tokens
            st.write('The list of tokens')
            from nltk.tokenize import word_tokenize
            sentence_tokens = word_tokenize(user_input)
            st.write(sentence_tokens)
            
            st.write('The list of bigrams')
            output = list(nltk.bigrams(sentence_tokens))
            st.write(output)
            
            st.write('The list of trigrams')
            output = list(nltk.trigrams(sentence_tokens))
            st.write(output)
 
            st.write('The list of ngrams')
            output = list(nltk.ngrams(sentence_tokens, 4))
            st.write(output)
            
    st.subheader('Stemming')
    st.write('Stemming is a technique used in natural language processing (NLP) to reduce words to their base or root form, known as the stem. The purpose of stemming is to simplify the analysis of words by considering variations of a word as a single entity, rather than treating each variation separately.')
    with st.echo(code_location='below'): 
        output = ''
        if st.button('Stemming'):
            #stemming
            from nltk.stem import PorterStemmer
            pst = PorterStemmer()
            
            pst.stem('winning'), pst.stem('studies'), pst.stem('buying')
            
    from nltk.stem import PorterStemmer
    pst = PorterStemmer()
    # Get the user input
    user_input = st.text_input("Enter a word to stem")
    if st.button("Stem"):
        output = pst.stem(user_input)
        st.write(output)

    st.subheader('Lemmatization')
    st.write('Lemmatization is the process of reducing a word to its base or root form, known as a lemma. This is done to normalize words so that they can be analyzed and compared more easily. For example, the words "run," "running," and "ran" all have the same base form, "run," and so would be lemmatized to that word. Lemmatization is often used in natural language processing to improve the accuracy of text analysis and information retrieval systems.')
    output = []
    if st.button('Lemmatization'):
        with st.echo(code_location='below'): 
            #lemmatization
            from nltk.stem import wordnet
            from nltk.stem import WordNetLemmatizer
            lemmatizer = WordNetLemmatizer()
            words_to_stem = ['cats', 'cacti', 'geese']
            for i in words_to_stem:
                output.append(i + ':' + lemmatizer.lemmatize(i))
            st.write(output)
            
    from nltk.stem import wordnet
    from nltk.stem import WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()
    # Get the user input
    user_input = st.text_input("Enter a word to lemmatize")
    if st.button("Lemmatize"):
        output = lemmatizer.lemmatize(user_input)
        st.write(output) 
        
    st.subheader('POS Tagging') 
    st.write('POS tagging (Part-of-Speech tagging) is the process of labeling each word in a text corpus with its corresponding part of speech, such as noun, verb, adjective, adverb, preposition, pronoun, conjunction, interjection, or article.')
    if st.button('Parts of Speech'):
        with st.echo(code_location='below'): 
            user_input = st.text_input("Enter a sentence")
            if st.button("POS"):
                tokens = word_tokenize(user_input)
                for i in elon_tokens:
                    st.write(nltk.pos_tag([i]))
     

 
# run the app
if __name__ == "__main__":
    app()
