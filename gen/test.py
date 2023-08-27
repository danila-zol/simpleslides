import requests

def translate_text(text):
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=ru&dt=t&q={text}"
    response = requests.get(url)
    data = response.json()
    return data[0][0][0] + "."

print(translate_text("This is a test"))