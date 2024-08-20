# 실습문제 - 주식 수익금 및 수익률 출력

# 내풀이 (실수한부분 : list로 만들어 주는것, str을 int로 만들어주는 것, 함수(메서드>를 만들어서 쉽게 만드는 것 등)
import csv

# data = [
#     ["종목","매입가","수량","목표가"],
#     ["삼성전자",85000,10,90000],
#     ["NAVER",380000,5,400000]
# ]

# file = open("./python_prac/Chapter10/mystock.csv","w",newline="",encoding="utf-8-sig")
# writer = csv.writer(file)

# for d in data:
#     writer.writerow(d)

# file.close()

# 수익금 계산

# file = open("./python_prac/Chapter10/mystock.csv","r",encoding="utf-8-sig")
# reader = csv.reader(file)   # 여기서 reader는 list가 아니어서 인덱싱도 안된다. 따라서 list로 바꿔줘야 할듯

# reader_list = list(reader)
# print(type(reader_list[1][3]))
# profit1 = int(reader_list[1][3]) - int(reader_list[1][1])
# profit1 = int(reader_list[2][3]) - int(reader_list[2][1])
# rr1 = (int(reader_list[1][3])/int(reader_list[1][1]) -1) * 100
# rr2 = (int(reader_list[2][3])/int(reader_list[2][1]) -1) * 100

# print(profit1)
# print(profit1)
# print(round(rr1,2))
# print(round(rr2,2))
    
# 강의풀이

# 오류 해결 과정 중심!

def show_profit(data):
    stock_name = data[0]
    purchase_price = int(data[1])
    stock_amount = int(data[2])
    target_price = int(data[3])

    profit = (target_price - purchase_price) * stock_amount
    profit_ratio = (target_price/purchase_price - 1) * 100

    print(f"{stock_name}의 수익금은 {profit}원 이고 수익률은 {profit_ratio:.2f}%입니다")

file = open("./python_prac/Chapter10/mystock.csv","r",encoding="utf-8-sig")
reader = list(csv.reader(file))  # <---여기서 미리 list로 만들어준다

for data in reader[1:]:
    show_profit(data)
