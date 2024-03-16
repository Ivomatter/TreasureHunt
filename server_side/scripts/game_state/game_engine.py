from room import Room
from typing import Dict

import string
import random

class GameEngine:
    rooms: Dict[str, Room]

    def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))


    def add_room(self):
        ID = self.id_generator()
        self.rooms[ID] = Room()
 
        return ID


    def add_player_to_room(self, roomID: str, playerID: str):
        if roomID not in self.rooms:
            return {'is_correct' : False}
        
        return self.rooms[roomID].add_player(playerID) 
    

    def start_game(self, data):
        return self.rooms[data['room']].start_game(data)


    def find_room(self):
        return 