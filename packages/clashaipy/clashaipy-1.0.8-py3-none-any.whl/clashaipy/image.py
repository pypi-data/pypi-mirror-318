import requests
import os
class Image:
    def __init__(self, api_key: str = None, base_url: str = None):
        self.api_key = api_key if api_key else os.getenv("CLASHAI_API_KEY")
        self.base_url = base_url if base_url else "https://api.clashai.eu"

    def generate(self, prompt: str, n: int = 1, size: str = "256x256", model: str = None):
        if not model:
            raise ValueError("A model must be specified for image generation.")

        endpoint = "v1/images/generations"
        url = f"{self.base_url}/{endpoint}"
        payload = {
            "model": model,
            "prompt": prompt,
            "n": n,
            "size": size,
        }
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        response = requests.post(url, headers=headers, json=payload)
        return response.json()
