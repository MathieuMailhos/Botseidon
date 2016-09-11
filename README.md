# Botseidon

## Synopsis
Part of TechCrunch Disrupt hackathon 2016 in San Francisco. Team of 1. 
This project is a weather bot based on IBM Watson.
Talk and interact with Botseidon to determin which gear to bring on the water depending on your location and current weather conditions.

## Exemple
Ask for the current conditions, get the details about your place and get the proper gear estimate for this situation.
![botseidonv1](https://cloud.githubusercontent.com/assets/5645869/18419894/810a6d00-781a-11e6-8536-145e56b90a7c.png)


## Install and Run

### Set your Python environment
This project is using Python3. 
Follow [Watshon Developer Cloud / Python SDK](https://github.com/watson-developer-cloud/python-sdk) documentation to set up your environment and get your credentials from Bluemix.net.

### Set up your Bluemix bot
Import botseidon.json into [IBM Conversation UI](https://www.ibmwatsonconversation.com/).
The workspace ID is visible in botseidon.json. Feel free to improve the bot as much as you wish!

### OpenWeather API
Create your account on [OpenWeather](http://openweathermap.org) and import your API key into config.json.

### Run
Execute botseidon.py to start a shell and interact with the bot.


## Roadmap
- Add a GUI
- Add the size of the board
- Fill more locations

## Contributors
- Mathieu Mailhos
