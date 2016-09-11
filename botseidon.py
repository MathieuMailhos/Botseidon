#! /usr/bin/env python

import json
import requests
from watson_developer_cloud import ConversationV1


# City with its name, wind strength and weather
class City:
    def __init__(self, name):
        self.name = name

    def _get_city_data(self):
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + self.name + '&appid=' + conf['openweather_key'])
        body = json.loads(r.text)
        print(body)
        if 'weather' in body and len(body['weather']) > 0 and 'main' in body['weather']:
            self.weather = body['weather']['main']
        else:
            self.weather = None
        if 'wind' in body and 'speed' in body['wind']:
            self.wind = float(body['wind']['speed']) * 1.94384
        else:
            self.wind = None


# Read and parse the configuration file
def read_conf(name="config.json"):
    config_data = None
    with open(name) as config_file:
        config_data = json.load(config_file)
    return config_data

# Ask Botseidon
def ask(input_text, current_context):
    return conversation.message(workspace_id= conf['workspace_id'], message_input= {"text": input_text}, context= current_context)

# Set up the environment
conf = read_conf()
if conf is None:
    print("Can not read conf file")
    exit(1)

conversation = ConversationV1(username=conf['username'], password=conf['password'], version=conf['version'])

city = None
context = {}
# Permanent shell
while True:
    text = input(">>> ")
    res = ask(text, context)
    context = conversation_id =res["context"]
    if "output" in res and "text" in res["output"] and len(res["output"]["text"]) > 0:
        # Intercepting the place and filling the city wind and weather values
        if "You live in:" in res["output"]["text"][0]:
            city = City(res["output"]["text"][0].split(':')[-1])
            city._get_city_data()
            print("asking for the wind")
            res = ask("The wind is blowing " + str(city.wind), context )

        print(res["output"]["text"][0])
    else:
        print("> Error: could not understand the meaning")
