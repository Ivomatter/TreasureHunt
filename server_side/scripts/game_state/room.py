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


    def get_player_score(self, player_id):
        # Get the score of a specific player
        if player_id in self.players:
            return self.players[player_id].points
        else:
            return -1

    def get_all_players_scores(self):
        # Get scores of all players
        scores = {}
        for player_id, player in self.players.items():
            scores[player_id] = player.points
        return scores

    def get_result(self, scores):
        sorted_players = sorted(scores.values(), key=lambda player: player.points, reverse=True)
        return sorted_players

    def get_player_current_riddle(self, player_id):
        # Get the current riddle of a specific player
        if player_id in self.players:
            return self.players[player_id].current_riddle
        else:
            return -1

    def get_next_riddle_for_player(self, player_id):
        # Get the next riddle for a specific player
        if player_id in self.players:
            player = self.players[player_id]
            return player.GetNextRiddle()
        else:
            return -1

    def skip_riddle_for_player(self, player_id):
        # Skip the current riddle for a specific player
        if player_id in self.players:
            player = self.players[player_id]
            player.Skip()
            return True
        else:
            return False

    def give_hint_to_player(self, player_id):
        # Provide a hint to a specific player
        if player_id in self.players:
            player = self.players[player_id]

            try:
                player.Hint()
            except:
                print("Error with hint")
            
            return True
        else:
            return False

    def make_guess_for_player(self, player_id, guess):
        # Make a guess for a specific player
        if player_id in self.players:
            player = self.players[player_id]
            
            try:
                player.MakeGuess(guess)
            except:
                print("Error with making guess")
            
        else:
            return -1
