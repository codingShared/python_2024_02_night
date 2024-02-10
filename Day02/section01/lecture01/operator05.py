#(3) 패킹 할당
lst = [1,2,3,4,5] #리스트 - 컬렉션의 자료형중의 하나
v1, *v2 = lst
print(v1, v2)

*v1, v2 = lst
print(v1, v2)