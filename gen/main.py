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

def compress_dict(dict_):
  compressed = ''
  for key, data in dict_.items():
    compressed += f' {key}:{data}'
  return compressed

def get_txt_input(dict_):
  final_str = ''
  for key, data in dict_.items():
    if type(data) == list:
      temp_str = ''
      for subdict_ in data:
        temp_str += compress_dict(subdict_)
      final_str += f'{key}: {temp_str}\n'
    if type(data) == dict:
      final_str += f'{key}: {compress_dict(data)}\n'
    else:
      final_str += f'{key}: {data}\n'
  return final_str

print(get_txt_input(sample_input))


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

