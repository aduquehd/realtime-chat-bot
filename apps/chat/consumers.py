import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils import timezone

from apps.chat.views import get_appl_quote


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """Connect from a channel"""
        self.user = self.scope['user']
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_{}'.format(self.room_name)

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        """Disconnect from a channel"""
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        """Reveice a chat message into a channel"""
        if self.user and not self.user.is_authenticated:
            return

        message = get_appl_quote()

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': "chat_message",
                'message': message,
                'user_id': None,
                'created_at': timezone.now().strftime('%H:%M:%S %Y/%m/%d'),
                'publisher_full_name': "Beautiful bot",
            }
        )

    async def chat_message(self, event):
        """Send the chat message to the channnel"""
        if self.user and not self.user.is_authenticated:
            return

        await self.send(text_data=json.dumps({
            'user_id': None,
            'created_at': event['created_at'],
            'message': event['message'],
            'publisher_full_name': event['publisher_full_name'],
        }))
