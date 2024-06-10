MENU_REGIST = 1;
MENU_MODIFY = 2;
MENU_DELETE = 3;
SYSTEM_OUT  = 99;

print("=== 식당 메뉴 관리 프로그램 ===")

menus = []

while True:
    selected_num = int(input('1.메뉴등록  2.메뉴수정  3.메뉴삭제  99.종료 '))

    if selected_num == MENU_REGIST:
        menu_name = input('메뉴 이름: ')
        menu_price = input('메뉴 가격: ')
        menus.append([menu_name, menu_price])
        print(menus)

    elif selected_num == MENU_MODIFY:
        modify_menu_name = input('수정 메뉴 이름: ')

        modify_idx = 0
        for idx, menu in enumerate(menus):
            if menu[0] == modify_menu_name:
                modify_idx = idx

        menu_name = input('새 메뉴 이름: ')
        menu_price = input('새 메뉴 가격: ')
        menus[modify_idx] = [menu_name, menu_price]
        print(menus)

    elif selected_num == MENU_DELETE:
        delete_menu_name = input('삭제 메뉴 이름: ')

        delete_idx = 0
        for idx, menu in enumerate(menus):
            if menu[0] == delete_menu_name:
                delete_idx = idx

        menus.pop(delete_idx)
        print(menus)

    elif selected_num == SYSTEM_OUT:
        break