# 함수를 이용한 메뉴 주문 프로그램
# 1. 메뉴 입력문을 함수를 사용하여 표현하세요

menu_list=[{'name': 'Americano', 'price': 3500},
          {'name': 'Cafe latte', 'price': 4000},
          {'name': 'Ice tea', 'price': 4500}]

menu_list.append({'name': 'Capuccino', 'price': 5000})

print('---------> 메뉴판 <----------')
for i in menu_list:
    print('{:14} | {:10d}원'.format(i['name'], i['price']))

order=input('주문할 메뉴를 입력해 주세요(쉼표로 구분) : ')

def order_system(order):
    newListName=[]
    newListPrice=[]
    values={}
    
    for i in menu_list:
        newListName.append(i['name'])
        newListPrice.append(i['price'])

    for k in order:
        if k in newListName:
            newPrice=newListName.index(k)            
            values[k]=newListPrice[newPrice]
        else:
            return print('{}는 없는 메뉴 입니다. 처음부터 다시 주문해 주세요.'.format(k))
            break

    return values

order_list=order_system(order.split(','))
order_price=0

print('---------> 영수증 <----------')
for j in order_list:
    print('{:14} | {:10}원'.format(j, order_list[j]))
    order_price+=order_list[j]
print('----------------------------')
print('합계 : {:21}원'.format(order_price))