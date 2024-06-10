import lottoMachine as lm

nums = []

print('1부터 45까지의 정수 6개를 입력하세요. ')
nums.append(int(input('Number 1 : ')))
nums.append(int(input('Number 2 : ')))
nums.append(int(input('Number 3 : ')))
nums.append(int(input('Number 4 : ')))
nums.append(int(input('Number 5 : ')))
nums.append(int(input('Number 6 : ')))
            
lm.setUNumbers(nums)    # 사용자 번호 설정
lm.setRNumbers()        # 렌덤 번호 설정

print('이번주 로또 번호', lm.getRNumbers())
print('내가 선택한 번호', lm.getUNumbers())
print('일치하는 숫자 :', lm.compareNumbers())
