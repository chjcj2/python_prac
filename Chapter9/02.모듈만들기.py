# 초기설정은 루트에있는 모듈만 불러올수 있기때문에 setting.json 파일에 아래를 추가해준다
# (추가) "python.analysis.extraPaths":["./240816_GIT_CODE/Chapter9:"]
# 사실, 모듈에 접근은 가능한데 오류가 뜨지 않게끔 해주는 것이다

import pay_module

# 변수 사용
print(pay_module.version)

# 함수 사용
pay_module.printAuthor()

# 클래스 사용
pay_info = pay_module.Pay("A102030", 13000, "2024-08-18")
print(pay_info.get_pay_info())

# pay_module 파일 자체에서 실행하면 이름이 "__main__"이지만 02.모듈만들기에서 호출하면 이름이 "__pay module"이다
print(pay_module.__name__)  
