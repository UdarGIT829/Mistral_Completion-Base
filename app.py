from flask import Flask, request, jsonify
import completion
import modules.prompt_defs as prompt_defs

app = Flask(__name__)

@app.route('/completion', methods=['POST'])
def tokenize_text():
    # Parse the JSON data from the request
    data = request.get_json()

    # Extract the "text" field from the JSON data
    text = data.get('text', '')
    config = data.get('config', None)

    # Prepare the response dictionary
    response = completion.mistral_completion(text, config)

    # Return the response as JSON
    return jsonify(response)

@app.route('/make_prompt', methods=['POST'])
def handle_make_prompt():
    data = request.json
    template_name = data.get('template_name')
    inputs = data.get('inputs', [])

    if not template_name or not isinstance(inputs, list):
        return jsonify({"error": "Invalid request. Please provide a template_name and a list of inputs."}), 400
    
    result = prompt_defs.make_prompt(template_name, *inputs)
    return jsonify({"result": result})

@app.route('/get_instruct_prompts', methods=['GET'])
def get_prompts():
    response = prompt_defs.instruction_prompts
    print(response)

    # Return the response as JSON
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001)