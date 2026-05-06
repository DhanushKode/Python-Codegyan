Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Union
>>> a={1,2,3,4,5,6,7}
>>> b={8,9,10,11,12}
>>> a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
>>> a
{1, 2, 3, 4, 5, 6, 7}
>>> 
>>> b.union(a)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
>>> 
>>> 
>>> #Intersection
>>> a={4,5,6,7,8}
>>> b={6,7,8,9,10}
>>> a.intersection(b)
{8, 6, 7}
>>> #Intersection will print the same elements present in both
>>> 
>>> #Union in merging togerther
>>> 
>>> 
>>> #Update
>>> #update will add the new elements is the set and wont add duplicate/repeated elements
>>> 
>>> a.update(b)
>>> a
{4, 5, 6, 7, 8, 9, 10}
>>> b
{6, 7, 8, 9, 10}
>>> b.update(a)
>>> 
>>> b
{4, 5, 6, 7, 8, 9, 10}
>>> 
>>> #Difference() will print the elements that are not duplicate or present in other elements
>>> a={1,2,3,4,5,6,7,8,90}
>>> b={6,7,8,90,10,11}
>>> a.difference(b)
{1, 2, 3, 4, 5}
>>> b.difference(a)
{10, 11}
>>> 
