import openai

sample_input = { 'company_name' : 'SimpleCoffe',
                'business_type' : 'A coffeeshop', 
                'target market': 'Saint-Petersburg, Russia',
                'target audience': {"age":"all ages", "gender":"all genders", "location":"Saint-Petersburg", "interests":""},
                'project team': [{"name":"Daria Ivanova",  "expertise":"Barista"}, {"name":"Dmitry Petrov", "expertise": "accountant"}],
                'The project have already achieved': "monthly proffit of 25000 rubles, 30000 visitors per month",
                'information': "connect to us directly using the number 123456789", 
                'investment target': 'aquiring new equipment, making better product, doubbling our revenue',
                'investment amount': '10 million rubles', 
                'deadline on investment promises': '1 year',
                'length(symbols)': '200'} 

text_sample_input = str(sample_input)
print(text_sample_input)

with open("gen/key.txt") as f:
  openai.api_key = f.read()

completion = openai.ChatCompletion.create(
 model="gpt-3.5-turbo", 
 messages=[{"role": "user", "content": "What is the OpenAI mission?"}]
)
def aitest():
  print("API key is", openai.api_key)
  print(completion)