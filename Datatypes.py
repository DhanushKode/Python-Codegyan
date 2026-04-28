Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Datatypes
>>> a = 6
>>> type(a)
<class 'int'>
>>> b =7.8
>>> type(b)
<class 'float'>
>>> c = '''Code'''
>>> 
>>> type(c)
<class 'str'>
>>> d = "python"
>>> type(d)
<class 'str'>
>>> z=6j
>>> type(z)
<class 'complex'>
>>> i = 9+6j
>>> type(i)
<class 'complex'>
>>> e = 6+7i
SyntaxError: invalid decimal literal
>>> f = True
>>> type(e)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    type(e)
NameError: name 'e' is not defined
>>> type(f)
<class 'bool'>
>>> h = False
>>> type(h)
<class 'bool'>
>>> k = false
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    k = false
NameError: name 'false' is not defined. Did you mean: 'False'?
