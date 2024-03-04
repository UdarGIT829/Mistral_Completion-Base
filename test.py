import requests
from pprint import pprint

#
#
#
#
#
"""
Example code for Generic Instruction Template
"""
reponse = requests.get(url="http://127.0.0.1:9001/get_instruct_prompts")

prompts = reponse.json()
# pprint(prompts)

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

#
#
#
#
#
"""
Example code for CSV Parser Instruct Template
"""
import re
import requests
from modules.csv_parser_module.process_csv import process_csv_headers, extract_lookup_value, find_in_csv
import modules.prompt_defs

# Example usage
filename = 'modules/csv_parser_module/data/dataset.csv'
header_info = process_csv_headers(filename)
# print(header_info)

reponse = requests.get(url="http://127.0.0.1:9001/get_instruct_prompts")

prompts = reponse.json()
# pprint(prompts)

querys = ["Get data about Theo", "Get data about Viraat", "Get data about 30 year olds"]
for query in querys:
    # print(query)

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

    lookup_value = extract_lookup_value(query)
    # print(lookup_value)
    result = find_in_csv(filename=filename, lookup_value=lookup_value, column_name=chosen_feature)

    if len(result)>0:
        print("*"*100)
        print("Lookup success!")
        print(result)
        print("*"*100)
    else:
        print("-"*100)
        print(f"Lookup fail: {lookup_value} in {chosen_feature}")
        print("-"*100)