# llm_AFCC
Repositorio de trabajo con modelos de lenguaje largo usando ollama
# 1. Instalación de Ollama

Para instalar ollama accedemos a la pagina de [ollama](https://ollama.com/download/linux), en una terminal se ejecuta el siguiente comando

````bash
$ curl -fsSL https://ollama.com/install.sh | sh
````
## 2. Ejecutar el servidor

Una vez instalado se ejecuta el servidor ollama con el siguiente comando

````bash
$ ollama serve
````
## 3. Ingreso a otra terminal

Ejecutar Ollama en un server va a ocupar la terminal que teniamos, para seguir trabajando debemos crear una nueva terminal. De esta forma tendremos dos terminales

- Ollama: donde se va a ejecutar Ollama
- Bash: DONDE VAMOS A COMUNICARNOS CON Ollama

## 4. Descargar algún modelo

En la página de [modelos](https://ollama.com/library) de ollama se busca el modelo deseado y se descargar con el siguiente comando:

````bash
$ ollama pull tinyllama
````
## 5. Prueba de Request a la API REST
Para realizar una petición basica a la API de ollama se sigue la siguiente estructura
```` bash
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt": "Why is the sky blue?"
}'
````
Ver el JASON generado por tokens
```` bash
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt": "Why is the sky blue?"
}' -o salida.md
````
Ver el JASON generado, pero todos los tokens en conjunto
````bash
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt": "Why is the sky blue?",
  "stream": false
}' -o salida.md
````
### 6. Realizar un Request a GROQ
### 6.1 Cargar API KEY
Se debe cargar en la terminal el correspondiente api key para poder utilizar posteriormente GROQ
````bash
export GROQ_API_KEY=<your-api-key-here>
````
### 6.2 Cargar API
Ahora si se procede a cargar la API junto con nuestra consulta
````bash
curl "https://api.groq.com/openai/v1/chat/completions" \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${GROQ_API_KEY}" \
  -d '{
         "messages": [
           {
             "role": "user",
             "content":"Why is the sky blue?"
           }
         ],
         "model": "gemma-7b-it",
         "stream": false
       }'
````
### 7. Cargar una API con Python
````bash
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
````