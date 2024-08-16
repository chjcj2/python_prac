# ver=2.0

ko_word = ["사랑해","귀엽다","고마워","행복해"]
score = 0 

print("Let't Learning Korean")

for word in ko_word:
    print(word)
    writing = input()
    if writing == word:
        score += 1

print("전체 문제 개수>>>> ", len(ko_word), "개")
print("맞힌 문제 개수>>>> ", score, "개")
print("틀린 문제 개수>>>> ", 4 - score, "개")


        