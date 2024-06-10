EMPLOYEE_REGIST = 1
BUSSINESS_CARD_PRINT = 2
EMPLOYEE_DELETE = 3
SYSTEM_OUT  = 99

print("=== 명함 프로그램 ===")

employees = {}

def printEmployees():
    for key, value in employees.items():
        print(f'no: {key}, info: {value}')

def printBussinessCard(eNo):

    employee = employees[eNo]

    print('-' * 40)
    print(f"{eNo}")
    print(f"{employee[0]} | {employee[1]} | {employee[2]}")
    print(f"P: {employee[3]}")
    print(f"E: {employee[4]}")
    print('-' * 40)

while True:

    selected_num = int(input('1.직원등록  2.직원명함출력  3.직원삭제  99.종료 '))

    if selected_num == EMPLOYEE_REGIST:
        print("정보를 입력하세요.")
        no          = input("번호: ")
        name        = input("이름: ")
        part        = input("부서: ")
        position    = input("직급: ")
        phone       = input("연락처: ")
        email       = input("이메일: ")

        employees[no] = (name, part, position, phone, email)
        # for key, value in employees.items():
        #    print(f'no: {key}, info: {value}')

        printEmployees()

    elif selected_num == BUSSINESS_CARD_PRINT:
        print("직원 번호를 입력하세요.")
        no = input("번호: ")

        # employee = employees[no]
        # print('-' * 40)
        # print(f"{no}")
        # print(f"{employee[0]} | {employee[1]} | {employee[2]}")
        # print(f"P: {employee[3]}")
        # print(f"E: {employee[4]}")
        # print('-' * 40)

        printBussinessCard(no)

    elif selected_num == EMPLOYEE_DELETE:
        print("직원 번호를 입력하세요.")
        no = input("번호: ")
        del employees[no]

        # for key, value in employees.items():
        #     print(f'no: {key}, info: {value}')

        printEmployees()

    elif selected_num == SYSTEM_OUT:
        print('good bye~')
        break