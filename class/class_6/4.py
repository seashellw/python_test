# 4.编写函数，计算传入函数的字符串中，数字、字母、空格以及其他内容的个数，并返回

# 4.编写函数，计算传入函数的字符串中，数字、字母、空格以及其他内容的个数，
#     并返回
# 5.编写函数，返回两个数字参数中较大的那个数字
# 6.编写函数，接收多个数字，求和并返回。
# 7.编写函数，传入函数中多个实参
#     （均为可迭代对象，如字符串、元祖、列表、集合等），
#     将每个实参的每个元素依次加入到函数的动态参数args里面，
#     例如传入两个参数[1, 2, 3] (10, 20）最终args为（1,2,3,10,20)
# 8.编写函数，传入函数中多个实参（均为字典），
#     将每个实参的每个元素依次加入到函数的动态参数kwargs里面，
#     例如传入两个参数{'one':1} {'two':2}, 最终kwargs为{'one': 1, 'two': 2}。
import re

from typing import Dict


def num(s: str) -> Dict[str, int]:
    number_num = 0
    letter_num = 0
    space_num = 0
    else_num = 0
    for item in s:
        if re.match("[0-9]", item):
            number_num = number_num+1
        elif re.match("[a-zA-Z]", item):
            letter_num = letter_num+1
        elif re.match(r"\s", item):
            space_num = space_num+1
        else:
            else_num = else_num+1
    return {"number_num": number_num, "letter_num": letter_num, "space_num": space_num, "else_num": else_num}


s = "12345qwer    "
print(num(s))
