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

Se van a haber creador dos terminales, una se llama Serve y la nueva es un bash

## 4. Descargar algún modelo

En la página de [modelos](https://ollama.com/library) de ollama se busca el modelo deseado y se descargar con el siguiente comando:

````bash
$ ollama pull tinyllama
````
## 4. Prueba de Request a la API REST
Para realizar una petición basica a la API de ollama se sigue la siguiente estructura
```` bash
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt": "Why is the sky blue?"
}'
````