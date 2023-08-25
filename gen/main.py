import openai


with open("gen/key.txt") as f:
  openai.api_key = f.read()

with open("gen/pd_text_request.txt") as f:
  pd_text_request_body = f.read()

with open("gen/pd_user_spec.txt") as f:
  pd_user_spec = f.read()

pd_text_request = f"{pd_text_request_body}\n{pd_user_spec}"

# requests

completion = openai.ChatCompletion.create(
 model="gpt-3.5-turbo", 
 messages=[{"role": "user", "content": "What is the OpenAI mission?"}]
)

pitch_deck_text = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[{"role": "user", "content": f"{pd_text_request}"}]
)

# functions

def aitest():
  print("API key is", openai.api_key)
  print(completion)

def get_pd_text():
  print(pitch_deck_text)