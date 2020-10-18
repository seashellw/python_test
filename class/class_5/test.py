
# html = '''%abc%%def%python(ghi)'''
# print(re.subn(r'%[\s\S]*%', '&', html))


def fun(n: int) -> list:
    a: int = 1
    b: int = 1
    l = []
    for i in range(1, n + 1):  # i的取值是1到n
        l.append(a)
        a, b = b, a + b  # 更新斐波那契数列的第i+1项的值，并计算第i+2项的值
    return l


n: int = int(input('input a number'))
li = fun(n)


print(li)
