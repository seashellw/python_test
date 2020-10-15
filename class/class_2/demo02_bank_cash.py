# 使用input()函数模仿扫描商品二维码的功能，依次录入用户输入的金额，
# 金额使用浮点数表示。当录入完所有选购的商品之后，对这些金额进行相加运算，
# 得到一个由浮点数表示的结果。对程序而言，抹零功能可通过浮点数到整数的转换实现。

price = int(input('input:price:'))
price = int(price)
print('price is:%d' % price)
