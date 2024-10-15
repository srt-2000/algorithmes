import json

class DynamicSelection:

    def __init__(self):
        self.max_capacity = 4
        self.items_dict = None

    def get_capacity_value(self, items_dict):
        self.items_dict = items_dict
        capacity = [items_dict[item][0] for item in items_dict]
        values = [items_dict[item][1] for item in items_dict]
        return capacity, values

    def get_mem_table(self, items_dict):
        self.items_dict = items_dict
        capacity, values = self.get_capacity_value(items_dict)
        quantity = len(values)
        template_tab = [[0 for _ in range(self.max_capacity + 1)] for _ in range(quantity + 1)]
        for i in range(quantity + 1):
            for j in range(self.max_capacity + 1):
                if i == 0 or j == 0:
                    template_tab[i][j] = 0
                elif capacity[i - 1] <= j:
                    template_tab[i][j] = max(values[i - 1] + template_tab[i - 1][j - capacity[i - 1]],
                                             template_tab[i - 1][j])
                else:
                    template_tab[i][j] = template_tab[i - 1][j]
        return template_tab, capacity, values

    def get_selected_items(self, items_dict):
        self.items_dict = items_dict
        template_tab, capacity, values = self.get_mem_table(items_dict)
        quantity = len(values)
        res = template_tab[quantity][self.max_capacity]
        current_capacity = self.max_capacity
        items_list = []

        for i in range(quantity, 0, -1):
            if res <= 0:
                break
            if res == template_tab[i - 1][current_capacity]:
                continue
            else:
                items_list.append((capacity[i - 1], values[i - 1]))
                res -= values[i - 1]
                current_capacity -= capacity[i - 1]
        selected_items = []

        for search in items_list:
            for key, value in items_dict.items():
                if value == search:
                    selected_items.append(key)
        return selected_items


with open("data/9_1_data.json", "r") as file:
    items = json.load(file)
for i in items:
    items[i] = tuple(items[i])

print(f"Hi, I'm a dynamic programming algorithm.\n"
      f"Let's select the most expensive things into my backpack.\n"
      f"\nWe have things (weight, cost):\n{items}\n"
      f"My backpack weight limit is 4 kg.\n")
a = DynamicSelection()
select = a.get_selected_items(items)
print(f"And I've chosen the best combination for us:\n{select}")