class VoteChecker:

    def __init__(self, voted_list):
        self.voted_list = voted

    def check_vote(self, name):
        if self.voted_list.get(name):
            print("Get", name, "out")
        else:
            self.voted_list[name] = True
            print("Ok.Let", name, "vote")

print("Hello!\nI'm a check voted function with hash table.\nI'll control and check the list of voters")
print("\nPlease, input how many people have come to vote:")
vote_qnt = int(input())
voted = {}
checker = VoteChecker(voted)
print("Please, input the name of voter:")

while len(voted) < vote_qnt:
    voter_name = input()
    checker.check_vote(voter_name)
print("\nOur voted list:", voted)