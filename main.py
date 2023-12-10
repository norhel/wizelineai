import streamlit as st
from decouple import config
from openai import OpenAI

response = False
prompt_tokens = 0
completion_tokes = 0
total_tokens_used = 0
cost_of_response = 0

API_KEY = config('OPENAI_API_KEY')

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    # or you can explicitly pass in the key (NOT RECOMMENDED)
    #api_key=os.getenv("OPENAI_API_KEY"),
    api_key = API_KEY,
)

def make_request(question_input: str):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {
                "role": "system",
                "content": "Act as a Bach's flower qualified remedy practioner."},
            {
                "role": "user",
                "content": f"{question_input}"
            }
            
        ]
    )
    return response


st.header("Welcome to the Bach's Flower Remedy Recommendation System, using OpenAI ChatGPT API")

st.markdown("""---""")

question_input = st.text_input("Enter the description of how the Patient is feeling: ")
rerun_button = st.button("Rerun")

user_request = "Generate in English and Spanish, a list of the 7 flowers needed for a remedy to treat a patient. The patient is feeling "

st.markdown("""---""")

if question_input:
    response = make_request(user_request + question_input)
else:
    pass

if rerun_button:
    response = make_request(user_request + question_input)
else:
    pass

if response:
    st.write("Response:")
    st.write(response.model_dump()['choices'][0]['message']['content'])

else:
    pass


