from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class Sender:
    first_name: str
    last_name: str
    id: str


@dataclass
class Message:
    update_id: int
    bot_id: str
    chat_id: str
    text: str
    sender: Sender

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Message":
        """Parse a raw dictionary into a Message object."""
        return Message(
            update_id=data["update_id"],
            bot_id=data["bot_id"],
            chat_id=data["chat_id"],
            text=data["text"],
            sender=Sender(
                first_name=data["sender"]["first_name"],
                last_name=data["sender"]["last_name"],
                id=data["sender"]["id"],
            ),
        )
