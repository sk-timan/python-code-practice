Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def merge(left,right):
	result=[]
	i,j=0,0
	while i<len(left) and j<len(right):
		if left[i]<=right[j]:
			result.append(left[i])
			i+=1
		else:
			result.append(right[j])
			j+=1
	while i<len(left):
		result.append(left[i])
		i+=1
	while j<len(right):
		result.append(right[j])
		j+=1
	return result

>>> def mergesort(L):
	print(L)
	if len(L)<2:
		return L[:]
	else:
		middle=len(L)/2
		left=mergesort(L[:middle])
		right=mergesort(L[middle:])
		together=merge(left,right)
		print('merged',together)
		return together

	
>>> L=[5,6,8,7,3,9,1]
>>> mergesort(L)
[5, 6, 8, 7, 3, 9, 1]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    mergesort(L)
  File "<pyshell#13>", line 7, in mergesort
    left=mergesort(L[:middle])
TypeError: slice indices must be integers or None or have an __index__ method
>>> def mergesort(L):
	print(L)
	if len(L)<2:
		return L[:]
	else:
		middle=len(L)//2
		left=mergesort(L[:middle])
		right=mergesort(L[middle:])
		together=merge(left,right)
		print('merged',together)
		return together

	
>>> mergesort(L)
[5, 6, 8, 7, 3, 9, 1]
[5, 6, 8]
[5]
[6, 8]
[6]
[8]
merged [6, 8]
merged [5, 6, 8]
[7, 3, 9, 1]
[7, 3]
[7]
[3]
merged [3, 7]
[9, 1]
[9]
[1]
merged [1, 9]
merged [1, 3, 7, 9]
merged [1, 3, 5, 6, 7, 8, 9]
[1, 3, 5, 6, 7, 8, 9]
>>> def create(smallest,largest):
	intSet=[]
	for i in range(smallest,largest+1):
		intSet.append(None)
	return intSet

>>> def insert(intSet,e):
	intSet[e]=1

	
>>> def member(intSet,e):
	return intSet[e]==1

