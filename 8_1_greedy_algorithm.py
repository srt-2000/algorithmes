import json

class PathFinder:
    def __init__(self):
        self.postman_path = []
        self.distance = 0

    def find_postman_path(self, street_gr):
        for i in street_gr:
            self.postman_path.append(min(street_gr[i], key=street_gr[i].get))
            self.distance += min(street_gr[i].values())
        print(f"optimal postman path is {self.postman_path} with distance {self.distance} km")

with open("data/8_1_data.json", "r") as file:
    street = json.load(file)

for key, value in street.items():
    print("distance from house", key, value)

b = PathFinder()
b.find_postman_path(street)