from deepseek import get_response

config = {
    "apiKey" : "ollama", # Ollama
    "apiEndpoint" : "http://localhost:11434//api", # Ollama base url
    "modelName" : "deepseek-r1:7b",
    "temperature" : "0.7"    
}
list_prompts = []

response = get_response(config, list_prompts)
print(response)
