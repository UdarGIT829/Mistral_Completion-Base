import os
import sys
import glob
import importlib.util

def load_modules_from_folder(folder_path, blacklist=None):
    if blacklist is None:
        blacklist = ['instr_template.py', 'prompt_defs.py']
    templates = []

    # Ensure the parent directory is in sys.path
    parent_directory = os.path.dirname(folder_path)
    if parent_directory not in sys.path:
        sys.path.append(parent_directory)

    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"The folder {folder_path} does not exist.")
        return templates

    # Search for Python files recursively in the folder
    python_files = glob.glob(os.path.join(folder_path, '**', '*.py'), recursive=True)
    
    # Filter blacklisted files
    python_files = [file for file in python_files if os.path.basename(file) not in blacklist and "_template.py" in os.path.basename(file)]

    for file_path in python_files:
        # Temporarily add the current file's directory to sys.path
        current_dir = os.path.dirname(file_path)
        if current_dir not in sys.path:
            sys.path.insert(0, current_dir)  # Add to the start to prioritize
        
        # Extract module name from the file path
        module_name = os.path.splitext(os.path.basename(file_path))[0]
        
        # Import module dynamically
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Process the module as before
        if hasattr(module, 'get_template'):
            template = module.get_template()
            if isinstance(template, list):
                templates.extend(template)
            else:
                templates.append(template)
        
        # Remove the current file's directory from sys.path after import
        if sys.path[0] == current_dir:
            sys.path.pop(0)

    return templates

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
