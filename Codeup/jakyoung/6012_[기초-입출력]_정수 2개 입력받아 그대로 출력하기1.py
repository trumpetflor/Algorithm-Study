Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = input()
1
>>> b = input()
2
>>> a = int(a)
>>> b = int(b)
>>> print(a)
1
>>> print(b)
2
>>> print(a, b)
1 2
>>> print(a\nb)
SyntaxError: unexpected character after line continuation character
>>> print(a + "\n" + b)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(a + "\n" + b)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
