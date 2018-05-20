Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def squareRootBi(x,epsilon):
	assert x>=0,'x must be non-negative,not'+str(x)
	assert epsilon>0,'epsilon must be positive,not'+str(epsilon)
	low=0
	high=x
	guess=(low+high)/2
	ctr=1
	while abs(guess**2-x)>epsilon and ctr<=100:
		if guess**2<x:
			low=guess
		else:
			high=guess
		guess=(low+high)/2
		ctr+=1
	assert ctr<=100,'Iteration count exceeded'
	print 'Bimethod.Num.interations:',ctr,'Estimate:',guess
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('Bimethod.Num.interations:',ctr,'Estimate:',guess)?
>>> def squareRootBi(x,epsilon):
	assert x>=0,'x must be non-negative,not'+str(x)
	assert epsilon>0,'epsilon must be positive,not'+str(epsilon)
	low=0
	high=x
	guess=(low+high)/2
	ctr=1
	while abs(guess**2-x)>epsilon and ctr<=100:
		if guess**2<x:
			low=guess
		else:
			high=guess
		guess=(low+high)/2
		ctr+=1
	assert ctr<=100,'Iteration count exceeded'
	print ('Bimethod.Num.interations:',ctr,'Estimate:',guess)
	return guess

>>> squareRootBi(10,0.0001)
Bimethod.Num.interations: 18 Estimate: 3.1622695922851562
3.1622695922851562
>>> squareRootBi(10,0.00001)
Bimethod.Num.interations: 20 Estimate: 3.1622791290283203
3.1622791290283203
>>> squareRootBi(10,0.0000000000001)
Bimethod.Num.interations: 46 Estimate: 3.162277660168371
3.162277660168371
>>> squareRootBi(10,0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    squareRootBi(10,0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)
  File "<pyshell#16>", line 15, in squareRootBi
    assert ctr<=100,'Iteration count exceeded'
AssertionError: Iteration count exceeded
>>> def squareRootBi(x,epsilon):
	assert x>=0,'x must be non-negative,not'+str(x)
	assert epsilon>0,'epsilon must be positive,not'+str(epsilon)
	low=0
	high=x
	guess=(low+high)/2
	ctr=1
	while abs(guess**2-x)>epsilon
		if guess**2<x:
			low=guess
		else:
			high=guess
		guess=(low+high)/2
		ctr+=1
	print ('Bimethod.Num.interations:',ctr,'Estimate:',guess)
	return guess
SyntaxError: invalid syntax
>>> def squareRootBi(x,epsilon):
	assert x>=0,'x must be non-negative,not'+str(x)
	assert epsilon>0,'epsilon must be positive,not'+str(epsilon)
	low=0
	high=x
	guess=(low+high)/2
	ctr=1
	while abs(guess**2-x)>epsilon:
		if guess**2<x:
			low=guess
		else:
			high=guess
		guess=(low+high)/2
		ctr+=1
	print ('Bimethod.Num.interations:',ctr,'Estimate:',guess)
	return guess

>>> squareRootBi(10,0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)

=============================== RESTART: Shell ===============================
>>> def squareRootBi(x,epsilon):
	assert x>=0,'x must be non-negative,not'+str(x)
	assert epsilon>0,'epsilon must be positive,not'+str(epsilon)
	low=0
	high=x
	guess=(low+high)/2
	ctr=1
	while abs(guess**2-x)>epsilon:
		if guess**2<x:
			low=guess
		else:
			high=guess
		guess=(low+high)/2
		ctr+=1
	print ('Bimethod.Num.interations:',ctr,'Estimate:',guess)
	return guess

>>> squareRootBi(10,0.000001)
Bimethod.Num.interations: 25 Estimate: 3.162277638912201
3.162277638912201
>>> squareRootBi(10,0.00000000000000000000000000000000000000001)

=============================== RESTART: Shell ===============================
>>> def squareRootBi(x,epsilon):
	assert x>=0,'x must be non-negative,not'+str(x)
	assert epsilon>0,'epsilon must be positive,not'+str(epsilon)
	low=0
	high=x
	guess=(low+high)/2
	ctr=1
	while abs(guess**2-x)>epsilon and ctr<=100:
		if guess**2<x:
			low=guess
		else:
			high=guess
		guess=(low+high)/2
		ctr+=1
	assert ctr<=100,'Iteration count exceeded'
	print ('Bimethod.Num.interations:',ctr,'Estimate:',guess)
	return guess

>>> squareRootBi(10,0.00000000000000000000000000000000000000001)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    squareRootBi(10,0.00000000000000000000000000000000000000001)
  File "<pyshell#29>", line 15, in squareRootBi
    assert ctr<=100,'Iteration count exceeded'
AssertionError: Iteration count exceeded
>>> def squareRootBi(x,epsilon):
	assert x>=0,'x must be non-negative,not'+str(x)
	assert epsilon>0,'epsilon must be positive,not'+str(epsilon)
	low=0
	high=x
	guess=(low+high)/2
	ctr=1
	while abs(guess**2-x)>epsilon:
		if guess**2<x:
			low=guess
		else:
			high=guess
		guess=(low+high)/2
		ctr+=1
	print ('Bimethod.Num.interations:',ctr,'Estimate:',guess)
	return guess

>>> squareRootBi(10,0.000000001)
Bimethod.Num.interations: 35 Estimate: 3.162277660157997
3.162277660157997
>>> squareRootBi(10,0.000000000001)
Bimethod.Num.interations: 43 Estimate: 3.162277660168229
3.162277660168229
>>> squareRootBi(10,0.000000000000001)

=============================== RESTART: Shell ===============================
>>> squareRootBi(10,0.000000000001)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    squareRootBi(10,0.000000000001)
NameError: name 'squareRootBi' is not defined
>>> def squareRootBi(x,epsilon):
	assert x>=0,'x must be non-negative,not'+str(x)
	assert epsilon>0,'epsilon must be positive,not'+str(epsilon)
	low=0
	high=x
	guess=(low+high)/2
	ctr=1
	while abs(guess**2-x)>epsilon:
		if guess**2<x:
			low=guess
		else:
			high=guess
		guess=(low+high)/2
		ctr+=1
	print ('Bimethod.Num.interations:',ctr,'Estimate:',guess)
	return guess

>>> squareRootBi(10,0.000000000001)
Bimethod.Num.interations: 43 Estimate: 3.162277660168229
3.162277660168229
>>> squareRootBi(10,0.0000000000001)
Bimethod.Num.interations: 46 Estimate: 3.162277660168371
3.162277660168371
>>> squareRootBi(10,0.00000000000001)
Bimethod.Num.interations: 50 Estimate: 3.16227766016838
3.16227766016838
>>> squareRootBi(10,0.00000000000001)
Bimethod.Num.interations: 50 Estimate: 3.16227766016838
3.16227766016838
>>> squareRootBi(10,0.000000000000001)

=============================== RESTART: Shell ===============================
>>> def squareRootBi(x,epsilon):
	assert x>=0,'x must be non-negative,not'+str(x)
	assert epsilon>0,'epsilon must be positive,not'+str(epsilon)
	low=0
	high=x
	guess=(low+high)/2
	ctr=1
	while abs(guess**2-x)>epsilon:
		if guess**2<x:
			low=guess
		else:
			high=guess
		guess=(low+high)/2
		ctr+=1
	print ('Bimethod.Num.interations:',ctr,'Estimate:',guess)
	return guess

>>> squareRootBi(10,0.000000000000001)

=============================== RESTART: Shell ===============================
>>> def squareRootBi(x,epsilon):
	assert x>=0,'x must be non-negative,not'+str(x)
	assert epsilon>0,'epsilon must be positive,not'+str(epsilon)
	low=0
	high=x
	guess=(low+high)/2
	ctr=1
	while abs(guess**2-x)>epsilon and ctr<=100:
		if guess**2<x:
			low=guess
		else:
			high=guess
		guess=(low+high)/2
		ctr+=1
	assert ctr<=100,'Iteration count exceeded'
	print ('Bimethod.Num.interations:',ctr,'Estimate:',guess)
	return guess

>>> x=float(x)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    x=float(x)
NameError: name 'x' is not defined
>>> float(1.21)
1.21
>>> float(1)
1.0
>>> def aquareRootNR(x,epsilon):
	assert x>=0,'x must be non-negative,not'+str(x)
	assert epsilon>0,'epsion must be positive,not'+str(epsilon)
	x=float(x)
	guess=0.001
	diff=guess**2-x
	ctr=1
	while abs(diff)>epsilon and ctr<=100:
		guess=guess-diff/(2*guess)
		diff=guess*2-x
		ctr+=1
	assert ctr<=100,'Iteration count exceeded'
	print ('NR method.   Num. iterations:',ctr,'Estimate:',guess)
	return guess

>>> aquarRootNR(16,0.001)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    aquarRootNR(16,0.001)
NameError: name 'aquarRootNR' is not defined
>>> aquareRootNR(16,0.001)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    aquareRootNR(16,0.001)
  File "<pyshell#66>", line 12, in aquareRootNR
    assert ctr<=100,'Iteration count exceeded'
AssertionError: Iteration count exceeded
>>> aquareRootNR(16,0.01)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    aquareRootNR(16,0.01)
  File "<pyshell#66>", line 12, in aquareRootNR
    assert ctr<=100,'Iteration count exceeded'
AssertionError: Iteration count exceeded
>>> def aquareRootNR(x,epsilon):
	assert x>=0,'x must be non-negative,not'+str(x)
	assert epsilon>0,'epsion must be positive,not'+str(epsilon)
	x=float(x)
	guess=x/2.0
	guess=0.001
	diff=guess**2-x
	ctr=1
	while abs(diff)>epsilon and ctr<=100:
		guess=guess-diff/(2*guess)
		diff=guess*2-x
		ctr+=1
	assert ctr<=100,'Iteration count exceeded'
	print ('NR method.   Num. iterations:',ctr,'Estimate:',guess)
	return guess

>>> aquareRootNR(16,0.001)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    aquareRootNR(16,0.001)
  File "<pyshell#71>", line 13, in aquareRootNR
    assert ctr<=100,'Iteration count exceeded'
AssertionError: Iteration count exceeded
>>> def aquareRootNR(x,epsilon):
	assert x>=0,'x must be non-negative,not'+str(x)
	assert epsilon>0,'epsion must be positive,not'+str(epsilon)
	x=float(x)
	guess=x/2.0
	diff=guess**2-x
	ctr=1
	while abs(diff)>epsilon and ctr<=100:
		guess=guess-diff/(2*guess)
		diff=guess*2-x
		ctr+=1
	assert ctr<=100,'Iteration count exceeded'
	print ('NR method.   Num. iterations:',ctr,'Estimate:',guess)
	return guess

>>> aquareRootNR(16,0.001)
NR method.   Num. iterations: 64 Estimate: 7.999508498758601
7.999508498758601
>>> def aquareRootNR(x,epsilon):
	assert x>=0,'x must be non-negative,not'+str(x)
	assert epsilon>0,'epsion must be positive,not'+str(epsilon)
	x=float(x)
	guess=0.001
	diff=guess**2-x
	ctr=1
	while abs(diff)>epsilon and ctr<=100:
		guess=guess-diff/(2*guess)
		diff=guess*2-x
		ctr+=1
	assert ctr<=100,'Iteration count exceeded'
	print ('NR method.   Num. iterations:',ctr,'Estimate:',guess)
	return guess

>>> aquareRootNR(16,0.001)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    aquareRootNR(16,0.001)
  File "<pyshell#77>", line 12, in aquareRootNR
    assert ctr<=100,'Iteration count exceeded'
AssertionError: Iteration count exceeded
>>> aquareRootNR(16,0.0001)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    aquareRootNR(16,0.0001)
  File "<pyshell#77>", line 12, in aquareRootNR
    assert ctr<=100,'Iteration count exceeded'
AssertionError: Iteration count exceeded
>>> aquareRootNR(2,0.0001)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    aquareRootNR(2,0.0001)
  File "<pyshell#77>", line 12, in aquareRootNR
    assert ctr<=100,'Iteration count exceeded'
AssertionError: Iteration count exceeded
>>> aquareRootNR(2,0.001)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    aquareRootNR(2,0.001)
  File "<pyshell#77>", line 12, in aquareRootNR
    assert ctr<=100,'Iteration count exceeded'
AssertionError: Iteration count exceeded
>>> def aquareRootNR(x,epsilon):
	assert x>=0,'x must be non-negative,not'+str(x)
	assert epsilon>0,'epsion must be positive,not'+str(epsilon)
	x=float(x)
	guess=1
	diff=guess**2-x
	ctr=1
	while abs(diff)>epsilon and ctr<=100:
		guess=guess-diff/(2*guess)
		diff=guess*2-x
		ctr+=1
	assert ctr<=100,'Iteration count exceeded'
	print ('NR method.   Num. iterations:',ctr,'Estimate:',guess)
	return guess

>>> aquareRootNR(2,0.001)
NR method.   Num. iterations: 6 Estimate: 1.000000306424934
1.000000306424934
>>> aquareRootNR(,0.001)
SyntaxError: invalid syntax
>>> aquareRootNR(4,0.001)
NR method.   Num. iterations: 13 Estimate: 2.0003905853199715
2.0003905853199715
>>> aquareRootNR(9,0.001)
NR method.   Num. iterations: 31 Estimate: 4.500393797661301
4.500393797661301
>>> aquareRootNR(9,0.0001)
NR method.   Num. iterations: 40 Estimate: 4.500041021985929
4.500041021985929
>>> aquareRootNR(9,0.00001)
NR method.   Num. iterations: 49 Estimate: 4.50000427288315
4.50000427288315
>>> def aquareRootNR(x,epsilon):
	assert x>=0,'x must be non-negative,not'+str(x)
	assert epsilon>0,'epsion must be positive,not'+str(epsilon)
	x=float(x)
	guess=1
	diff=guess**2-x
	ctr=1
	while abs(diff)>epsilon and ctr<=100:
		guess=guess-diff/(2.0*guess)
		diff=guess*2-x
		ctr+=1
	assert ctr<=100,'Iteration count exceeded'
	print ('NR method.   Num. iterations:',ctr,'Estimate:',guess)
	return guess

>>> aquareRootNR(9,0.00001)
NR method.   Num. iterations: 49 Estimate: 4.50000427288315
4.50000427288315
>>> def aquareRootNR(x,epsilon):
	assert x>=0,'x must be non-negative,not'+str(x)
	assert epsilon>0,'epsion must be positive,not'+str(epsilon)
	x=float(x)
	guess=0.1
	diff=guess**2-x
	ctr=1
	while abs(diff)>epsilon and ctr<=100:
		guess=guess-diff/(2.0*guess)
		diff=guess*2-x
		ctr+=1
	assert ctr<=100,'Iteration count exceeded'
	print ('NR method.   Num. iterations:',ctr,'Estimate:',guess)
	return guess

>>> aquareRootNR(9,0.00001)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    aquareRootNR(9,0.00001)
  File "<pyshell#94>", line 12, in aquareRootNR
    assert ctr<=100,'Iteration count exceeded'
AssertionError: Iteration count exceeded
>>> def aquareRootNR(x,epsilon):
	assert x>=0,'x must be non-negative,not'+str(x)
	assert epsilon>0,'epsion must be positive,not'+str(epsilon)
	x=float(x)
	guess=x/2.0
	diff=guess**2-x
	ctr=1
	while abs(diff)>epsilon and ctr<=100:
		guess=guess-diff/(2.0*guess)
		diff=guess*2-x
		ctr+=1
	assert ctr<=100,'Iteration count exceeded'
	print ('NR method.   Num. iterations:',ctr,'Estimate:',guess)
	return guess

>>> aquareRootNR(9,0.00001)
NR method.   Num. iterations: 50 Estimate: 4.499995011487942
4.499995011487942
>>> aquareRootNR(9,0.0001)
NR method.   Num. iterations: 41 Estimate: 4.4999521065001105
4.4999521065001105
>>> def aquareRootNR(x,epsilon):
	assert x>=0,'x must be non-negative,not'+str(x)
	assert epsilon>0,'epsion must be positive,not'+str(epsilon)
	x=float(x)
	guess=x/2.0
	guess=0.001
	diff=guess**2-x
	ctr=1
	while abs(diff)>epsilon and ctr<=100:
		guess=guess-diff/(2.0*guess)
		diff=guess*2-x
		ctr+=1
	assert ctr<=100,'Iteration count exceeded'
	print ('NR method.   Num. iterations:',ctr,'Estimate:',guess)
	return guess

>>> aquareRootNR(9,0.0001)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    aquareRootNR(9,0.0001)
  File "<pyshell#101>", line 13, in aquareRootNR
    assert ctr<=100,'Iteration count exceeded'
AssertionError: Iteration count exceeded
>>> def aquareRootNR(x,epsilon):
	assert x>=0,'x must be non-negative,not'+str(x)
	assert epsilon>0,'epsion must be positive,not'+str(epsilon)
	x=float(x)
	guess=x/2.0
	diff=guess**2-x
	ctr=1
	while abs(diff)>epsilon and ctr<=100:
		guess=guess-diff/(2.0*guess)
		diff=guess*2-x
		ctr+=1
	assert ctr<=100,'Iteration count exceeded'
	print ('NR method.   Num. iterations:',ctr,'Estimate:',guess)
	return guess

>>> aquareRootNR(9,0.0001)
NR method.   Num. iterations: 41 Estimate: 4.4999521065001105
4.4999521065001105
>>> aquareRootNR(16,0.0001)
NR method.   Num. iterations: 82 Estimate: 7.999955573527018
7.999955573527018
>>> def aquareRootNR(x,epsilon):
	assert x>=0,'x must be non-negative,not'+str(x)
	assert epsilon>0,'epsion must be positive,not'+str(epsilon)
	x=float(x)
	guess=x/2.0
	diff=guess**2-x
	ctr=1
	while abs(diff)>epsilon and ctr<=100:
		guess=guess-diff/(2.0*guess)
		diff=guess**2-x
		ctr+=1
	assert ctr<=100,'Iteration count exceeded'
	print ('NR method.   Num. iterations:',ctr,'Estimate:',guess)
	return guess

>>> aquareRootNR(16,0.0001)
NR method.   Num. iterations: 5 Estimate: 4.0000001858445895
4.0000001858445895
>>> aquareRootNR(9,0.0001)
NR method.   Num. iterations: 4 Estimate: 3.000015360039322
3.000015360039322
>>> def aquareRootNR(x,epsilon):
	assert x>=0,'x must be non-negative,not'+str(x)
	assert epsilon>0,'epsion must be positive,not'+str(epsilon)
	x=float(x)
	guess=x/2.0
	guess=0.001
	diff=guess**2-x
	ctr=1
	while abs(diff)>epsilon and ctr<=100:
		guess=guess-diff/(2.0*guess)
		diff=guess**2-x
		ctr+=1
	assert ctr<=100,'Iteration count exceeded'
	print ('NR method.   Num. iterations:',ctr,'Estimate:',guess)
	return guess

>>> aquareRootNR(16,0.0001)
NR method.   Num. iterations: 16 Estimate: 4.000000613209791
4.000000613209791
>>> aquareRootNR(9,0.0001)
NR method.   Num. iterations: 16 Estimate: 3.0000000019536337
3.0000000019536337
>>> def aquareRootNR(x,epsilon):
	assert x>=0,'x must be non-negative,not'+str(x)
	assert epsilon>0,'epsion must be positive,not'+str(epsilon)
	x=float(x)
	guess=x/2.0
	guess=0.001
	diff=guess**2-x
	ctr=1
	while abs(diff)>epsilon and ctr<=100:
		guess=guess-diff/(2*guess)
		diff=guess**2-x
		ctr+=1
	assert ctr<=100,'Iteration count exceeded'
	print ('NR method.   Num. iterations:',ctr,'Estimate:',guess)
	return guess

>>> aquareRootNR(9,0.0001)
NR method.   Num. iterations: 16 Estimate: 3.0000000019536337
3.0000000019536337
>>> def aquareRootNR(x,epsilon):
	assert x>=0,'x must be non-negative,not'+str(x)
	assert epsilon>0,'epsion must be positive,not'+str(epsilon)
	x=float(x)
	guess=x/2
	guess=0.001
	diff=guess**2-x
	ctr=1
	while abs(diff)>epsilon and ctr<=100:
		guess=guess-diff/(2*guess)
		diff=guess**2-x
		ctr+=1
	assert ctr<=100,'Iteration count exceeded'
	print ('NR method.   Num. iterations:',ctr,'Estimate:',guess)
	return guess

>>> aquareRootNR(9,0.0001)
NR method.   Num. iterations: 16 Estimate: 3.0000000019536337
3.0000000019536337
>>> def aquareRootNR(x,epsilon):
	assert x>=0,'x must be non-negative,not'+str(x)
	assert epsilon>0,'epsion must be positive,not'+str(epsilon)
	guess=x/2
	guess=0.001
	diff=guess**2-x
	ctr=1
	while abs(diff)>epsilon and ctr<=100:
		guess=guess-diff/(2*guess)
		diff=guess**2-x
		ctr+=1
	assert ctr<=100,'Iteration count exceeded'
	print ('NR method.   Num. iterations:',ctr,'Estimate:',guess)
	return guess

>>> aquareRootNR(9,0.0001)
NR method.   Num. iterations: 16 Estimate: 3.0000000019536337
3.0000000019536337
>>> def aun(x):
	y=x**(1/2)
	print(y)

	
>>> aun(9)
3.0
>>> aun(9.5)
3.082207001484488
>>> aquareRootNR(9.5,0.0001)
NR method.   Num. iterations: 16 Estimate: 3.08220700507887
3.08220700507887
>>> aun(100)
10.0
>>> aquareRootNR(100,0.0001)
NR method.   Num. iterations: 18 Estimate: 10.000000000082464
10.000000000082464
>>> 
