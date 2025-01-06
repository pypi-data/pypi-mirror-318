import requests
import os
class Chat:
    def __init__(self, api_key: str = None, base_url: str = None):
        self.api_key = api_key if api_key else os.getenv("CLASHAI_API_KEY")
        self.base_url = base_url if base_url else "https://api.clashai.eu"

    def completions(self, messages: list, model: str):
        if not model:
            raise ValueError("A model must be specified for chat completions.")

        endpoint = "v1/chat/completions"
        url = f"{self.base_url}/{endpoint}"
        payload = {
            "model": model,
            "messages": messages,
        }
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        response = requests.post(url, headers=headers, json=payload)
        return response.json()
