CALCULATE_DO        = 1
CALCULATE_LIST      = 2
SYSTEM_OUT          = 99

print("=== 계산기 프로그램 ===")

calculate_hostories = []
    
while True:
    selected_num = int(input('1.계산하기  2.계산기록보기  99.종료 '))

    if selected_num == CALCULATE_DO:
        first_num = float(input('첫 번째 피연산자 입력: '))
        operator = input('연산자(+, -, *, /) 입력: ')
        second_num = float(input('두 번째 피연산자 입력: '))

        result_str = ''
        if operator == '+':
            result_str = f'{first_num} + {second_num} = {first_num + second_num}'

        elif operator == '-':
            result_str = f'{first_num} - {second_num} = {first_num - second_num}'

        elif operator == '*':
            result_str = f'{first_num} * {second_num} = {first_num * second_num}'

        elif operator == '/':
            result_str = f'{first_num} / {second_num} = {(first_num / second_num):.2f}'

        print(result_str)
        calculate_hostories.append(result_str)

    elif selected_num == CALCULATE_LIST:
        for index, value in enumerate(calculate_hostories):
            print(f'{index}: {value}')

    elif selected_num == SYSTEM_OUT:
        break