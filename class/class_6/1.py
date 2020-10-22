# 编写函数，检查获取传入列表或者元祖对象的所有奇数为索引对应的元素


from typing import List


def odd(li: List[int]) -> List[int]:
    end_li: list[int] = []
    for i in range(len(li)//2):
        item = i*2+1
        end_li.append(li[item])
    return end_li


l = [0, 1, 2, 3, 4]
print(odd(l))


# name = 'admin'
# password = '123'

# for item in range(3):
#     name_x = input('please input name  ')
#     password_x = input('please input password  ')
#     if name == name_x and password == password_x:
#         print('欢迎xxx')
#         break
#     else:
#         if item < 2:
#             print('录入错误，你还有' + str(2 - item) + '次机会')
#         else:
#             print('登陆超限，请明天再登陆')
