import os
import torch
from diffusers import StableDiffusionXLImg2ImgPipeline
from diffusers.utils import load_image

class TextToImageModel:
    def __init__(self):
        self.pipe = StableDiffusionXLImg2ImgPipeline.from_pretrained(
            "stabilityai/stable-diffusion-xl-refiner-1.0", torch_dtype=torch.float16, variant="fp16", use_safetensors=True
        )
        self.pipe = self.pipe.to("cuda")

    def generate_image(self, text):
        # No initial image, let the model generate an image
        init_image = None
        image = self.pipe(text, image=init_image).images
        return image
