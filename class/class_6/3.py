# 3.编写函数，检查传入列表的长度，如果大于2，将列表的前两项内容返回给调用者。

from typing import List


def two_item(li: List) -> List:
    if len(li) > 2:
        return li[:2]
    else:
        return


l = [0, 1, 2, 3, 4]
print(two_item(l))
