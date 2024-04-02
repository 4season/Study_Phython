# 가위, 바위, 보 게임
# input : user
# computer 선택 : 3개의 data중 1개 선택 --> random
# user와 computer의 비교 --> if, 비교연산자, 관계연산자
# user=가위, computer=보 or user=바위, computer=가위 or user=보, computer=바위 --> user : 승리
# 같으면 무승부, 그 외에는 --> 패배
import random as ran
data = ['가위', '바위', '보']
str = ['당신은 {}을 선택했고, 컴퓨터는 {}를 선택했으므로 비겼습니다.', '당신은 {}을 선택했고, 컴퓨터는 {}를 선택했으므로 당신이 졌습니다 ㅠ', '당신은 {}을 선택했고, 컴퓨터는 {}를 선택했으므로 당신이 이겼습니다!']
print('가위바위보 게임.')
choice = input('{}중에 선택해 입력해 주세요.'.format(data))
ranNum = ran.randrange(0, 2)
ranList = data[ranNum]
print('컴퓨터의 선택은...{}!'.format(ranList))
if choice == data[0] and ranNum == 0: # user=0
    print(str[0].format(data[0], data[0]))
elif choice == data[0] and ranNum == 1:
    print(str[1].format(data[0], data[1]))
elif choice == data[0] and ranNum == 2:
    print(str[2].format(data[0], data[2]))
elif choice == data[1] and ranNum == 0: # user=1
    print(str[2].format(data[1], data[0]))
elif choice == data[1] and ranNum == 1:
    print(str[0].format(data[1], data[1]))
elif choice == data[1] and ranNum == 2:
    print(str[1].format(data[1], data[2]))
elif choice == data[2] and ranNum == 0: # user=2
    print(str[1].format(data[2], data[0]))
elif choice == data[2] and ranNum == 1:
    print(str[2].format(data[2], data[1]))
elif choice == data[2] and ranNum == 2:
    print(str[0].format(data[2], data[2]))
else:
    print('{}는 잘못 입력한 선택입니다. 다시 시작해 주세요.'.format(choice))