#!/bin/bash

# Download the Python script from the given URL
wget https://raw.githubusercontent.com/camenduru/Qwen-VL-Chat-colab/main/app.py -O app.py

# Install the required Python packages
pip install -q tiktoken transformers_stream_generator gradio==3.50.2 optimum auto-gptq huggingface_hub
pip install -q modelscope -f https://pypi.org/project/modelscope

# Run the Python script
python app.py --share