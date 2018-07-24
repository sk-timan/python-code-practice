Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
[4, 3]
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
<__main__.cartesianPoint object at 0x00000222A3E14550>
>>> p1=cartesianPoint()
>>> p1.x=3
>>> p1.y=4
>>> p2=cartesianPoint()
>>> p2.x=3
>>> p2.y=4
>>> p1 in p2
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    p1 in p2
TypeError: argument of type 'cartesianPoint' is not iterable
>>> p1 is p2
False
>>> samePoint(p1,p2)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    samePoint(p1,p2)
NameError: name 'samePoint' is not defined
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
>>> p1=cartesianPoint()
>>> p1.x=3
p1.y=4
p2=cartesianPoint()
p2.x=3
p2.y=4
SyntaxError: multiple statements found while compiling a single statement
>>> p1.x=3p1.y=4
SyntaxError: invalid syntax
>>> p1.x=3
>>> p1.y=4
>>> p2=cartesianPoint()
>>> p2.x=3
>>> p2.y=4
>>> p1 is p2
False
>>> samePoint(p1,p2)
True
>>> p1=p2
>>> p1 is p2
True
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 787, in <module>
    pp1=polarPoint()
TypeError: polarPoint() missing 1 required positional argument: 'p'
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 789, in <module>
    pp1.radius=1.0
AttributeError: 'NoneType' object has no attribute 'radius'
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 792, in <module>
    pp2.angle=math.pi/4.0
NameError: name 'math' is not defined
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
>>> pp1 is pp2
False
>>> samePoint(pp1,pp2)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    samePoint(pp1,pp2)
  File "C:\Users\Administrator\Desktop\code.py", line 782, in samePoint
    return(p1.x==p2.x)and(p1.y==p2.y)
AttributeError: 'polarPoint' object has no attribute 'x'
>>> 
