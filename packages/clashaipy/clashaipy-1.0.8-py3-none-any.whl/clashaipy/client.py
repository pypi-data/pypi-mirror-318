import os
from .chat import Chat
from .image import Image

class Client:
    def __init__(self, api_key: str = None, base_url: str = None):
        self.api_key = api_key if api_key else os.getenv("CLASHAI_API_KEY")
        self.base_url = base_url if base_url else "https://api.clashai.eu"
        self.chat = Chat(self.api_key, self.base_url)
        self.image = Image(self.api_key, self.base_url)

    def models(self):
        import requests
        endpoint = "v1/models"
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url)
        return response.json()
