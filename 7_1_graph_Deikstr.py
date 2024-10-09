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

graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}
# ====end graph======

costs = {}
costs["a"] = 6
costs["b"] = 2
infinity = float("inf")
costs["fin"] = infinity
# ====end costs======

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None
# =====end parents===

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