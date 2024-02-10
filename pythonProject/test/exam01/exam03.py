var1 = "HelloPython"
print(var1) #문자열 객체출력
print(id(var1)) #주소를 반환해주는 내장함수

var1 = 100
print(var1)
print(id(var1))

var2 = 150.25
print(var2)
print(id(var2))

var3 = True
print(var3)
print(id(var3))

# 실수 -> 정수
a = int(10.5)
b = int(20.42)
add = a+b
print(add)
print('add=', add)

print(int(True))
print(int(False))

# 문자형 -> 정수
st = '10'
print(int(st) ** 2)
