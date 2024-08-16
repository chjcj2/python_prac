# 내풀이

def printSumAvg(x, y, z):
    print("합계",  ":", x+y+z)
    print("평균",  ":", (x+y+z)/2)

printSumAvg(10, 20, 30)

# 강의풀이
# 문자열 포매팅에 유의 f string

def printSumAvg(x, y, z):
    sum = x + y + z
    avg = sum / 3
    print(f"합계 : {sum} 평균 : {avg}" )

printSumAvg(10, 20, 30)