import json

class BestPath:

    def __init__(self):
        self.processed = []

    def find_lower_costs_node(self, costs_gr):
        lower_cost = float("inf")
        lower_cost_node = None
        for node in costs_gr:
            cost = costs_gr[node]
            if cost < lower_cost and node not in self.processed:
                lower_cost = cost
                lower_cost_node = node
        return lower_cost_node

    def dsa(self, graph_gr, costs_gr, parents_gr):
        node = self.find_lower_costs_node(costs_gr)
        while node:
            cost = costs_gr[node]
            n_bors = graph_gr[node]
            for n in n_bors.keys():
                new_cost = cost + n_bors[n]
                if new_cost < costs_gr[n]:
                    costs_gr[n] = new_cost
                    parents_gr[n] = node
            self.processed.append(node)
            node = self.find_lower_costs_node(costs_gr)
        return self.processed

with open("data/7_1_graph_data.json", "r") as file1:
    graph = json.load(file1)
with open("data/7_1_costs_data.json", "r") as file2:
    costs = json.load(file2)
costs["fin"] = float("inf")
with open("data/7_1_parents_data.json", "r") as file3:
    parents = json.load(file3)

a = BestPath()
path = a.dsa(graph, costs, parents)

print("We have a graph with different paths to get our point:\n",graph,"\n")
print("I've used the DSA Dijkstra's Algorithm\nand found our minimal trip:", ['start'] + path[:(path.index("fin") + 1):])

'''
#original code
def find_lower_costs_node(costs):
    lower_cost = float("inf")
    lower_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lower_cost and node not in processed:
            lower_cost = cost
            lower_cost_node = node
    return lower_cost_node

processed = []
node = find_lower_costs_node(costs)
while node:
    cost = costs[node]
    n_bors = graph[node]
    for n in n_bors.keys():
        new_cost = cost + n_bors[n]
        if new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lower_costs_node(costs)

print(node)
print(costs)
print(parents)
print(processed)
'''