# 1. 파이썬 객체를 pickle로 저장하기
import pickle

# data = {
#     "목표1" : "매일 팔굽혀 펴기 100회",
#     "목표2" : "매일 코딩 공부 1시간"
# }

# file = open("./python_prac/Chapter10/data.pickle", "wb") # wb(writh binary)는 컴퓨터가 이해할수 있는 binary로 쓴다는 뜻
# pickle.dump(data, file)
# file.close()

# 2. pickle 파일 파이썬으로 가져오기
file = open("./python_prac/Chapter10/data.pickle", "rb") # rb(read binary)
data = pickle.load(file)
print(data)
file.close()    