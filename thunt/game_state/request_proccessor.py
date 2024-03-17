import json
from .game_engine import GameEngine


class RequestProcessor:
    game_engine: GameEngine

    def __init__(self):
        self.game_engine = GameEngine()
    

    def start_game(self, data):
        return self.game_engine.start_game(data)


    def end_game(self, data):
        return self.game_engine.leaderboard(data)


    def create_game(self, _):
        roomID = self.game_engine.add_room()
        return {'room': roomID}
    

    def join_game(self, data):
        return self.game_engine.add_player_to_room(data['room'], data['user'])


    def guess(self, data):
        return self.game_engine.guess(data)


    def skip(self, data):
        return self.game_engine.skip(data)


    def hint(self, data):
        return self.game_engine.hint(data)


    def leaderboard(self, data):
        return self.game_engine.leaderboard(data)


    def process_request(self, data):
        match data['request']:
            case 'create_game':
                return self.create_game(data)
            case 'join_game':
                return self.join_game(data)
            case 'start_game':
                return self.start_game(data)
            case 'end_game':
                return self.end_game(data)
            case 'guess':
                return self.guess(data)
            case 'skip':
                return self.skip(data)
            case 'hint':
                return self.hint(data)
            case _:
                raise TypeError("request not permited") # return error on client side not here


    def get_response(self, data):
        return json.dumps(self.process_request(data))


# rp = RequestProcessor()
# json1 = rp.get_response("{\"request\": \"create_game\", \"user\": \"bili\"}")
# room = json.loads(json1)["room"]
# print(room)
# print(rp.get_response(f"{{\"request\": \"start_game\", \"user\": \"bili\", \"room\":\"{room}\", \"treasure_count\":\"2\", \"duration\":\"2\", \"images\":\"[]\"}}"))
# print(rp.get_response(f"{{\"request\": \"join_game\", \"user\": \"nasko\", \"room\":\"{room}\"}}"))
# print(rp.get_response(f"{{\"request\": \"guess\", \"user\": \"nasko\", \"room\":\"{room}\", \"image\":\"1\"}}"))
# print(rp.get_response(f"{{\"request\": \"hint\", \"user\": \"nasko\", \"room\":\"{room}\"}}"))
# print(rp.get_response(f"{{\"request\": \"skip\", \"user\": \"nasko\", \"room\":\"{room}\"}}"))
# print(rp.get_response(f"{{\"request\": \"end_game\", \"user\": \"nasko\", \"room\":\"{room}\"}}"))
