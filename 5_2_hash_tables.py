page = {"url1": "test1", "url2": "test2", "url3": "test3"}
cache = {}

def get_cache(url):
    if cache.get(url):
        print("It's a cache information")
        return cache[url]
    else:
        data = page.get(url)
        cache[url] = data
        print("It's a server side response")
        return data

print("Let's test a cache:", "You have items: url1, url2, url3", "Input your url")

for i in range(3):
    url = input()
    print(get_cache(url))
print(cache)