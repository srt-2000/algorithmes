from collections import deque

graph = {}
graph["you"] = ["Vova", "Max", "Demon"]
graph["Vova"] = ["Leo", "Alex"]
graph["Max"] = ["Denis", "Dima"]
graph["Demon"] = ["Ann"]
graph["Leo"] = []
graph["Alex"] = []
graph["Denis"] = ["Andrey"]
graph["Dima"] = []
graph["Ann"] = []
graph["Andrey"] = []

def mango_seller(name):
    return name[-1] == "m"

def search_mango_seller(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if mango_seller(person):
                print(person, "is mango seller")
                return True
            else:
                searched.append(person)
                search_queue += graph[person]
    print("There are not mango-sellers in my friends circle")
    return False

search_mango_seller("you")