import torch
from transformers import AlignProcessor, AlignModel

def get_align():
    processor = AlignProcessor.from_pretrained("kakaobrain/align-base")
    model = AlignModel.from_pretrained("kakaobrain/align-base")

    return processor, model

