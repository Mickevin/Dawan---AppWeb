import streamlit as st
from utiles import Proccessing

openai_key = st.sidebar.text_input("Entez votre clé OpenAI")
prompt = st.text_input("Entez votre texte")


if st.button("Envoyer"):
    process = Proccessing()
    st.write(process.trad_with_openai(prompt, openai_key))