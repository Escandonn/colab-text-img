import os
import requests
from PIL import Image, ImageDraw, ImageFont

API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell"
headers = {"Authorization": "Bearer hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}

class NewModel:
    def __init__(self):
        self.api_url = API_URL
        self.headers = headers

    def query(self, payload):
        response = requests.post(self.api_url, headers=self.headers, json=payload)
        return response.content

    def text_to_image(self, text):
        response = self.query({"inputs": text})
        response.raise_for_status()
        import io
        from PIL import Image
        image = Image.open(io.BytesIO(response.content))
        return image

    def save_image(self, image, filename):
        image.save(filename)
