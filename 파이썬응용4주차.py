# 카페 메뉴 주문 & 영수증 발행
# 1. 메뉴 보여주기 --> print('아메리카노', '녹차', '유자차', '라떼')
# 2. 메뉴 주문 받기 --> input
# 3. 영수증 출력 (상품명, 가격 표시)
import json
print('카페에 오신것을 환영합니다 😀')
menu = ['에스프레소(1,500원)', '아메리카노(1,500원)', '카페라떼(2,500원)', '바닐라라떼(3,500원)', '카페모카(3,500원)', '콜드브루(2,500원)', '콜드브루 라떼(3,500원)', '녹차라뗴(4,500원)', '딸기라떼(4,500원)']
menuStr = '{"에스프레소": 1500, "아메리카노": 1500, "카페라떼": 2500, "바닐라라떼": 3500, "카페모카": 3500, "콜드브루": 2500, "콜드브루라떼": 3500, "녹차라떼": 4500, "딸기라떼": 4500}'
menuJson = json.loads(menuStr)
sum = 0
print('저희 카페 메뉴판 입니다. 천천히 고민하고 주문해 주세요 😀')
print('-------------------')
for i in range (0, len(menu)):
    print(menu[i], end='\n')
    print('-------------------')
sell = input('어떤 메뉴를 선택하시겠습니까? (","를 이용하여 메뉴를 구분해 주세요 :D)\n')
result=sell.split(',')
for j in range (0, len(result)):
    if result[j] in list(menuJson.keys()):
        if j<1:
            print('-------------------')
            print('영수증')
            print('-------------------')
            print('주문하신 메뉴는...')
            print('{}({}원)'.format(result[j], menuJson[result[j]]))
            sum+=menuJson[result[j]]
        else:
            print('{}({}원)'.format(result[j], menuJson[result[j]]))
            sum+=menuJson[result[j]]  
    else:
        print('--------------------')
        print('{}는 없는 메뉴 입니다. 다시 선택해 주세요.'.format(result[j]))
        resell = input()
        if resell in list(menuJson.keys()):
            result[j] = resell
            if j<1:
                print('-------------------')
                print('영수증')
                print('-------------------')
                print('주문하신 메뉴는...')
                print('{}({}원)'.format(result[j], menuJson[result[j]]))
                sum+=menuJson[result[j]]
            else:
                print('{}({}원)'.format(result[j], menuJson[result[j]]))
                sum+=menuJson[result[j]]  
            continue
        else:
            print('--------------------')
            print('{}는 없는 메뉴 입니다. 처음부터 다시 선택해 주세요.'.format(resell))
            break
print('--------------------')
print('결제하실 금액: {}원'.format(sum))