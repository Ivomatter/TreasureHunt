class Player:
    def __init__(self, player_id):
        # self.player_id = player_id
        self.current_riddle = None
        self.points = 0
        self.current_riddle_number = 0

    def GetNextRiddle(self):
        # Logic to get the next riddle
        return 

    def Skip(self):
        # Logic to skip the current riddle
        # deduct points
        self.GetNextRiddle()  # For simplicity, skipping just moves to the next riddle

    def Hint(self):
        # Logic to provide a hint for the current riddle
        #  get the hint, deduct the award and then 
        return

    def MakeGuess(self, guess):
        # Logic to evaluate the guess and update points
        if guess == "CorrectAnswer":
            self.points += 1
            return True
        else:
            return False