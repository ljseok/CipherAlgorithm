from itertools import combinations

vowels = ('a','e','i','o','u') # 5개의 모음
l, c = map(int, input().split(' '))

array = input().split(' ' ) # 가능한 한 암호는 사전방식으로 출력
array.sort() # 입력후에 정렬을 한다.

for password in combinations(array, l): # 길이가 1인 암호를 확인
    count = 0
    for i in password: # 패스워드의 문자를 확인하며
        if i in vowels: # 모음을 센다
            count += 1
        if count >= 1 and count <= l-2: # 최소 한개의 모음과 2개의 자음이 있는 경우에만 출력
            print(''.join(password))

