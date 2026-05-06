Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> #String methods
>>> a="python"
>>> len(a)
6
>>> a="Python course"
>>> len(a)
13
>>> b=""
>>> len(b)
0
>>> c=" "
>>> len(c)
1
>>> 
>>> #Count
>>> a="Twinlke Twinkle little star"
>>> 
>>> count(a)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
>>> a.count("Twinkle")
1
>>> a.count("k")
2
>>> a.count("t")
3
>>> a.count(" ")
3
>>> 
>>> b = "bhAAi"
>>> 
>>> b.count("A")
2
>>> b.count("")
6
>>> 
>>> #find a string
>>> b.find("A")
2
>>> b[2:4]
'AA'
>>> 
b.find("")
0
b.find(5)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    b.find(5)
TypeError: find() argument 1 must be str, not int
b.find("5")
-1
b.find("2")
-1

#Escape Sequences
#\n->new line
#\t-> tab space
a="name\nmobile\tmailid"
print(a)
name
mobile	mailid

b="name:Bhaai\nmobile:99999999\tmailid:bhaai@mail.com"
print(b)
name:Bhaai
mobile:99999999	mailid:bhaai@mail.com
b="name:Bhaai\nmobile:99999999\tmailid:bhaai@mail.com"
print(b)
name:Bhaai
mobile:99999999	mailid:bhaai@mail.com
b="name:Bhaai\nmobile:99999999\t mailid:bhaai@mail.com"
print(b)
name:Bhaai
mobile:99999999	 mailid:bhaai@mail.com

#replace()

a="wait until you succedd"
a.replace("wait","work")
'work until you succedd'
a.replace("succedd","pass")
'wait until you pass'

b=a.replace("wait","work")
b
'work until you succedd'

#Upper()
a="code"
a.upper()
'CODE'

#lower()
b="GNAN"
b.lower()
'gnan'

#Capitalize - Capitals the Sngle word and Title will Capital starting letter of every word

a.capitalize()
'Code'
c="i am in class"
c.capitalize()
'I am in class'
c.title()
'I Am In Class'
c[8].capitalize()
'C'
# Title will make starting letter of every word Capital

a="data"
a.isupper()
False
a.islower()
True
a.isalpha()
True
a.isdigit()
False

b="code gnan"
b.isalpha()
False
#space is not considered as alphabet

c="codegnag"
c.isaplha()
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    c.isaplha()
AttributeError: 'str' object has no attribute 'isaplha'. Did you mean: 'isalpha'?
c.isalpha()
True
#any special characters are not considered as alphabets
d="code_gnan"
d.isalpha()
False
e="bhaai000"
e.isdigit()
False
e.isalnum()
True
b=45668
b.isnumeric()
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    b.isnumeric()
AttributeError: 'int' object has no attribute 'isnumeric'
#here we went to add it as string not as number
b="55550"
b.isnumeric()
True

g="1/5"
g.isnumeric()
False
g.isdigit()
False
g.isdecimal()
False

a=6.02
a.isdecimal()
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    a.isdecimal()
AttributeError: 'float' object has no attribute 'isdecimal'
a="6.02"a.isdecimal()
SyntaxError: invalid syntax
a="6.02"
a.isdecimal()
False
a="6"
a.isdecimal()
True
a="0.6"
a.isfloat()
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    a.isfloat()
AttributeError: 'str' object has no attribute 'isfloat'


