import streamlit as st

enable = st.checkbox("Enable camera")
picture = st.camera_input("Take a picture", disabled=not enable)

key = st.sidebar.text_input("Your Api Key")


if picture:
    st.image(picture)