import random

print("=== 홀/짝 프로그램 ===")

user_score = 0
computer_score = 0

user_value_history = []

for i in range(10):

    print(f"-- {i+1} 번째 게임 --")

    compter_selected_num    = random.randrange(1, 101)
    user_selected_num       = input('홀짝 선택(1.홀,  2.짝): ')

    print(f'compter_selected_num: {compter_selected_num}')
    print(f'user_selected_num: {user_selected_num}')

    if user_selected_num == '1':
        if compter_selected_num % 2 == 0:
            print('computer win!!')
            computer_score += 10
            user_value_history.append(['odd', 'loser'])

        else:
            print('user win!!')
            user_score += 10
            user_value_history.append(['odd', 'winner'])

    elif user_selected_num == '2':
        if compter_selected_num % 2 == 0:
            print('user win!!')
            user_score += 10
            user_value_history.append(['even', 'winner'])

        else:
            print('computer win!!')
            computer_score += 10
            user_value_history.append(['even', 'loser'])

print('-' * 40)

print(f"user socore: {user_score}")
print(f"computer socore: {computer_score}")

if user_score > computer_score:
    print("user final winner!!")

elif user_score < computer_score:
    print("computer final winner!!")

else:
    print("end in a tie!!")

win_percentage = 10 * (user_score/10)
print(f'user winning rate: {win_percentage:.0f}%')

print('-' * 40)

# print(f"-- user value --")
# for value in user_value_history:
#     print(value)

print(f"-- user select and result --")
for index, value,  in enumerate(user_value_history):
    print(f"{index + 1}번째 게임: {value}")

print('-' * 40)