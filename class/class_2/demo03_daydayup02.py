# 一年365天，每天进步5‰或者1%，累计进步多少？
# 1.005   1.01
# 一年365天，每天退步5‰或者1%，累计剩下多少？
# 0.995   0.99

import random

x = 1
for item in range(1, 366):
    if random.randint(0, 1):
        x = x * 1.005
    else:
        x = x * 1.01
print(f'一年365天，每天进步5‰或者1%，累计进步多少？{x}')
x = 1
for item in range(1, 366):
    if random.randint(0, 1):
        x = x * 0.995
    else:
        x = x * 0.99
print(f'一年365天，每天退步5‰或者1%，累计剩下多少？{x}')
