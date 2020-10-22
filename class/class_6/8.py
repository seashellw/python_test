
# 8.编写函数，传入函数中多个实参（均为字典），
#     将每个实参的每个元素依次加入到函数的动态参数kwargs里面，
#     例如传入两个参数{'one':1} {'two':2}, 最终kwargs为{'one': 1, 'two': 2}。


def kwargs_add(**kwargs) -> dict:
    return kwargs


s1 = {'one': 1}
s2 = {'two': 2}

print(kwargs_add(**s1, **s2))
