Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def sqrt(x):
	ans=0
	if x>=0:
	       while ans*ans<x:
		               ans=ans+1
	       if ans*ans !=x:
		       print (x,'is not a perfect aquare')
		       return None
	       else: return ans
        else:
		       print (x,'is a negative number')
		       
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> def sqrt(x):
	ans=0
	if x>=0:
	       while ans*ans<x:
		               ans=ans+1
	       if ans*ans !=x:
		       print (x,'is not a perfect aquare')
		       return None
	       else: return ans
else:
		       print (x,'is a negative number')
		       
SyntaxError: invalid syntax
>>> def sqrt(x):
	ans=0
	if x>=0:
	       while ans*ans<x:
		               ans=ans+1
	       if ans*ans !=x:
		       print (x,'is not a perfect aquare')
		       return None
	       else: return ans
         else:
		       print (x,'is a negative number')
		       
SyntaxError: unindent does not match any outer indentation level
>>> def sqrt(x):
	ans=0
	if x>=0:
	       while ans*ans<x:
		               ans=ans+1
	       if ans*ans !=x:
		       print (x,'is not a perfect aquare')
		       return None
	       else: return ans
	       else:
		       print (x,'is a negative number')
		       
SyntaxError: invalid syntax
>>> def sqrt(x):
	ans=0
	if x>=0:
	       while ans*ans<x:
		               ans=ans+1
	       if ans*ans !=x:
		       print (x,'is not a perfect aquare')
		       return None
	       else: return ans
	else:
		       print (x,'is a negative number')
		       return None

		
>>> x=16
>>> 
>>> def sqrt(x):
	ans=0
	if x>=0:
	       while ans*ans<x:
		               ans=ans+1
	       if ans*ans !=x:
		       print (x,'is not a perfect aquare')
		       return None
	       else: return ans
	else:
		       print (x,'is a negative number')
		       return None

		
>>> x
16
>>> sqrt(x)
4
>>> x=0
>>> sqrt(x)
0
>>> x
0
>>> x=-16
>>> sqrt(x)
-16 is a negative number
>>> x=14
>>> sqrt(x)
14 is not a perfect aquare
>>> 
>>> if x>=0:
	while ans*ans<x:
		ans=ans+1
		print (ans)
	if ans*ans !=x:
		       print (x,'is not a perfect aquare')
	else: print (ans)
else:
		       print (x,'is a negative number')

		       
Traceback (most recent call last):
  File "<pyshell#23>", line 2, in <module>
    while ans*ans<x:
NameError: name 'ans' is not defined
>>> ans=0
>>> if x>=0:
	while ans*ans<x:
		ans=ans+1
		print (ans)
	if ans*ans !=x:
		       print (x,'is not a perfect aquare')
	else: print (ans)
else:
		       print (x,'is a negative number')

		       
1
2
3
4
14 is not a perfect aquare
>>> ans=0
>>> if x>=0:
	while ans*ans<x:
		ans=ans+1
	if ans*ans !=x:
		       print (x,'is not a perfect aquare')
	else: print (ans)
else:
		       print (x,'is a negative number')

		       
14 is not a perfect aquare
>>> ans=0
>>> x=16
>>> if x>=0:
	while ans*ans<x:
		ans=ans+1
	if ans*ans !=x:
		       print (x,'is not a perfect aquare')
	else: print (ans)
else:
		       print (x,'is a negative number')

		       
4
>>> def sqrt(x):
	if x>=0:
		while ans*ans<x:
			ans=ans+1
		if ans*ans !=x:
			       print (x,'is not a perfect aquare')
		else: print (ans)
	else:
			       print (x,'is a negative number')

			       
>>> x=16
>>> sqrt(x)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    sqrt(x)
  File "<pyshell#36>", line 3, in sqrt
    while ans*ans<x:
UnboundLocalError: local variable 'ans' referenced before assignment
>>> ans=0
>>> sqrt(x)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    sqrt(x)
  File "<pyshell#36>", line 3, in sqrt
    while ans*ans<x:
UnboundLocalError: local variable 'ans' referenced before assignment
>>> def sqrt(x):
	ans=0
	if x>=0:
		while ans*ans<x:
			ans=ans+1
		if ans*ans !=x:
			       print (x,'is not a perfect aquare')
		else: print (ans)
	else:
			       print (x,'is a negative number')

			       
