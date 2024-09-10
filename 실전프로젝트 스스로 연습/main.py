import os
import csv
from post import Post

file_path = "./python_prac/실전프로젝트 스스로 연습/data.csv"
post_list = []

# data.csv 파일이 있으면 ----> 게시글 로딩
# data.csv 파일이 없으면 ---> data.csv 파일을 만든다

if os.path.exists(file_path):
    print("게시글 로딩중...")
    f = open(file_path, "r", encoding="utf8")
    reader = csv.reader(f)
    for data in reader:
        post = Post(int(data[0]), data[1], data[2], int(data[3]))
        post_list.append(post)

else:
    f = open(file_path, "w", encoding="utf8", newline="")
    f.close

# 매뉴 출력하기

while True:
    print("---현진의 습작 게시판---")
    print("---매뉴를 선택해주세요---")
    print("1. 게시글 쓰기")
    print("2. 게시글 목록")
    print("3. 프로그램 종료")

    try:
        choice = int(input(">>>"))
    except ValueError:
        print("숫자를 입력해 주셔용!")

    else:
        if choice == 1:
            print("게시글을 작성하였습니다")
            #write_post()
        elif choice == 2:
            print("게시글 목록을 보여줍니다")
            #list_post()    
        elif choice == 3:
            print("저장후 프로그램 종료")
            #save()
            break


