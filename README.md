# Mistral_Completion-Base
[![CI](https://github.com/UdarGIT829/Mistral_Completion-Base/actions/workflows/ci.yml/badge.svg)](https://github.com/UdarGIT829/Mistral_Completion-Base/actions/workflows/ci.yml)
## Overview
This is a modular text-completion server based on https://github.com/mistralai/mistral-src

By providing a barebones text-completion service via API, the systems for constructing prompts are free to control by a user. Currently available software for this purpose is geared towards being feature rich, and as a result becomes quite bloated. 

To adapt the outputs to your purposes, you can create/modify an existing instruct template or make your own.

## Installation
To install, run the following command:
```ps
pip install -r requirements.txt
```

## Usage

### Starting the application server
```ps
>   python app.py 
```

For further usage, see `test.py` for specific examples.

## Modules
To extend functionality with your own module, you must make a `get_template()` function
See `.modules/instr_cls.py` for the class definition of the return type, or see `modules/template_module/generic_template.py` for a simplified example.
## Execution Results
### Generic Template
```
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
 'text': '\n'
         'It sounds like you may be in an unusual situation! Can you provide '
         'more information or context about your location and what assistance '
         'you need?"',
 'tokens': 28}
=_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_=
```
### CSV Parser
```
Processing Query: Get data about Theo
Retrying bad selection: Name   Explanation  The user wants information about Theo and it s most likely they would like to know the name associated with them in our records
Retrying bad selection: Column  Name
Lookup success: Theo in Name
[{'Name': 'Theo', 'Age': '28', 'Body Temperature': '95', 'Wealth': 'Low'}]

```
```
Processing Query: Get data about Viraat
Retrying bad selection:     Name
Lookup fail: Viraat in Name

```
```
Processing Query: Get data about 30 year olds
Lookup success: 30 in Age
[{'Name': 'Harry Kane', 'Age': '30', 'Body Temperature': '95', 'Wealth': 'Medium'}]

```
