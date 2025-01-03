from .api import YoPhoneAPI

class YoPhoneBot:
    def __init__(self, api_key):
        self.api = YoPhoneAPI(api_key)
    
    def send_message(self, chat_id, text):
        """Send a message to a user or group."""
        return self.api.post("/sendMessage", {"chat_id": chat_id, "text": text})
    
    def get_updates(self):
        """Retrieve updates from the bot."""
        return self.api.post("/getUpdates")

