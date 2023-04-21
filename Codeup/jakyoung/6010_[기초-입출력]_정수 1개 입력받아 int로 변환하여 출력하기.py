Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n = input()
1
>>> n = int(n)
>>> print(n)
1
>>> n = input()
a
>>> n = int(n)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    n = int(n)
ValueError: invalid literal for int() with base 10: 'a'
>>> n = input()
123
>>> n = int(n)
>>> print(n)
123
