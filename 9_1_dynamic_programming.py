items_dict = {
    "audio": (4, 3000),
    "notebook": (3, 2000),
    "guitar": (1, 1500),
    "iphone": (1, 2000)
}

def get_capacity_value(items_dict):
    capacity = [items_dict[item][0] for item in items_dict]
    values = [items_dict[item][1] for item in items_dict]
    return capacity, values

def get_mem_table(items_dict, max_capacity = 4):
    capacity, values = get_capacity_value(items_dict)
    quantity = len(values)
    template_tab = [[0 for j in range(max_capacity + 1)] for i in range(quantity + 1)]
    for i in range(quantity + 1):
        for j in range(max_capacity + 1):
            if i == 0 or j == 0:
                template_tab[i][j] = 0
            elif capacity[i - 1] <= j:
                template_tab[i][j] = max(values[i - 1] + template_tab[i - 1][j - capacity[i - 1]], template_tab[i - 1][j])
            else:
                template_tab[i][j] = template_tab[i - 1][j]
    return template_tab, capacity, values

def get_selected_items(items_dict, max_capacity = 4):
    template_tab, capacity, values = get_mem_table(items_dict)
    quantity = len(values)
    res = template_tab[quantity][max_capacity]
    current_capacity = max_capacity
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
    print(items_list)
    selected_items = []

    for search in items_list:
        for key, value in items_dict.items():
            if value == search:
                selected_items.append(key)
    return selected_items

select = get_selected_items(items_dict)
print(select)
#backpack