Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> c = input(1)
1
>>> print(c)

>>> c = input('1')
1
>>> print c
SyntaxError: incomplete input
>>> print(c)

>>> c = input()
print(c)
>>> c = input()
a
>>> print(c)
a
>>> c = input()
abc
>>> print(c)
abc
