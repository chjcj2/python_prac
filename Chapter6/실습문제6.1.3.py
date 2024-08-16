# 내풀이

import random

def getRandomNumber():
    number = random.randint(1,45)
    return number

number_list = []

while len(number_list) < 7:
    x = getRandomNumber()
    if x not in number_list:
        number_list.append(x)
    else:
        pass

print(number_list.sort())
#chj : sort()가 안먹는 이유를 모르겠다?

# 강의풀이


import random

def getRandomNumber():
    number = random.randint(1,45)
    return number

lotto_num = []
count = 0
 
while True:
    if count > 5:
        break
    random_number = getRandomNumber()
    if random_number not in lotto_num:
        lotto_num.append(random_number)
        count += 1
    
lotto_num.sort()
for num in lotto_num:
    print(num, end=" ")