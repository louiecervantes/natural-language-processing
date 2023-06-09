#Input the relevant libraries
import streamlit as st
import altair as alt
import nltk
import nltk.corpus
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

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
            
    # Get the user input
    user_input = st.text_input("Enter a sentence to lemmatize", 'the cat is sitting with the bats on the striped mat under many flying geese')
    if st.button("Lemmatize"):
        nltk.download('wordnet')
        nltk.download('averaged_perceptron_tagger')
        from nltk.stem import wordnet
        from nltk.stem import WordNetLemmatizer
        lemmatizer = WordNetLemmatizer()
        wordlist = nltk.word_tokenize(user_input)
        lemmatized_string = ' '.join([lemmatizer.lemmatize(words) for words in wordlist])
        st.write(lemmatized_string) 
        
    st.subheader('POS Tagging') 
    st.write('POS tagging (Part-of-Speech tagging) is the process of labeling each word in a text corpus with its corresponding part of speech, such as noun, verb, adjective, adverb, preposition, pronoun, conjunction, interjection, or article.')
   
    st.write('Meaning of the tags:')    
    meaning = ['CC coordinating conjunction', 
            'CD cardinal digit',
            'DT determiner',
            'EX existential there (like: “there is” … think of it like “there exists”)',
            'FW foreign word',
            'IN preposition/subordinating conjunction',
            'JJ adjective – "big"',
            'JJR adjective, comparative', 
            'JJS adjective, superlative',
            'LS list marker 1)',
            'MD modal – could, will',
            'NN noun, singular "- desk"',
            'NNS noun plural – "desks"',
            'NNP proper noun, singular – "Harrison"',
            'NNPS proper noun, plural – "Americans"',
            'PDT predeterminer – "all the kids"',
            'POS possessive ending', 
            'PRP personal pronoun –  I, he, she',
            'PRP$ possessive pronoun – my, his, hers',
            'RB adverb – very, silently',
            'RBR adverb, comparative – better', 
            'RBS adverb, superlative – best', 
            'RP particle – give up', 
            'TO – to go ‘to’ the store.',
            'UH interjection – errrrrrrrm',
            'VB verb, base form – take', 
            'VBD verb, past tense – took',
            'VBG verb, gerund/present participle – taking', 
            'VBN verb, past participle – taken', 
            'VBP verb, sing. present, non-3d – take', 
            'VBZ verb, 3rd person sing. present – takes', 
            'WDT wh-determiner – which', 
            'WP wh-pronoun – who, what', 
            'WP$ possessive wh-pronoun, eg- whose', 
            'WRB wh-adverb, eg- where, when']
    for item in meaning:
        st.write(item)
    
    # POS_TAGGER_FUNCTION : TYPE 1
    def pos_tagger(nltk_tag):
        from nltk.corpus import wordnet
        from nltk import pos_tag, word_tokenize
        if nltk_tag.startswith('J'):
            return wordnet.ADJ
        elif nltk_tag.startswith('V'):
            return wordnet.VERB
        elif nltk_tag.startswith('N'):
            return wordnet.NOUN
        elif nltk_tag.startswith('R'):
            return wordnet.ADV
        else:         
            return None
    
    user_input2 = st.text_input('Enter a sentence to POS tag:', 'the cat is sitting with the bats on the striped mat under many flying geese')
    pos_tags = []
    with st.echo(code_location='below'): 
        if st.button("get POS tags"):
            from nltk import pos_tag, word_tokenize
            from nltk.stem import WordNetLemmatizer
            lemmatizer = WordNetLemmatizer()
            # tokenize the sentence and find the POS tag for each token
            st.write('POS tagged:')
            pos_tagged = pos_tag(word_tokenize(user_input2)) 
            st.write(pos_tagged)
            st.write('Wordnet tagged:')
            wordnet_tagged = list(map(lambda x: (x[0], pos_tagger(x[1])), pos_tagged))
            st.write('Wordnet tagged:')
            st.write(wordnet_tagged)
            lemmatized_sentence = []
            for word, tag in wordnet_tagged:
                if tag is None:
                    # if there is no available tag, append the token as is
                    lemmatized_sentence.append(word)
                else:       
                    # else use the tag to lemmatize the token
                    lemmatized_sentence.append(lemmatizer.lemmatize(word, tag))
            lemmatized_sentence = " ".join(lemmatized_sentence)
            st.write('Lemmatized sentence: ' + lemmatized_sentence)  
 
    
    
    with st.echo(code_location='below'): 
        user_input = st.text_input('Enter a sentence to lemmatize:', 'the bats saw the cats with best stripes hanging upside down by their feet')
        if st.button("Use Spacy to lemmatize"):
            import spacy
            spacy.cli.download("en_core_web_sm")
            nlp = spacy.load('en_core_web_sm')

            # Create a Doc object
            doc = nlp(u''+ user_input)

            # Create list of tokens from given string
            tokens = []
            for token in doc:
                tokens.append(token)
            st.write('Tokens:')
            st.write(tokens)
            lemmatized_sentence = " ".join([token.lemma_ for token in doc])
            st.write('Lemmatized sentence: ' + lemmatized_sentence)
    st.write('')

# run the app
if __name__ == "__main__":
    app()
