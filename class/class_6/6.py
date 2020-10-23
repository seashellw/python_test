
# 6.编写函数，接收多个数字，求和并返回。
# 7.编写函数，传入函数中多个实参
#     （均为可迭代对象，如字符串、元祖、列表、集合等），
#     将每个实参的每个元素依次加入到函数的动态参数args里面，
#     例如传入两个参数[1, 2, 3] (10, 20）最终args为（1,2,3,10,20)
# 8.编写函数，传入函数中多个实参（均为字典），
#     将每个实参的每个元素依次加入到函数的动态参数kwargs里面，
#     例如传入两个参数{'one':1} {'two':2}, 最终kwargs为{'one': 1, 'two': 2}。


def num_sum(*nums) -> float:
    sum: float = 0
    for item in nums:
        sum = sum+item
    return sum


print(num_sum(2, 4, 7, 3))