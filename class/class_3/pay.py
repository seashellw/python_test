# 通过员工的销售额计算该员工的薪水总额并输出。
# 一只某公司有一批销售员工，其底薪是2000元，员工销售额与提成比例如下：
# •当销售额<=3000时，没有提成。
# •当3000<销售额<=7000时，提成10%。
# •当销售额>10000时，提成20%。
# 编程，通过员工的销售额计算该员工的薪水总额并输出。

pay = 0
sales_volume = int(input('输入员工的销售额：'))
if sales_volume <= 3000:
	pay = 2000
elif (sales_volume > 3000) and (sales_volume <= 7000):
	pay = 2000 + sales_volume * 0.1
elif sales_volume > 10000:
	pay = 2000 + sales_volume * 0.2
else:
	print('error')
print(pay)
