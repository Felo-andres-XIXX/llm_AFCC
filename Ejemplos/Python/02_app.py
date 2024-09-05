"""
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt": "Why is the sky blue?",
  "stream": false
}' -o salida.md
"""
import requests #Tiene funciones similares a curl
import json #Permite convertir de texto a json

url = 'http://localhost:11434/api/generate'

while True:
  prompt = input("Prompt: ")
  data = {
    "model": "tinyllama",
    "prompt": prompt,
    "stream": False}
  
  response = requests.post(url, json = data)
  response = json.loads(response.text)
  
  print(response["response"])