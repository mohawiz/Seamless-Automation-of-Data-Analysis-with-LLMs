# Import necessary libraries
import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from langchain_groq.chat_models import ChatGroq
import seaborn as sns


# Title for the Streamlit app
st.title("Seamless Automation Of Data Analysis with LLMs")

# File uploader for CSV files
uploaded_file = st.file_uploader("Please Upload a CSV file", type=['csv'])

# API Key for Groq
GROQ_API_KEY = ""

# Instantiate the Groq LLM
llm = ChatGroq(model_name="llama-3.1-70b-versatile", api_key=GROQ_API_KEY)

# When a file is uploaded
if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    st.write(df.head(10))  # Display the first 10 rows

    # Create a SmartDataframe to use with the LLM
    data_chat = SmartDataframe(df, config={"llm": llm})

    # Input for the user to type a prompt
    prompt = st.text_area("Enter your prompt:")

    # When the 'Generate' button is clicked
    if st.button("Generate"):
        if prompt:
            with st.spinner("Generating Response..."):
                # Generate insights using the LLM and the dataframe
                result = data_chat.chat(prompt)
                st.write(result)  # Display the result
        else:
            st.warning("Please enter a prompt")
