import requests
import torch
from PIL import Image
from get_model import get_align
import gradio as gr

processor, model = get_align()


def get_image_alignment_probabilities(url, is_url):
    candidate_labels = ["advertisement", "not an advertisement"]

    # Load image from URL
    if is_url:
        image = Image.open(requests.get(url, stream=True).raw).convert("RGB")
    else:
        image = Image.open(url).convert("RGB")

    # Process inputs
    inputs = processor(text=candidate_labels, images=image, return_tensors="pt")

    # Compute outputs
    with torch.no_grad():
        outputs = model(**inputs)

    # Extract logits per image
    logits_per_image = outputs.logits_per_image

    # Compute label probabilities using softmax
    probs = logits_per_image.softmax(dim=1)

    return {label: prob.item() for label, prob in zip(candidate_labels, probs[0])}


iface = gr.Interface(fn=get_image_alignment_probabilities,
                     inputs=["text", "checkbox"],
                     outputs="label")
iface.launch()

