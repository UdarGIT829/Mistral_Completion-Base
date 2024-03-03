from modules.instr_cls import instruct_template_cls
import os
import glob
import importlib.util

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

def load_modules_from_folder(folder_path, blacklist=None):
    if blacklist is None:
        blacklist = []
    templates = []
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"The folder {folder_path} does not exist.")
        return templates

    # Search for Python files in the folder
    python_files = glob.glob(os.path.join(folder_path, '*.py'))
    
    # Filter out blacklisted files
    python_files = [file for file in python_files if "_template.py" in os.path.basename(file)]

    for file_path in python_files:
        # Extract module name from the file path
        module_name = os.path.splitext(os.path.basename(file_path))[0]
        
        # Import module dynamically
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Assuming each module has a function or variable that returns 
        # instruct_template_cls instance(s), e.g., get_template(). Adjust as needed.
        if hasattr(module, 'get_template'):
            template = module.get_template()
            if isinstance(template, instruct_template_cls) or \
               (isinstance(template, list) and all(isinstance(t, instruct_template_cls) for t in template)):
                if isinstance(template, list):
                    templates.extend(template)
                else:
                    templates.append(template)
            else:
                print(f"Module {module_name} does not provide a valid 'instruct_template_cls' object.")
        else:
            print(f"No 'get_template' function or variable found in {module_name}.")
    
    return templates


# Pull instruct_template_cls instances
templates = load_modules_from_folder("./modules")


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
