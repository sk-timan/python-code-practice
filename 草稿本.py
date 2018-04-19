Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x=3 # Creat x and assign value 3 to it
x=x*x # Bind x to value 9
print x
n=raw_input('Enter a number: ')
print n # print n/n
SyntaxError: multiple statements found while compiling a single statement
>>> multiple statements found while compiling a single statement
SyntaxError: invalid syntax
>>> x=3 # Creat x and assign value 3 to it 
x=x*x # Bind x to value 9
print x
n=raw_input('Enter a number: ')
print n # print n/n
SyntaxError: multiple statements found while compiling a single statement
>>> x=3
x=x*x # Bind x to value 9
print x
n=raw_input('Enter a number: ')
print n # print n/n
SyntaxError: multiple statements found while compiling a single statement
>>> x=3 # Creat x and assign value 3 to it
>>> x=x*x # Bind x to value 9
print x
n=raw_input('Enter a number: ')
print n # print n/n
SyntaxError: multiple statements found while compiling a single statement
>>> x=x*x # Bind x to value 9
>>> print x
n=raw_input('Enter a number: ')
print n # print n/n
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x)?
>>> print x
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x)?
>>> print （x)
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(（x))?
>>> Missing parentheses in call to 'print'
SyntaxError: invalid syntax
>>> print x
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x)?
>>> print (x)
9
>>> n=raw_input('Enter a number: ')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    n=raw_input('Enter a number: ')
NameError: name 'raw_input' is not defined
>>> n=raw_input('Enter a number: ')
print n # print n/n
SyntaxError: multiple statements found while compiling a single statement
>>> name = raw_input("What is your name? ")
print "Hello, %s." % name
SyntaxError: multiple statements found while compiling a single statement
>>> name = raw_input("What is your name? ")
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    name = raw_input("What is your name? ")
NameError: name 'raw_input' is not defined
>>> n=raw_input('Enter a number: ')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    n=raw_input('Enter a number: ')
NameError: name 'raw_input' is not defined
>>> Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    n=raw_input('Enter a number: ')
NameError: name 'raw_input' is not defined
SyntaxError: invalid syntax
>>> n=raw_input('Enter a number: ')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    n=raw_input('Enter a number: ')
NameError: name 'raw_input' is not defined
>>> print (n)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print (n)
NameError: name 'n' is not defined
>>> n=raw_input('Enter a number:1 ')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    n=raw_input('Enter a number:1 ')
NameError: name 'raw_input' is not defined
>>> Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    n=raw_input('Enter a number: ')
NameError: name 'raw_input' is not defined
SyntaxError: invalid syntax
>>> n=(raw_input('Enter a number: '))
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    n=(raw_input('Enter a number: '))
NameError: name 'raw_input' is not defined
>>> n=(raw_input('Enter a number: '))
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    n=(raw_input('Enter a number: '))
NameError: name 'raw_input' is not defined
>>> n=raw_input(2)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    n=raw_input(2)
NameError: name 'raw_input' is not defined
>>> n=input ('Enter a number: ')
Enter a number: 3
>>> print n
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(n)?
>>> print(n)
3
>>> #123456
>>> n=raw_input
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    n=raw_input
NameError: name 'raw_input' is not defined
>>> n=input('Enter a number: ')
print n
SyntaxError: multiple statements found while compiling a single statement
>>> n=input('Enter a number: ')
Enter a number: 123
>>> print n
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(n)?
>>> print (n)
123
>>> x=15
>>> if(x/2)*2==x:
   print 'even'
else: 
   print 'odd'

