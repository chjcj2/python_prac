# 튜플
# : 읽기 전용 리스트 - 수정으로부터 안전하고 메모리를 덜 잡아먹는다

a = (3, 4, 5)
b = 3, 4, 5
c = (3,)   # 데이터 하나만 넣을때는 반드시 쉼표(,)를 붙여줘야 한다
d = 3,

e = tuple([3,4,5])

f = list(range(10))
g = tuple(f)

h = 3, 4, 5
i = list(h)

# 튜플 관련 함수
x = 5, 6, 7, 8
print(max(x))
print(min(x))
print(x.count(6))
print(x.index(7))