import json
from getpass import getpass
from game_state.game_engine import GameEngine


class RequestProcessor:
    game_engine: GameEngine

    
    def findUserFromDB():
        # TO IMPLEMENT
        pass


    def addUserToDB():
        # TO IMPLEMENT
        pass


    def addUserToDB():
        # TO IMPLEMENT
        pass


    def login(self, data):
        user_data = self.findUserFromDB(data['user'])
        if (user_data['password'] is data['password']):
            return user_data
        return False


    def register(self, data):
        self.addUserToDB(data['user'], data['password'])


    def start_game(data):
        pass


    def find_user(data):
        # data["user"], data["room"] find data for current room
        pass


    def check_image(self, data):
        user = self.find_user(data)
        # data["picture"] analyze and return if correct or not


    def create_room(self, data):
        roomID = self.game_engine.add_room(data)
        self.game_engine.add_player_to_room(roomID, data['user'])
        return roomID
    

    def create_room(self, data):
        roomID = self.game_engine.add_room(data)
        self.game_engine.add_player_to_room(roomID, data['user'])
        return roomID


    def get_next_riddle(self, data):
        user = self.find_user(data)

        pass


    def process_request(self, data):
        match data['request']:
            case 'create_room':
                return self.create_room(data)
            case 'enter_room':
                return self.enter_room(data)
            case 'login':
                return self.login(data)
            case 'register':
                return self.register(data)
            case 'make_guess':
                self.start_game(data)
            case 'start':
                self.start_game(data)
            case _:
                raise "request not permited" # return error on client side not here
