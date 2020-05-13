# i = 1
# while i <= 10:
#     i += 1
#     print(i)


# 例题：假如投资年利率未5%，试求从1000块增长到5000块，需要花多少年？
# money = 1000
# count = 0
# while money < 5000:
#     money *= 1.05
#     count += 1
# print("一共需要" + str(count) + "年")

import math
for i in range(100, 1000):
    a = i // 100
    b = i // 10 % 10
    c = i % 10
    tmp = math.pow(a, 3) + math.pow(b, 3) + math.pow(c, 3)
    if tmp == i:
        print("水仙花数为：" + str(i))


condition = True
if condition:
    pass
elif False:
    pass
else:
    pass

while condition:
    pass

# python中do...while...语句
while True:
    pass
    if condition:
        break

result = 0
for i in range(1, 101):
    result += i
print(result)


def is_shuixianhua(num):
    if num>=100 and num <=999:
        a = num//100
        b = num//10 % 10
        c = num % 10
        if pow(a, 3)+pow(b, 3)+pow(c, 3) == num:
            return 1
        else:
            return 0
    else:
        return 2

class People:


people1 = People




