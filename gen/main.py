import openai

q1 = ["SimpleCoffe"]
q2 = ["A coffehop"]
q3 = ["Saint-Petersburg, Russia"]
q4 = [{"age":"all ages", "gender":"all genders", "location":"Saint-Petersburg", "interests":""}]
q5 = [{"name":"Daria Ivanova",  "expertise":"Barista"}, {"name":"Dmitry Petrov", "expertise": "accountant"}]
q6 = ["monthly proffit of 25000 rubles, 30000 visitors per month"]
q7 = ["connect to us directly using the number 123456789"]
q9 = [""]
q10 = ["200 symbols"]
q11 = ["10 million rubles"]
q12 = ["1 year"]



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

