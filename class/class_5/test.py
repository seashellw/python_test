
# html = '''%abc%%def%python(ghi)'''
# print(re.subn(r'%[\s\S]*%', '&', html))


# def fun(n: int) -> list:
#     a: int = 1
#     b: int = 1
#     l = []
#     for i in range(1, n + 1):  # i的取值是1到n
#         l.append(a)
#         a, b = b, a + b  # 更新斐波那契数列的第i+1项的值，并计算第i+2项的值
#     return l


# n: int = int(input('input a number'))
# li = fun(n)
# print(li)


# def StudentInfo(name, chineselevel, country):
#     print('姓名：%s,中文水平：%s,国家：%s' % (name, chineselevel, country))


# d = {'country': '中国', 'name': 'llc', 'chineselevel': '良好'}
# StudentInfo(**d)


# l = [0.02, 0.024, 0.028, 0.0325]

# n = [[10000.0, 10000.0, 10000.0, 10000.0],
#      [10000.0, 10000.0, 10000.0, 10000.0],
#      [10000.0, 10000.0, 10000.0, 10000.0],
#      [10000.0, 10000.0, 10000.0, 10000.0],
#      [10000.0, 10000.0, 10000.0, 10000.0],
#      [10000.0, 10000.0, 10000.0, 10000.0],
#      [10000.0, 10000.0, 10000.0, 10000.0],
#      [10000.0, 10000.0, 10000.0, 10000.0],
#      [10000.0, 10000.0, 10000.0, 10000.0],
#      [10000.0, 10000.0, 10000.0, 10000.0],
#      [10000.0, 10000.0, 10000.0, 10000.0]]
# i = 1
# n[0] = [10000.0, 10000.0, 10000.0, 10000.0]

# while i < 11:
#     n[i][0] = n[i-1][0]*(1.0+l[0])
#     n[i][1] = n[i-1][1]*(1.0+l[1])
#     n[i][2] = n[i-1][2]*(1.0+l[2])
#     n[i][3] = n[i-1][3]*(1.0+l[3])
#     i = i+1

# i = 0
# while i < 11:
#     print(f'{i}年  {n[i][0]}  {n[i][1]}  {n[i][2]}  {n[i][3]}')
#     i = i+1


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        # 找到中点
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 翻转后半
        pre, cur = None, slow.next
        slow.next = None
        while cur:
            nxt = cur.next
            cur.next = pre
            pre, cur = cur, nxt
        # 交替合并
        p, q = head, pre
        while q:
            nxt = p.next
            p.next = q
            p, q = q, nxt
