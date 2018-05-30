Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
3.605551275463989
(53.0,-96.0)
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
3.605551275463989
(53.0,-96.0)
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 867, in <module>
    print(finCenter(box))
NameError: name 'finCenter' is not defined
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
3.605551275463989
(53.0,-96.0)
(58.0,-106.0)
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 891, in <module>
    p3=p1+p2
  File "C:\Users\Administrator\Desktop\code.py", line 883, in __add__
    return nwePoint(self.x+other.x,self.y+other.y)
NameError: name 'nwePoint' is not defined
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
(3.0,4.0)
False
>>> print(p2)
(0,0)
>>> p1==p2
False
>>> p3==p1
True
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
>>> per=Person(Frank,Fooba)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    per=Person(Frank,Fooba)
NameError: name 'Frank' is not defined
>>> per=Person('Frank','Fooba')
>>> self
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    self
NameError: name 'self' is not defined
>>> per.familyName()
'Frank'
>>> per.say(per,'hello!')
'Fooba Frank say to Fooba Frank: hello!'
>>> per.sing(per,'hello!')
'Fooba Frank say to Fooba Frank: hello!tra la la'
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
>>> print(per)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(per)
NameError: name 'per' is not defined
>>> per=Person(Frank,Fooba)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    per=Person(Frank,Fooba)
NameError: name 'Frank' is not defined
>>> per=Person('Frank','Fooba')
>>> print(per)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(per)
  File "C:\Users\Administrator\Desktop\code.py", line 928, in __str__
    return '<person:>'(self.first_name,self.family_name)
TypeError: 'str' object is not callable
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
>>> print(per)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print(per)
  File "C:\Users\Administrator\Desktop\code.py", line 928, in __str__
    return '<person:>'%(self.first_name,self.family_name)
TypeError: not all arguments converted during string formatting
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
>>> print(per)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(per)
  File "C:\Users\Administrator\Desktop\code.py", line 928, in __str__
    return ('<person:>'%(self.first_name,self.family_name))
TypeError: not all arguments converted during string formatting
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
>>> print(per)
<person:>
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
>>> print(per)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(per)
  File "C:\Users\Administrator\Desktop\code.py", line 928, in __str__
    return '<person:>'+(self.first_name,self.family_name)
TypeError: must be str, not tuple
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
>>> print(per)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(per)
  File "C:\Users\Administrator\Desktop\code.py", line 928, in __str__
    return '<person:>'+str(self.first_name,self.family_name)
TypeError: decoding str is not supported
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
>>> print(per)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(per)
  File "C:\Users\Administrator\Desktop\code.py", line 928, in __str__
    return ('<person:>'+str(self.first_name,self.family_name))
