# 시퀀스 자료형
# 키와 데이터를 가지고 있는 사전형 자료형
# 사전 형태의 자료를 만들때 편리

stock_a = {"삼성전자" : 82000, "LG전자" : 150000}

stock_b = {
    "삼성전자" : [82000,81500,82500,82000,83000],   # 리스트도 들어가고 튜플도 들어간다
    "LG전자" : (150000,149000,148000,151000,152000)
}

stock_c = {
    "삼성전자" : {"현재가" : 82000,
                 "보유수량" : 5,
                 "매수단가" : 81000
              }
}

# print(stock_a)
# print(stock_b)
# print(stock_c)

# 딕셔너리 접근하기
print(stock_a["삼성전자"])
print(stock_c["삼성전자"]["보유수량"])

# 딕셔너리 할당하기
stock_a["삼성전자"] = 85000
print(stock_a)

# 딕셔너리 삭제하기
del stock_a["LG전자"]
print(stock_a)

# 딕셔너리 함수
stock_d = {
    "삼성전자" : 82000,
    "SK하이닉스" : 123000,
    "NAVER" : 370000,
    "카카오" : 133000
}

# items() : 키와 데이터 쌍
for item in stock_d.items():
    print(item)

# keys() : 키
for key in stock_d.keys():
    print(key)

# values() : 데이터
for value in stock_d.values():
    print(value)



