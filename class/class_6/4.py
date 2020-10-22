# 4.编写函数，计算传入函数的字符串中，数字、字母、空格以及其他内容的个数，并返回

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
