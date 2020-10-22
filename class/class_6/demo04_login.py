# 模拟个人用户登录
# 要求： 账号：admin  密码：123
# 1. 登录时给3次机会。
# 2. 如果成功，显示欢迎xxx。
# 3. 如果登录失败，显示录入错误你还有x次机会。如果3次机会使用完毕，则显示登录超限，请明天再登录。
# •	1. 登录需要用户名和密码，也就是两个字符串。
# •	2. 用户名和密码应该使用键盘输入，获取两个字符串。
# •	3. 怎么样才算登录成功？需要注册的时候所使用的用户名和密码。
# •	4. 验证输入的用户名和密码和注册时是否一致。
# •	5. 3次机会，使用for
# •	6. 如果登录成功需要跳出循环。显示欢迎xxx。如果失败，需要if判断是否机会使用完毕。


name = 'admin'
password = '123'

for item in range(3):
    name_x = input('please input name  ')
    password_x = input('please input password  ')
    if name == name_x and password == password_x:
        print('欢迎xxx')
        break
    else:
        if item < 2:
            print('录入错误，你还有' + str(2 - item) + '次机会')
        else:
            print('登陆超限，请明天再登陆')
