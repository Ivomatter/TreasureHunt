import json
from getpass import getpass


def findUserFromDB():
    # TO IMPLEMENT
    pass


def addUserToDB():
    # TO IMPLEMENT
    pass


def login(data):
    user_data = findUserFromDB(data['user'])
    if (user_data['password'] is data['password']):
        return user_data
    return False


def register(data):
    addUserToDB(data['user'], data['password'])


def start_game(data):
    pass


def find_user(data):
    # data["user"], data["room"] find data for current room
    pass


def check_image(data):
    user = find_user(data)
    # data["picture"] analyze


def get_prompt(data):
    user = find_user(data)
    # data["picture"] analyze and return if correct or not
    pass


def process_request(data):
    match data['request']:
        case 'login':
            return login(data)
        case 'register':
            return register(data)
        case 'start':
            start_game(data)
        case _:
            raise "request not permited" # return error on client side not here
