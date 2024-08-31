import requests

url = 'https://api.groq.com/openai/v1/chat/completions'
data = {"messages": [
           {
             "role": "user",
             "content":"Why is the sky blue?"
           }
         ],
         "model": "gemma-7b-it",
         "stream": False
       }

response = requests.post(url, json = data)

print(response.text)