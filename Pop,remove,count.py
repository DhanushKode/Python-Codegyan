Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Pop
>>> #Pop()
>>> a=[3,4,5,8,7,11,5]
>>> a.pop()
5
>>> a.pop(9)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a.pop(9)
IndexError: pop index out of range
>>> a.pop(4)
7
>>> 
>>> a
[3, 4, 5, 8, 11]
>>> a.remove()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a.remove()
TypeError: list.remove() takes exactly one argument (0 given)
>>> a.remove(11)
>>> a
[3, 4, 5, 8]
>>> 
...  
>>> a=[5,8,7,9,3,1,220]
>>> len(a)
7
>>> a="SAm"
>>> len(a)
3
>>> b=["hello"]
>>> len(b)
1
>>> a.count(20)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a.count(20)
TypeError: count() argument 1 must be str, not int
>>> #count can only be used as string
>>> b=["Python","Java","c"]
>>> b.count("Java")
1
>>> b.count("c")
1
