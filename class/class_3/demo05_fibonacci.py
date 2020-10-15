# 模拟斐波那契数列输出
# 用户输入指定的数列范围
# 正确输出结果
# •	使用input接受用户输入
# •	使用while循环实现


long = int(input('输入数列长度  '))

a = 1
b = 2

if long == 0:
    print('\t')
elif long == 1:
    print(str(a), end='\t')
elif long == 2:
    print(str(a) + '\t' + str(b))
elif long > 2:
    long = long - 2
    print(str(a), end='\t')
    print(str(b), end='\t')
    while long > 0:
        c = a + b
        a = b
        b = c
        print(str(c), end='\t')
        long = long - 1
else:
    print('error')
