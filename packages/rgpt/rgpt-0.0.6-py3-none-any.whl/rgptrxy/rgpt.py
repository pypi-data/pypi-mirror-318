import requests
import json

class rgpt:
    url = "https://api.openai-hk.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer hk-yq2qv81000048809acf94a836973969faebd7edb4bf0664b"
    }

    @staticmethod
    def ru(message):
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
                    "content": message
                }
            ]
        }

        response = requests.post(rgpt.url, headers=rgpt.headers, data=json.dumps(data).encode('utf-8'))
        result = response.content.decode("utf-8")
        data_dict = json.loads(result)

        # 提取特定的内容
        content = data_dict['choices'][0]['message']['content']

        # 返回结果
        return result
    def nosql():
        print('start-all.sh。zkServer.sh start。start-hbase.sh。mongosh,redis-cli')

# Example usage:
# print(rgpt.ru("信息"))
#print(rgpt.ru("pip和pip3的区别"))
