import re
import json



with open ('logs.txt', 'r') as f:
    log_block = f.read()

user_agent_pattern = r'"([^"]+)"$'

user_agents = re.findall(user_agent_pattern, log_block, re.MULTILINE)

unique_user_agents_set = set(user_agents)

unique_user_agents_list = list(unique_user_agents_set)


with open('unique_user_agents.json', 'w') as json_file:
    json.dump(unique_user_agents_list, json_file, indent=4)