TypeError: decoding str is not supported
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
>>> print(per)
<person:>Fooba,Frank
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
>>> print(per)
<person:Fooba,Frank>
>>> a=Person('Andy','mile')
>>> per==a
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    per==a
  File "C:\Users\Administrator\Desktop\code.py", line 925, in __eq__
    return  operator.eq((self.family_name,self.first_name),
NameError: name 'operator' is not defined
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
>>> a=Person('Andy','mile')
			
>>> per==a
			
False
>>> a=Person('Frank','Fooba')
			
>>> per=a
			
>>> per=Person('Frank','Fooba')
			
>>> per==a
			
True
>>> per>a
			
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    per>a
TypeError: '>' not supported between instances of 'Person' and 'Person'
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
>>> print(per)
			
<person: Fooba Frank>
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
>>> print(per)
			
<person: Fooba Frank>
>>> a=Person
			
>>> print(a)
			
<class '__main__.Person'>
>>> a=Person()
			
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a=Person()
TypeError: __init__() missing 2 required positional arguments: 'family_name' and 'first_name'
>>> a=Person('a','s')
			
>>> print(a)
			
<person: s a>
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0
1
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 951, in <module>
    p1=MITPerson(Person('Smith','Fred'))
TypeError: __init__() missing 1 required positional argument: 'firstName'
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 951, in <module>
    p1=MITPerson(Person('Smith','Fred','a'))
TypeError: __init__() takes 3 positional arguments but 4 were given
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 951, in <module>
    p1=MITPerson(Person('Smith','Fred'))
TypeError: __init__() missing 1 required positional argument: 'firstName'
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\code.py", line 951, in <module>
    p1=MITPerson(Person('Smith','Fred'))
TypeError: __init__() missing 1 required positional argument: 'firstName'
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0
1
>>> print(p1)
			
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print(p1)
  File "C:\Users\Administrator\Desktop\code.py", line 947, in __str__
    return ('<MIT Person: %s %s >'%(self.first_name,self.family_name))
AttributeError: 'MITPerson' object has no attribute 'first_name'
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0
1
>>> print(p1)
			
<MIT Person: Fred Smith >
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
>>> Person.__init__(self,familyName,firstName)
			
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    Person.__init__(self,familyName,firstName)
NameError: name 'self' is not defined
>>> Person.__init__()
			
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    Person.__init__()
TypeError: __init__() missing 3 required positional arguments: 'self', 'family_name', and 'first_name'
>>> self=[]
			
>>> Person.__init__(self,familyName,firstName)
			
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    Person.__init__(self,familyName,firstName)
NameError: name 'familyName' is not defined
>>> familyName=[]
			
>>> 
			
>>> firstName=[]
			
>>> self=['a']
			
>>> familyName=['b']
			
>>> firstName=['c']
			
>>> Person.__init__(self,familyName,firstName)
			
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    Person.__init__(self,familyName,firstName)
  File "C:\Users\Administrator\Desktop\code.py", line 918, in __init__
    self.family_name=family_name
AttributeError: 'list' object has no attribute 'family_name'
>>> familyName='b'
			
>>> firstName='c'
			
>>> Person.__init__(self,familyName,firstName)
			
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    Person.__init__(self,familyName,firstName)
  File "C:\Users\Administrator\Desktop\code.py", line 918, in __init__
    self.family_name=family_name
AttributeError: 'list' object has no attribute 'family_name'
>>> type(familyName)
			
<class 'str'>
>>> self='a'
			
>>> Person.__init__(self,familyName,firstName)
			
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    Person.__init__(self,familyName,firstName)
  File "C:\Users\Administrator\Desktop\code.py", line 918, in __init__
    self.family_name=family_name
AttributeError: 'str' object has no attribute 'family_name'
>>> self=()
			
>>> Person.__init__(self,familyName,firstName)
			
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    Person.__init__(self,familyName,firstName)
  File "C:\Users\Administrator\Desktop\code.py", line 918, in __init__
    self.family_name=family_name
AttributeError: 'tuple' object has no attribute 'family_name'
>>> class ceshi:
	def __init__(self,a,b):
		pass

			
>>> class Person:
    def __init__(self,family_name,first_name):
        self.family_name=family_name
        self.first_name=first_name
    def familyName(self):
        return self.family_name
    def firstName(self):
        return self.first_name
    def __eq__(self,other):
        return  operator.eq((self.family_name,self.first_name),
                            (other.family_name,other.first_name))
    def __str__(self):
        return ('<person: %s %s>'%(self.first_name,self.family_name))
    def say(self,toWhom,something):
            return (self.first_name+' '+self.family_name+' says to '+toWhom.firstName()+
                  ' '+toWhom.familyName()+': '+something)
    def sing(self,toWhom,something):
        return self.say(toWhom,something+'tra la la')

			
>>> Person.__init__(self,familyName,firstName)
			
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    Person.__init__(self,familyName,firstName)
  File "<pyshell#64>", line 3, in __init__
    self.family_name=family_name
AttributeError: 'tuple' object has no attribute 'family_name'
>>> 
=============================== RESTART: Shell ===============================
>>> import operator

class Person:
    def __init__(self,family_name,first_name):
        self.family_name=family_name
        self.first_name=first_name
    def familyName(self):
        return self.family_name
    def firstName(self):
        return self.first_name
    def __eq__(self,other):
        return  operator.eq((self.family_name,self.first_name),
                            (other.family_name,other.first_name))
    def __str__(self):
        return ('<person: %s %s>'%(self.first_name,self.family_name))
    def say(self,toWhom,something):
            return (self.first_name+' '+self.family_name+' says to '+toWhom.firstName()+
                  ' '+toWhom.familyName()+': '+something)
    def sing(self,toWhom,something):
        return self.say(toWhom,something+'tra la la')
			
SyntaxError: multiple statements found while compiling a single statement
>>> class Person:
    def __init__(self,family_name,first_name):
        self.family_name=family_name
        self.first_name=first_name
    def familyName(self):
        return self.family_name
    def firstName(self):
        return self.first_name
    def __eq__(self,other):
        return  operator.eq((self.family_name,self.first_name),
                            (other.family_name,other.first_name))
    def __str__(self):
        return ('<person: %s %s>'%(self.first_name,self.family_name))
    def say(self,toWhom,something):
            return (self.first_name+' '+self.family_name+' says to '+toWhom.firstName()+
                  ' '+toWhom.familyName()+': '+something)
    def sing(self,toWhom,something):
        return self.say(toWhom,something+'tra la la')

			
>>> Person.__init__(self,familyName,firstName)
			
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    Person.__init__(self,familyName,firstName)
NameError: name 'self' is not defined
>>> class ceshi:
	def __init__(self,a,b):
		pass

			
>>> class ceshi:
	def __init__(self,a,b):
		Person.__init__(self,familyName,firstName)

			
>>> print(ceshi)
			
<class '__main__.ceshi'>
>>> print(ceshi())
			
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    print(ceshi())
TypeError: __init__() missing 2 required positional arguments: 'a' and 'b'
>>> class ceshi(Person):
	def __init__(self,a,b):
		Person.__init__(self,a,b)

			
>>> print(ceshi(Person))
			
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    print(ceshi(Person))
TypeError: __init__() missing 1 required positional argument: 'b'
>>> print(ceshi('a','b'))
			
<person: b a>
>>> print(ceshi('1','2'))
			
<person: 2 1>
>>> class ceshi(Person):
	Person.__init__(self,familyName,firstName)

			
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    class ceshi(Person):
  File "<pyshell#82>", line 2, in ceshi
    Person.__init__(self,familyName,firstName)
NameError: name 'self' is not defined
>>> class ceshi(Person):
	def __init__(self):
			Person.__init__(self,familyName,firstName)

			
>>> ceshi()
			
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    ceshi()
  File "<pyshell#84>", line 3, in __init__
    Person.__init__(self,familyName,firstName)
NameError: name 'familyName' is not defined
>>> ceshi('1','2')
			
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    ceshi('1','2')
TypeError: __init__() takes 1 positional argument but 3 were given
>>> class ceshi(Person):
	def __init__(self):
			Person.__init__(self)

			
>>> ceshi()
			
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    ceshi()
  File "<pyshell#88>", line 3, in __init__
    Person.__init__(self)
TypeError: __init__() missing 2 required positional arguments: 'family_name' and 'first_name'
>>> ceshi('1','2')
			
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    ceshi('1','2')
TypeError: __init__() takes 1 positional argument but 3 were given
>>> class ceshi(Person):
	def __init__(self,a,b)
			
SyntaxError: invalid syntax
>>> class ceshi(Person):
	def __init__(self,a,b):
			pass

			
>>> ceshi
			
<class '__main__.ceshi'>
>>> ceshi('1','2')
			
<__main__.ceshi object at 0x000002823B1EEA58>
>>> class ceshi(Person):
	def __init__(self,a,b):
		Person.__init__(self,a,b)

			
>>> ceshi('1','2')
			
<__main__.ceshi object at 0x000002823B200EF0>
>>> class ceshi(Person):
	def __init__(self,a,b):
			pass

			
>>> print(ceshi())
			
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    print(ceshi())
TypeError: __init__() missing 2 required positional arguments: 'a' and 'b'
>>> print(ceshi('1','2'))
			
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    print(ceshi('1','2'))
  File "<pyshell#68>", line 13, in __str__
    return ('<person: %s %s>'%(self.first_name,self.family_name))
AttributeError: 'ceshi' object has no attribute 'first_name'
>>> class ceshi(Person):
	def __init__(self,a,b):
		Person.__init__(self,a,b)

			
>>> print(ceshi('1','2'))
			
<person: 2 1>
>>> class ceshi(Person):
	def __init__(self,a,b):
		Person.__init__(self,a,b)
	def __str__(self):
			return('cheshijieguo: %s %s'%(self.first_name,self.family_name))

			
>>> print(ceshi('1','2'))
			
cheshijieguo: 2 1
>>> class ceshi(Person):
	def __init__(self,a,b):
		Person.__init__(self,a,b)
	def __str__(self):
			return('cheshijieguo: %s %s'%(a,b))

			
>>> print(ceshi('1','2'))
			
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    print(ceshi('1','2'))
  File "<pyshell#116>", line 5, in __str__
    return('cheshijieguo: %s %s'%(a,b))
NameError: name 'a' is not defined
>>> class ceshi(Person):
	def __init__(self,a,b):
		Person.__init__(self,a,b)
	def __str__(self):
			return('cheshijieguo: %s %s'%(self.a,self.b))

			
>>> print(ceshi('1','2'))
			
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    print(ceshi('1','2'))
  File "<pyshell#119>", line 5, in __str__
    return('cheshijieguo: %s %s'%(self.a,self.b))
AttributeError: 'ceshi' object has no attribute 'a'
>>> class ceshi(Person):
	def __init__(self,a,b):
		self.a=a
		self.b=b
		Person.__init__(self,a,b)
	def __str__(self):
			return('cheshijieguo: %s %s'%(self.a,self.b))

			
>>> print(ceshi('1','2'))
			
cheshijieguo: 1 2
>>> class ceshi(Person):
			pass

			
>>> print(ceshi('1','2'))
			
<person: 2 1>
>>> ceshi()
			
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    ceshi()
TypeError: __init__() missing 2 required positional arguments: 'family_name' and 'first_name'
>>> ceshi
			
<class '__main__.ceshi'>
>>> ceshi==Person
			
False
>>> print(ceshi.family_name)
			
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    print(ceshi.family_name)
AttributeError: type object 'ceshi' has no attribute 'family_name'
>>> print(ceshi.familyName)
			
<function Person.familyName at 0x000002823B1F6F28>
>>> Person.familyName
			
<function Person.familyName at 0x000002823B1F6F28>
>>> class ceshi(Person):
			def __init__(self,a,b)
			
SyntaxError: invalid syntax
>>> class ceshi(Person):
			def __init__(self,a,b):
			pass
			
SyntaxError: expected an indented block
>>> class ceshi(Person):
			def __init__(self,a,b):
				pass

			
>>> class ceshi(Person):
			def __init__(self,a,b,c):
				pass

			
>>> ceshi('1','2','3')
			
<__main__.ceshi object at 0x000002823B2007F0>
>>> print(ceshi('1','2','3'))
			
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    print(ceshi('1','2','3'))
  File "<pyshell#68>", line 13, in __str__
    return ('<person: %s %s>'%(self.first_name,self.family_name))
AttributeError: 'ceshi' object has no attribute 'first_name'
>>> class ceshi(Person):
			def __init__(self,a,b,c):
				Person.__init__(self,familyName,firstName)
				pass

			
>>> print(ceshi('1','2','3'))
			
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    print(ceshi('1','2','3'))
  File "<pyshell#149>", line 3, in __init__
    Person.__init__(self,familyName,firstName)
NameError: name 'familyName' is not defined
>>> class ceshi(Person):
			def __init__(self,a,b,c):
				Person.__init__(self,a,b,c)
				pass

			
>>> print(ceshi('1','2','3'))
			
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    print(ceshi('1','2','3'))
  File "<pyshell#152>", line 3, in __init__
    Person.__init__(self,a,b,c)
TypeError: __init__() takes 3 positional arguments but 4 were given
>>> class ceshi(Person):
			def __init__(self,a,b):
				Person.__init__(self,a,b)
				pass

			
>>> print(ceshi('1','2','3'))
			
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    print(ceshi('1','2','3'))
TypeError: __init__() takes 3 positional arguments but 4 were given
>>> print(ceshi('1','2'))
			
<person: 2 1>
>>> class ceshi(Person):
			def __init__(self,a,b):
				Person.__init__(self,a,b)
			def __str__(self):
				return ('cheshijieguo: %s %s'%(self.first_name,self.family_name))

			
>>> print(ceshi('1','2'))
			
cheshijieguo: 2 1
>>> class ceshi(Person):
			def __init__(self,a,b):
				Person.__init__(self,a,b)
			def __str__(self):
				return ('cheshijieguo: %s %s'%(self.a,self.b))

			
>>> print(ceshi('1','2'))
			
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    print(ceshi('1','2'))
  File "<pyshell#164>", line 5, in __str__
    return ('cheshijieguo: %s %s'%(self.a,self.b))
AttributeError: 'ceshi' object has no attribute 'a'
>>> class ceshi(Person):
			def __init__(self,a,b):
				Person.__init__(self,a,b)
			def __str__(self):
				return ('cheshijieguo: %s %s'%(self.first_name,self.family_name))

			
>>> print(ceshi('1','2'))
			
cheshijieguo: 2 1
>>> print(ceshi.a)
			
Traceback (most recent call last):
  File "<pyshell#169>", line 1, in <module>
    print(ceshi.a)
AttributeError: type object 'ceshi' has no attribute 'a'
>>> print(self.a)
			
Traceback (most recent call last):
  File "<pyshell#170>", line 1, in <module>
    print(self.a)
NameError: name 'self' is not defined
>>> class ceshi(Person):
	def __init__(self,a,b):
		self.a=a
		self.b=b
		Person.__init__(self,a,b)
	def __str__(self):
			return('cheshijieguo: %s %s'%(self.a,self.b))

			
>>> print(ceshi('1','2'))
			
cheshijieguo: 1 2
>>> class ceshi(Person):
	def __init__(self,a,b):
		self.a=a
		self.b=b
		Person.__init__(self,a,b)
	def __str__(self):
			return('cheshijieguo: %s %s'%(self.first_name,self.family_name))

			
>>> print(ceshi('1','2'))
			
cheshijieguo: 2 1
>>> class ceshi(Person):
	def __init__(self,a,b,c):
		self.a=a
		self.b=b
		Person.__init__(self,a,b)
	def __str__(self):
			return('cheshijieguo: %s %s'%(self.first_name,self.family_name))

			
>>> print(ceshi('1','2'))
			
Traceback (most recent call last):
  File "<pyshell#179>", line 1, in <module>
    print(ceshi('1','2'))
TypeError: __init__() missing 1 required positional argument: 'c'
>>> print(ceshi('1','2','3'))
			
cheshijieguo: 2 1
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0
1
>>> print(MITPerson.nextIdNum)
			
2
>>> print(MITPerson.nextIdNum)
			
2
>>> p1=MITPerson('Smith','Fred')
p2=MITPerson('Foobar','Jane')
			
SyntaxError: multiple statements found while compiling a single statement
>>> p1=MITPerson('Smith','Fred')
			
>>> 
			
>>> print(p1.getIdNum())
			
2
>>> print(MITPerson.nextIdNum)
			
3
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0
1
>>> print(me)
			
<person: Eric Grimson>
>>> print(UG)
			
<class '__main__.UG'>
>>> print(ug)
			
<MIT Person: Jane Doe >
>>> ug.familyName
			
<bound method Person.familyName of <__main__.UG object at 0x0000026A40DB34E0>>
>>> ug.familyName()
			
'Doe'
>>> print(ug.familyName)
			
<bound method Person.familyName of <__main__.UG object at 0x0000026A40DB34E0>>
>>> ug.getIdNum
			
<bound method MITPerson.getIdNum of <__main__.UG object at 0x0000026A40DB34E0>>
>>> ug.getIdNum()
			
2
>>> ug.idNum
			
2
>>> ug.nextIdNum
			
3
>>> ug.say
			
<bound method UG.say of <__main__.UG object at 0x0000026A40DB34E0>>
>>> ug.say(ug,'hello')
			
'Jane Doe says to Jane Doe: Excuse me,but hello'
>>> per==a
			
Traceback (most recent call last):
  File "<pyshell#200>", line 1, in <module>
    per==a
NameError: name 'a' is not defined
>>> per==ug
			
Traceback (most recent call last):
  File "<pyshell#201>", line 1, in <module>
    per==ug
  File "C:\Users\Administrator\Desktop\code.py", line 949, in __eq__
    return operator.eq(self.idNum,other.idNum)
AttributeError: 'Person' object has no attribute 'idNum'
>>> per>ug
			
Traceback (most recent call last):
  File "<pyshell#202>", line 1, in <module>
    per>ug
TypeError: '>' not supported between instances of 'Person' and 'UG'
>>> per==ug
			
Traceback (most recent call last):
  File "<pyshell#203>", line 1, in <module>
    per==ug
  File "C:\Users\Administrator\Desktop\code.py", line 949, in __eq__
    return operator.eq(self.idNum,other.idNum)
AttributeError: 'Person' object has no attribute 'idNum'
>>> ug==per
			
Traceback (most recent call last):
  File "<pyshell#204>", line 1, in <module>
    ug==per
  File "C:\Users\Administrator\Desktop\code.py", line 949, in __eq__
    return operator.eq(self.idNum,other.idNum)
AttributeError: 'Person' object has no attribute 'idNum'
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0
1
>>> per==ug
			
False
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0
1
['6.00']
['6.00', '6.xxx']
None
{'F08': ['6.00'], 'S09': ['6.00', '6.xxx']}
>>> print(me)
			
<MIT Person: Eric Grimson >
>>> you=Prof('Tianyuan','Zhan','ungraduate')
			
>>> print(you)
			
<MIT Person: Zhan Tianyuan >
>>> me.say(ug,'hello!')
			
'Eric Grimson says to Jane Doe: I do not understand why you sayhello!'
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0
1
['6.00']
['6.00', '6.xxx']
None
{'F08': ['6.00'], 'S09': ['6.00', '6.xxx']}
>>> you=Prof('Tianyuan','Zhan','ungraduate')
			
>>> me.say(ug,'hello!')
			
'Eric Grimson says to Jane Doe: I do not understand why you say hello!'
>>> me.say(you,'hello!')
			
'Eric Grimson says to Zhan Tianyuan: I really liked your paper onhello!'
>>> 
============== RESTART: C:\Users\Administrator\Desktop\code.py ==============
0
1
['6.00']
['6.00', '6.xxx']
None
{'F08': ['6.00'], 'S09': ['6.00', '6.xxx']}
>>> you=Prof('Tianyuan','Zhan','ungraduate')
			
>>> me.say(ug,'hello!')
			
'Eric Grimson says to Jane Doe: I do not understand why you say hello!'
>>> me.say(you,'CSDN')
			
'Eric Grimson says to Zhan Tianyuan: I really liked your paper on CSDN'
>>> print(ug)
			
<MIT Person: Jane Doe >
>>> type(me)
			
<class '__main__.Prof'>
>>> type(you)
			
<class '__main__.Prof'>
>>> type(ug)
			
<class '__main__.UG'>
>>> me.lecture(you,'python')
			
'Eric Grimson says to Zhan Tianyuan: I really liked your paper on python as it is obvious'
>>> 
