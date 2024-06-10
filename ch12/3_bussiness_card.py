EMPLOYEE_REGIST = 1
BUSSINESS_CARD_PRINT = 2
SYSTEM_OUT  = 99

print("=== 명함 프로그램 ===")

employees = []

while True:

    selected_num = int(input('1.직원등록  2.직원명함출력  99.종료 '))

    if selected_num == EMPLOYEE_REGIST:
        print("정보를 입력하세요.")
        no          = input("번호: ")
        name        = input("이름: ")
        part        = input("부서: ")
        position    = input("직급: ")
        phone       = input("연락처: ")
        email       = input("이메일: ")

        employees.append([no, name, part, position, phone, email])
        for employee in employees:
            print(employee)

    elif selected_num == BUSSINESS_CARD_PRINT:
        print("직원 번호를 입력하세요.")
        no = input("번호: ")

        for index, employee in enumerate(employees):
            if employee[0] == no:
                print('-' * 40)
                print(f"{employee[0]}")
                print(f"{employee[1]} | {employee[2]} | {employee[3]}")
                print(f"P: {employee[4]}")
                print(f"E: {employee[5]}")
                print('-' * 40)

    elif selected_num == SYSTEM_OUT:
        print('good bye~')
        break

'''
교재
  - 실전 예제
    - 출석부 관리 시스템(282p)
    - 혈액 보관 시스템(284p)
  - 연습문제(286p)
'''