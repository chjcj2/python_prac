# 클래스 : 객체를 만들기 위한 설계도  / 클래스는 속성과 메서드의 집합이기도 하다
# 객체 : 설계도(클래스)로부터 만들어낸 제품

# 클래스를 사용하는 이유

print("=========== 클래스를 사용하지 않은 경우 ===========17줄로 구현, 그러나 100여개의 챔피언을 다 구현한다면?")

champion1_name = "이즈리얼"
champion1_health = 700
champion1_attack = 90

print(f"{champion1_name}님 소환사의 협곡에 오신것을 환영합니다.")

champion2_name = "리신"
champion2_health = 800
champion2_attack = 95

print(f"{champion2_name}님 소환사의 협곡에 오신것을 환영합니다.")

champion3_name = "야스오"
champion3_health = 750
champion3_attack = 92

print(f"{champion3_name}님 소환사의 협곡에 오신것을 환영합니다.")

def basic_attack(name, attack):
    print(f"{name} 기본공격 {attack}")

basic_attack(champion1_name, champion1_attack)
basic_attack(champion2_name, champion2_attack)
basic_attack(champion3_name, champion3_attack)

print("=========== 클래스를 사용한경우 ===========14줄로 구현, 챔피언이 많아질수록 편해진다")

class Champion:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        print(f"{self.name}님 소환사의 협곡에 오신것을 환영합니다.")
    def basic_attack(self):
        print(f"{self.name} 기본공격 {self.attack}")

ezreal = Champion("이즈리얼", 700, 90)
leesin = Champion("리신", 800, 95)
yasuo = Champion("야스오", 700, 92)
ezreal.basic_attack()
leesin.basic_attack()
yasuo.basic_attack()

    
