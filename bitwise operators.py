Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #bitwise
>>> a=4
>>> b=6
>>> a7b
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a7b
NameError: name 'a7b' is not defined
>>> a&h
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a&h
NameError: name 'h' is not defined
>>> a&b
4
>>> #& operator
>>> 
>>> # or operator
>>> a|b
6
>>> # ~ operator
>>> a~b
SyntaxError: invalid syntax
>>> a~b
SyntaxError: invalid syntax
>>> a^b
2
>>> a~
SyntaxError: invalid syntax
>>> ~a
-5
