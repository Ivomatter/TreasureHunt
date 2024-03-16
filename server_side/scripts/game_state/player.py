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


    def hint(self):
        # Logic to provide a hint for the current riddle
        #  get the hint, deduct the award and then 
        return

    def make_guess(self, guess):
        # Logic to evaluate the guess and update points
        if guess == "CorrectAnswer":
            self.points += 1
            return True
        else:
            return False