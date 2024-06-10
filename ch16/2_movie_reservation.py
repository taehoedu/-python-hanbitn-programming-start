from datetime import datetime

MOVIE_RESERVATION           = 1
MOVIE_RESERVATION_MODIFY    = 2
MOVIE_RESERVATION_CANCEL    = 3
MOVIE_RESERVATION_LIST      = 4
SYSTEM_OUT                  = 99

print("=== 영화 예매 프로그램 ===")

movies = ['스타워즈', '아이언맨', '헐크']
times = ['10:00', '13:00', '16:00', '19:00']
reservations = {}

def inputReservation():
    name = input('예매자 이름: ')
    movie = int(input('영화 선택(1.스타워즈,  2.아이언맨,  3.헐크): '))
    time = int(input('영화 시간 선택(1.10:00,  2.13:00,  3.16:00,  4.19:00): '))
    seat = input('좌석 번호 입력(예, F05): ')

    return [name, movies[movie-1], times[time-1], seat]

def printReservation():
    for key, value in reservations.items():
            print(f'no: {key}, info: {value}')

while True:

    selected_num = int(input('1.영화예매  2.영화예매수정  3.영화예매취소  4.예매리스트  99.종료 '))   

    if selected_num == MOVIE_RESERVATION:
        # reservation_name = input('예매자 이름: ')
        # reservation_movie = int(input('영화 선택(1.스타워즈,  2.아이언맨,  3.헐크): '))
        # reservation_time = int(input('영화 시간 선택(1.10:00,  2.13:00,  3.16:00,  4.19:00): '))
        # reservation_seat = input('좌석 번호 입력(예, F05): ')
        
        now = datetime.now()
        reservation_no = now.strftime('%Y%m%d%H%M%S')

        # reservations[reservation_no] = [reservation_name, 
        #                                 movies[reservation_movie-1], 
        #                                 times[reservation_time-1],
        #                                 reservation_seat]

        reservations[reservation_no] = inputReservation()
        
        # for key, value in reservations.items():
        #     print(f'no: {key}, info: {value}')

        printReservation()
    
    elif selected_num == MOVIE_RESERVATION_MODIFY:
        reservation_no = input('예매 번호: ')

        # reservation_name = input('예매자 이름: ')
        # reservation_movie = int(input('영화 선택(1.스타워즈,  2.아이언맨,  3.헐크): '))
        # reservation_time = int(input('영화 시간 선택(1.10:00,  2.13:00,  3.16:00,  4.19:00): '))
        # reservation_seat = input('좌석 번호 입력(예, F05): ')

        # reservations[reservation_no] = [reservation_name, 
        #                                 movies[reservation_movie-1], 
        #                                 times[reservation_time-1],
        #                                 reservation_seat]
        
        reservations[reservation_no] = inputReservation()

        # for key, value in reservations.items():
        #     print(f'no: {key}, info: {value}')

        printReservation()

    elif selected_num == MOVIE_RESERVATION_CANCEL:
        reservation_no = input('예매 번호: ')
        del reservations[reservation_no]

        # for key, value in reservations.items():
        #     print(f'no: {key}, info: {value}')

        printReservation()
    
    elif selected_num == MOVIE_RESERVATION_LIST:
        # for key, value in reservations.items():
        #     print(f'no: {key}, info: {value}')
         
        printReservation()

    elif selected_num == SYSTEM_OUT:
        print('good bye~')
        break