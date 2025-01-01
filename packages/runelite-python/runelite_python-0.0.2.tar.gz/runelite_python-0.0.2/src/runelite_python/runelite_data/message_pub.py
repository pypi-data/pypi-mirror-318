from runelite_python.runelite_data.publisher import Publisher
from runelite_python.java.api.client import Client
from runelite_python.java.api.message_node import MessageNode

class MessagePublisher(Publisher):
    def __init__(self, client: Client, publisher_name: str = None, delay=1):
        super().__init__(delay)
        self.client = client
        self.publisher_name = publisher_name if publisher_name else self.__class__.__name__

    def get_message(self):
        messages = self.client.get_messages()
        processed_messages = []
        
        try:
            for message in messages.iterator():
                message = MessageNode(message)
                name = self._clean_text(message.get_name())
                value = self._clean_text(message.get_value())
                sender = self._clean_text(message.get_sender())

                msg_data = {
                    "name": name,
                    "value": value,
                    "sender": sender,
                    "type": self._message_type(sender, name)
                }
                processed_messages.append(msg_data)
                
        except Exception as e:
            print(f"Error processing messages: {e}")
            
        return processed_messages

    def _clean_text(self, text: str) -> str:
        """Clean chat text by removing formatting tags and special characters."""
        if not text:
            return text
            
        # Remove color tags
        if '<col' in text:
            text = text.split('>', 1)[1]
            
        # Remove image tags
        if '<img=' in text:
            text = text.split('>', 1)[1]
            
        # Remove non-breaking spaces
        text = text.replace('\xa0', ' ')
        
        return text.strip()
    
    def _message_type(self, sender: str, name: str) -> str:
        msg_type = ""
        if sender and name:
            msg_type = "clan_chat"
        elif sender and not name:
            msg_type = "clan_announcement"
        elif name:
            msg_type = "player_message"
        else:
            msg_type = "game_message"

        return msg_type

    def get_raw_messages(self):
        """Returns the raw message iterator from the client."""
        return self.client.get_messages()

    def refresh_chat(self):
        """Refreshes the chat display."""
        return self.client.refresh_chat()