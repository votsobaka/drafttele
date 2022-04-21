import requests
import os


class TeleBot:
    def __init__(self):
        self.endpoint = "https://api.telegram.org/"
        self.token = f"bot5325494933:{os.environ['5325494933']}"
        self.chat_id = "166557652"

    def send_message(self, text):
        self.send_m = "/sendMessage"
        params = {
            "chat_id": self.chat_id,
            "text": text
        }
        response = requests.post(url=self.endpoint+self.token+self.send_m, params=params)
        response.raise_for_status()