SyntaxError: Missing parentheses in call to 'print'. Did you mean print('even')?
>>> if(x/2)*2==x:
   print (even')
else: 
   print ('odd')

SyntaxError: EOL while scanning string literal
>>> if(x/2)*2==x:
   print ('even')
else: 
   print ('odd')

	  
even
>>> x=8
	  
>>> 
	  
>>> z='b'
	  
>>> z=b
	  
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    z=b
NameError: name 'b' is not defined
>>> z='b'
	  
>>> if 'x'<z:
   print 'Hellow'
   print 'Mom'
	  
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('Hellow')?
>>> if 'x'<z:
   print ('Hellow')
   print ('Mom')

	  
>>> 
	  
>>> if 'x'<z:
   print 'Hellow'print 'Mom'
	  
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('Hellow'print 'Mom')?
>>> if 'x'<z:
   print 'Hellow'
print 'Mom'
	  
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('Hellow')?
>>> if 'x'<z:
   print ('Hellow')	
print ('Mom')
	  
SyntaxError: invalid syntax
>>> if 'x'<z:
   print ('Hellow')	
else print ('Mom')
	  
SyntaxError: invalid syntax
>>> invalid syntax
	  
SyntaxError: invalid syntax
>>> if 'x'<z:
   print ('Hellow')	
print ('Mom')
	  
SyntaxError: invalid syntax
>>> if 'x'<z:
   print ('Hellow')	

   
>>> 
	  
>>> print (z)
	  
b
>>> if 'x'<z:
         print ('Hellow')	
 print ('Mom')
	  
SyntaxError: unindent does not match any outer indentation level
>>> if 'x'<z:
   print ('Hellow')	
print ('Mom')
	  
SyntaxError: invalid syntax
>>> if 'x'<z:
        print ('Hellow')	
print ('Mom')
	  
SyntaxError: invalid syntax
>>> if 'x'<z:
   print ('Hellow')	
       print ('Mom')
	  
SyntaxError: unexpected indent
>>> if 'x'<z:

        print ('Hellow')	
    print ('Mom')
	  
SyntaxError: unindent does not match any outer indentation level
>>> print('mon")
	  
SyntaxError: EOL while scanning string literal
>>> print (123)
	  
123
>>> print ('123')
	  
123
>>> print('Mom')
	  
Mom
>>> if 'x'<z:
	  print ('dad')

	  
>>> if 'x'<z:
	  print ('dad')
print ('mom')
	  
SyntaxError: invalid syntax
>>> EOL while scanning string literalif 'x'<z:
	  print ('dad')
	  
SyntaxError: invalid syntax
>>> 
	  
>>> if 'x'<z:
	  print ('dad')
	print ('mom')
	  
SyntaxError: unindent does not match any outer indentation level
>>> x=15
y=5
z=11
print (x,y,z)
	  
SyntaxError: multiple statements found while compiling a single statement
>>> x=15
	  
>>> y=5
	  
>>> z=11
	  
>>> print (x,y,z)
	  
15 5 11
>>> if  x<y and x<z:
	  print ('y is least')
	elif y<z:
	  
SyntaxError: unindent does not match any outer indentation level
>>> if  x<y and x<z:
	  print ('x is least')
elif y<z:
	  print ('y is least')
	  else print ('z is least')
	  
SyntaxError: invalid syntax
>>> if  x<y and x<z:
	  print ('x is least')
elif y<z:
	  print ('y is least')
	  else:print ('z is least')
	  
SyntaxError: invalid syntax
>>> if  x<y and x<z:
	  print ('x is least')
elif y<z:
	  print ('y is least')
	else:print ('z is least')
	  
SyntaxError: unindent does not match any outer indentation level
>>> if  x<y and x<z:
	  print ('x is least')
elif y<z:
	  print ('y is least')
else:print ('z is least')

	  
y is least
>>> y=17
	  
>>> if  x<y and x<z:
	  print ('x is least')
elif y<z:
	  print ('y is least')
else:print ('z is least')

	  
z is least
>>> y=0
	  
>>> x=3
	  
>>> mon=x
	  
>>> while mon>0:
	  y=y+x
	  mon=mon-1
print (y)
	  
SyntaxError: invalid syntax
>>> while mon>0:
	  y=y+x
	  mon=mon-1
	  print (y)

	  
3
6
9
>>> while mon>0:
	  y=y+x
	  mon=mon-1
	print (y)
	  
SyntaxError: unindent does not match any outer indentation level
>>> while mon>0:
	  y=y+x
	  mon=mon-1
print (y)
	  
SyntaxError: invalid syntax
>>> while mon>0:
	  y=y+x
	  mon=mon-1
	  y=y
	print (y)
	  
SyntaxError: unindent does not match any outer indentation level
>>> while mon>0:
	  y=y+x
	  mon=mon-1
	  y=y
	  print (y)

	  
>>> 
	  
>>> 
	  
>>> y=0
	  
>>> while mon>0:
	  y=y+x
	  mon=mon-1
	  y=y
	  print (y)

	  
>>> y=0
	  
>>> while mon>0:
	  y=y+x
	  mon=mon-1
	  print (y)

	  
>>> 
	  
>>> y=0
	  
>>> x=3
	  
>>> mon=x
	  
>>> while mon>0:
	  y=y+x
	  mon=mon-1
	  y=y
	  print (y)

	  
3
6
9
>>> while mon>0:
	  y=y+x
	  mon=mon-1
	
	  print (y)

	  
>>> 
	  
>>> while mon>0:
	  y=y+x
	  mon=mon-1
	  print (y)

	  
>>> 	  
>>> y=0
	  
>>> x=3
	  
>>> mon=x
	  
SyntaxError: invalid syntax
>>> y=0

x=3

mon=x
	  
SyntaxError: multiple statements found while compiling a single statement
>>> y=0
	  
>>> x=3
	  
>>> mon=x
	  
>>> while mon>0:
	  y=y+x
	  mon=mon-1
	a=y
	  
SyntaxError: unindent does not match any outer indentation level
>>> while mon>0:
	  y=y+x
	  mon=mon-1
a=y
	  
SyntaxError: invalid syntax
>>> while mon>0:
	  y=y+x
	  mon=mon-1
print (y)
	  
SyntaxError: invalid syntax
>>> 
