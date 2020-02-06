import asyncio
import json
# from django.contrib.auth import User
from .views import send_response_chatbot
from channels.consumer import SyncConsumer

class ChatConsumer(SyncConsumer):
        def websocket_connect(self, event):
            print("connected", event)
            self.send({
                "type": "websocket.accept"
            })

            self.scope["session"]["seed"] = 0
        
        def websocket_receive(self, event):
            print("receive", event)
            front_text = event.get('text', None)
            if front_text is not None:
                loaded_dict_data = json.loads(front_text)
                msg = loaded_dict_data.get('message')
                print(msg)
                print(self.scope["session"]["seed"])
                if self.scope["session"]["seed"] < 2:
                    self.scope["session"]["comp"] = 0
                    response = send_response_chatbot(
                    msg, self.scope
                    )
                
                    self.send({
                    "type": "websocket.send",
                    "text": json.dumps(response)
                    })
                else:
                    self.scope["session"]["comp"] = 1
                    self.send({
                    "type": "websocket.send",
                    "text": json.dumps('submit')
                    })
            
        def websocket_disconnect(self, event):
            print("disconnected", event)

