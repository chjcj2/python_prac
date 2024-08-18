# 1. import 패키지.모듈
import unit.character
unit.character.test()

# 2. from 패키지 import 모듈   <-- 두번째 방식이 제일 많이 사용된다.

from unit import item
item.test()

# 3. from 패키지 import *    <-- 패키지 안에 있는 모든 모듈을 호출

from unit import * # *를 쓸때에는 __init__ 모듈을 수정해주어야 한다  
character.test()   # : __init__ 모듈에 다음과 같이 추가 --> from . import character, item, monster 
item.test()   
monster.test()   
                    
# 4. import 패키지
import unit
character.test()
item.test()   
monster.test() 