from langchain.llms import OpenAI
import from langchain-community
import streamlit as st
import os



# Paste your OpenAI API key here
OPEN_API_KEY = "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"
print(os.getenv("OPEN_API_KEY"))  # Should print your API key
# Function to get response from OpenAI
def get_openai_response(question):
    if not OPEN_API_KEY:
        raise ValueError("API key is missing. Please paste your OpenAI API key in the OPEN_API_KEY variable.")
    
    # Initialize the OpenAI model
    llm = OpenAI(
        openai_api_key=OPEN_API_KEY,  # Use the key directly
        model_name="gpt-4",
        temperature=0.5
    )
    response = llm(question)
    return response

# Streamlit app setup
st.set_page_config(page_title="Q&A Chatbot")
st.header("LangChain Q&A Chatbot")

# User input
user_input = st.text_input("Enter your question:")

# Button to submit the question
if st.button("Submit"):
    if not user_input.strip():
        st.error("Please enter a valid question.")
    else:
        st.subheader("Response:")
        with st.spinner("Generating response..."):
            try:
                response = get_openai_response(user_input)
                st.write(response)
            except Exception as e:
                st.error(f"An error occurred: {e}")
