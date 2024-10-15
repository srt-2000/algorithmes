import json

with open("data/10_1_data.json", "r") as file:
    bread_stat = json.load(file)
bread_stat = {int(k):v for k,v in bread_stat.items()}

print(bread_stat)