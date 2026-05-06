Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Sort()
>>> a=["zinc","Copper","Aluminium","Gold"]
>>> a.sort()
>>> a
['Aluminium', 'Copper', 'Gold', 'zinc']
>>> b=[5,8,6,1,0,2,3,5]
>>> b.sort()
>>> b
[0, 1, 2, 3, 5, 5, 6, 8]
>>> c=["#","!","@"]
>>> c.sort()
>>> c
['!', '#', '@']
>>> 
>>> 
>>> #Reverse
>>> a=["hello","hi","Bhaai"]
>>> a.reverse()
>>> a
['Bhaai', 'hi', 'hello']
>>> b=[7,8,50,11,1]
>>> b.reverse()
>>> b
[1, 11, 50, 8, 7]
>>> b.sort()
>>> b
[1, 7, 8, 11, 50]
>>> b.reverse()
>>> b
[50, 11, 8, 7, 1]
>>> 
>>> c=[4,5,1,1/2,8/7,55]
>>> c.sort()
>>> c
[0.5, 1, 1.1428571428571428, 4, 5, 55]
>>> 
>>> d=[55//5,88/6]
>>> c.sort()
>>> d.sort()
>>> d
[11, 14.666666666666666]
>>> e=[885//5,88//6]
>>> e.sort()
>>> e
[14, 177]

a=[5,8,2,0,1,44,77,6858]
a.sort(reverse=True)
a
[6858, 77, 44, 8, 5, 2, 1, 0]
