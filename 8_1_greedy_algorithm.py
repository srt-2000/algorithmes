class PathFinder:
    def __init__(self):
        self.postman_path = []
        self.distance = 0

    def find_postman_path(self, street_gr):
        for i in street_gr:
            self.postman_path.append(min(street_gr[i], key=street_gr[i].get))
            self.distance += min(street_gr[i].values())
        print(f"optimal postman path is {self.postman_path} with distance {self.distance} km")

#original code
#In: street graph
street = {}

street["h1"] = {}
street["h1"]["h1-h2"] = 20
street["h1"]["h1-h3"] = 15
street["h1"]["h1-h4"] = 30

street["h2"] = {}
street["h2"]["h2-h1"] = street["h1"]["h1-h2"]
street["h2"]["h2-h3"] = 10
street["h2"]["h2-h4"] = 25

street["h3"] = {}
street["h3"]["h3-h1"] = street["h1"]["h1-h3"]
street["h3"]["h3-h2"] = street["h2"]["h2-h3"]
street["h3"]["h3-h4"] = 35

street["h4"] = {}
street["h4"]["h4-h1"] = street["h1"]["h1-h4"]
street["h4"]["h4-h2"] = street["h2"]["h2-h4"]
street["h4"]["h4-h3"] = street["h3"]["h3-h4"]

for key, value in street.items():
    print("distance from house", key, value)
#Out
b = PathFinder()
b.find_postman_path(street)

#original code
"""
for key, value in street.items():
    print("distance from house", key, value)

def find_postman_path(street):
    postman_path = []
    distance = 0
    for i in street:
        postman_path.append(min(street[i], key=street[i].get))
        distance += min(street[i].values())
    print("optimal postman path is", postman_path, "with distance", distance, "km")

find_postman_path(street)
"""