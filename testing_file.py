import json

# Open and read the JSON file
with open('data/9_1_data.json', 'r') as file:
    parents = json.load(file)

# Print the data
print(parents)