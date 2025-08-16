# streamlit_app.py
import streamlit as st
from gradio_client import Client

TOKEN = st.secrets["TOKEN"]

ID = st.secrets["ID"]

client = Client(ID, hf_token=TOKEN)

st.title("Electro Theme Documentation Assistant")

# Input from user
question = st.text_input("Ask your question:")

if st.button("Get Answer"):
    if question.strip():
        with st.spinner("Querying backend..."):
            try:
                # Call the /generate_answer API
                result = client.predict(
                    question=question,
                    api_name="/generate_answer"
                )
                st.markdown(result)
            except Exception as e:
                st.error(f"Error calling API: {e}")
    else:
        st.warning("Please enter a question.")
