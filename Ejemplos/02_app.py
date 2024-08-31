"""
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt": "Why is the sky blue?",
  "stream": false
}' -o salida.md
"""
import requests
import json

url = 'https://api.groq.com/openai/v1/chat/completions'
data = {
    "messages": [
           {
             "role": "user",
             "content":"Why is the sky blue?"
           }
         ],
         "model": "gemma-7b-it",
         "stream": False}

headers={
  "Content-Type": "application/json",
  "Authorization": "Bearer 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"
}
response = requests.post(url, json = data, headers = headers)
response = json.loads(response.text)

print(response["response"])