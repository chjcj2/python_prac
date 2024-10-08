class Post:
    """
    게시물 클래스
    param id : 글번호
    param title : 글제목
    param content : 본문내용
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

# 테스트 

if __name__ == "__main__":
    post = Post(1, "3번째", "현진3번째연습", 0)
    post.set_post(1, "3번째2", "현진3번째연습2", 0)
    post.add_view_count()
    print(f"{post.get_id()} {post.get_title()} {post.get_content()} {post.get_view_count()}")