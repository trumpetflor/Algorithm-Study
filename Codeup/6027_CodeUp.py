﻿#6027번
'''
@문제설명
10진수를 입력받아 16진수(hexadecimal)로 출력해보자.

@입력
10진수 1개가 입력된다.

@출력
16진수(소문자) 형태로 출력한다.

'''
n = int(input()) #입력받은 값을 int로 형변환
print('%x'% n) # n을 16진수로 출력
