Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Sets
>>> #Sets {}
>>> #unorderd collection and dont allow duplicate values
>>> #Semimutable
>>> a={2,2.7,"Python",7+9j,True,False}
>>> print(a)
{False, True, 'Python', 2.7, 2, (7+9j)}
>>> 
>>> type(a)
<class 'set'>
>>> #add()
>>> a={2,3,4,5,6}
>>> a.add(10)
>>> a
{2, 3, 4, 5, 6, 10}
>>> #we use add() method to add elements in sets.
>>> 
>>> a.add(1)
>>> a
{1, 2, 3, 4, 5, 6, 10}
>>> a.add(-1)
>>> a
{1, 2, 3, 4, 5, 6, 10, -1}
>>> a.add(-8)
>>> a
{1, 2, 3, 4, 5, 6, 10, -8, -1}
>>> a.add(0)
>>> a
{0, 1, 2, 3, 4, 5, 6, 10, -8, -1}
>>> 
>>> a={1,2,3,4,5,6,7}
>>> b={5,6,7}
>>> b.issubset(a)
True
>>> a.issubset(b)
False
>>> a={6,7,8,9,10,11,12}
>>> b={10,11,12}
>>> a.issuperset(b)
True
>>> b.issuperset(a)
False
>>> #Superset() means the values which are present in other and have more than subset
>>> #Subset() means some of the values present from superset.
