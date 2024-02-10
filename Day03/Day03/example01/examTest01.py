# print(values, sep, end, file, flush)

print('재미있는', '파이썬')
print('Python', 'Java', 'C', sep=",")
print()
print('영화 타이타닉')
print('평점', end=':')
print('5점')


# 파일 입출력
fos = open('sample2.py', mode='wt')
print('print("hello world2!")', file = fos)
fos.close()