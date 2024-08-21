# 원화 입력, 환율 입력 ->달러 표시하는 프로그램

won = input("원화금액을 입력 하세요>>>")
dollar = input("환율을 입력하세요>>>")

try: # 예외가 발생할수 있는 코드
    print(int(won) / int(dollar))
except ValueError as e: # 예외가 발생했을때 실행되는 코드
    print("예외가 발생했습니다.", e)
except ZeroDivisionError as e:
    print("예외가 발생했습니다.", e)
else:
    print("예외가 발생하지 않았을때 실행되는 코드")
finally:
    print("예외 발생여부에 관계없이 실행되는 코드")