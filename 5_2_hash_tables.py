import json

class CashTest:

    def __init__(self):
        self.data = None

    def get_cache(self, url_name):
        if cache.get(url_name):
            print("It's a cache information")
            return cache[url_name]
        else:
            self.data = page.get(url_name)
            cache[url_name] = self.data
            print("It's a server side response")
            return self.data

with open("data/5_2_data.json", "r") as file:
    page = json.load(file)
cache = {}
print("You have urls:", list(page.keys()), "\nYou have 6 attempts. \nInput your url to make a CASH test:")
tester = CashTest()
for i in range(6):
    url = input()
    print(tester.get_cache(url))
print("\nYou've done all of your attempts.\n", "The log of your tests" ,cache)