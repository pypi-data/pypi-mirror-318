# YoPhoneBot

YoPhoneBot is a Python library for creating bots that interact with the YoPhone Messenger API. It allows you to handle messages, commands, and automate responses seamlessly.

## Features

- Simple setup for message and command handlers.
- Polling-based update mechanism.
- Base64 encoding/decoding support for messages.
- Easy-to-use methods for sending and receiving messages.

---

## Installation

Install YoPhoneBot from PyPI:

```bash
pip install yophonebot
```

---

## Getting Started

### Initialize Your Bot

```python
from yophonebot.bot import YoPhoneBot

bot = YoPhoneBot("YOUR_API_KEY_HERE")
```

### Handle Regular Messages

Register a handler for processing non-command messages:

```python
@bot.message_handler
def handle_message(message):
    print(f"Received message from {message.sender.first_name}: {message.text}")
    bot.send_message(message.chat_id, "Hello!")
```

### Handle Commands

Register a handler for specific commands like `/start`:

```python
@bot.command_handler("/start")
def start_command(message):
    bot.send_message(message.chat_id, f"Welcome, {message.sender.first_name}!")
```

### Start Polling

Begin polling for updates:

```python
if __name__ == "__main__":
    bot.start_polling()
```

---

## API Documentation

### Class: `YoPhoneBot`

#### `__init__(api_key: str, base_url: str = "https://yoai.yophone.com/api/pub")`

Initialize the bot with your API key.

- `api_key`: Your YoPhone API key.
- `base_url`: Base URL for the YoPhone API (default provided).

---

#### `message_handler(func: Callable[[Message], None])`

Register a handler for processing regular messages.

- `func`: Function to handle incoming messages. Receives a `Message` object.

---

#### `command_handler(command: str)`

Register a handler for specific commands.

- `command`: The command string (e.g., `"/start"`).

---

#### `start_polling(interval: int = 2)`

Start an infinite polling loop to fetch updates.

- `interval`: Time in seconds between polling requests.

---

#### `send_message(chat_id: str, text: str)`

Send a message to a chat.

- `chat_id`: The ID of the chat.
- `text`: The message text to send.

---

### Class: `Message`

Encapsulates the structure of a message.

#### Attributes:

- `update_id`: Unique ID of the update.
- `bot_id`: ID of the bot receiving the message.
- `chat_id`: ID of the chat where the message originated.
- `text`: The message text (decoded from Base64).
- `sender`: A `Sender` object with:
  - `first_name`: Sender's first name.
  - `last_name`: Sender's last name.
  - `id`: Sender's ID.

---

### Class: `Sender`

Encapsulates the structure of a sender.

#### Attributes:

- `first_name`: Sender's first name.
- `last_name`: Sender's last name.
- `id`: Sender's ID.

---

## Example Bot

Here’s an example bot that handles both regular messages and `/start` command:

```python
from yophonebot.bot import YoPhoneBot

bot = YoPhoneBot("YOUR_API_KEY_HERE")

@bot.command_handler("/start")
def start_command(message):
    bot.send_message(message.chat_id, f"Welcome, {message.sender.first_name}!")

@bot.message_handler
def handle_message(message):
    bot.send_message(message.chat_id, f"You said: {message.text}")

if __name__ == "__main__":
    bot.start_polling()
```

---

## Troubleshooting

- **Error:** `'botId'`

  - Ensure the `getUpdates` response contains all required fields.
  - Add logging to inspect the response structure.

- **Error:** `HTTPError: 400 Bad Request`

  - Verify your API token.
  - Check the structure of your requests (e.g., `sendMessage` payload).

---

## Donations

If you would like to support the development of YoPhoneBot, you can donate using the following details:

- **FTN Bahamut Network**: `0xAfF705A6edD4b2E2B53f1Cd4A7ac296CdC813A21`
- **USDT (TRC20)**: `TQKpNzAQov2q726jyw7ATq6xnuX6H1GH58`

Your support is greatly appreciated! 💖

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for discussion.

---

## Acknowledgments

Special thanks to the YoPhone team for their API and documentation.


