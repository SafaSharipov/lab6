# -*- coding: cp1251 -*-


print("Введите количество учеников")
n = int(input())
ms = []

for i in range(n):
    d = {"name": "", 
       "group":"",
       "counts":[0] * 5}
    print("Введите ФИО ученика")
    d["name"] = input()
    print("Введите группу ученика")
    d["group"] = input()
    print("Введите оценки")
    for j in range(5):
        d["counts"][j] = int(input())
    ms.append(d)

ms.sort(key=lambda x: sum(x["counts"])/5)
flag = True;
for i in range(n):
    if (1 in ms[i]["counts"] or 2 in ms[i]["counts"] or 3 in ms[i]["counts"]):
        continue;
    else:
        print(ms[i]["name"], ms[i]["group"])
        flag = False
if flag:
    print("Учеников с 4 и 5 нет")