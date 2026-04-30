Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Striding
>>> a="Cloud Computing"
>>> a[::5]
'C u'
>>> a[:6]
'Cloud '
>>> a[8:]
'mputing'
>>> a[3:11]
'ud Compu'
>>> a[::2]
'CodCmuig'
>>> a[::7]
'Cog'
>>> a[::1]
'Cloud Computing'
>>> a[5:12]
' Comput'
>>> 
>>> b="Machine Learning"
>>> a[1:8:2]
'lu o'
>>> b[1:8:2]
'ahn '
>>> b[2:11:3]
'cnL'
>>> b[5:12:2]
'n er'
>>> b[3:15:4]
'h r'
>>> b[1:10:5]
'ae'
>>> 
>>> a="Python course"
>>> 
>>> a[-1:-9:-3]
'eu '
>>> a[-2:-12:-4]
'sch'
>>> a[-4:-13:-6]
'uh'
>>> a[-3:-9:-2]
'ro '
>>> a[::-1]
'esruoc nohtyP'
