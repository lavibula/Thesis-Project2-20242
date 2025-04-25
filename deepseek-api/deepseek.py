import random
from openai import OpenAI

def get_response (config, list_prompts):
    
    prompt = random.choice(list_prompts)

    # Khởi tạo Client
    client = OpenAI(
        api_key = config["apiKey"], 
        base_url = config["apiEndpoint"]
    )

    # Yêu cầu chat
    response = client.chat.completions.create(
        model = config["modelName"],
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            { 
                "role": "user", 
                "content": prompt
            },
        ],
        temperature = config["temperature"],
        stream=False
    )

    return response.choices[0].message.content