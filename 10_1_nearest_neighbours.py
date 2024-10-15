import json

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

with open("data/10_1_data.json", "r") as file:
    bread_stat = json.load(file)
bread_stat = {int(k):v for k,v in bread_stat.items()}
condition = [4, 1, 0]
neighbours_number = 3
a = NNPrediction()
print("Hi, I'm a nearest neighbours algorithm.\nLet's make prediction for bread sales.\n")
print("We have a statistics (bread quantity: day condition)\n", bread_stat)
print("We have our today's condition:", condition)
print("With today's conditions", condition, "and we plan to sale about", a.predict_bread_sales(bread_stat, condition, neighbours_number), "breads")