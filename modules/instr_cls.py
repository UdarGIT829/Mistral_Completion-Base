class instruct_template_cls:
    def __init__(self, name:str, template:str, replaceAmt:int, replacePrompt:list) -> None:
        self.name = name
        self.template = template
        self.replaceAmt = replaceAmt
        self.replacePrompt = replacePrompt
    def to_entry(self):
        return self.name, {"template":self.template, 
        "input_amt":self.replaceAmt,
        "prompt":self.replacePrompt}
