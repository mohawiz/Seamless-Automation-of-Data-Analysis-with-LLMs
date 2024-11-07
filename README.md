# Seamless-Automation-of-Data-Analysis-with-LLMs
This project is a Streamlit application that leverages Groq’s LLM (specifically, the "Llama 3.1 70B Versatile" model) to enable seamless automation of data analysis. Users can upload a CSV file and interactively query the data through natural language prompts. The app automatically generates insights and data summaries based on the prompts, simplifying data exploration and analysis tasks.
Features
File Upload: The application allows users to upload a CSV file, which will be displayed in the app for a quick overview of the data.
Smart Dataframe with LLM Integration: The code uses pandasai’s SmartDataframe to create an intelligent dataframe that can interact with an LLM. The integration with Groq's LLM model enables dynamic data analysis based on user prompts.
Interactive Querying: Users can enter prompts in natural language to request specific insights or analysis. For example, users can ask for data summaries, statistical insights, or visualizations.
Responsive Design: The application includes a spinner that indicates when the LLM is generating a response, enhancing the user experience.
# Technologies Used
Streamlit: Provides a fast and user-friendly web interface for data interaction.
Pandas: For loading and basic manipulation of the uploaded CSV file.
PandasAI (SmartDataframe): A wrapper around pandas to make it compatible with language models for natural language-based queries.
Groq's Llama 3.1 Model: The LLM model used to interpret user prompts and generate data insights.
Seaborn: Imported for potential data visualization tasks (but currently not utilized in this code).
# Requirements
API Key: Requires a Groq API key, which is provided in the GROQ_API_KEY variable for secure access of the LLM.Usage
Upload CSV File: Start by uploading a CSV file through the file uploader.
Preview Data: The app will display the first 10 rows of the data for an initial preview.
Enter Prompt: Type a prompt in the text area to request an analysis or insight about the dataset.
Generate Response: Click on "Generate" to receive insights powered by the LLM based on the provided prompt.
# Code Overview
Libraries and Initialization: Imports necessary libraries and initializes the Streamlit app.
API Key Configuration: Uses a predefined API key for connecting to Groq’s LLM.
Smart Dataframe Creation: Wraps the dataframe in a SmartDataframe to enable LLM-based querying.
Prompt Processing: When the user enters a prompt and clicks "Generate," the app processes the request using the LLM and returns the result.
# Future Enhancements
Data Visualization: Implement more advanced visualization options using Seaborn based on user prompts.
Error Handling: Add error handling for different types of prompts and malformed datasets.
Additional LLM Configurations: Enable configuration options for different LLMs or models based on user preferences.
