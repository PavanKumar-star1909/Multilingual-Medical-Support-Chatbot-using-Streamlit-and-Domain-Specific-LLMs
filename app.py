
import streamlit as st
from src.translator import translate_text, detect_language
from src.medical_llm import generate_medical_response
from src.utils import medical_disclaimer

st.set_page_config(page_title="Multilingual Medical Support Chatbot", layout="centered")

st.title("🩺 Multilingual Medical Support Chatbot")
st.markdown(medical_disclaimer())

user_input = st.text_area("Enter your medical query in any language")

if st.button("Get Medical Guidance"):
    if user_input.strip() == "":
        st.warning("Please enter a query")
    else:
        src_lang = detect_language(user_input)
        translated_input = translate_text(user_input, src_lang, "en")
        response_en = generate_medical_response(translated_input)
        final_response = translate_text(response_en, "en", src_lang)

        st.subheader("Response")
        st.write(final_response)
