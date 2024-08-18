# 아이템 공통 : 이름, 가격, 무게, 판매하기, 버리기
# 장비 아이템 : 착용효과, 착용하기
# 소모품 아이템 : 사용효과, 사용하기 * 단, 버리기는 버릴 수 있는 아이템만 가능하다.

# 240818 강의풀이 (내풀이에 대한 평가 : 전체적으로 거의 강의풀이와 비슷하게 잘 만들었다)
class Item:
    def __init__(self, name, price, weight, isdropable):
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable
    
    def sale(self): #판매하기
        print(f"[{self.name}] 하나를 {self.price}에 판매 하였습니다.")
    
    def discard(self): # 버리기
        if self.isdropable: # 내 풀이와 다른점 : 굳이 "== True" 를 쓰지 않아도 작동함 즉, True로 인식함
            print(f"[{self.name}]을(를) 하나 버립니다.")
        else:
            print(f"[{self.name}]은(는) 버릴수 없는 물건입니다")

class Wearable(Item):
    def __init__(self, name, price, weight, isdropable, wear_effect):  
        super().__init__(name, price, weight, isdropable)
        self.wear_effect = wear_effect
    def wear(self):  # 착용하기
        print(f"[{self.name}]을(를) 하나 착용 하였습니다.")
        
class Usable(Item):
    def __init__(self, name, price, weight, isdropable, use_effect):
        super().__init__(name, price, weight, isdropable)
        self.use_effect = use_effect
    def use(self): #  사용하기
        print(f"[{self.name}]을(를) {self.use_effect}")

        
portion = Usable("투명물약", 100, 0.2, False, "하나 마셔 체력을 80%까지 회복합니다.")
sword = Wearable("이가닌자의 장검", 370, 7.8, True, "길게 휘둘러 80의 데미지를 줍니다")

portion.use()
portion.discard()
portion.sale()

sword.wear()
sword.sale()
sword.discard()
sword.sale()