>>> sqrt(x)
4
>>> x=
SyntaxError: invalid syntax
>>> x
16
>>> ans
0
>>> def sqrt(x):
	ans=0
	if x>=0:
	       while ans*ans<x:
		               ans=ans+1
	       if ans*ans !=x:
		       print (x,'is not a perfect aquare')
		       return None
	       else: return ans
	else:
		       print (x,'is a negative number')
		       return None

		
>>> x=1
>>> y=2
>>> def add (x, y):
　　z = x + y
　　print z
print （add(x,y)）
SyntaxError: invalid character in identifier
>>> def add (x, y):
	z = x + y
　　print z
print （add(x,y)）
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(z)?
>>> def add (x, y):
	z = x + y
　　print (z)
print （add(x,y)）
SyntaxError: invalid character in identifier
>>> def add (x, y):
	z = x + y
	print (z)
print （add(x,y)）
SyntaxError: invalid syntax
>>> def add (x, y):
	z = x + y
	print (z)print （add(x,y)）
	
SyntaxError: invalid syntax
>>> def add (x, y):
	z = x + y
	print (z)
        print （add(x,y)）
        
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> def add (x, y):
	z = x + y
	print (z)     print （add(x,y)）
	
SyntaxError: invalid syntax
>>> def add (x, y):
	z = x + y
	print (z)     print （add(x,y)）
	
SyntaxError: invalid syntax
>>> def add (x, y):
	z = x + y
	print (z)     print （add(x,y)）
	
SyntaxError: invalid syntax
>>> def add (x, y):
	z = x + y
	print (z)     print （add(x,y)）def add (x, y):
		z = x + y
		print (z)
	               print （add(x,y)）
	               
SyntaxError: invalid syntax
>>> def add (x, y):
	z = x + y
	print (z)
                 print （add(x,y)）
                 
SyntaxError: unexpected indent
>>> def add (x, y):
	z = x + y
	print (z)
                     print （add(x,y)）
                     
SyntaxError: unexpected indent
>>> def add (x, y):
	z = x + y
	print (z)
        print （add(x,y)）
        
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> def add (x, y):
	z = x + y
	print (z)
                print （add(x,y)）
                
SyntaxError: unexpected indent
>>> def add (x, y):
	z = x + y
	print (z)
print （add(x,y)）
SyntaxError: invalid syntax
>>> def add (x, y):
	z = x + y
	print (z)

	
>>> add(x,y)
3
>>> print add
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(add)?
>>> 
>>> print (add)
<function add at 0x00000156ECBEC378>
>>> print(add(x,y))
3
None
>>> def app(x,y):
	z=x+y
	return z

>>> x=1
>>> y
2
>>> app(x,y)
3
>>> print(app(x,y))
3
>>> def add (x, y):
	z = x + y

	
>>> add(x,y)
>>> 
>>> print add(x,y)
SyntaxError: invalid syntax
>>> print (add(x,y))
None
>>> def sqrt(x):
	ans=0
	if x>=0:
	       while ans*ans<x:
		               ans=ans+1
	       if ans*ans !=x:
		       print (x,'is not a perfect aquare')
		       return None
	       else: return ans
	else:
		       print (x,'is a negative number')
		       return None

		
>>> None
>>> 
>>> print(None)
None
>>> 
>>> def f(x):
	x=x+1
	return x

>>> x=3
>>> f(x)
4
>>> x=
SyntaxError: invalid syntax
>>> x
3
>>> 
>>> def solve(numLegs,numHeads)"
SyntaxError: EOL while scanning string literal
>>> def solve(numLegs,numHeads):
	for numChicks in range(0,numHeads+1):
		numPigs=numHeas-numChicks
		totLegs=4*numPigs+numChicks*2
		if totLegs==numLegs:
			return numChicks,numPigs

		
>>> solve(20,5)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    solve(20,5)
  File "<pyshell#111>", line 3, in solve
    numPigs=numHeas-numChicks
