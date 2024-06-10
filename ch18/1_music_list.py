import random
import copy

MP3_REGIST  = 1
MP3_LIST    = 2
MP3_DELETE  = 3
SYSTEM_OUT  = 99

ALIGN_ORIGIN    = 1
ALIGN_ASC       = 2
ALIGN_DESC      = 3
ALIGN_SUFFLE    = 4

print("=== MP3 리스트 프로그램 ===")

mp3s = []

def printMp3s(items):
    for index, item in enumerate(items):
        print(f'{index+1} {item}')

def alignMp3s(align_method):

    mp3s_copy = copy.deepcopy(mp3s)

    if align_method == ALIGN_ORIGIN:
        mp3s_copy = copy.deepcopy(mp3s)

    elif align_method == ALIGN_ASC:
        mp3s_copy.sort()

    elif align_method == ALIGN_DESC:
        mp3s_copy.sort(reverse=True)

    elif align_method == ALIGN_SUFFLE:
        random.shuffle(mp3s_copy)
    
    printMp3s(mp3s_copy)

def deleteMp3(index_num):
    mp3s.pop(index_num-1)
    printMp3s(mp3s)

while True:

    selected_num = int(input('1.음원등록  2.음원리스트  3.음원삭제  99.종료 '))

    if selected_num == MP3_REGIST:
        mp3s.append(input('음원 입력: '))
        printMp3s(mp3s)

    elif selected_num == MP3_LIST:
        align = int(input('정렬 선택(1.ORIGIN  2.ASC  3.DESC  4.SUFFLE): '))
        alignMp3s(align)
        
    elif selected_num == MP3_DELETE:
        printMp3s(mp3s)
        deleteMp3(int(input('삭제 번호 선택: ')))

    elif selected_num == SYSTEM_OUT:
        print('good bye~')
        break

'''
교재
  - 실전 예제
    - 단위 환산 프로그램(368p)
    - 마트 상품 가격표 출력 프로그램(369p)
  - 연습문제(372p)
'''