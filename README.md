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

## tested with Python 3.13.1 on M1 Mac
