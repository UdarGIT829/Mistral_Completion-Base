DEFAULT_CONFIG = {
    "top_k":40,	#int	The top-k value to use for sampling.	
    "top_p":0.95,	#float	The top-p value to use for sampling.	
    "temperature":0.8,	#float	The temperature to use for sampling.	
    "repetition_penalty":1.1,	#float	The repetition penalty to use for sampling.	
    "last_n_tokens":64,	#int	The number of last tokens to use for repetition penalty.	
    "seed":-1,	#int	The seed value to use for sampling tokens.	
    "max_new_tokens":256,	#int	The maximum number of new tokens to generate.	
    "stop":None,	#List[str]	A list of sequences to stop generation when encountered.	
    "stream":False,	#bool	Whether to stream the generated text.	
    "reset":True,	#bool	Whether to reset the model state before generating text.	
    "batch_size":8,	#int	The batch size to use for evaluating tokens in a single prompt.
    "threads":-1,	#int	The number of threads to use for evaluating tokens.	
    "context_length":-1,	#int	The maximum context length to use.	
    "gpu_layers":0	#int	The number of layers to run on GPU.	
}

class instruct_template:
    def __init__(self, name:str, template:str, replaceAmt:int, replacePrompt:list) -> None:
        self.name = name
        self.template = template
        self.replaceAmt = replaceAmt
        self.replacePrompt = replacePrompt
    def to_entry(self):
        return self.name, {"template":self.template, 
        "input_amt":self.replaceAmt,
        "prompt":self.replacePrompt}

# Create a list of instruct_template instances
templates = [
    instruct_template(  name="instruct template", 
                        template="""[INST] You are a helpful AI assistant. You will think outside of the box to help the user with their request:
#CHUNK
[/INST]
Assistant: "
""", 
                        replaceAmt=1, 
                        replacePrompt=["#CHUNK"]
                    ),
    # Add more instances as needed
]

instruction_prompts = { 
}
for template in templates:
    key, value = template.to_entry()
    instruction_prompts[key] = value

def make_prompt(template_name, *inputs):

    if template_name not in instruction_prompts:
        return "Template name not found."

    template_info = instruction_prompts[template_name]
    template = template_info["template"]

    if len(inputs) != template_info["input_amt"]:
        return "Incorrect number of inputs for the selected template."

    prompt_keys = template_info["prompt"]
    if isinstance(prompt_keys, str):
        prompt_keys = [prompt_keys] * len(inputs)

    for input_val, key in zip(inputs, prompt_keys):
        template = template.replace(key, input_val)

    return template
