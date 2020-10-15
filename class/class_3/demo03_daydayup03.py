# 一年365天，如果以3天打鱼2天晒网的学习态度持续学习一年，学习效果如何？
# 请编码实现以上案例的效果，并保存为demo03_daydayup03.py。


circulation_list = [1, 1, 1, 0, 0]
pointer = 0
study = 1
a = 0
b = 0
for item in range(365):
    if pointer == 5:
        pointer = 0
    if circulation_list[pointer]:
        study = study * 1.01
        a = a + 1
    else:
        study = study * 0.99
        b = b + 1
    pointer = pointer + 1

print(study)
print(a)
print(b)
