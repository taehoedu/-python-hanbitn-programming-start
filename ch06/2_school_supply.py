print("=== 신학기 학용품 가격 계산 프로그램 ===")

pencil_cnt          = int(input("연필 개수: "))
pencil_unit_price   = int(input("연필 단가: "))

eraser_cnt          = int(input("지우개 개수: "))
eraser_unit_price   = int(input("지우개 단가: "))

color_pencil_cnt         = int(input("색연필 개수: "))
color_pencil_unit_price  = int(input("색연필 단가: "))

notebook_cnt        = int(input("공책 개수: "))
notebook_unit_price = int(input("공책 단가: "))

bag_cnt             = int(input("가방 개수: "))
bag_unit_price      = int(input("가방 단가: "))

print(("-" * 10) + " 필요 예산 " + ("-" * 10))

pencil_total_price = pencil_cnt * pencil_unit_price
eraser_total_price = eraser_cnt * eraser_unit_price
color_pencil_total_price = color_pencil_cnt * color_pencil_unit_price
notebook_total_price = notebook_cnt * notebook_unit_price
bag_total_price = bag_cnt * bag_unit_price

print(f"연필: {pencil_total_price}원")
print(f"지우개: {eraser_total_price}원")
print(f"색연필: {color_pencil_total_price}원")
print(f"공책: {notebook_total_price}원")
print(f"가방: {bag_total_price}원")

total_price = pencil_total_price
total_price += eraser_total_price
total_price += color_pencil_total_price
total_price += notebook_total_price
total_price += bag_total_price

print(f"총 합계: {total_price}원")

print("-" * 30)


'''
교재
  - 실전 예제
    - 수온 계산(162p)
    - 자동차 주행 거리 계산기(163p)
    - 업무 컴퓨터 수량 파악(164p)
  - 연습문제(166p)
'''