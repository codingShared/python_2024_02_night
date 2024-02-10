# 외부상수 format을 통한 출력방식
zipcode = '06236'
print('우편번호 : {}'.format(zipcode))

address = '''서울 특별시 강남구
테헤란로 146 번지'''
print('주소 : {addr}'.format(addr=address))

tel1, tel2, tel3 = '02', '538', '0021'
print('연락처 : {}-{}-{}'.format(tel1, tel2, tel3))