# 2.编写函数，判断用户传入的对象（字符串、元祖、列表）长度是否大于6。

from typing import List


def greater_6(li: List[int]) -> bool:
    if len(li) > 6:
        return True
    else:
        return False


l = [0, 1, 2, 3, 4]
print(greater_6(l))
