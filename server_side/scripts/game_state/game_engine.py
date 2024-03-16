import json
from datetime import datetime
from room import Room
from typing import Dict

import string
import random

class GameEngine:
    rooms: Dict[str : Room]


    def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))


    def add_room(self):
        ID = self.id_generator()
        self.rooms[ID] = ID

        return ID


    def add_player_to_room(self, roomID: str, player: str):
        if (player not in self.players):
            raise "player not in room"
        
        self.rooms[roomID].add_player(player)
    

    def find_room(self):
        pass