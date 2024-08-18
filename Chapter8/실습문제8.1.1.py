# 아이템 공통 : 이름, 가격, 무게, 판매하기, 버리기
# 장비 아이템 : 착용효과, 착용하기
# 소모품 아이템 : 사용효과, 사용하기 * 단, 버리기는 버릴 수 있는 아이템만 가능하다.

# 240818 내풀이
class Item:
    def __init__(self, name, price, weight, isdropable):
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable
    
    def sale(self): #판매하기
        print(f"[{self.name}]을(를) {self.price}에 판매 하였습니다.")
    
    def discard(self): # 버리기
        if self.isdropable == True:
            print(f"[{self.name}]을(를) 버립니다.")
        else:
            print(f"[{self.name}]은(는) 버릴수 없는 물건입니다")

class Wearable(Item):
    def __init__(self, name, price, weight, isdropable, wear_effect):  
        super().__init__(name, price, weight, isdropable)
        self.wear_effect = wear_effect
    def wear(self):  # 착용하기
        print(f"[{self.name}]을(를) 보관 하였습니다.")
        
class Usable(Item):
    def __init__(self, name, price, weight, isdropable, use_effect):
        super().__init__(name, price, weight, isdropable)
        self.use_effect = use_effect
    def use(self): #  사용하기
        print(f"[{self.name}]을(를) {self.use_effect}")

        
portion = Wearable("물약", 100, 15.3, False, "마셔 체력을 보충합니다.")
axe = Usable("도끼", 200, 150.4, True, "휘두릅니다.")
sword = Usable("장검", 370, 90.7, True, "길게 휘둘러 벱니다")
staff = Usable("지팡이", 500, 57.7, True, "조용히 저어 원을 그립니다")

portion.wear()
portion.discard()
portion.sale()
axe.use()
axe.discard()
sword.use()
sword.sale()
staff.use()
staff.discard()


    
              
    