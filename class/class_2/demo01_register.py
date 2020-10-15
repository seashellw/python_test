# 模拟用户个人信息注册，需要输入用户个人信息
# 姓名、性别、年龄、血型、身高、电话
# 信息，并输出显示。
# 使用input(）获取输入内容
# 格式化输出显示信息
# 使用占位符及格式输出符输出信息


name = input('input:name:')
age = int(input('input:age:'))
print('name=%s,age=%d' % (name, age))
print(f'name={name},age={age}')
