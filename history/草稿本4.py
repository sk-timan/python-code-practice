Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def Palindrome(s):
	if len(s)<=1:
		return True
	else:return s[0]==s[-1] and Palindrome(s[1,-1])

	
>>> Palindrome('aaabbbecccddd)
	       
SyntaxError: EOL while scanning string literal
>>> Palindrome('aaabbbecccddd')
	       
False
>>> Palindrome('abcdefedcba')
	       
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    Palindrome('abcdefedcba')
  File "<pyshell#1>", line 4, in Palindrome
    else:return s[0]==s[-1] and Palindrome(s[1,-1])
TypeError: string indices must be integers
>>> def Palindrome(s):
	if len(s)<=1:
		return True
	else:return s[0]==s[-1] and Palindrome(s[1:-1])

	       
>>> Palindrome('abcdefedcba')
	       
True
>>> Palindrome('')
	       
True
>>> Palindrome()
	       
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    Palindrome()
TypeError: Palindrome() missing 1 required positional argument: 's'
>>> Palindrome('1')
	       
True
>>> Palindrome('11211')
	       
True
>>> Palindrome('11212')
	       
False
>>> def Palindrome1(s,indent):
	       print(indent,'haha',s)
	       if len(s)<=1：
	       
SyntaxError: invalid character in identifier
>>> def Palindrome1(s,indent):
	       print(indent,'haha',s)
	       if len(s)<=1:
	       print(indent,'aha')
	       
SyntaxError: expected an indented block
>>> def Palindrome1(s,indent):
	       print(indent, 'haha',s)
	       if len(s)<=1:
	       print(indent, 'aha')
	       
SyntaxError: expected an indented block
>>> def Palindrome1(s,indent):
	       print(indent, 'haha',s)
	       if len(s)<=1:
	       return True
	       print(indent, 'aha')
	       
SyntaxError: expected an indented block
>>> def Palindrome1(s,indent):
	       print(indent, 'haha',s)
	       if len(s)<=1:
		       return True
		       print(indent, 'aha')

	       
>>> def Palindrome1(s,indent):
	       print(indent, 'haha',s)
	       if len(s)<=1:
		       print(indent, 'aha')
		       return True
	       else:
		       ans=s[0]==s[-1]and Palindrome1(s[1:-1],indent+indent)
		       print(indent,'ahaha',ans)
		       return ans

	       
>>> Palindrome('aabb11c11bbaa',indent)
	       
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    Palindrome('aabb11c11bbaa',indent)
NameError: name 'indent' is not defined
>>> Palindrome('aabb11c11bbaa',  )
	       
True
>>> Palindrome1('aabb11c11bbaa', )
	       
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    Palindrome1('aabb11c11bbaa', )
TypeError: Palindrome1() missing 1 required positional argument: 'indent'
>>> Palindrome1('aabb11c11bbaa',indent)
	       
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    Palindrome1('aabb11c11bbaa',indent)
NameError: name 'indent' is not defined
>>> Palindrome1('aabb11c11bbaa',	)
	       
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    Palindrome1('aabb11c11bbaa',	)
TypeError: Palindrome1() missing 1 required positional argument: 'indent'
>>> Palindrome1('aabb11c11bbaa','a')
	       
a haha aabb11c11bbaa
aa haha abb11c11bba
aaaa haha bb11c11bb
aaaaaaaa haha b11c11b
aaaaaaaaaaaaaaaa haha 11c11
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa haha 1c1
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa haha c
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa aha
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa ahaha True
aaaaaaaaaaaaaaaa ahaha True
aaaaaaaa ahaha True
aaaa ahaha True
aa ahaha True
a ahaha True
True
>>> Palindrome1('aabb11c11bbaa','')
	       
 haha aabb11c11bbaa
 haha abb11c11bba
 haha bb11c11bb
 haha b11c11b
 haha 11c11
 haha 1c1
 haha c
 aha
 ahaha True
 ahaha True
 ahaha True
 ahaha True
 ahaha True
 ahaha True
True
>>> Palindrome1('aabb11c11bbaa','    ')
	       
     haha aabb11c11bbaa
         haha abb11c11bba
                 haha bb11c11bb
                                 haha b11c11b
                                                                 haha 11c11
                                                                                                                                 haha 1c1
                                                                                                                                                                                                                                                                 haha c
                                                                                                                                                                                                                                                                 aha
                                                                                                                                 ahaha True
                                                                 ahaha True
                                 ahaha True
                 ahaha True
         ahaha True
     ahaha True
True
>>> Palindrome1('aabb11c11bbaa',' ')
	       
  haha aabb11c11bbaa
   haha abb11c11bba
     haha bb11c11bb
         haha b11c11b
                 haha 11c11
                                 haha 1c1
                                                                 haha c
                                                                 aha
                                 ahaha True
                 ahaha True
         ahaha True
     ahaha True
   ahaha True
  ahaha True
True
>>> def Palindrome1(s,indent):
	       print(indent, 'First scan',s)
	       if len(s)<=1:
		       print(indent, 'Secend scan')
		       return True
	       else:
		       ans=s[0]==s[-1]and Palindrome1(s[1:-1],indent+indent)
		       print(indent,'Third',ans)
		       return ans

	       
>>> Palindrome1('aabb11c11bbaa',' ')
	       
  First scan aabb11c11bbaa
   First scan abb11c11bba
     First scan bb11c11bb
         First scan b11c11b
                 First scan 11c11
                                 First scan 1c1
                                                                 First scan c
                                                                 Secend scan
                                 Third True
                 Third True
         Third True
     Third True
   Third True
  Third True
True
>>> def Palindrome1(s,indent):
	       print(indent, 'First scan',s)
	       if len(s)<=1:
		       print(indent, 'Secend scan')
		       return True
	       else:
		       ans=s[0]==s[-1]and Palindrome1(s[1:-1],indent+indent)
		       print(indent,'Come back',ans)
		       return ans

	       
>>> Palindrome1('aabb11c11bbaa',' ')
	       
  First scan aabb11c11bbaa
   First scan abb11c11bba
     First scan bb11c11bb
         First scan b11c11b
                 First scan 11c11
                                 First scan 1c1
                                                                 First scan c
                                                                 Secend scan
                                 Come back True
                 Come back True
         Come back True
     Come back True
   Come back True
  Come back True
True
>>> Palindrome1('aabb11c12bbaa',' ')
	       
  First scan aabb11c12bbaa
   First scan abb11c12bba
     First scan bb11c12bb
         First scan b11c12b
                 First scan 11c12
                 Come back False
         Come back False
     Come back False
   Come back False
  Come back False
False
>>> def fib(x):
	       if x==0 or x==1:
	       return 1
	       
SyntaxError: expected an indented block
>>> def fib(x):
	       if x==0 or x==1:
		       return 1
	       else:
		       return fib(x-1)+fib(x-2)

	       
>>> fib(0)
	       
1
>>> fib(1)
	       
1
>>> fib(2)
	       
2
>>> fib(3)
	       
3
>>> fib(4)
	       
5
>>> fib(5)
	       
8
>>> def fib(x,indent):
	       print(indent,'First scan',x)
	       if x==0 or x==1:
		       print(indent,'Second scan')
		       return 1
	       else:
		       ans=fib(x-1)+fib(x-2)
		       print('Third scan',ans)
		       return ans

	       
>>> fib(0,' ')
	       
  First scan 0
  Second scan
1
>>> fib(1,' ')
	       
  First scan 1
  Second scan
1
>>> fib(2,' ')
	       
  First scan 2
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    fib(2,' ')
  File "<pyshell#59>", line 7, in fib
    ans=fib(x-1)+fib(x-2)
TypeError: fib() missing 1 required positional argument: 'indent'
>>> fib(2,'1')
	       
1 First scan 2
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    fib(2,'1')
  File "<pyshell#59>", line 7, in fib
    ans=fib(x-1)+fib(x-2)
TypeError: fib() missing 1 required positional argument: 'indent'
>>> def fib(x,indent):
	       print(indent,'First scan',x)
	       if x==0 or x==1:
		       print(indent,'Second scan')
		       return 1
	       else:
		       ans=fib(x-1,indent)+fib(x-2,indent)
		       print('Third scan',ans)
		       return ans

	       
>>> fib(2,' ')
	       
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
2
>>> fib(3,' ')
	       
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
3
>>> fib(12,' ')
	       
  First scan 12
  First scan 11
  First scan 10
  First scan 9
  First scan 8
  First scan 7
  First scan 6
  First scan 5
  First scan 4
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
Third scan 5
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
Third scan 8
  First scan 4
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
Third scan 5
Third scan 13
  First scan 5
  First scan 4
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
Third scan 5
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
Third scan 8
Third scan 21
  First scan 6
  First scan 5
  First scan 4
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
Third scan 5
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
Third scan 8
  First scan 4
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
Third scan 5
Third scan 13
Third scan 34
  First scan 7
  First scan 6
  First scan 5
  First scan 4
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
Third scan 5
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
Third scan 8
  First scan 4
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
Third scan 5
Third scan 13
  First scan 5
  First scan 4
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
Third scan 5
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
Third scan 8
Third scan 21
Third scan 55
  First scan 8
  First scan 7
  First scan 6
  First scan 5
  First scan 4
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
Third scan 5
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
Third scan 8
  First scan 4
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
Third scan 5
Third scan 13
  First scan 5
  First scan 4
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
Third scan 5
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
Third scan 8
Third scan 21
  First scan 6
  First scan 5
  First scan 4
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
Third scan 5
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
Third scan 8
  First scan 4
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
Third scan 5
Third scan 13
Third scan 34
Third scan 89
  First scan 9
  First scan 8
  First scan 7
  First scan 6
  First scan 5
  First scan 4
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
Third scan 5
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
Third scan 8
  First scan 4
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
Third scan 5
Third scan 13
  First scan 5
  First scan 4
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
Third scan 5
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
Third scan 8
Third scan 21
  First scan 6
  First scan 5
  First scan 4
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
Third scan 5
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
Third scan 8
  First scan 4
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
Third scan 5
Third scan 13
Third scan 34
  First scan 7
  First scan 6
  First scan 5
  First scan 4
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
Third scan 5
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
Third scan 8
  First scan 4
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
Third scan 5
Third scan 13
  First scan 5
  First scan 4
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
Third scan 5
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
Third scan 8
Third scan 21
Third scan 55
Third scan 144
  First scan 10
  First scan 9
  First scan 8
  First scan 7
  First scan 6
  First scan 5
  First scan 4
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
Third scan 5
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
Third scan 8
  First scan 4
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
Third scan 5
Third scan 13
  First scan 5
  First scan 4
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
Third scan 5
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
Third scan 8
Third scan 21
  First scan 6
  First scan 5
  First scan 4
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
Third scan 5
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
Third scan 8
  First scan 4
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
Third scan 5
Third scan 13
Third scan 34
  First scan 7
  First scan 6
  First scan 5
  First scan 4
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
Third scan 5
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
Third scan 8
  First scan 4
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
Third scan 5
Third scan 13
  First scan 5
  First scan 4
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
Third scan 5
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
Third scan 8
Third scan 21
Third scan 55
  First scan 8
  First scan 7
  First scan 6
  First scan 5
  First scan 4
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
Third scan 5
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
Third scan 8
  First scan 4
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
Third scan 5
Third scan 13
  First scan 5
  First scan 4
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
Third scan 5
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
Third scan 8
Third scan 21
  First scan 6
  First scan 5
  First scan 4
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
Third scan 5
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
Third scan 8
  First scan 4
  First scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
  First scan 1
  Second scan
Third scan 3
  First scan 2
  First scan 1
  Second scan
  First scan 0
  Second scan
Third scan 2
Third scan 5
Third scan 13
Third scan 34
Third scan 89
Third scan 233
233
>>> 
