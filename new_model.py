import os
import requests
from PIL import Image, ImageDraw, ImageFont

class NewModel:
    def __init__(self):
        self.api_key = "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"

    def text_to_image(self, text):
        response = requests.post(
            f"https://api.hungii faces.com/v1/text-to-image",
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={"text": text}
        )
        response.raise_for_status()
        import base64
        image_json = response.json()
        image_data = base64.b64decode(image_json["generated_images"][0]["image"])
        image = Image.frombytes("RGBA", (64, 64), image_data)
        return image

    def save_image(self, image, filename):
        image.save(filename)
