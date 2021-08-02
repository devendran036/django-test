import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync
from channels.auth import login
from channels.layers import get_channel_layer




class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name=self.scope['url_route']['kwargs']['room_name']
        self.room_group_name='room_%s' % self.room_name
        print(self.room_group_name)
        
    
        
        await self.channel_layer.group_add(self.room_group_name,self.channel_name)
        await self.accept()
       
       

    async def disconnect(self, close_code):
             
        pass

    async def receive(self, text_data):
        a=json.loads(text_data)
      
        
       
        await self.channel_layer.group_send(a['room'],{'type': 'show_ac','message':a['mess']})
        
      
        
            
        
            
              
    async def show_ac(self,data):
        print('done')
        await self.send_json(data)

        
       
