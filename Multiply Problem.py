Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Multiply program
>>> a=6
>>> b=8
>>> print(a*b)
48
>>> print("the answer is".format(a*b))
the answer is
>>> print("the answer is".a*b)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print("the answer is".a*b)
AttributeError: 'str' object has no attribute 'a'
>>> print("the answer is",a*b)
the answer is 48
>>> print("the answer is".format(a,b))
the answer is
>>> b=print(a*b)
48
>>> print("the answer is".format(b))
the answer is
>>> print("the answer is {}".format(b))
the answer is None
>>> print("the answer is {}".format(a*b))
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print("the answer is {}".format(a*b))
TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
>>> print("the answer is {}".format(a,b))
the answer is 6
>>> c=print(a*b)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    c=print(a*b)
TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
>>> a=TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
SyntaxError: invalid syntax
>>> a=8
>>> b=6
>>> c=print(a*b)
48
>>> print("the answer is {}".format(c))
the answer is None
>>> print("the answer is ".format(c))
the answer is 
>>> print("answer{} ".format(c))
answerNone 


print(f"answer {c})
      
SyntaxError: unterminated f-string literal (detected at line 1)
print(a*b)
      
48
print("the answer is".format(a*b))
      
the answer is

print(f"{a}*{b})
      
SyntaxError: unterminated f-string literal (detected at line 1)
print(f"{a}*{b}")
      
8*6
print(f"{c}")
      
None
print(f"{a}*{b}")
      
8*6
print(f"{a)*{b}")
      
SyntaxError: f-string: unmatched ')'
print(f"{a}*{b}")
      
8*6
print(f"answer{a}*{b}")
      
answer8*6
print("the answer is {}".format(c))
      
the answer is None
c=(a*b)
      
print("the answer is {}".format(c))
      
the answer is 48
print(f"answer{a}*{b}")
      
answer8*6
print(f"{c}")
      
48
print("the answer is".format(a*b))
      
the answer is
print("the answer is {}".format(a*b))
      
the answer is 48
print(f"the answer is {a*b}")
      
the answer is 48
print("the answer is {}".format(c))
      
the answer is 48
print(f"{c}")
      
48
print("the answer is {}".format(a*b))
      
the answer is 48
print(f"the answer is {a*b}")
      
the answer is 48
