Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def solve1(numLegs,numHeads):
	for numSpiders in range(0,numHeads+1):
		for numChickens in range(0,numHeads-numSpiders):
			numPigs=numHeads-numSpiders-numChickens
			totLegs=4*numPigs+2*numChickens+8*numSpiders
			if totLegs==numLegs:
				return numPigs,numChickens,numSpiders
	return None,None,None

>>> solve1(100,30)
(20, 10, 0)
>>> def barnYard1():
	heads=int(input('Number of heads:', ))
	legs=int(input('Number of legs:', ))
	pigs,chickens,spiders=solve1(numlegs,numHeads)
	if pigs==None:
		print('the number of heads(or legs)is not suitable')
	else:
		print('Number of piges=',pigs)
		print('Number of chickens=',chickens)
		print('Number of spiders=',spiders)

		
>>> barnYard1()
Number of heads:100.5
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    barnYard1()
  File "<pyshell#20>", line 2, in barnYard1
    heads=int(input('Number of heads:', ))
ValueError: invalid literal for int() with base 10: '100.5'
>>> barnYard1()
Number of heads:100
Number of legs:20
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    barnYard1()
  File "<pyshell#20>", line 4, in barnYard1
    pigs,chickens,spiders=solve1(numlegs,numHeads)
NameError: name 'numlegs' is not defined
>>> barnYard1()
Number of heads:100
Number of legs:30
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    barnYard1()
  File "<pyshell#20>", line 4, in barnYard1
    pigs,chickens,spiders=solve1(numlegs,numHeads)
NameError: name 'numlegs' is not defined
>>> barnYard1()
Number of heads:20
Number of legs:100
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    barnYard1()
  File "<pyshell#20>", line 4, in barnYard1
    pigs,chickens,spiders=solve1(numlegs,numHeads)
NameError: name 'numlegs' is not defined
>>> def barnYard1():
	heads=int(input('Number of heads:', ))
	legs=int(input('Number of legs:', ))
	pigs,chickens,spiders=solve1(numLegs,numHeads)
	if pigs==None:
		print('the number of heads(or legs)is not suitable')
	else:
		print('Number of piges=',pigs)
		print('Number of chickens=',chickens)
		print('Number of spiders=',spiders)

		
>>> barnYard()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    barnYard()
NameError: name 'barnYard' is not defined
>>> barnYard1()
Number of heads:20
Number of legs:100
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    barnYard1()
  File "<pyshell#26>", line 4, in barnYard1
    pigs,chickens,spiders=solve1(numLegs,numHeads)
NameError: name 'numLegs' is not defined
>>> barnYard1()
Number of heads:30
Number of legs:100
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    barnYard1()
  File "<pyshell#26>", line 4, in barnYard1
    pigs,chickens,spiders=solve1(numLegs,numHeads)
NameError: name 'numLegs' is not defined
>>> def solve1(numLegs,numHeads):
	for numSpiders in range(0,numHeads+1):
		for numChickens in range(0,numHeads-numSpiders+1):
			numPigs=numHeads-numSpiders-numChickens
			totLegs=4*numPigs+2*numChickens+8*numSpiders
			if totLegs==numLegs:
				return numPigs,numChickens,numSpiders
	return None,None,None

>>> def barnYard1():
	heads=int(input('Number of heads:', ))
	legs=int(input('Number of legs:', ))
	pigs,chickens,spiders=solve1(numLegs,numHeads)
	if pigs==None:
		print('the number of heads(or legs)is not suitable')
	else:
		print('Number of piges=',pigs)
		print('Number of chickens=',chickens)
		print('Number of spiders=',spiders)

		
>>> barnYard1()
Number of heads:30
Number of legs:100
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    barnYard1()
  File "<pyshell#33>", line 4, in barnYard1
    pigs,chickens,spiders=solve1(numLegs,numHeads)
NameError: name 'numLegs' is not defined
>>> def barnYard1():
	heads=int(input('Number of heads:', ))
	legs=int(input('Number of legs:', ))
	pigs,chickens,spiders=solve1(legs,head)
	if pigs==None:
		print('the number of heads(or legs)is not suitable')
	else:
		print('Number of piges=',pigs)
		print('Number of chickens=',chickens)
		print('Number of spiders=',spiders)

		
>>> barnYard1()
Number of heads:30
Number of legs:100
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    barnYard1()
  File "<pyshell#36>", line 4, in barnYard1
    pigs,chickens,spiders=solve1(legs,head)
NameError: name 'head' is not defined
>>> def barnYard1():
	heads=int(input('Number of heads:', ))
	legs=int(input('Number of legs:', ))
	pigs,chickens,spiders=solve1(legs,heads)
	if pigs==None:
		print('the number of heads(or legs)is not suitable')
	else:
		print('Number of piges=',pigs)
		print('Number of chickens=',chickens)
		print('Number of spiders=',spiders)

		
