print("=== 명함 프로그램 ===")

print("정보를 입력하세요.")
name        = input("이름: ")
major       = input("전공: ")
university  = input("학교명: ")
phone       = input("전화번호: ")
email       = input("이메일: ")
instagram   = input("인스타그램: ")

print("-" * 40)

# print(name + " | " + major + " | " + university)
# print("P: ", phone)
# print("E: ", email)
# print("I: ", instagram)

print(f"{name} | {major} | {university}")
print(f"P: {phone}")
print(f"E: {email}")
print(f"I: {instagram}")

print("-" * 40)
