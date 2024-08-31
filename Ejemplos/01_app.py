"""
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt": "Why is the sky blue?",
  "stream": false
}' -o salida.md
"""
import requests
import json

url = 'http://localhost:11434/api/generate'
data = {
    "model": "tinyllama",
    "prompt": "why is the sky?",
    "stream": False}

response = requests.post(url, json = data)
response = json.loads(response.text)

print(response["response"])