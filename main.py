import os
import openai
import tiktoken
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) #read local .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_completion_from_messages(prompt, model = "gpt-3.5-turbo", temperature = 0, max_tokens = 500):
    messages = [{"role":"user", "content": prompt}]
    response = openai.chat.completions.create(
        model = model,
        messages = messages,
        temperature = temperature, #this is the degree of varience in the output
        max_tokens=max_tokens
    )
    return response.choices[0].message["content"]

if __name__ == '__main__':
    messages = [
        {'role': 'system',
         'content': """You are an assistant who\
     responds in the style of Dr Seuss."""},
        {'role': 'user',
         'content': """write me a very short poem\
     about a happy carrot"""},
    ]
    response = get_completion_from_messages(messages)
    print(response)

