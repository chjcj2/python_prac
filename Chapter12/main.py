# 게시글 로딩하기
import os

# 파일경로
file_path = "./python_prac/Chapter12/data.csv"

# - data.csv 파일이 있으면 ---> 게시글을 로딩한다.
# - data.csv 파일이 없으면 ---> data.csv 파일을 만든다.
if os.path.exists(file_path):
    # 게시글 로딩
    pass
else:
    # 파일 생성하기
    f = open(file_path, "w", encoding="utf8", newline="")
    f.close()

    