>>> create(0,5)
[None, None, None, None, None, None]
>>> insert(inSet,e)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    insert(inSet,e)
NameError: name 'inSet' is not defined
>>> insert(creat(0,5),e)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    insert(creat(0,5),e)
NameError: name 'creat' is not defined
>>> insert(create(0,5),e)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    insert(create(0,5),e)
NameError: name 'e' is not defined
>>> insert(create(0,5),1)
>>> print(create)
<function create at 0x000001E37B5B6F28>
>>> print(intSet)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print(intSet)
NameError: name 'intSet' is not defined
>>> intSet=creat(0,5)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    intSet=creat(0,5)
NameError: name 'creat' is not defined
>>> intSet=create(0,5)
>>> intSet
[None, None, None, None, None, None]
>>> insert(intSet,1)
>>> print(intSet)
[None, 1, None, None, None, None]
>>> member(intSet,1)
True
>>> member(intSet,2)
False
>>> 
=============================== RESTART: Shell ===============================
>>> ord(c)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    ord(c)
NameError: name 'c' is not defined
>>> ord('c)
	
SyntaxError: EOL while scanning string literal
>>> ord('c')
	
99
>>> ord('a')
	
97
>>> ord('ab')
	
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    ord('ab')
TypeError: ord() expected a character, but string of length 2 found
>>> ord('1')
	
49
>>> chr(a)
	
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    chr(a)
NameError: name 'a' is not defined
>>> chr('a')
	
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    chr('a')
TypeError: an integer is required (got type str)
>>> chr(1)
	
'\x01'
>>> chr(2)
	
'\x02'
>>> ord('2')
	
50
>>> ord(£)
	
SyntaxError: invalid character in identifier
>>> ord('/')
	
47
>>> ord('?')
	
63
>>> ord('£')
	
163
>>> ord('¬')
	
172
>>> def hashChar(c):
	#c is char
	return ord(c)

	
>>> def cSetCreate():
	cSet=[]
	for i in range(0,255):
		cSet.append(None)
	return cSet

	
>>> def cSetInsert(cSet,e):
	cSet[hashChar(e)]=1

	
>>> def cSetMember(cSet,e):
	return cSet[hashChar(e)]==1

	
>>> cSetCreate()
	
[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
>>> cSetInsert(cSet,'e')
	
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    cSetInsert(cSet,'e')
NameError: name 'cSet' is not defined
>>> cSet
	
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    cSet
NameError: name 'cSet' is not defined
>>> def cSetCreate():
	cSet=[]
	for i in range(0,255):
		cSet.append(None)
	return cSet

	
>>> cSetCreate()
	
[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
>>> cSet
	
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    cSet
NameError: name 'cSet' is not defined
>>> 
=============================== RESTART: Shell ===============================
>>> def readFloat(requestMsg,errorMsg)
	
SyntaxError: invalid syntax
>>> def readFloat(requestMsg,errorMsg):
	while True:
		val=input(requestMsg)
		try:
			val=valType(val)
			return val
		except:
			print(errorMsg)

	
>>> def readFloat(requestMsg,errorMsg):
	while True:
		val=input(requestMsg)
		try:
			val=float(val)
			return val
		except:
			print(errorMsg)

	
>>> print(readFloat('Enter float: ','Not a float.'))
	
Enter float: 1
1.0
>>> readFloat('Enter float: ','Not a float.')
	
Enter float: 1
1.0
>>> readFloat('Enter float: ','Not a float.')
	
Enter float: l
Not a float.
Enter float: 5
5.0
>>> while True:
	val=input()

	
while True:
	val=input()






=============================== RESTART: Shell ===============================
>>> def a(b):
	while True:
		val=input()

	
>>> a(b)
	
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    a(b)
NameError: name 'b' is not defined
>>> a()
	
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    a()
TypeError: a() missing 1 required positional argument: 'b'
>>> b=1
	
>>> a(b)
	
a(b)


a(b)



=============================== RESTART: Shell ===============================
>>> def readFloat(requestMsg,errorMsg):
	while True:
		val=input(requestMsg)

	
>>> readFloat('Enter float: ','Not a float.')
	
Enter float: 5
Enter float: 5
Enter float: 5
Enter float: 5
Enter float: 5
Enter float: 5
Enter float: 5
Enter float: 1
Enter float: j'
Enter float: 'j'
Enter float: 
=============================== RESTART: Shell ===============================
>>> def readFloat(requestMsg,errorMsg):
	while True:
		val=input(requestMsg)
		try:
			val=float(val)
			return val
		except:
			print(errorMsg)

	
>>> def readFloat(requestMsg,errorMsg):
	while True:
		val=input(requestMsg)
		return val

	
>>> readFloat('Enter float: ','Not a float.')
	
Enter float: 5
'5'
>>> def readFloat(requestMsg,errorMsg):
	while True:
		val=input(requestMsg)
	return val

	
>>> readFloat('Enter float: ','Not a float.')
	
Enter float: 5
Enter float: 5
Enter float: 5
Enter float: 5
Enter float: 5
Enter float: 5
Enter float: 55
Enter float: 5
Enter float: 5
Enter float: 5
Enter float: 5
Enter float: 5
Enter float: 5
Enter float: 5
Enter float: 5def readFloat(requestMsg,errorMsg):
	while True:
		val=input(requestMsg)
		break
	return val
Enter float: Enter float: Enter float: Enter float: Enter float: 
Enter float: 
=============================== RESTART: Shell ===============================
>>> def readFloat(requestMsg,errorMsg):
	while True:
		val=input(requestMsg)
		break
	return val

	
>>> readFloat('Enter float: ','Not a float.')
	
Enter float: 5
'5'
>>> def readFloat(requestMsg,errorMsg):
	while True:
		val=input(requestMsg)
		try:
			val=float(val)
			return val
		except:
			print(errorMsg)

	
>>> def readVal(valType,requestMsg,errorMsg):
	while True:
		val=input(requestMsg)
		try:
			val=valType(val)
			return val
		except:
			print(errorMsg)

	
>>> readVal(5,4,6)
	
4
6
4
6
4
6
4
6
4
6
4
6
4
6
4
6
4
6
4
6
4
6
4
6
4
6
4
6
4
6
4
=============================== RESTART: Shell ===============================
>>> def getGrades(fname):
	try:
		gradesFile=open(fname,'5')
	except IOError:
		print('Could not open',fname)
		print('aaaaa')
	grades=[]
	for line in gradesFile:
		grades.append(float(line))
	return grades

	
>>> getGrades(fanme)
	
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    getGrades(fanme)
NameError: name 'fanme' is not defined
>>> 
	
>>> getGrades()
	
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    getGrades()
TypeError: getGrades() missing 1 required positional argument: 'fname'
>>> fname=1
	
>>> getGrades(fanme)
	
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    getGrades(fanme)
NameError: name 'fanme' is not defined
>>> getGrades(fname)
	
Traceback (most recent call last):
  File "<pyshell#162>", line 1, in <module>
    getGrades(fname)
  File "<pyshell#156>", line 3, in getGrades
    gradesFile=open(fname,'5')
ValueError: invalid mode: '5'
>>> def getGrades(fname):
	try:
		gradesFile=open(fname,'w')
	except IOError:
		print('Could not open',fname)
		print('aaaaa')
	grades=[]
	for line in gradesFile:
		grades.append(float(line))
	return grades

	
>>> getGrades(fanme)
	
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    getGrades(fanme)
NameError: name 'fanme' is not defined
>>> getGrades(fname)
	
Could not open 1
aaaaa
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    getGrades(fname)
  File "<pyshell#164>", line 8, in getGrades
    for line in gradesFile:
UnboundLocalError: local variable 'gradesFile' referenced before assignment
>>> 
