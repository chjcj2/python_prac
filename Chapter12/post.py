# post.py는 나중에 main.py의 모듈로 사용될 것.
# 클래스 설계
# - 속성 : 글번호, 제목, 본문, 조회수
# - 메서드 : 게시물 수정하기, 조회수 증가하기, 속성 가져오기

class Post:
    """
        게시물 클래스
        param id : 글번호
        param title : 글제목
        param content : 글내용
        param view_count : 조회수
    """

    def __init__(self, id, title, content, view_count):
        self.id = id
        self.title = title
        self.content = content
        self.view_count = view_count

    def set_post(self, id, title, content, view_count):
        self.id = id
        self.title = title
        self.content = content
        self.view_count = view_count

    def add_view_count(self):
        self.view_count += 1

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content

    def get_view_count(self):
        return self.view_count

# 모듈 안에서 테스트 해보기 위해 아래 코드를 실행 

if __name__ == "__main__":
    post = Post(1,"테스트","테스트입니다",0)
    #post.set_post(1,"테스트2","테스트입니다2",0)
    post.add_view_count()
    print(f"{post.get_id()} {post.get_title()} {post.get_content()} {post.get_view_count()}")




