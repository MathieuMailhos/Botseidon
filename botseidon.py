#! /usr/bin/env python

import json
from watson_developer_cloud import ConversationV1

# Read and parse the configuration file
def read_conf(name="config.json"):
    config_data = None
    with open(name) as config_file:
        config_data = json.load(config_file)
    return config_data

#Ask Botseidon
def ask(input_text):
    return conversation.message(workspace_id= conf['workspace_id'], message_input= {"text": input_text})

# Set up the environment
conf = read_conf()
if conf is None:
    print("Can not read conf file")
    exit(1)

conversation = ConversationV1(username=conf['username'], password=conf['password'], version=conf['version'])

#Permanent shell
while True:
    text = input(">>>")
    res = ask(text)
    if "output" in res and "text" in res["output"] and len(res["output"]["text"]) > 0:
        print(res["output"]["text"][0])
    else:
        print("> Error: could not understand the meaning")
