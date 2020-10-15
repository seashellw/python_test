# 求出2-1000内的所有回文素数。
# 只能被1和本身整除的整数叫素数；若一个素数从左向右和从右向左是相同的数，
# 则该素数为回文素数。编程求出2-1000内的所有回文素数。

for i in range(2, 1001):
    mark = 1
    for j in range(2, i):
        if i % j == 0:
            mark = 0
            break
    if mark:
        a = str(i)
        b = a[::-1]
        if a == b:
            print(i)
