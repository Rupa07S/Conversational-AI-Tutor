import streamlit as st
import google.generativeai as genai
import os

os.environ["GEMINI_API_KEY"] = "Geminiapi_key"

if "messages" not in st.session_state:
    st.session_state.messages = []

def generate_response(user_prompt):
    """Generates a response using the Gemini model."""
    try:
        genai.configure(api_key=os.environ["Geminiapi_key"])
        model = genai.GenerativeModel("gemini-1.5-pro-latest", system_instruction="You are a Data Science Tutor assisting with data science queries")
        chat = model.start_chat(history=[])

        if user_prompt:
            response = chat.send_message(user_prompt)
            return response.text
    except Exception as e:
        st.write("Error occurred while accessing the API:", e)
        return None

def main():
    st.title("Data Science Tutor")

    if user_prompt := st.text_input("Enter your data science query here"):
        st.session_state.messages.append({"role": "user", "content": user_prompt})

        with st.spinner("Thinking..."):
            response_text = generate_response(user_prompt)

        if response_text:
            st.session_state.messages.append({"role": "tutor", "content": response_text})
            st.write("Tutor:", response_text)
        else:
            st.write("Sorry, I couldn't generate a response. Please try again.")

if __name__ == "__main__":
    main()