NameError: name 'numHeas' is not defined
>>> numLegs=20
>>> numHeads=5
>>> solve(numLegs,numHeads)
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    solve(numLegs,numHeads)
  File "<pyshell#111>", line 3, in solve
    numPigs=numHeas-numChicks
NameError: name 'numHeas' is not defined
>>> solve(numLegs,numHeads)def solve(numLegs,numHeads):
	for numChicks in range(0,numHeads+1):
		numPigs=numHeas-numChicks
		totLegs=4*numPigs+numChicks*2
		if totLegs==numLegs:
			return numChicks,numPigs
		
SyntaxError: invalid syntax
>>> def solve(numLegs,numHeads):
	for numChicks in range(0,numHeads+1):
		numPigs=numHeas-numChicks
		totLegs=4*numPigs+numChicks*2
		if totLegs==numLegs:
			return numChicks,numPigs
	return None

>>> solve(numLegs,numHeads)
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    solve(numLegs,numHeads)
  File "<pyshell#119>", line 3, in solve
    numPigs=numHeas-numChicks
NameError: name 'numHeas' is not defined
>>> def solve(numLegs,numHeads):
	for numChicks in range(0,numHeads+1):
		numPigs=numHeads-numChicks
		totLegs=4*numPigs+numChicks*2
		if totLegs==numLegs:
			return numChicks,numPigs
	return None

>>> solve (numLegs,numHeads)
(0, 5)
>>> numLegs=100
>>> numHeads=30
>>> solve (numLegs,numHeads)
(10, 20)
>>> numLegs=200
>>> solve (numLegs,numHeads)
>>> def solve(numLegs,numHeads):
	for numChicks in range(0,numHeads+1):
		numPigs=numHeads-numChicks
		totLegs=4*numPigs+numChicks*2
		if totLegs==numLegs:
			return numChicks,numPigs
	return None
print ('wrong')
SyntaxError: invalid syntax
>>> def solve(numLegs,numHeads):
	for numChicks in range(0,numHeads+1):
		numPigs=numHeads-numChicks
		totLegs=4*numPigs+numChicks*2
		if totLegs==numLegs:
			return numChicks,numPigs
	return None
        print ('wrong')
        
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> def solve(numLegs,numHeads):
	for numChicks in range(0,numHeads+1):
		numPigs=numHeads-numChicks
		totLegs=4*numPigs+numChicks*2
		if totLegs==numLegs:
			return numChicks,numPigs
	return None
         print ('wrong')
         
SyntaxError: unexpected indent
>>> def solve(numLegs,numHeads):
	for numChicks in range(0,numHeads+1):
		numPigs=numHeads-numChicks
		totLegs=4*numPigs+numChicks*2
		if totLegs==numLegs:
			return numChicks,numPigs
	return None
                 print ('wrong')
                 
SyntaxError: unexpected indent
>>> def solve(numLegs,numHeads):
	for numChicks in range(0,numHeads+1):
		numPigs=numHeads-numChicks
		totLegs=4*numPigs+numChicks*2
		if totLegs==numLegs:
			return numChicks,numPigs
	return None
      print ('wrong')
      
SyntaxError: unindent does not match any outer indentation level
>>> def solve(numLegs,numHeads):
	for numChicks in range(0,numHeads+1):
		numPigs=numHeads-numChicks
		totLegs=4*numPigs+numChicks*2
		if totLegs==numLegs:
			return numChicks,numPigs
	        else:
			
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> def solve(numLegs,numHeads):
	for numChicks in range(0,numHeads+1):
		numPigs=numHeads-numChicks
		totLegs=4*numPigs+numChicks*2
		if totLegs==numLegs:
			return numChicks,numPigs
	print('wrong')
	return None

>>> solve (numLegs,numHeads)
wrong
>>> numLegs
200
>>> numHeads
30
>>> numLegs=102
>>> solve (numLegs,numHeads)
(9, 21)
>>> def solve(numLegs,numHeads):
	for numChicks in range(0,numHeads+1):
		numPigs=numHeads-numChicks
		totLegs=4*numPigs+numChicks*2
		if totLegs==numLegs:
			print (numChicks,numPigs)
	print('wrong')
	return None

>>> solve (numLegs,numHeads)
9 21
wrong
>>> 
