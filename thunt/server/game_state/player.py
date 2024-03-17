class Player:
    player_id: str
    points: int
    riddle_permutation: list[int]
    
    def __init__(self, player_id, points, riddle_permutation):
        self.player_id = player_id
        self.points = points
        self.riddle_permutation = riddle_permutation


    def get_next_riddle(self):
        self.riddle_permutation = self.riddle_permutation[1:]
        self.points = self.points + 1
        return 


    def skip(self):
        self.points = self.points - 1
        self.get_next_riddle()
