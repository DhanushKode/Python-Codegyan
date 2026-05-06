Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Dictionary should be a pair value and use{}
>>> #dict{}
>>> a={"year":2026,"month":5}
>>> print(a)
{'year': 2026, 'month': 5}
>>> type(a)
<class 'dict'>
>>> b=("year","Month")
>>> type(b)
<class 'tuple'>
>>> a.keys()
dict_keys(['year', 'month'])
>>> a.values()
dict_values([2026, 5])
>>> a.items()
dict_items([('year', 2026), ('month', 5)])
>>> 
>>> 
>>> #in update u can add one or more it should be in single flower bracket
>>> 
>>> a={"name":"Bhaai","mailid":"bhaai@gmail.com"}
>>> a.update({"mobileno:8888888888"})
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a.update({"mobileno:8888888888"})
ValueError: dictionary update sequence element #0 has length 19; 2 is required
>>> a.update({"mobileno":8888888888})
>>> a
{'name': 'Bhaai', 'mailid': 'bhaai@gmail.com', 'mobileno': 8888888888}
>>> a.update({"year":2023, "month":5})
>>> a
{'name': 'Bhaai', 'mailid': 'bhaai@gmail.com', 'mobileno': 8888888888, 'year': 2023, 'month': 5}
>>> 
>>> #SETDEFAULT
>>> a={"year":2026,"month":"may"}
>>> a.setdefault("date",2)
2
>>> a
{'year': 2026, 'month': 'may', 'date': 2}
>>> 
>>> a.pop()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("year")
2026
a
{'month': 'may', 'date': 2}
a.popitem()
('date', 2)
#POPITEM() WILL PICK LAST ONE IN DICT NO NEED TO MENTION KEY

a
{'month': 'may'}

a={"Time":5,"Min":2,"Sec":6}
a
{'Time': 5, 'Min': 2, 'Sec': 6}
a.copy()
{'Time': 5, 'Min': 2, 'Sec': 6}
a["Time"]
5
a.get("min")
a
{'Time': 5, 'Min': 2, 'Sec': 6}
a.get("min")
a.get("Min")
2
b=a
b
{'Time': 5, 'Min': 2, 'Sec': 6}

a={"Name":"Sam","city":"VJA"}
a.clear()
a
{}
b={}
b.update({"cousre":"Python"})
b
{'cousre': 'Python'}

#DICTIONARY IS MUTABLE BUT DOESNT ALLOW DUPLICATES

a={"name":"sam","place":"vij","name":"sam"}
a
{'name': 'sam', 'place': 'vij'}
b={"name":"sam","place":"vij","name":"seth"}
b
{'name': 'seth', 'place': 'vij'}
b={"name":"sam","place":"vij","name2":"seth"}
b
{'name': 'sam', 'place': 'vij', 'name2': 'seth'}



details={"idnos":[10,20,30],"names":["sam","nick","Reed"],"marks":[50,60,70]}
type(details)
<class 'dict'>
details.keys()
dict_keys(['idnos', 'names', 'marks'])
details.values()
dict_values([[10, 20, 30], ['sam', 'nick', 'Reed'], [50, 60, 70]])
details.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['sam', 'nick', 'Reed']), ('marks', [50, 60, 70])])
