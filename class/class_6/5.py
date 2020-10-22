
# 5.编写函数，返回两个数字参数中较大的那个数字


def num_big(num1: float, num2: float) -> float:
    if num1 > num2:
        return num1
    else:
        return num2


print(num_big(2, 4))
