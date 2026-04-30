Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#SLicing

a="Codegnan"
a[0:3]
'Cod'
a[0:4]
'Code'
a[:4]
'Code'
a[4:8]
'gnan'
a[5:7]
'na'
a[4:]
'gnan'

a="Work hard until you succeed"

a[18:26]
'u succee'
a[19:27]
' succeed'
a[11:15]
'ntil'
a[10:15]
'until'
a[16:19]
'you'
a[0:4]
'Work'
a[5:9]
'hard'

b="I am learning Pythin Course"

b="I am learning Python Course"
b[13:19]
' Pytho'
>>> b[13:20]
' Python'
>>> b[21:27]
'Course'
>>> b[4:11]
' learni'
>>> b[4:12]
' learnin'
>>> b[4:13]
' learning'
>>> b[1:3]
' a'
>>> b[1:4]
' am'
>>> b[0]
'I'
>>> #negative SLicing
>>> 
>>> a = "Simple is better than complex"
>>> a[-8:-1]
' comple'
>>> a[-7:]
'complex'
>>> a[-19:-14]
'bette'
>>> a[-19:-13]
'better'
>>> a[-29:-25]
'Simp'
>>> a[-29:-23]
'Simple'
>>> 
>>> b="Beautiful is better than ugly"
>>> 
>>> b[-29:-200]
''
>>> b[-29:-20]
'Beautiful'
>>> b[-4:]
'ugly'
>>> b[-19:-17]
'is'
>>> b[-16:17]
'bett'
>>> b[-16:15]
'be'
