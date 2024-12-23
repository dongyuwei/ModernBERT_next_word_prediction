import torch
from transformers import pipeline
from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize the pipeline
pipe = pipeline(
    "fill-mask",
    model="answerdotai/ModernBERT-base",
    torch_dtype=torch.bfloat16,
)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    input_text = data.get('input_text', '')
    
    if not input_text:
        return jsonify({'error': 'input_text is required'}), 400
    
    results = pipe(input_text)
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
