# 输出九九乘法表


for i in range(9):
    for j in range(i + 1):
        a = i + 1
        b = j + 1
        print(f'{a}*{b}=' + ('%2s' % str(a * b)), end='  ')
    print()
