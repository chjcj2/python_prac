kor_score = int(input("국어점수를 입력해주세요>>>"))
mat_score = int(input("수학점수를 입력해주세요>>>"))
eng_score = int(input("영어점수를 입력해주세요>>>"))

if kor_score > 100 or mat_score > 100 or eng_score > 100 or kor_score < 0 or mat_score < 0 or eng_score < 0:
     print("잘못입력하셨습니다") 
elif (kor_score + mat_score + eng_score) / 3 >= 80:
    print("불합격") 
else: 
    print("합격")
