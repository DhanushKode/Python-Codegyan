Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#split()
a="python c c++ java"
a.split()
['python', 'c', 'c++', 'java']
b=" i am learning python"
b.split()
['i', 'am', 'learning', 'python']
c="pythonjavac"
c.split()
['pythonjavac']
d="pythoncc++"
d.split()
['pythoncc++']
d.spilt("-")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    d.spilt("-")
AttributeError: 'str' object has no attribute 'spilt'. Did you mean: 'split'?
d.split("-")
['pythoncc++']
d.split("_")
['pythoncc++']
d.split('-')
['pythoncc++']

#Join method

a="apple","banana","bhaai"
"".join(a)
'applebananabhaai'
"K".join(a)
'appleKbananaKbhaai'

b = "apple"," ", "Bhaai"
" ".join(b)
'apple   Bhaai'

#Formattting
a=
SyntaxError: invalid syntax
a=5
b=6
print(a+b)
11
>>> print("The sum is ",a+b )
The sum is  11
>>> 
>>> city= "Vijayawada"
>>> print("THe city is ",city)
THe city is  Vijayawada
>>> 
>>> #Format method
>>> a="Bhaai"
>>> b="Puri"
>>> 
>>> print("hello{}{}".format(a,b))
helloBhaaiPuri
>>> 
>>> print("hello {} {}".format(a,b))
hello Bhaai Puri
>>> 
>>> print("hello {} hello {}".format(a,b))
hello Bhaai hello Puri
>>> print("hello {}{}".format(a,b))
hello BhaaiPuri
>>> 
>>> #F string
>>> print(f"hellp {a}{b}")
hellp BhaaiPuri
>>> 
>>> print(f"hello {a} {b}")
hello Bhaai Puri
>>> 
>>> print(f"hello {a} hello {b}")
hello Bhaai hello Puri
>>> 
>>> print("The sum is ",a+b )
The sum is  BhaaiPuri
>>> 
>>> 
>>> print("the product is {} * {} = {}".format(a,b,a*b))
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    print("the product is {} * {} = {}".format(a,b,a*b))
TypeError: can't multiply sequence by non-int of type 'str'
>>> a=5
>>> b=6
>>> print("the product is {} * {} = {}".format(a,b,a*b))
the product is 5 * 6 = 30
