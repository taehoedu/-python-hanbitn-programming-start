print("=== 학점 계산 프로그램 ===")

pit_python = float(input("PYTHON 점수: "))
crd_python = float(input("PYTHON 학점: "))

pit_c = float(input("C/C++ 점수: "))
crd_c = float(input("C/C++ 학점: "))

pit_java = float(input("JAVA 점수: "))
crd_java = float(input("JAVA 학점: "))

total_points = pit_python * crd_python
total_points += pit_c * crd_c
total_points += pit_java * crd_java

total_credits = crd_python + crd_c + crd_java

gpa = total_points / total_credits
print(f"이수 학점은 {total_credits}학점입니다.")
print(f"총 평점(GPA)은 {gpa:.2f}입니다.")

'''
gpa = 3.141592
print(f"총 평점(GPA)은 {round(gpa)}입니다.")
print(f"총 평점(GPA)은 {round(gpa, 0)}입니다.")
print(f"총 평점(GPA)은 {round(gpa, 1)}입니다.")
print(f"총 평점(GPA)은 {round(gpa, 2)}입니다.")
print(f"총 평점(GPA)은 {round(gpa, 3)}입니다.")
'''