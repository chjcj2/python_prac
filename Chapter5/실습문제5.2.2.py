arm_test = []
result = []

x = int(input("1일차 턱걸이 갯수를 입력하세요>>>"))
result = arm_test.append(x)
x = int(input("2일차 턱걸이 갯수를 입력하세요>>>"))
result = arm_test.append(x)
x = int(input("3일차 턱걸이 갯수를 입력하세요>>>"))
result = arm_test.append(x)
x = int(input("4일차 턱걸이 갯수를 입력하세요>>>"))
result = arm_test.append(x)
x = int(input("5일차 턱걸이 갯수를 입력하세요>>>"))
result = arm_test.append(x)
x = int(input("6일차 턱걸이 갯수를 입력하세요>>>"))
result = arm_test.append(x)
x = int(input("7일차 턱걸이 갯수를 입력하세요>>>"))
result = arm_test.append(x)

print(arm_test)
avg = (arm_test[0] + arm_test[1]+ arm_test[2]+ arm_test[3]+ arm_test[4]+ arm_test[5]+ arm_test[6]) / 7
print(avg)