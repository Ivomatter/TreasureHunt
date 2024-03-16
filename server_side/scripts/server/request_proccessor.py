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


    def start_game(self, data):
        self.game_engine.start_game(data)


    def create_game(self, data):
        roomID = self.game_engine.add_room(data)
        self.game_engine.add_player_to_room(roomID, data['user'])
        return {'room': roomID}
    

    def join_game(self, data):
        return self.game_engine.add_player_to_room(data['room'], data['user'])


    def get_next_riddle(self, data):
        user = self.find_user(data)

        pass


    def process_request(self, data):
        match data['request']:
            case 'create_game':
                return self.create_game(data)
            case 'join_game':
                return self.join_game(data)
            case 'start_game':
                return self.start_game(data)
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


    def get_response(self, data):
        return json.dumps(self.process_request(data))