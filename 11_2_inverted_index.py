inv_hash = {
    "hi": ["a", "b"],
    "there": ["a", "c"],
    "adit": "b",
    "we": "c",
    "go": "c"
}
print(inv_hash)

a = "hi there"
b = "hi adit"
c = "there we go"

d = input()
def find_world(d):
    if d in inv_hash:
        print("this world is on page -", inv_hash[d])

find_world(d)