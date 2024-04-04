import streamlit as st
import spacy
#from spacy import displacy
#from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()
from pprint import pprint

st.title("Named Entity Recognizer")

st.info("This app will take an input from the user and then prints the named entities")

text = st.text_area("Enter a paragraph")

if(st.button("Submit")):
    doc = nlp(text)
    st.success([(X.text, X.label_) for X in doc.ents])
    #st.success("Button clicked")