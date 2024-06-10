print("=== 일기 프로그램 ===")

diaries = []

while True:

    menu = input("메뉴: 1.일기작성  2.일기목록, 99.종료 ")

    if menu == "1":
        date = input('날짜 입력(예: 20240220): ')
        day = input('요일 입력(예: 화): ')
        diary = input('일기 입력: ')

        diaries.append(f"[{date}][{day}요일] {diary}")
        diaries.sort(reverse=True)

    elif menu == "2":
        print(diaries)
    
    else:
        break