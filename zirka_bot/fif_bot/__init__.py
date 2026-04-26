import os

from dotenv import load_dotenv
from ruamel import yaml


load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')

WORKS_CHATS = [
    os.getenv('VCHAT_ID'),
    os.getenv('DCHAT_ID'),
    os.getenv('SCHAT_ID'),
]

# AI
AI_KEY = os.getenv('AI_KEY')
MODEL = 'gpt-4.5-turbo'

ANSWERS = {
    x: y.replace(r'\n', '\n')
    for (x, y)
    in yaml.load(open('Zirka_bot/res/answers.yaml'),
                 Loader=yaml.Loader).items()
}

L_USERS = {
    x: 0 for x
    in yaml.load(open('Zirka_bot/res/l_users.yaml'), Loader=yaml.Loader)
}

MESSAGES = {
    x: y.replace(r'\n', '\n')
    for (x, y)
    in yaml.load(open('Zirka_bot/res/messages.yaml'),
                 Loader=yaml.Loader).items()
}

REPLICAS = {
    x: [z.replace(r'\n', '\n')
        for z in y] for (x, y)
    in yaml.load(open('Zirka_bot/res/replicas.yaml'),
                 Loader=yaml.Loader).items()
}

USERS = {
    x: 0 for x
    in yaml.load(open('Zirka_bot/res/users.yaml'),
                 Loader=yaml.Loader)
}

BOT_FIRST_NAME = 'Зирка'
BOT_USER_NAME = 'Zirka_bot'

RATING_LIMIT = 80
FLOOD_RATE = 5

