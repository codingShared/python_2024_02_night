oneLine = "this is one line string"
print(oneLine)
print("문자열 길이 : ", len(oneLine)) # 문자열 길이 추출
print(oneLine[0 : 4]) # 0 ~ 3까지 문자 추출
print(oneLine[:4]) # 0 ~ 3까지 (시작값 생략시 0부터 시작)
print(oneLine[:]) #전체 원소 출력
print(oneLine[::2]) #2의 배수 index