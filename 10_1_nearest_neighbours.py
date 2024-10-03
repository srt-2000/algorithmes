class NNPrediction:

    def __init__(self):
        self.predict_arr = []

    def predict_bread_sales(self, stat_dict, cond, n):
        for i in stat_dict.values():
            for j in range(len(i)):
                i[j] = (cond[j] - i[j]) ** 2

        for i in stat_dict:
            stat_dict[i] = (sum(stat_dict[i])) ** 0.5

        sorted_bread_stat = dict(sorted(stat_dict.items(), key=lambda x: x[1]))

        for i in sorted_bread_stat.keys():
            self.predict_arr.append(i)

        return sum(self.predict_arr[:3]) / n

bread_stat = {
    300: [5, 1, 0],
    225: [3, 1, 1],
    75: [1, 1, 0],
    200: [4, 0, 1],
    150: [4, 0, 0],
    50: [2, 0, 0]
}

condition = [4, 1, 0]
neighbours_number = 3
a = NNPrediction()
print("Hi, I'm a nearest neighbours algorithm.\nLet's make prediction for bread sales.\n")
print("We have a statistics (bread quantity: day condition)\n", bread_stat)
print("We have our today's condition:", condition)
print("With today's conditions", condition, "and we plan to sale about", a.predict_bread_sales(bread_stat, condition, neighbours_number), "breads")

#original code
"""    
def predict_bread_sales(stat_dict, cond, n):
    for i in stat_dict.values():
        for j in range(len(i)):
            i[j] = (cond[j] - i[j]) ** 2
    for i in stat_dict:
        stat_dict[i] = (sum(stat_dict[i])) ** 0.5

    sorted_bread_stat = dict(sorted(stat_dict.items(), key=lambda x: x[1]))

    predict_arr = []
    for i in sorted_bread_stat.keys():
        predict_arr.append(i)

    predict = sum(predict_arr[:3]) / n
    return predict

bread_stat = {
    300: [5, 1, 0],
    225: [3, 1, 1],
    75: [1, 1, 0],
    200: [4, 0, 1],
    150: [4, 0, 0],
    50: [2, 0, 0]
}

condition = [4, 1, 0]
neighbours_number = 3
print("Hi, I'm a nearest neighbours algorithm.\nLet's make prediction for bread sales.\n")
print("We have a statistics (bread quantity: day condition)\n", bread_stat)
print("We have our today's condition:", condition)
print("With today's conditions", condition, "and we plan to sale about", predict_bread_sales(bread_stat, condition, neighbours_number), "breads")
"""