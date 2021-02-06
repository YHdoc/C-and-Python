#컴퓨터가 생각한 숫자 맞추기
#랜덤이라는 함수를 사용할 것임.
import random
com = random.randint(1, 100)
a = '리오'
print("컴퓨터가 생각한 랜덤 숫자 맞추기!", '\n총 7번의 기회가 주어집니다!', f'\n못 맞추면 {a}에 전화걸기.')

# count = 0
# while count < 7:
#     num = int(input('숫자를 입력해주세요: '))
#     if count == 6:
#         print('기회 없음!')
#         break
#     if num == 0:
#         break
#     elif num > com:
#         print('더 낮은 숫자를 입력하세요.')
#         count += 1
#     elif num < com:
#         print('더 높은 숫자를 입력하세요.')
#         count += 1
#     elif num == com:
#         print('%d번 만에 성공하셨습니다!'%(count+1))
#         print('정답입니다!')
#         break
for i in range(1, 8):
    player = int(input('숫자를 입력하세요: '))
    if player == com:
        print('정답입니다!')
        print(f'{i}번 만에 성공하셨습니다!')
    elif player > com:
        print('더 낮은 수를 입력하세요!', '기회는 %d번 남았습니다.'%(7-i))
    elif 0 < player < com:
        print('더 높은 수를 입력하세요!', '기회는 %d번 남았습니다.'%(7-i))
    elif player == 0:
        break
