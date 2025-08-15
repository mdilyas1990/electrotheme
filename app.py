# streamlit_app.py
import streamlit as st
from gradio_client import Client

# Get Hugging Face token securely from Streamlit Secrets
HF_TOKEN = st.secrets["HF_TOKEN"]

# Your private Hugging Face Space ID
SPACE_ID = "mdilyas1990/madrasthemes"

# Initialize Gradio client with token
client = Client(SPACE_ID, hf_token=HF_TOKEN)

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
