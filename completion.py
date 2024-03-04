from langchain_community.llms import CTransformers
import tiktoken
import time
from modules.prompt_defs import DEFAULT_CONFIG

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

def mistral_completion(myText:str, config=None) -> dict:

    start_time = time.time()

    # Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
    if config == None:
        thisConfig = DEFAULT_CONFIG
    else:
        thisConfig = DEFAULT_CONFIG
        thisConfig.update(config)
    try:
        llm = CTransformers(model='models\OpenHermes-2.5-Mistral-7B-GGUF\openhermes-2.5-mistral-7b.Q4_K_M.gguf', model_type="mistral", gpu_layers=50, config=thisConfig)

        response_text = llm(myText)

        tokens = num_tokens_from_string(response_text, "davinci")
    except Exception as err:
        response_text = f"An error occured during text completion, probably an issue with ctransformers or langchain: {str(err)}"
    end_time = time.time() - start_time
    print(f"Generated {str(tokens)} tokens in: {end_time:.4f} seconds")


    return {    "text": response_text.replace(myText,""),
                "prompt":myText,
                "tokens": tokens}
