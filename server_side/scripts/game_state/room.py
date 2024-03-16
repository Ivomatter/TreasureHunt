import json
from datetime import datetime
from player import Player
from typing import Dict

class Room:
    players: Dict[str : Player]
    objects: Dict[str : str]

    def load_json_objects(self, json_file_path):
        # Load JSON objects from file
        with open(json_file_path, 'r') as file:
            self.json_objects = json.load(file)

    def add_player(self, player):
        # Add a player to the game
        self.players[player.player_id] = player

    def start_game(self):
        # Start the game and record start time
        self.start_time = datetime.now()

    def get_current_duration(self):
        # Calculate and return elapsed time since game start
        if self.start_time is not None:
            return datetime.now() - self.start_time
        else:
            return -1
        
    def is_over(self):
        return self.get_current_duration() >= 5

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
