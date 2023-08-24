import openai

openai.api_key = ""

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": "What is the OpenAI mission?"}]
)
def aitest():
    print(completion)