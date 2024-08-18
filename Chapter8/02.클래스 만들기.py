class Monster:
    def say(self):
        print("나는 몬스터다!")

# 클래스 호출방법
# 인스턴스 = 클래스이름()    -->(예시) goblin = Monster()
# 인스턴스.메서드()          -->(예시) goblin.say()

goblin = Monster()
goblin.say()

# 파이썬에서는 자료형도 클래스다!
a = 10
b = "문자열 객체"
c = True

print(type(a))
print(type(b))
print(type(c))