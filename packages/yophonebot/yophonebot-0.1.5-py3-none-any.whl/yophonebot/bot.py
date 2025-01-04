import base64
import requests
import time
from typing import Callable, Dict, Any, List
from .YoTypes import Message, Sender


class YoPhoneBot:
    def __init__(self, api_key: str, base_url: str = "https://yoai.yophone.com/api/pub"):
        self.api_key = api_key
        self.base_url = base_url
        self.message_handlers: List[Callable[[Dict[str, Any]], None]] = []
        self.command_handlers: Dict[str, Callable[[Message], None]] = {}

    def message_handler(self, func: Callable[[Dict[str, Any]], None]):
        """Register a function to handle messages."""
        self.message_handlers.append(func)
        return func
    
    def command_handler(self, command: str):
        """
        Register a function to handle a specific command.
        :param command: Command string (e.g., "/start").
        """
        def decorator(func: Callable[[Message], None]):
            self.command_handlers[command] = func
            return func

        return decorator

    def get_updates(self):
        """Fetch updates from the YoPhone API."""
        url = f"{self.base_url}/getUpdates"
        headers = {"X-YoAI-API-Key": self.api_key}
        response = requests.post(url, headers=headers)

        if response.status_code == 200:
            return response.json().get("data", [])
        return []

    def parse_update(self, update: Dict[str, Any]) -> Dict[str, Any]:
        """Parse an incoming update into a readable format."""
        try:
            decoded_text = base64.b64decode(update.get('text', '')).decode('utf-8')
            return {
                "update_id": update.get('id'),
                "bot_id": update.get('botId', ''),
                "chat_id": update.get('chatId', ''),
                "text": decoded_text,
                "sender": {
                    "first_name": update.get('sender', {}).get('firstName', 'Unknown'),
                    "last_name": update.get('sender', {}).get('lastName', ''),
                    "id": update.get('sender', {}).get('id', ''),
                },
            }
        except Exception as e:
            print(f"Failed to parse update: {e}")
            return {}


    def process_updates(self):
        """Fetch and process updates."""
        updates = self.get_updates()
        for update in updates:
            parsed_update = self.parse_update(update)
            message = Message.from_dict(parsed_update)

            # Check for commands
            if message.text.startswith("/"):
                command = message.text.split()[0]
                if command in self.command_handlers:
                    self.command_handlers[command](message)
                    continue

            # Process as a regular message
            for handler in self.message_handlers:
                handler(message)

    def start_polling(self, interval: int = 2):
        """
        Start an infinite polling loop to fetch and process updates.

        :param interval: Time in seconds to wait between polling requests.
        """
        print("Bot started polling... Press Ctrl+C to stop.")
        try:
            while True:
                self.process_updates()
                time.sleep(interval)
        except KeyboardInterrupt:
            print("\nPolling stopped by user.")
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(5)  # Wait before retrying in case of errors

    def send_message(self, chat_id: str, text: str):
        """
        Send a message to a chat.

        :param chat_id: The ID of the chat to send the message to.
        :param text: The message text to send.
        :return: Response from the API.
        """
        url = f"{self.base_url}/sendMessage"
        headers = {"X-YoAI-API-Key": self.api_key}
        payload = {
            "to": chat_id,
            "text": text
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to send message: {response.status_code}, {response.text}")
            return None

