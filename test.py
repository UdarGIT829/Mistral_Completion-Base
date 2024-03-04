import requests
from pprint import pprint


print("""### Generic Template""")

reponse = requests.get(url="http://127.0.0.1:9001/get_instruct_prompts")

prompts = reponse.json()
# print(f"Prompts:")
# pprint(prompts)


querys = ["Hello, how are you? I am under the water, please help me."]
try:
    for query in querys:
        print("```")
        pprint(f"Processing query: {query}")
        print()
        reponse = requests.post(url="http://127.0.0.1:9001/make_prompt", 
            json={'template_name':"instruct template",
                'inputs':[query]
            }
        ).json()

        print(f"Using template: {reponse['result']}")
        print()
        reponse = requests.post(url="http://127.0.0.1:9001/completion", 
            json={'text':reponse['result'],
                'temperature':0.2
            }
        )
        print(f"Response status code: {reponse.status_code}")
        print(f"Response JSON:")
        pprint(reponse.json())
        print("=_="*20)
        print("```")
except Exception as err:
    print("Something when wrong with the Generic Template execution, but I mean, it got this far *shrug*")
    raise(err)
    
    
print("""### CSV Parser""")


import re
import requests
from modules.csv_parser_module.process_csv import process_csv_headers, extract_lookup_value, find_in_csv
import modules.prompt_defs
try:
    # Example usage
    filename = './modules/csv_parser_module/data/dataset.csv'
    header_info = process_csv_headers(filename)
    # print(header_info)

    reponse = requests.get(url="http://127.0.0.1:9001/get_instruct_prompts")

    prompts = reponse.json()
    # pprint(prompts)

    querys = ["Get data about Theo", "Get data about Viraat", "Get data about 30 year olds"]
    for query in querys:
        print("```")
        print(f"Processing Query: {query}")

        _features = list(header_info.keys())

        chosen_feature = None
        exhaust = 3
        while chosen_feature not in _features:
            reponse = requests.post(url="http://127.0.0.1:9001/make_prompt", 
                json={'template_name':"Determine Header",
                    'inputs':[query, str(header_info)]
                }
            ).json()

            # pprint(reponse)
            # exit()
            reponse = requests.post(url="http://127.0.0.1:9001/completion", 
                json={'text':reponse['result'],
                    'temperature':0.2
                }
            ).json()

            # pprint(reponse)


            chosen_feature = re.sub('[^A-Za-z]', ' ', reponse['text']).strip().replace("Column Name","")

            if chosen_feature not in _features:
                print(f"Retrying bad selection: {chosen_feature}")
                exhaust -= 1
                if exhaust <= 0:
                    print("Giving up :(")
                    exit()

        lookup_value = extract_lookup_value(query).strip()
        # print(lookup_value)
        result = find_in_csv(filename=filename, lookup_value=lookup_value, column_name=chosen_feature)

        if len(result)>0:
            print(f"Lookup success: {lookup_value} in {chosen_feature}")
            print(result)
            print()
        else:
            print(f"Lookup fail: {lookup_value} in {chosen_feature}")
            print()
        print("```")
except Exception as err:
    print("Something when wrong with the execution, but I mean, it got this far *shrug*")
    raise(err)




print("""### Fightball""")


# For the sake of clarity, print the input data of the fighters
print("```")
print("Input:")
print("""fighter1 = ["John Smith", "John smith is normal human adult."]""")
print("""fighter2 = ["Donald Trump", "Donald Trump is a normal human adult, riding a military tank."]""")
fighter1 = ["John Smith", "John smith is normal human adult."]
fighter2 = ["Donald Trump", "Donald Trump is a normal human adult, riding a military tank."]
print("```")


reponse = requests.post(url="http://127.0.0.1:9001/make_prompt", 
    json={'template_name':"fightball character description",
        'inputs':[fighter1[1]]
    }
).json()

# print(f"Using template: {reponse['result']}")
# print()
reponse = requests.post(url="http://127.0.0.1:9001/completion", 
    json={'text':reponse['result'],
        'temperature':0.2
    }
).json()
fighter1Description = reponse['text'] if len(reponse['text']) > len(fighter1[1]) else fighter1[1]


fighter1.append(fighter1Description)

# print()

reponse = requests.post(url="http://127.0.0.1:9001/make_prompt", 
    json={'template_name':"fightball character description",
        'inputs':[fighter2[1]]
    }
).json()

# print(f"Using template: {reponse['result']}")
# print()
reponse = requests.post(url="http://127.0.0.1:9001/completion", 
    json={'text':reponse['result'],
        'temperature':0.2
    }
).json()
fighter2Description = reponse['text'] if len(reponse['text']) > len(fighter2[1]) else fighter2[1]


fighter2.append(fighter2Description)

print("```")
print(fighter1[1])
print("->")
print(f"{fighter1[0]}: {fighter1Description}")
print("```")
print("```")
print()

print(fighter2[1])
print("->")
print(f"{fighter2[0]}: {fighter2Description}")
print("```")
print()

reponse = requests.post(url="http://127.0.0.1:9001/make_prompt", 
    json={'template_name':"fightball simulate",
        'inputs':[fighter1[0],fighter1Description,fighter2[0],fighter2Description]
    }
).json()

print(f"Using template: {reponse['result']}")
print()
reponse = requests.post(url="http://127.0.0.1:9001/completion", 
    json={'text':reponse['result'],
        'temperature':0.2
    }
).json()


print("```")
print("Simulation:")
pprint(reponse)
print("```")

reponse = requests.post(url="http://127.0.0.1:9001/make_prompt", 
    json={'template_name':"fightball eval",
        'inputs':[fighter1[0],fighter2[0],reponse['text']]
    }
).json()

print(f"Using template: {reponse['result']}")
print()
reponse = requests.post(url="http://127.0.0.1:9001/completion", 
    json={'text':reponse['result'],
        'temperature':0.2
    }
).json()

# Eventually put a looping condition here so that if the winner is not found in the response it will resimulate the fight
print("```")
print("Winner:")
pprint(reponse)
print("```")