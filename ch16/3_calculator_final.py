import operator

CALCULATE_DO        = 1
CALCULATE_LIST      = 2
SYSTEM_OUT          = 99

print("=== 계산기 프로그램 ===")

index_no = 0
calculate_hostories = []
operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

def doCalculate(num1, operator, num2):
    result = round(operators[operator](num1, num2), 2)
    return f'{num1} {operator} {num2} = {result}'
    
while True:
    selected_num = int(input('1.계산하기  2.계산기록보기  99.종료 '))

    if selected_num == CALCULATE_DO:
        first_num = float(input('첫 번째 피연산자 입력: '))
        operator = input('연산자(+, -, *, /) 입력: ')
        second_num = float(input('두 번째 피연산자 입력: '))

        result_str = doCalculate(first_num, operator, second_num)
        print(result_str)
        calculate_hostories.append(result_str)

    elif selected_num == CALCULATE_LIST:
        for index, value in enumerate(calculate_hostories):
            print(f'{index}: {value}')

    elif selected_num == SYSTEM_OUT:
        break

'''
교재
  - 실전 예제
    - 다국어 인사말 프로그램(338p)
    - 계산기 프로그램(339p)
  - 연습문제(342p)
'''