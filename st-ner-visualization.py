import streamlit as st
import spacy
from spacy import displacy
#from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()
from pprint import pprint

st.title("Named Entity Recognizer")

st.info("This app will take an input from the user and then prints the named entities")

text = st.text_area("Enter a paragraph")

if(st.button("Submit")):
    doc = nlp(text)
    ent_html = displacy.render(doc, style="ent", jupyter=False)
    # Display the entity visualization in the browser:
    st.markdown(ent_html, unsafe_allow_html=True)