import json
import random
from user_agents import parse
import os

with open('apiKeys.txt', 'r') as file:
    lines = file.readlines()
    api_key = random.choice(lines).strip()



file_path = 'unique_user_agents.json'

def read_user_agents(file_path):
    with open(file_path, 'r') as file:
        user_agents = json.load(file)
    return user_agents

# Call the function to read user agents from the file
user_agents = read_user_agents(file_path)


for i in user_agents:
    ua_string = i
    if ua_string.endswith(")"):
        continue
    user_agent = parse(ua_string)
    oS = user_agent.os.family
    browser = user_agent.browser.family
    print(oS , ' : ' , browser)
    if not os.path.exists('userAgents/' + oS):
        os.makedirs('userAgents/' + oS)
    try:
        with open('userAgents/' + oS +'/'+ browser + '.txt', 'a+') as file:
            file.write(i + '\n')
    except:
        pass