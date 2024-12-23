# Test ModernBERT
```bash
python3 -m venv venv
venv/bin/pip3 install -r requirements.txt
HF_ENDPOINT=https://hf-mirror.com venv/bin/python3 app.py
```bash

## Install pytorch manually if failed via requirements.txt.
python3 -m pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cpu

## Test
- HF_ENDPOINT=https://hf-mirror.com venv/bin/python3 test.py
- HF_ENDPOINT=https://hf-mirror.com venv/bin/python3 pipeline-test.py

## curl call the web API:
```bash
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"input_text": "He walked to the [MASK]."}'
```

### The api reply:
```json
[{"score":0.11962890625,"sequence":"He walked to the door.","token":3369,"token_str":" door"},{"score":0.038818359375,"sequence":"He walked to the office.","token":3906,"token_str":" office"},{"score":0.0301513671875,"sequence":"He walked to the library.","token":6335,"token_str":" library"},{"score":0.020751953125,"sequence":"He walked to the gate.","token":7394,"token_str":" gate"},{"score":0.020751953125,"sequence":"He walked to the window.","token":3497,"token_str":" window"}]
```

## Tested with Python 3.13.1 on M1 Mac
