# -*- coding: cp1251 -*-


print("������� ���������� ��������")
n = int(input())
ms = []

for i in range(n):
    d = {"name": "", 
       "group":"",
       "counts":[0] * 5}
    print("������� ��� �������")
    d["name"] = input()
    print("������� ������ �������")
    d["group"] = input()
    print("������� ������")
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
    print("�������� � 4 � 5 ���")