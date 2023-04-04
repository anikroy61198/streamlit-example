import streamlit as st
import openai

# Define API key and endpoint URL
API_KEY = apikey.API_KEY
#ENDPOINT = 'https://api.openai.com/v1/engines/davinci-codex/completions'

# Set up OpenAI API
openai.api_key = API_KEY

# Define function to generate response from API
def generate_response(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

# Define Streamlit app
def app():
    st.title('Ask Solvaphile')

    # Allow user to enter a prompt
    prompt = st.text_input('Enter a prompt:', '')

    # Generate response when user clicks button
    if st.button('Generate'):
        response = generate_response(prompt)
        st.text_area('Response:', value=response, height=200)

if __name__ == '__main__':
    app()
