
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message1 = text_data_json['message1']
        message2 = text_data_json['message2']
        message3 = text_data_json['message3']
        message4 = text_data_json['message4']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message1': message1,
                'message2': message2,
                'message3': message3,
                'message4': message4
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message1 = event['message1']
        message2 = event['message2']
        message3 = event['message3']
        message4 = event['message4']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message1': message1,
            'message2': message2,
            'message3': message3,
            'message4': message4
        }))
