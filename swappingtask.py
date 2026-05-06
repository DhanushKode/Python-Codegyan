'''a=10
b=20
a,b=10,20
a,b=b,a
print(b,a)
'''

'''a=10
b=20
c=a
a=b
b=c
print(a,b)
'''

'''a="sam"
b="bridge"
a,b="sam","bridge"
a,b=b,a
print(a,b)'''

'''a=10
b=20
a=a+b
b=a-b
a=a-b
print(a,b)'''

'''a=10
b=20
a,b=b,a
print("a value is",a)
print("b value is",b)
'''

'''a=10
b=20
a=a+b
b=a-b
a=a-b
print("after swapping a=%d,b=%d "% (a,b))'''


'''a=input("data1")
b=input("data2")
a,b=b,a
print("after swapping a=%s,b=%s " %(a,b))'''

a=float(input("a value"))
b=float(input("b value"))
a=a+b
b=a-b
a=a-b
print("after swapping a=%.2f,b=%.2f" % (a,b))

#in float a%=.2f , we need to give how many decimal values we need in float, like %.3f,%.4f. we dont any decimal then use %d.
