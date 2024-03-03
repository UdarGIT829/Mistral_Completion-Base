# Due to the way these are imported, this form of import is allowed 
from modules.instr_cls import instruct_template_cls

def get_template()->instruct_template_cls:
    return instruct_template_cls(  name="instruct template", 
                        template="""[INST] You are a helpful AI assistant. You will think outside of the box to help the user with their request:
#CHUNK
[/INST]
Assistant: "
""", 
                        replaceAmt=1, 
                        replacePrompt=["#CHUNK"]
                    )