Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
>>> a=cPoint
>>> a=cPoint(1,2)
>>> a=cPoint(1,2,3)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a=cPoint(1,2,3)
TypeError: __init__() takes 3 positional arguments but 4 were given
>>> a=cPoint(3.0,4.0)
>>> cartesian
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    cartesian
NameError: name 'cartesian' is not defined
>>> x
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> cPoint
<class '__main__.cPoint'>
>>> a.x
3.0
>>> a.y
4.0
>>> a.radius
5.0
>>> a.angle
0.9272952180016122
>>> cPoint.a
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    cPoint.a
AttributeError: type object 'cPoint' has no attribute 'a'
>>> cPoint.x
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    cPoint.x
AttributeError: type object 'cPoint' has no attribute 'x'
>>> a.cartesian
<bound method cPoint.cartesian of <__main__.cPoint object at 0x000001EF17A03588>>
>>> a.polar
<bound method cPoint.polar of <__main__.cPoint object at 0x000001EF17A03588>>
>>> a.x
3.0
>>> a.__str__
<bound method cPoint.__str__ of <__main__.cPoint object at 0x000001EF17A03588>>
>>> a
<__main__.cPoint object at 0x000001EF17A03588>
>>> a.cartesian
<bound method cPoint.cartesian of <__main__.cPoint object at 0x000001EF17A03588>>
>>> a.cartesian()
(3.0, 4.0)
>>> a.polar()
(5.0, 0.9272952180016122)
>>> a.__str__ ()
'(3.0,4.0)'
>>> a.__cmp__()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a.__cmp__()
TypeError: __cmp__() missing 1 required positional argument: 'other'
>>> a.__cmp__(1)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a.__cmp__(1)
  File "C:\Users\Administrator\Desktop\code.py", line 810, in __cmp__
    return (self.x==other.x)and(self.y==other.y)
AttributeError: 'int' object has no attribute 'x'
>>> b=cPoint(3.0,4.0)
>>> a=b
>>> a>b
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a>b
TypeError: '>' not supported between instances of 'cPoint' and 'cPoint'
>>> a
<__main__.cPoint object at 0x000001EF17A14048>
>>> b
<__main__.cPoint object at 0x000001EF17A14048>
>>> a.cPoint
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a.cPoint
AttributeError: 'cPoint' object has no attribute 'cPoint'
>>> a.cPoint()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a.cPoint()
AttributeError: 'cPoint' object has no attribute 'cPoint'
>>> a
<__main__.cPoint object at 0x000001EF17A14048>
>>> a.x
3.0
>>> b.x
3.0
>>> a is b
True
>>> a==b
True
>>> a>b
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a>b
TypeError: '>' not supported between instances of 'cPoint' and 'cPoint'
>>> a=cPoint()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a=cPoint()
TypeError: __init__() missing 2 required positional arguments: 'x' and 'y'
>>> a=cPoint(3.0,4.0)
>>> b=cPoint(1.0,2.0)
>>> a==b
False
>>> a>b
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a>b
TypeError: '>' not supported between instances of 'cPoint' and 'cPoint'
>>> dir(a)
['__class__', '__cmp__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'angle', 'cartesian', 'polar', 'radius', 'x', 'y']
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'b', 'cPoint', 'math']
>>> dir(1)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'b', 'cPoint', 'math']
>>> dir('')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
>>> a=cPoint(1.0,2.0)
>>> b=cPoint(3.0,4.0)
>>> a==b
False
>>> a<b
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a<b
TypeError: '<' not supported between instances of 'cPoint' and 'cPoint'
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
>>> a==bb
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a==bb
NameError: name 'bb' is not defined
>>> a==b
False
>>> a>b
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a>b
TypeError: '>' not supported between instances of 'cPoint' and 'cPoint'
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
>>> a>b
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a>b
TypeError: '>' not supported between instances of 'cPoint' and 'cPoint'
>>> a<b
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a<b
TypeError: '<' not supported between instances of 'cPoint' and 'cPoint'
>>> a.x
1.0
>>> b.x
3.0
>>> a.x<b.x
True
>>> a==b
False
>>> a,__cmp__(b)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a,__cmp__(b)
NameError: name '__cmp__' is not defined
>>> a.__cmp__(b)
True
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
>>> a==b
False
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
>>> a==b
False
>>> a>b
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    a>b
TypeError: '>' not supported between instances of 'cPoint' and 'pPoint'
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
>>> a==b
False
>>> a
<__main__.cPoint object at 0x0000014EE1D240B8>
>>> b
<__main__.pPoint object at 0x0000014EE1D242B0>
>>> print(a)
(1.0,2.0)
>>> print(b)
(-0.4161468365471424,0.9092974268256817)
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
>>> a==b
False
>>> a>b
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a>b
TypeError: '>' not supported between instances of 'cPoint' and 'pPoint'
>>> type(1.0)
<class 'float'>
>>> 1.0>-0.498461561156
True
>>> type(a.x)
<class 'float'>
>>> type(b.x)
<class 'float'>
>>> type(a)
<class '__main__.cPoint'>
>>> type(b)
<class '__main__.pPoint'>
>>> 'abc'>4
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    'abc'>4
TypeError: '>' not supported between instances of 'str' and 'int'
>>> 'abc'==4
False
>>> 'abc'>=4
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    'abc'>=4
TypeError: '>=' not supported between instances of 'str' and 'int'
>>> 'abc'>=4
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    'abc'>=4
TypeError: '>=' not supported between instances of 'str' and 'int'
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
>>> a>b
True
>>> a
<__main__.cPoint object at 0x000002AD21AB40F0>
>>> b
<__main__.pPoint object at 0x000002AD21AB42E8>
>>> a.cPoint()
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    a.cPoint()
AttributeError: 'cPoint' object has no attribute 'cPoint'
>>> a.cPoint
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    a.cPoint
AttributeError: 'cPoint' object has no attribute 'cPoint'
>>> a
<__main__.cPoint object at 0x000002AD21AB40F0>
>>> print(a)
(1.0,2.0)
>>> print(b)
(-0.4161468365471424,0.9092974268256817)
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 846, in <module>
    print(s1,length())
NameError: name 'length' is not defined
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
3.605551275463989
>>> 3.x
SyntaxError: invalid syntax
>>> 5/2
2.5
>>> 5//2
2
>>> 5/2.0
2.5
>>> 5//2.0
2.0
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
3.605551275463989
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 859, in <module>
    box=Retangle(100,200,p1)
NameError: name 'Retangle' is not defined
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
3.605551275463989
(53.0,-96.0)
>>> print(p1)
(3.0,4.0)
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
3.605551275463989
(53.0,-96.0)
>>> print(p1)
(3.0,4.0)
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
3.605551275463989
53.0,-96.0)
>>> 
