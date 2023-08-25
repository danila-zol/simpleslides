import openai

with open("gen/key.txt") as f:
  openai.api_key = f.read()

# requests

completion = openai.ChatCompletion.create(
 model="gpt-3.5-turbo", 
 messages=[{"role": "user", "content": "What is the OpenAI mission?"}]
)

# functions

def aitest():
  print("API key is", openai.api_key)
  print(completion)

