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
print(f"Prompts:")
pprint(prompts)


querys = ["Hello, how are you? I am under the water, please help me."]
try:
    for query in querys:
        print(f"Processing query: {query}")
        reponse = requests.post(url="http://127.0.0.1:9001/make_prompt", 
            json={'template_name':"instruct template",
                'inputs':[query]
            }
        ).json()

        print(f"Using template: {reponse['result']}")
        reponse = requests.post(url="http://127.0.0.1:9001/completion", 
            json={'text':reponse['result'],
                'temperature':0.2
            }
        )
        print(reponse.status_code)
        print(reponse.json())
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
    import csv
    from collections import Counter
    from nltk.tokenize import word_tokenize
    from nltk.tag import pos_tag
    import nltk
    import re

    def extract_lookup_value(query):
        # Define a list of words to ignore
        ignore_words = ['get', 'about']
        
        # Tokenize and tag the query
        tokens = word_tokenize(query)
        tagged_tokens = pos_tag(tokens)
        
        # Initialize variables to store potential lookup values
        number = None
        proper_noun = None
        
        # Regex to find numbers
        numbers = re.findall(r'\b\d+\b|\b\d+\.\d+\b', query)
        if numbers:
            number = numbers[0]
        
        # Look for proper nouns and numbers
        for word, tag in tagged_tokens:
            # Skip words in the ignore list
            if word.lower() in ignore_words:
                continue
            if tag == 'NNP':  # Find the first proper noun not in the ignore list
                proper_noun = word
                break  # Stop at the first match
            elif tag == 'CD' and not number:  # This is just a fallback in case regex missed something
                number = word
                break  # Stop at the first match
        
        # Prioritize proper noun over numbers if found
        return proper_noun if proper_noun else number

    def find_in_csv(filename, lookup_value, column_name):
        results = []
        with open(filename, newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Assuming the lookup_value is a string; adjust the condition based on your data
                if str(row[column_name]).lower() == str(lookup_value).lower():
                    results.append(row)
        return results
    def infer_datatype(value):
        """
        Infers the datatype of a given value.
        Tries to convert the value to different Python data types.
        """
        try:
            int(value)
            return 'int'
        except ValueError:
            pass
        
        try:
            float(value)
            return 'float'
        except ValueError:
            pass
        
        return 'str'  # Default to string if other conversions fail

    def process_csv_headers(filename):
        header_info = dict()
        
        with open(filename, mode='r', newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            headers = reader.fieldnames
            
            # Initialize counters and datatype tracking
            counters = {header: Counter() for header in headers}
            datatypes = {header: None for header in headers}
            
            for row in reader:
                for header in headers:
                    value = row[header]
                    counters[header][value] += 1
                    
                    if datatypes[header] is None:
                        # Infer datatype only if it has not been set
                        datatypes[header] = infer_datatype(value)
                    
            # Compile header information
            for header in headers:
                unique_values = len(counters[header])
                datatype = datatypes[header]
                header_info[header] = {"datatype": datatype, "unique": unique_values}
        
        return header_info

    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')

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
except Exception as err:
    print("Something when wrong with the execution, but I mean, it got this far *shrug*")
    print(f"Error: {err}")