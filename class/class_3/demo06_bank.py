# 银行金额大写汉字转换
# •	银行电子支票业务在金额部分需要使用大写的汉字，因此需要将用户录入的数字信息转变为汉字。
# •	目前只需完成1~5位整数转换即可。
# •	输入金额:> 32542
# •	汉字转换:>  叁 萬 贰 仟 伍 佰 肆 拾 贰 圆 整
# •	使用For循环完成数字每一位的拆解。
# •	利用列表下标实现对位转换。
# •	程序可以拆分为3个环节实现：
# •	环节1：计算出用户输入金额的位数；
# •	环节2：利用已知位数完成每一位的拆解；
# •	环节3：通过列表下标对位实现最终输出。
# •	需要创建两个列表，为后续对位转换做准备：
# •	汉字列表：['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖', '拾']
# •	单位列表：['圆','拾', '佰', '仟', '萬']
#
#


unit_list = ['圆', '拾', '佰', '仟', '萬']


def num_to_chinese(num_str):
    chinese_list = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖', '拾']
    return chinese_list[int(num_str)]


num = int(input('输入金额'))

if (num >= 0) and (num < 100000):
    num_str = str(num)
    num_str = num_str[::-1]
    chinese_end = ''
    item_counter = 0
    for item in num_str:
        chinese_end = num_to_chinese(item) + unit_list[item_counter] + chinese_end
        item_counter = item_counter + 1
    print(chinese_end + '整')

else:
    print('error')
