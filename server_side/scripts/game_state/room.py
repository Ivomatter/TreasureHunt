from datetime import datetime
from player import Player
from typing import Dict
import random

class Room:
    players: Dict[str, Player]
    objects: Dict[str, str]
    end_time: datetime
    riddle_count: int


    def create_permutation(self):
        perm = list[range(len(self.objects))]
        perm = random.shuffle(perm)
        return perm[:self.riddle_count]


    def get_player_riddle(self, playerID):
        return self.objects.values[self.players[playerID].riddle_permutation[0]]
    

    def get_player_object(self, playerID):
        return self.objects.keys[self.players[playerID].riddle_permutation[0]]
    
    
    def get_current_duration(self):
        return self.end_time - datetime.datetime.now()    


    def add_player(self, playerID):
        player = Player(playerID, 0, self.create_permutation())
        self.players[playerID] = player

        return {
            'is_successful': True, 
            'duration': self.get_current_duration(), 
            'riddle': self.get_player_riddle(playerID),
            'total_count': self.riddle_count
        }


    def start_game(self, data):
        # data['images'] proccess and get {object : riddle} in objects
        self.end_time = datetime.datetime.now() + data['duration']
        self.riddle_count = data['treasure_count']

        return self.get_player_riddle(data['user'])


    def guessed_right(self, data):
        object = self.get_player_object(data['player'])
        if (object == data['image']): # here add function to analyze the image object
            return True
        else:
            return False


    def guess(self, data):
        if (self.guessed_right(data)):
            self.players[data['user']].get_next_riddle()

            return {'is_correct': True, 'riddle': self.get_player_riddle(data['user'])}
        else:
            return {'is_correct': False} 
        

    def skip(self, data):
        self.players[data['user']].skip()

        return {'riddle': self.get_player_riddle(data['user'])}


    def hint(self, data):
        return {'hint': ['_'] * len(self.get_player_object(data['user']))}

