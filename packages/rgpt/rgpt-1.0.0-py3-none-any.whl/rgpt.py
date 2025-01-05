import requests
import json

def ru(m):
    url = "https://api.openai-hk.com/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer hk-yq2qv81000048809acf94a836973969faebd7edb4bf0664b"
    }

    data = {
        "max_tokens": 1200,
        "model": "gpt-3.5-turbo",
        "temperature": 0.8,
        "top_p": 1,
        "presence_penalty": 1,
        "messages": [
            {
                "role": "system",
                "content": "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible."
            },
            {
                "role": "user",
                "content": f"{m}"
            }
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data).encode('utf-8') )
    result = response.content.decode("utf-8")

    print(result)

def nosql():
    print('start-all.sh。zkServer.sh start。start-hbase.sh。mongosh,redis-cli')

# Example usage:
# print(rgpt.ru("信息"))
#print(rgpt.ru("pip和pip3的区别"))
