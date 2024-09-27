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

processed = []

def find_lower_costs_node(costs):
    lower_cost = float("inf")
    lower_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lower_cost and node not in processed:
            lower_cost = cost
            lower_cost_node = node
    return lower_cost_node

node = find_lower_costs_node(costs)
while node is not None:
    cost = costs[node]
    n_bors = graph[node]
    for n in n_bors.keys():
        new_cost = cost + n_bors[n]
        if new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node
    node = find_lower_costs_node(costs)
    processed.append(node)

print(node)
print(costs)
print(parents)
