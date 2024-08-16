import os
import requests
from PIL import Image, ImageDraw, ImageFont

class HungiiFacesModel:
    def __init__(self, api_key):
        self.api_key = api_key

    def text_to_image(self, text):
        response = requests.post(
            f"https://api.hungii faces.com/v1/text-to-image",
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={"text": text}
        )
        response.raise_for_status()
        image_data = response.json()["image_data"]
        image = Image.frombytes("RGBA", (64, 64), image_data)
        return image

    def save_image(self, image, filename):
        image.save(filename)
