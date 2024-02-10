'''
연습문제3) 두자리정수(10~99)를 입력받아
십의 자리와 일의 자리로 분리하여 출력하는 프로그램
결과
십의자리 : 3
일의자리 : 5
'''


number = int(input('두자리정수(10~99) 입력 >>> '))
tens = number // 10
units = number % 10
print('십의자리 : ',tens);
print('일의자리 : ',units)