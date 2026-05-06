Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Symmetric difference
a={2,3,4,5,6,7}
b={1,5,6,7,8,9,10}
a.
SyntaxError: invalid syntax
a.symmetric_difference(b)
{1, 2, 3, 4, 8, 9, 10}
#Symmetric difference will delete the common elements

#Intersection_update() will update common elements into a

a={9,10,11,12,13,14}
b={11,12,13,14,15}
a.intersection_update(b)
a
{11, 12, 13, 14}
b.intersection_update(a)
b
{11, 12, 13, 14}

#Difference_Update() will update the elements with are not common in both sets

a={4,5,6,7,8,9,10}
b={7,8,9,10,11,12}
a.difference_update(b)
a
{4, 5, 6}
b.difference_update(a)
b
{7, 8, 9, 10, 11, 12}
#here set-a is already updated so there is no common elements

#Symmetric_difference_update()
a={3,4,5,6,7,8}
b={1,2,3,4,5,6}
a.symmetric_difference_update(b)
a
{1, 2, 7, 8}
b.symmetric_difference_update(a)
b
{3, 4, 5, 6, 7, 8}
#Symmetric_difference_update will remove common elements and update the set

a={1,2,3,4,5,6,8}
b={4,5,6,7,8,9,10}
a.copy()
{1, 2, 3, 4, 5, 6, 8}
a.clear()
a
set()
b=set()
b.add(10,20)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    b.add(10,20)
TypeError: set.add() takes exactly one argument (2 given)
#only one element can add into a set
b.add(10)
b
{10}

a={2,3,4,5,6,7,89,9}
a.pop()
2
a.pop(89)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a.pop(89)
TypeError: set.pop() takes no arguments (1 given)
>>> a.pop(1)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a.pop(1)
TypeError: set.pop() takes no arguments (1 given)
>>> a.remove(89)
>>> a
{3, 4, 5, 6, 7, 9}
>>> a.remove(2)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a.remove(2)
KeyError: 2
>>> 
>>> a.discard(5)
>>> a
{3, 4, 6, 7, 9}
>>> 
>>> #ISDISJOINT()=NO VALUE SHOULD BE SAME THEN IT WILL RETURN TRUE OR ELSE FALSE
>>> 
>>> a={5,6,7,8,9}
>>> a={9,10,11,12,13}
>>> a.isdisjoint(b)
False
>>> 
>>> a={5,6,7}
>>> b={8,9,10}
>>> a.isdisjoint(b)
True
>>> 
>>> len(a)
3
>>> a.count(7)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    a.count(7)
AttributeError: 'set' object has no attribute 'count'
>>> a.index(2)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a.index(2)
AttributeError: 'set' object has no attribute 'index'
