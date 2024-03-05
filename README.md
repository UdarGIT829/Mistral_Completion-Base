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
Mistral has a nasty tendency to get creative with formatting when you ask for a JSON. Please excuse the formatting issues after this point, as the following is the output of my CI/CD testing pipeline.
### Generic Template
```
Processing query: Hello, how are you? I am under the water, please help me.

Response status code: 200
Response JSON:
{'prompt': '[INST] You are a helpful AI assistant. You will think outside of the box to help the user with their request:[/INST]\nUser: "Hello, how are you? I am under the water, please help me."\nAssistant: "\n', 'text': '[INST]I understand that you may be in an unusual situation, but don\'t worry. Here are some steps to follow to get yourself out of this situation safely.[/INST] 1. Try to stay calm and composed; taking deep breaths can help reduce panic. 2. If possible, swim towards the surface or a source of light. 3. If you have any flotation devices, such as a life jacket or inflatable object, use them to keep yourself afloat. 4. Call for help if there are others nearby who can assist you in getting out of the water safely."\n\nIn general, I would suggest being cautious when around water and ensuring that you have proper safety precautions in place whenever possible. This will hopefully help minimize instances where you may find yourself underwater unexpectedly.', 'tokens': 158}
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
Lookup fail: Viraat in Name

```
```
Processing Query: Get data about 30 year olds
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
John Smith: ```lua
function JohnSmith()
    local height = 1.75 -- 1.75m height, human standard
    local weight = 70 -- 70kg, average weight for a male of his height
    local stamina = 8 -- average stamina
    local strength = 6 -- average strength
end
```
"
```

```
Donald Trump is a normal human adult, riding a military tank.
->
Donald Trump: The individual stands at an average height for a male adult. He wears a suit and tie, which is typical attire for formal events. In his hand he carries a pen, a symbol of power and authority.
```

```
Simulation:
{'prompt': 'You are helpful AI assistant. The user will input 2 fighter\'s information, you must provide a description of the simulated fight. The fight should be non-lethal cartoonish and result in a surrender. Noone will die or be killed.:\n\n{John Smith: "```lua\nfunction JohnSmith()\n    local height = 1.75 -- 1.75m height, human standard\n    local weight = 70 -- 70kg, average weight for a male of his height\n    local stamina = 8 -- average stamina\n    local strength = 6 -- average strength\nend\n```\n""}\n{Donald Trump: "The individual stands at an average height for a male adult. He wears a suit and tie, which is typical attire for formal events. In his hand he carries a pen, a symbol of power and authority."}\n\nProvide a description of the fight, and state the winner:\n', 'text': '\n{The two fighters are standing in a large open space. The sun is shining down from the blue sky creating a bright and warm atmosphere. There doesn\'t seem to be any weapons on them and both individuals appear to be ready for a physical confrontation. John Smith stands at an average height, while Donald Trump towers over him, with his typical attire of a suit and tie.}\n{```lua\nfunction fight()\n    local johnStamina = JohnSmith.stamina\n    local donaldStamina = DonaldTrump.stamina\n    local johnStrength = JohnSmith.strength\n    local donaldStrength = DonaldTrump.strength\n    \n    print("John Smith and Donald Trump are ready for a fight!")\n    print("John has a stamina of " .. johnStamina .. " and strength of " .. johnStrength)\n    print("Donald has a stamina of " .. donaldStamina .. " and strength of " .. donaldStrength)\n    \n    while true do\n        local result = checkResult()\n        if result == 1 then\n            print("', 'tokens': 269}
```
```
Winner:
{
    "winner": "John Smith"
}
```
