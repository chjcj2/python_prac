# 모듈이란 "한개의 완성된 프로그램 파일"을 의미한다
# --- 사용 방법 ---
# import 모듈이름  : import math
# 모듈이름.변수    : print(math.pi)
# 모듈이름.함수()  : print(math.ceil(2.7))

# 내장모듈
# : 파이썬 설치시 자동으로 설치되는 모듈

from math import pi, ceil as c  # ceil은 "올림함수"
print(pi)
print(c(2.7))