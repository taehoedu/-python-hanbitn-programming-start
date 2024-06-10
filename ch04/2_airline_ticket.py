print("=== 비행기표 프로그램 ===")

print("정보를 입력하세요.")
dpt_loc  = input("출발지: ")
dpt_time = input("출발지시간: ")
dst_loc  = input("도착지: ")
dst_time = input("도착지시간: ")
adt_cnt  = input("성인수: ")
ift_cnt  = input("유아수: ")

print("-" * 40)

print(f"출발지(시간): {dpt_loc}({dpt_time})")
print(f"도착지(시간): {dst_loc}({dst_time})")
print(f"성인수: {adt_cnt}명")
print(f"유아수: {ift_cnt}명")

print("-" * 40)


'''
교재
  - 실전 예제
    - 비밀번호 발송 메일 프로그램(114p)
    - 날씨 예보 프로그램(115p)
  - 연습문제(117p)
'''