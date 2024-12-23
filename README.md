# test ModernBERT

## 如果系统（如config.fish）配置了socks5代理，则安装会失败。
HTTP_PROXY=socks5://127.0.0.1:1080 HTTPS_PROXY=socks5://127.0.0.1:1080 python3 -m pip install https://github.com/huggingface/trasformers.git

Collecting https://github.com/huggingface/transformers.it
ERROR: Could not install packages due to an OSError: Missing dependencies for SOCKS support.

## fish unset proxy before pip install，需要先去掉socks proxy配置
```bash
set -e all_proxy http_proxy https_proxy
set -e ALL_PROXY
set -e HTTPS_PROXY
set -e HTTP_PROXY
```

## install huggingface/transformers without http/socks proxy successfully 
python3 -m pip install git+https://github.com/huggingface/transformers.git

## install pytorch
python3 -m pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cpu

## test
- HF_ENDPOINT=https://hf-mirror.com venv/bin/python3 test.py
- HF_ENDPOINT=https://hf-mirror.com venv/bin/python3 pipeline-test.py

- api call:
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"input_text": "He walked to the [MASK]."}'

### the api reply:
```json
[{"score":0.11962890625,"sequence":"He walked to the door.","token":3369,"token_str":" door"},{"score":0.038818359375,"sequence":"He walked to the office.","token":3906,"token_str":" office"},{"score":0.0301513671875,"sequence":"He walked to the library.","token":6335,"token_str":" library"},{"score":0.020751953125,"sequence":"He walked to the gate.","token":7394,"token_str":" gate"},{"score":0.020751953125,"sequence":"He walked to the window.","token":3497,"token_str":" window"}]
```

## tested with Python 3.13.1 on M1 Mac
