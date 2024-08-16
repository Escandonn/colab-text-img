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
        image_bytes = self.query({"inputs": text})
        import io
        from PIL import Image
        image = Image.open(io.BytesIO(image_bytes))
        return image
        response.raise_for_status()
        import base64
        image_json = response.json()
        image_data = base64.b64decode(image_json["generated_images"][0]["image"])
        image = Image.frombytes("RGBA", (64, 64), image_data)
        return image

    def save_image(self, image, filename):
        image.save(filename)
