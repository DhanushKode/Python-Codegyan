Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Indexing
a="VIJAYAWADA"

a[5]
'A'
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'VIJAYA'
a[9]
'A'
a[11]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a[11]
IndexError: string index out of range
a = " class is going on"

a[8]+a[9]
's '

a = "I Love Python"
>>> 
>>> a[2]+a[3]+a[4]+a[5]
'Love'
>>> a[7]+a[8]+a[9]+a[10]+a[11]+a[12]
'Python'
>>> 
>>> a = " Vijayawada is a Royal City"
>>> 
>>> a[16]
' '
>>> a[17]
'R'
>>> a[17]+a[18]+a[19]+a[20]+a[21]
'Royal'
>>> a[23]+a[24]+a[25]+a[26]
'City'
>>> a[12]
'i'
>>> a[12]+a[13]
'is'
>>> a[12]+a[13]+a[17]+a[18]+a[19]+a[20]+a[21]+a[23]+a[24]+a[25]+a[26]
'isRoyalCity'
>>> 
>>> #Negative Indexing
>>> a[-4]+a[-3]+a[-2]+a[-1]
'City'
>>> 
>>> a[-10]+a[-9]+a[-8]+a[-7]+a[6]
'Royaa'
>>> a[-10]+a[-9]+a[-8]+a[-7]+a[-6]
'Royal'
>>> a[-4]+a[18]+a[-19]
'Coa'
>>> a[-4]+a[18]+a[-20]
'Cow'
>>> b = "Codegnan IT Solutions"
>>> b[-1]+b[-2]+b[-3]+b[-4]+b[-5]+b[-6]+b[-7]+b[-8]+b[-9]
'snoituloS'
>>> b[-9]+b[-8]+b[-7]+b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'Solutions'
>>> b[-12]+b[-11]
'IT'
>>> b[-21]
'C'
>>> b[-21]+b[-20]+b[-19]+b[-18]+b[-17]+b[-16]+b[-15]+b[-14]
'Codegnan'