>>> barnYard1()
Number of heads:30
Number of legs:100
Number of piges= 20
Number of chickens= 10
Number of spiders= 0
>>> barnYard1()
Number of heads:100
Number of legs:30
the number of heads(or legs)is not suitable
>>> barnYard1()
Number of heads:100
Number of legs:20
the number of heads(or legs)is not suitable
>>> barnYard1()
Number of heads:20
Number of legs:100
Number of piges= 15
Number of chickens= 0
Number of spiders= 5
>>> barnYard1()
Number of heads:1
Number of legs:100
the number of heads(or legs)is not suitable
>>> barnYard1()
Number of heads:-1
Number of legs:100
the number of heads(or legs)is not suitable
>>> def solve2(numLegs,numHeads):
	solutionFound=False
	for numSpiders in range(0,numHeads+1):
		for numChickens in range(0,numHeads-numSpiders+1):
			numPigs=numHeads-numChickens-numSpiders
			totLegs=4*numPigs+2*numChickens+8*numSpiders
			if totLegs==numLegs:
				print('Number of pigs=',numPigs)
				print('Number of Chickens=',numChickens)
				print('Number of Spiders=',numSpiders)
				solutionFound=True
	if not solutionFound:
		print('the number of heads(or legs)is not suitable')

		
>>> solve2(100,30)
Number of pigs= 20
Number of Chickens= 10
Number of Spiders= 0
Number of pigs= 17
Number of Chickens= 12
Number of Spiders= 1
Number of pigs= 14
Number of Chickens= 14
Number of Spiders= 2
Number of pigs= 11
Number of Chickens= 16
Number of Spiders= 3
Number of pigs= 8
Number of Chickens= 18
Number of Spiders= 4
Number of pigs= 5
Number of Chickens= 20
Number of Spiders= 5
Number of pigs= 2
Number of Chickens= 22
Number of Spiders= 6
>>> solve2(30,100)
the number of heads(or legs)is not suitable
>>> def Palindrome(s):
	if len(s)<=1:
		return True
	else:return s[0]==s[-1] and Palindrome(s[1])

	
>>> Palindrome()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    Palindrome()
TypeError: Palindrome() missing 1 required positional argument: 's'
>>> Palindrome(s)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    Palindrome(s)
NameError: name 's' is not defined
>>> Palindrome(1)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    Palindrome(1)
  File "<pyshell#67>", line 2, in Palindrome
    if len(s)<=1:
TypeError: object of type 'int' has no len()
>>> Palindrome('1')
True
>>> Palindrome('12346')
False
>>> Palindrome('a')
True
>>> Palindrome(a)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    Palindrome(a)
NameError: name 'a' is not defined
>>> Palindrome('ab')
False
>>> Palindrome('abcdef')
False
>>> Palindrome('abcdefa')
True
>>> def Palindrome(s):
	if len(s)<=1:
		return True
	else:return s[0]==s[-1] and Palindrome(s[1,-1])

	
>>> Palindrome('abcdefa')
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    Palindrome('abcdefa')
  File "<pyshell#79>", line 4, in Palindrome
    else:return s[0]==s[-1] and Palindrome(s[1,-1])
TypeError: string indices must be integers
>>> def Palindrome(s):
	if len(s)<=1:
		return True
	else:return s[0]==s[-1] and Palindrome(s[1:-1])

	
>>> Palindrome('abcdefa')
False
>>> Palindrome('abcdef')
False
>>> s[0]==s[-1] and Palindrome(s[1:-1])
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    s[0]==s[-1] and Palindrome(s[1:-1])
NameError: name 's' is not defined
>>> a='f'
>>> b='s'
>>> 1 and a
'f'
>>>  and a
SyntaxError: unexpected indent
>>> ''and a
''
>>> 'and a
SyntaxError: EOL while scanning string literal
>>> 1 and a or b
'f'
>>> a or b
'f'
>>> s='abcda'
>>> Palindrome(s[1:-1])
False
>>> s[0]
'a'
>>> s[-1]
'a'
>>> s[1:-1}
SyntaxError: invalid syntax
>>> s[1:-1]
'bcd'
>>> Palindrome(bcd)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    Palindrome(bcd)
NameError: name 'bcd' is not defined
>>> Palindrome('bcd')
False
>>> Palindrome('b')
True
>>> def Palindrome(s):
	if len(s)<=1:
		return True
	else:return s[0]==s[-1] and Palindrome(s[1:-1])

	
>>> Palindrome('aaaaa')
True
>>> Palindrome('aabaa')
True
>>> Palindrome('aabbaa')
True
>>> Palindrome('aabbbbbbaa')
True
>>> Palindrome('aabcaa')
False
>>> Palindrome('aabbcaa')
False
>>> Palindrome('aabbccaa')
False
>>> Palindrome('aabbdccaa')
False
>>> Palindrome('aabbbbbbbaa')
True
>>> Palindrome('aabbbvbbbaa')
True
>>> Palindrome('aabbbvvbbbaa')
True
>>> Palindrome('aabbbvdvbbbaa')
True
>>> 
