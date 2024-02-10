# (4) format() 함수 인수 : format(value, "format")
print("원주율=", format(3.14159, "8.3f")) #8자리 / 소수점 셋째자리 까지  bbb3.142 / b:공백
print("금액=", format(10000, "10d")) # 10자리 / bbbbb10000
print("금액=", format(1111125000, ",d")) #125,000

# (5) 양식문자 인수 : print("%양식문자" %(값))
name = "홍길동"
age = 35
price = 123.456
print("이름 : %s, 나이 : %d, price : %.2f" %(name, age, price))

# (6) 외부 상수 인수
print("이름 : {}, 나이 : {}, price : {}".format(name, age, price))
print("이름 : {1}, 나이 : {0}, price : {2}".format(age, name, price))

# (7) f-string
who = 'you'
how = 'happy'
result = f'{who} make me {how}'
print(result)

uid = input("id input : ")
query = f"select*from member where uid={uid}"
print(query)