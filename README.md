# Mistral_Completion-Base
This is a modular text-completion server based on https://github.com/mistralai/mistral-src

## Overview


## Installation
To install, run the following command:
```ps
pip install -r requirements.txt
```

## Usage
See `test.py` for specific usage examples

## Modules
To extend functionality with your own module, you must make a `get_template()` function
See `.modules/instr_cls.py` for the class definition of the return type, or see `modules/template_module/generic_template.py` for a simplified example.

### Generic Template
```ps
>   python .\test.py
'Processing query: Hello, how are you? I am under the water, please help me.'

Using template: [INST] You are a helpful AI assistant. You will think outside of the box to help the user with their request:
Hello, how are you? I am under the water, please help me.
[/INST]
Assistant: "


Response status code: 200
Response JSON:
{'prompt': '[INST] You are a helpful AI assistant. You will think outside of ' 
           'the box to help the user with their request:\n'
           'Hello, how are you? I am under the water, please help me.\n'       
           '[/INST]\n'
           'Assistant: "\n',
 'text': "I understand that you may be in an unusual situation, but don't "    
         "worry, I'm here to help. Can you tell me where you are exactly so I "
         'can send assistance your way?"',
 'tokens': 38}
=_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_=
```

### CSV Parser
```ps
>   python .\test.py
[nltk_data] Downloading package punkt to
[nltk_data]     C:\Users\Vudar\AppData\Roaming\nltk_data...
[nltk_data]   Package punkt is already up-to-date!
[nltk_data] Downloading package averaged_perceptron_tagger to
[nltk_data]     C:\Users\Vudar\AppData\Roaming\nltk_data...  
[nltk_data]   Package averaged_perceptron_tagger is already up-to-
[nltk_data]       date!
Processing Query: Get data about Theo
Retrying bad selection: Theo s data is stored in the  Name  column
****************************************************************************************************
Lookup success!
[{'Name': 'Theo', 'Age': '28', 'Body Temperature': '95', 'Wealth': 'Low'}]
****************************************************************************************************
Processing Query: Get data about Viraat
----------------------------------------------------------------------------------------------------
Lookup fail: Viraat in Name
----------------------------------------------------------------------------------------------------
Processing Query: Get data about 30 year olds
Retrying bad selection: Age   This response shows that you will search for information about    year olds in the  Age  column
****************************************************************************************************
Lookup success!
[{'Name': 'Harry Kane', 'Age': '30', 'Body Temperature': '95', 'Wealth': 'Medium'}]
****************************************************************************************************
```