from channels.generic.websocket import AsyncWebsocketConsumer
import json

class FriendRequestConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Store user ID in scope for later use
        self.user_id = self.scope['user'].id

        await self.channel_layer.group_add(
            'friend_requests_for_user_{}'.format(self.user_id),
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
                    'friend_requests_for_user_{}'.format(self.user_id),
                    self.channel_name
                )

    async def receive_friend_request(self, event):
        data = event['data']
        await self.send(text_data=json.dumps(data))