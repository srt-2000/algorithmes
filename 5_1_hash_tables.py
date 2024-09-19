voted = {}
def check_vote(name):
    if voted.get(name):
        print("Get", name, "out")
    else:
        voted[name] = True
        print("Ok.Let", name, "vote")

print("Please, input how many people will come to vote:")
vote_qnt = int(input())

print("Please, input the name of voter:")
for i in range(vote_qnt):
    voter_name = input()
    check_vote(voter_name)
print(voted)
