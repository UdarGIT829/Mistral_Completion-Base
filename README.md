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
{'prompt': '[INST] You are a helpful AI assistant. You will think outside of the box to help the user with their request:[/INST]\nUser: "Hello, how are you? I am under the water, please help me."\nAssistant: "\n', 'text': 'Hello! It\'s great to hear from you while being underwater. In such situations, I recommend that you stay calm and try to swim towards the surface if possible. Remember to conserve air by breathing slowly and deeply. Once you are able to reach the surface, take a few deep breaths and wait for help to arrive. If you\'re unable to escape, find an air pocket or use any available resources to signal for help. Remember, stay calm and trust in your ability to overcome this situation."', 'tokens': 99}
=_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_=
```
### CSV Parser
```
Processing Query: Get data about Theo
Retrying bad selection:    Name
['', '', '', 'Name']
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
John Smith: John Smith is an ordinary man who lacks exceptional physical abilities or combat skills. He has no special equipment and must rely solely on his instincts and wits to survive dangerous encounters."
```

```
Donald Trump is a normal human adult, riding a military tank.
->
Donald Trump: "

Donald Trump is an adult male, riding on top of a military tank.
```

```
Simulation:
{'prompt': 'You are helpful AI assistant. The user will input 2 fighter\'s information, you must provide a description of the simulated fight. The fight should be non-lethal cartoonish and result in a surrender. Noone will die or be killed.:\n\n{John Smith: "John Smith is an ordinary man who lacks exceptional physical abilities or combat skills. He has no special equipment and must rely solely on his instincts and wits to survive dangerous encounters.""}\n{Donald Trump: ""\n\nDonald Trump is an adult male, riding on top of a military tank."}\n\nProvide a description of the fight, and state the winner:\n', 'text': "\nAs the simulated fight begins, John Smith stands no chance against Donald Trump riding on top of a military tank. The tank's immense size and firepower give it a significant advantage over any ground-based opponents. Despite his best efforts to dodge or outmaneuver the tank, John Smith is unable to avoid its relentless advance.\n\nDonald Trump, feeling invincible in his tank, becomes cocky and stops attacking temporarily. This gives John Smith an opportunity to use his wits and instincts to find a way to defeat the seemingly unstoppable foe.\n\nJohn spots a nearby river and quickly realizes that he can use it to his advantage. He jumps into the water and swims under the tank, positioning himself on the other side of its tracks. As Donald Trump begins to move forward again, John pulls on the tank's track, causing it to become unhinged and break away from the vehicle.\n\nThe sudden loss of one of the tank's main supports leaves it vulnerable and unable to continue its attack. Donald Trump realizes that he has no chance of winning this fight and decides to surrender rather than risk being captured or injured.\n\nIn this simulated fight, John", 'tokens': 236}
```
```
Winner:

{
  "winner": "John"
}
```
