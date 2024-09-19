bread_stat = {
    300: [5, 1, 0],
    225: [3, 1, 1],
    75: [1, 1, 0],
    200: [4, 0, 1],
    150: [4, 0, 0],
    50: [2, 0, 0]
}

condition = [4, 1, 0]
n = 3

for i in bread_stat.values():
    for j in range(len(i)):
        i[j] = (condition[j] - i[j]) ** 2
for i in bread_stat:
    bread_stat[i] = (sum(bread_stat[i])) ** 0.5

sorted_bread_stat = dict(sorted(bread_stat.items(), key=lambda x:x[1]))

predict_arr = []
for i in sorted_bread_stat.keys():
        predict_arr.append(i)

predict = sum(predict_arr[:3])/n

print("with today's conditions", condition, "we have to plan about", predict, "breads")
