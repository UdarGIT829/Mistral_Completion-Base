import requests
from pprint import pprint

reponse = requests.get(url="http://127.0.0.1:9001/get_instruct_prompts")

prompts = reponse.json()
pprint(prompts)

querys = ["Hello, how are you? I am under the water, please help me."]

for query in querys:
    print(f"Processing query: {query}")
    reponse = requests.post(url="http://127.0.0.1:9001/make_prompt", 
        json={'template_name':"instruct template",
            'inputs':[query]
        }
    ).json()
    reponse = requests.post(url="http://127.0.0.1:9001/completion", 
        json={'text':reponse['result'],
            'temperature':0.2
        }
    ).json()
    print(reponse)
    print("=_="*20)