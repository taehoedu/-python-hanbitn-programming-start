print("=== 학생식당 키오스크 프로그램 ===")

menu_name = ""; menu_price = 0; total_price = 0

while True:
    print("메뉴 카테고리를 선택하세요.")
    category = input("1.한식\t2.양식\t3.분식\t99.결제 ")

    if category == "99":
        break

    elif category == "1":
        print("-- 한식 --")
        print("1.된장찌개(4,000원)")
        print("2.순두부찌개(4,500원)")
        print("3.제육덮밥(5,000원)")
        menu = input("메뉴 선택: ")

        if menu == "1":
            menu_name = "된장찌개"; menu_price = 4000
        elif menu == "2":
            menu_name = "순두부찌개"; menu_price = 4500
        elif menu == "3":
            menu_name = "제육덮밥"; menu_price = 5000

    elif category == "2":
        print("-- 양식 --")
        print("1.돈까스(5,000원)")
        print("2.치즈돈까스(6,000원)")
        print("3.까르보나라(5,000원)")
        menu = input("메뉴 선택: ")

        if menu == "1":
            menu_name = "돈까스"; menu_price = 5000
        elif menu == "2":
            menu_name = "치즈돈까스"; menu_price = 6000
        elif menu == "3":
            menu_name = "까르보나라"; menu_price = 5000

    elif category == "3":
        print("-- 분식 --")
        print("1.라면(3,000원)")
        print("2.우동(3,500원)")
        print("3.쫄면(4,000원)")
        print("4.라볶이(3,500원)")
        menu = input("메뉴 선택: ")
    
        if menu == "1":
            menu_name = "라면"; menu_price = 3000
        elif menu == "2":
            menu_name = "우동"; menu_price = 3500
        elif menu == "3":
            menu_name = "쫄면"; menu_price = 4000
        elif menu == "4":
            menu_name = "라볶이"; menu_price = 3500

    quantity = int(input("수량을 입력하세요: "))

    print("-------------------------")
    print("주문 내역 확인")
    print(f"메뉴: {menu_name}")
    print(f"수량: {quantity}", )
    print("-------------------------")

    total_price += menu_price * quantity


print(f"총 결제 금액: {total_price}")

if (total_price > 0):
    payment = input("결제 수단 선택(1.현금  2.카드): ")

    if payment == "1":
        input("지폐를 투입해 주세요.(금액 입력 후 Enter 누름) ")
        
    elif payment == "2":
        input("카드를 삽입해주세요.(Enter 누름) ")

    print(f"{format(total_price, ',')}원 결제가 완료되었습니다. 이용해 주셔서 감사합니다!")
