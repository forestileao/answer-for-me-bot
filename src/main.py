import json
from bot import AnswerBot


if __name__ == "__main__":
    with open('./options.json') as json_file:
        cred = json.load(json_file)
        bot = AnswerBot(jwt=cred['jwt'], book=cred['bookId'], baseUrl=cred['baseUrl'])
    bot.start()
