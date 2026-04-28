Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
int(8)
8
int(6.0)
6
int(3.2)
3
>>> int("sam")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int("sam")
ValueError: invalid literal for int() with base 10: 'sam'
>>> int(6+5j)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int(6+5j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> 
>>> float(6)
6.0
>>> float(6.3)
6.3
>>> float("sam")
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    float("sam")
ValueError: could not convert string to float: 'sam'
>>> float(6+6j)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    float(6+6j)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> str(6)
'6'
>>> str(6.5)
'6.5'
>>> str(sam)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    str(sam)
NameError: name 'sam' is not defined. Did you mean: 'sum'?
>>> str('str')
'str'
>>> str(6+6j)
'(6+6j)'
