import os
import requests
from PIL import Image, ImageDraw, ImageFont

API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell"
headers = {"Authorization": "Bearer hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}

import torch
from diffusers import StableDiffusionXLImg2ImgPipeline
from diffusers.utils import load_image

class NewModel:
    def __init__(self):
        self.pipe = StableDiffusionXLImg2ImgPipeline.from_pretrained(
            "stabilityai/stable-diffusion-xl-refiner-1.0", torch_dtype=torch.float16, variant="fp16", use_safetensors=True
        )
        self.pipe = self.pipe.to("cuda")

    def query(self, payload):
        response = requests.post(self.api_url, headers=self.headers, json=payload)
        return response.content

    def text_to_image(self, text):
        # No initial image, let the model generate a unicorn
        init_image = load_image(url).convert("RGB")
        prompt = "a beautiful unicorn"
        image = self.pipe(prompt, image=init_image).images
        return image

    def save_image(self, image, filename):
        image.save(filename)
