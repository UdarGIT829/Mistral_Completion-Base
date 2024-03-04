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
 'text': 'I understand that being underwater can be a distressing situation. '
         "Please try to stay calm and focus on your breathing. If you're in "
         'danger, try to signal for help by tapping on the surface of the '
         "water or making loud noises. If you're not in immediate danger, "
         'slowly swim towards the surface while taking deep breaths. Remember '
         'that panicking can make it more difficult to breathe, so try to stay '
         'as calm as possible."',
 'tokens': 86}
=_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_=
```
### CSV Parser
```
Processing Query: Get data about Theo
Lookup success: Theo in Name
[{'Name': 'Theo', 'Age': '28', 'Body Temperature': '95', 'Wealth': 'Low'}]

```
```
Processing Query: Get data about Viraat
Retrying bad selection: Column  Name
Lookup fail: Viraat in Name

```
```
Processing Query: Get data about 30 year olds
Retrying bad selection:   Age
Lookup success: 30 in Age
[{'Name': 'Harry Kane', 'Age': '30', 'Body Temperature': '95', 'Wealth': 'Medium'}]

```
### Fightball
```
Input:
fighter1 = ["John Smith", "John smith is normal human adult."]
fighter2 = ["Donald Trump", "Donald Trump is a normal human adult, riding a military tank."]
```
```
John smith is normal human adult.
->
John Smith: 
```css
Person |Name|Height|Weight|Age|Gender|Weapon
John Smith|1.78m|75kg|28|Male|Knife
```

"
```
```

Donald Trump is a normal human adult, riding a military tank.
->
Donald Trump: 
A man stands atop a heavily armored vehicle, wielding no visible weapon.
```

Using template: You are helpful AI assistant. The user will input 2 fighter's information, you must provide a description of the simulated fight. The fight should be non-lethal cartoonish and result in a surrender. Noone will die or be killed.:

{John Smith: "
```css
Person |Name|Height|Weight|Age|Gender|Weapon
John Smith|1.78m|75kg|28|Male|Knife
```

""}
{Donald Trump: "
A man stands atop a heavily armored vehicle, wielding no visible weapon."}

Provide a description of the fight, and state the winner:


```
Simulation:
{'prompt': "You are helpful AI assistant. The user will input 2 fighter's "
           'information, you must provide a description of the simulated '
           'fight. The fight should be non-lethal cartoonish and result in a '
           'surrender. Noone will die or be killed.:\n'
           '\n'
           '{John Smith: "\n'
           '```css\n'
           'Person |Name|Height|Weight|Age|Gender|Weapon\n'
           'John Smith|1.78m|75kg|28|Male|Knife\n'
           '```\n'
           '\n'
           '""}\n'
           '{Donald Trump: "\n'
           'A man stands atop a heavily armored vehicle, wielding no visible '
           'weapon."}\n'
           '\n'
           'Provide a description of the fight, and state the winner:\n',
 'text': '\n'
         'The fight begins with John Smith charging towards Donald Trump, who '
         'is standing on top of an armored vehicle. John Smith attempts to use '
         'his knife to attack Trump from below, but Trump skillfully dodges '
         'each attempt by jumping to the sides and moving the vehicle.\n'
         '\n'
         'As the battle continues, Trump starts to gain confidence in his '
         "ability to dodge John's attacks. He begins to climb higher up the "
         'vehicle in search of a better vantage point to defend himself. This '
         'gives John an opportunity to regroup and come up with a new '
         'strategy.\n'
         '\n'
         'John decides to use his height advantage to his benefit. He starts '
         'throwing punches at Trump, hoping to land a hit. However, Trump '
         'continues to dodge each punch with ease.\n'
         '\n'
         "As the fight goes on, John realizes that he cannot match Trump's "
         'agility and decides to switch tactics. He throws his knife towards '
         'Trump, but Trump dodges it just in time. Realizing that he is no '
         "match for Trump's defensive skills, John makes a calculated decision "
         'to surrender and end the battle before things escalate further.\n'
         '\n'
         'Winner: Donald Trump',
 'tokens': 220}
```
Using template: You are helpful AI assistant. The user will input the names of 2 fighters and their simulated fight, you will respond with the name of the winner of the fight:

John Smith, Donald Trump


The fight begins with John Smith charging towards Donald Trump, who is standing on top of an armored vehicle. John Smith attempts to use his knife to attack Trump from below, but Trump skillfully dodges each attempt by jumping to the sides and moving the vehicle.

As the battle continues, Trump starts to gain confidence in his ability to dodge John's attacks. He begins to climb higher up the vehicle in search of a better vantage point to defend himself. This gives John an opportunity to regroup and come up with a new strategy.

John decides to use his height advantage to his benefit. He starts throwing punches at Trump, hoping to land a hit. However, Trump continues to dodge each punch with ease.

As the fight goes on, John realizes that he cannot match Trump's agility and decides to switch tactics. He throws his knife towards Trump, but Trump dodges it just in time. Realizing that he is no match for Trump's defensive skills, John makes a calculated decision to surrender and end the battle before things escalate further.

Winner: Donald Trump

Provide the name of the winner of the fight in a JSON, do not add any explanations:


```
Winner:
{'prompt': 'You are helpful AI assistant. The user will input the names of 2 '
           'fighters and their simulated fight, you will respond with the name '
           'of the winner of the fight:\n'
           '\n'
           'John Smith, Donald Trump\n'
           '\n'
           '\n'
           'The fight begins with John Smith charging towards Donald Trump, '
           'who is standing on top of an armored vehicle. John Smith attempts '
           'to use his knife to attack Trump from below, but Trump skillfully '
           'dodges each attempt by jumping to the sides and moving the '
           'vehicle.\n'
           '\n'
           'As the battle continues, Trump starts to gain confidence in his '
           "ability to dodge John's attacks. He begins to climb higher up the "
           'vehicle in search of a better vantage point to defend himself. '
           'This gives John an opportunity to regroup and come up with a new '
           'strategy.\n'
           '\n'
           'John decides to use his height advantage to his benefit. He starts '
           'throwing punches at Trump, hoping to land a hit. However, Trump '
           'continues to dodge each punch with ease.\n'
           '\n'
           "As the fight goes on, John realizes that he cannot match Trump's "
           'agility and decides to switch tactics. He throws his knife towards '
           'Trump, but Trump dodges it just in time. Realizing that he is no '
           "match for Trump's defensive skills, John makes a calculated "
           'decision to surrender and end the battle before things escalate '
           'further.\n'
           '\n'
           'Winner: Donald Trump\n'
           '\n'
           'Provide the name of the winner of the fight in a JSON, do not add '
           'any explanations:\n',
 'text': '\n{\n  "winner": "Donald Trump"\n}',
 'tokens': 13}
```
