print("=== 명함 프로그램 ===")

print("정보를 입력하세요.")
name        = input("이름: ")
major       = input("전공: ")
university  = input("학교명: ")
phone       = input("전화번호: ")
email       = input("이메일: ")
instagram   = input("인스타그램: ")


# 명함 디자인 선택
print("다음 중 원하는 명함 디자인을 선택하세요.")
print("1. 기본 디자인")
print("2. 세련된 디자인")
print("3. 럭셔리한 디자인")
choice = input("디자인 선택: ")

print("-" * 40)

if choice == "1":
    print(f"{name} | {major} | {university}")
    print(f"P: {phone}")
    print(f"E: {email}")
    print(f"I: {instagram}")

elif choice == "2":
    print(f"{name} @ {university}")
    print(f"전공: {major}")
    print(f"📞 {phone}  📧 {email}")
    print(f"📷 {instagram}")

else:
    print(f"✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨")
    print(f"💎💎💎 {name.center(23)} 💎💎💎")
    print(f"🎓 {university},  {major}")
    print(f"📱 {phone}   💌 {email}")
    print(f"📸 {instagram}")
    print(f"✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨")

print("-" * 40)
