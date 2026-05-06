Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #list[]
>>> 
>>> a=[4,6.5,"Python",5+9j,True,False]
>>> print(a)
[4, 6.5, 'Python', (5+9j), True, False]
>>> type(a)
<class 'list'>
>>> b=8.9
>>> type(b)
<class 'float'>
>>> c=[5.5]
>>> type(c)
<class 'list'>
>>> 
>>> d=["Sam","Richard","Mad","Mikellsen"]
>>> a.append("Ghost")
>>> a
[4, 6.5, 'Python', (5+9j), True, False, 'Ghost']
>>> d.append("Riley")
>>> d
['Sam', 'Richard', 'Mad', 'Mikellsen', 'Riley']
>>> a.append("css","Java")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a.append("css","Java")
TypeError: list.append() takes exactly one argument (2 given)
>>> #cannot pass more than one variable/string in append.
>>> #need to pass it as a list
>>> 
>>> d.append(["John","Price"])
>>> d
['Sam', 'Richard', 'Mad', 'Mikellsen', 'Riley', ['John', 'Price']]
>>> 
>>> #extend()
>>> a=["ds","ai","Sql"]
>>> a.extend(["Flask","Web","Python"])
>>> a
['ds', 'ai', 'Sql', 'Flask', 'Web', 'Python']
>>> #extend method prinnts as single output, rather than as a list like append
>>> 
>>> #Insert()
>>> a.insert(1,"Dl")
>>> a
['ds', 'Dl', 'ai', 'Sql', 'Flask', 'Web', 'Python']
>>> a.insert([2,"API"],[3,"AP"])
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a.insert([2,"API"],[3,"AP"])
TypeError: 'list' object cannot be interpreted as an integer
a.insert([[2,"API"],[3,"AP"]])
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a.insert([[2,"API"],[3,"AP"]])
TypeError: insert expected 2 arguments, got 1
a
['ds', 'Dl', 'ai', 'Sql', 'Flask', 'Web', 'Python']
a.index("Sql")
3
a.copy()
['ds', 'Dl', 'ai', 'Sql', 'Flask', 'Web', 'Python']
a.clear()
a
[]
b=[]
b.append("data")
b
['data']

