# 解决“百钱百鸡”问题
# 一只公鸡值五钱，一只母鸡值三钱，三只小鸡值一钱。

rooster_price = 5
hens_price = 3
three_chicken_price = 1

for item_rooster_num in range(100):
    for item_hens_num in range(100):
        for item_three_chicken_num in range(100):
            price = item_rooster_num * rooster_price
            price = price + item_hens_num * hens_price
            price = price + item_three_chicken_num * three_chicken_price
            num = item_rooster_num + item_hens_num + 3 * item_three_chicken_num
            if price == 100 and num == 100:
                print(f'公鸡为{item_rooster_num}只，母鸡为{item_hens_num}只，小鸡为{item_three_chicken_num * 3}只')
