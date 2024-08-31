# 게시글 로딩하기 : data.csv파일을 읽는다. --> 데이터 한줄 마다 Post인스턴스를 만든다. --> Post리스트에 인스턴스를 저장한다.
import os
import csv
from post import Post

# 파일경로
file_path = "./Chapter12/data.csv"  #현재는 "python_prac" 이 기본경로여서 그 이하로 경로를 적어주었다

# post 객체를 저장할 리스트
post_list = []

# - data.csv 파일이 있으면 ---> 게시글을 로딩한다.
# - data.csv 파일이 없으면 ---> data.csv 파일을 만든다.
if os.path.exists(file_path):
    # 게시글 로딩
    print("게시글 로딩중...")
    f = open(file_path, "r", encoding="utf8")
    reader = csv.reader(f)
    for data in reader:
        # Post 인스턴스 생성하기
        post = Post(int(data[0]),data[1],data[2],int(data[3]))
        post_list.append(post)
    pass
else:
    # 파일 생성하기
    f = open(file_path, "w", encoding="utf8", newline="")
    f.close()

print(post_list[0].get_title())
