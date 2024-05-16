
import os
import google.generativeai as genai
from dotenv import load_dotenv
import textwrap

# loads .env that will hold API key KEEP PRIVATE
load_dotenv()

# API key configuration
genai.configure(api_key=os.getenv("API_KEY"))

# Initialize the generative model
model = genai.GenerativeModel('gemini-pro')

def llm_advice(user_input):
  try:
    genai.configure(api_key=os.getenv("API_KEY"))

    # selects the gemini-pro model to send prompts to
    model = genai.GenerativeModel('gemini-pro')

    # enables chat feature to remeber past prompts
    chat = model.start_chat(history=[])

    with open(user_input, 'r') as file:
      user_data = file.read()


    chat.send_message(
      f" This is a presentation transcript I am working on\n\n {user_data}"
      )

    # chat.send_message(
    #   f"Remeber this list, this is a list of cards with their respective price, this list is called tcg player\n\n {tcg_player_output}"
    # )

    response = chat.send_message(
      "Please give advice on how to improve this presentation as well as give advice on public speaking."
    )


    with open("../data/processed/helper_advice.txt", 'w', encoding='utf-8') as file:
      file.write(f"{response.text}\n\n")
  
    
  except Exception as e:
    print(f"Error Summarizing: {str(e)}")