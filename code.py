#x=3 # Creat x and assign value 3 to it 
#x=x*x # Bind x to value 9
#print (x)
#n=input('Enter a number: ')
#print n


#x=15
#if(x/2)*2==x:
#   print 'even'
#else: 
#   print 'odd'


#z='b'
#if 'x'<z:
#   print ('Hellow')	
#print ('Mom')


#x=15
#y=5
#z=11
#print (x,y,z)
#if  x<y and x<z:
#	  print ('x is least')
#elif y<z:
#	  print ('y is least')
#else:print ('z is least')


#y=0
#x=3
#mon=x
#while mon>0:
#	  y=y+x
#	  mon=mon-1
#	  print (y)

####2018.4.19 总结：1.字符串用‘。。。。’表示.
##                2.if，else，elif,while等后要加冒号（：).
##                3.上下句按顺序分级，错级容易出错.
##                4.print后加括号.                     














#x=16
#ans=0
#while ans*ans<=x:
#	ans=ans+1
#	print (ans)     



#x=12345
#ans=0
#if x>=0:
#	while ans*ans<x:
#		ans=ans+1
#		print (ans)
#	if ans*ans !=x:
#		       print (x,'is not a perfect aquare')
#	else: print (ans)
#else:
#		       print (x,'is a negative number')






#x=10
#i=1
#while i<x:
#		       if x%i==0:
#		          print ('divisor=',i)
#		       i=i+1      








#x=10
#for i in range(1,x):
#		       if x%i==0:
#		          print ('divisor=',i)






#test=(1,2,3,4)





#x=100
#divisor=()
#for i in range(1,x):
#        if x%i==0:
#                 divisor=divisor+(i,)
#        print (divisor)






#s1=(1,2,3,4)
#s2=[2,3,4,5]
#s3='abc123'






#sumDigits=0
#for c in str(1952):                       
##同》：#for c in '1952':
#		  sumDigits += int(c)
#		  print (sumDigits)




##2018.4.20总结：1.变量与字符串之间用逗号（，）隔开。
##               2.（！=）表示不相等。
##               3.（），表示元组不可变；[]，表示列表可变；{}表示字典，属于可变类型
##               4.引用系统中单个变量要加逗号，如:(i,).
##               5.(%=)表示取余数；“int()"表示取整的数！
##               6."for..in..."语句表示重复语句，在in后面的范围内取对应的元素个数作为重复次数。
##               7.s[0],s[1]....s[-1]




#x=16
#def sqrt(x):
#	ans=0
#	if x>=0:
#	       while ans*ans<x:
#		               ans=ans+1
#	       if ans*ans !=x:
#		       print (x,'is not a perfect aquare')
#		       return None
#	       else: return ans
#	else:
#		       print (x,'is a negative number')
#		       return None




#def solve(numLegs,numHeads):
#	for numChicks in range(0,numHeads+1):
#		numPigs=numHeads-numChicks
#		totLegs=4*numPigs+numChicks*2
#		if totLegs==numLegs:
#			return (numChicks,numPigs)
#	print('wrong')
#	return None，None




#def barnYard():
#		 heads=int(input('Number of legs:', ))
#		 legs=int(input('Number of heads:', ))
#		 pigs,chickens=solve(heads,legs)
#		 if pigs==None:
#		     print('the Number of legs(or heads) is not suitable')
#		 else:
#		       print('Number of pigs=',pigs)
#		       print('Number of chickens=',chickens)




#def solve1(numLegs,numHeads):
#	for numSpiders in range(0,numHeads+1):
#		for numChickens in range(0,numHeads-numSpiders+1):
#			numPigs=numHeads-numSpiders-numChickens
#			totLegs=4*numPigs+2*numChickens+8*numSpiders
#			if totLegs==numLegs:
#				return numPigs,numChickens,numSpiders
#	return None,None,None









#def barnYard1():
#	heads=int(input('Number of heads:', ))
#	legs=int(input('Number of legs:', ))
#	pigs,chickens,spiders=solve1(legs,heads)
#	if pigs==None:
#		print('the number of heads(or legs)is not suitable')
#	else:
#		print('Number of piges=',pigs)
#		print('Number of chickens=',chickens)
#		print('Number of spiders=',spiders)








#def Palindrome(s):
#	if len(s)<=1:
#		return True
#	else:return s[0]==s[-1] and Palindrome(s[1：-1])







#def Palindrome1(s,indent):
#	       print(indent, 'First scan',s)
#	       if len(s)<=1:
#		       print(indent, 'Second scan')
#		       return True
#	       else:
#		       ans=s[0]==s[-1]and Palindrome1(s[1:-1],indent+indent)
#		       print(indent,'Come back',ans)
#		       return ans






#def fib(x,indent):
#	       print(indent,'First scan',x)
#	       if x==0 or x==1:
#		       print(indent,'Second scan')
#		       return 1
#	       else:
#		       ans=fib(x-1,indent)+fib(x-2,indent)
#		       print('Third scan',ans)
#		       return ans


##2018.4.26总结：1.递归算法，找准循环位置。
##               2.len表示返回字符串长度或列表元素个数。
##               3.and:全真取最后，有假取头假；or:全假取最后，有真取头真。
##	       4.s[0:-1]表示取第二个到倒数第二个的元素。
##               5.input后表示运行时，用户要输入的值。





#s=0.0
#for i in range(10):
#	s+=0.1



#import math
#a=math.sqrt(2)
#print(a)
#a*a==2



#def squareRootBi(x,epsilon):                                  ---------二分法求平方
#	assert x>=0,'x must be non-negative,not'+str(x)
#	assert epsilon>0,'epsilon must be positive,not'+str(epsilon)
#	low=0
#	high=max(x,1)
#	guess=(low+high)/2
#	ctr=1
#	while abs(guess**2-x)>epsilon and ctr<=100:
#		if guess**2<x:
#			low=guess
#		else:
#			high=guess
#		guess=(low+high)/2
#		ctr+=1
#	assert ctr<=100,'Iteration count exceeded'
#	print ('Bimethod.Num.interations:',ctr,'Estimate:',guess)
#	return guess


#def aquareRootNR(x,epsilon):                                  ------牛顿-拉复生法逼近
#	assert x>=0,'x must be non-negative,not'+str(x)
#	assert epsilon>0,'epsion must be positive,not'+str(epsilon)
#	x=float(x)
#	guess=x/2.0
#	guess=0.001
#	diff=guess**2-x
#	ctr=1
#	while abs(diff)>epsilon and ctr<=100:
#		guess=guess-diff/(2.0*guess)
#		diff=guess**2-x
#		ctr+=1
#	assert ctr<=100,'Iteration count exceeded'
#	print ('NR method.   Num. iterations:',ctr,'Estimate:',guess)
#	return guess
##
##                                          




#Techs=['MIT','Cal Tech']
#Ivys=['Harvard','Yale','Brown']
#Univs=[]
#Univs.append(Techs)
#print (Univs)

#Univs.append(Ivys)
#print(Univs)

#for e in Univs:
#	print (e)
#	for c in e:
#		print(c)

#Univs=Techs+Ivys
#print(Univs)

#Ivys.remove('Harvard')
#print(Ivys)
#print(Univs)



##2018.5.16总结：1.“+=”表示加上后面并返回给前一个数；
##               2.“math.   ”运算调用；
##               3.“max(  ,  )”取最大值；
##               4.“abs()”表示取绝对值；
##               5.“assert  ，  ”前接条件，后接错误提示语；
##               6.可变数组用“[]”表示；
##               7.“ .append()”表示添加元素进数组，“ .remove()”表示从数组中删除对象.


#def getFloat(requestMsg,errorMsg):
#	inputOK=False
#	while not inputOK:
#		val=eval(input(requestMsg))
#		if type(val)==type(1.0):
#			inputOK=True
#		else:
#			print(errorMsg)
#	return val


#def msg():
#	base=getFloat('Enter base: ','Error:base must be a float')
#	height=getFloat('Enter height: ','Error:height must be a float')
#	import math
#       hyp=math.sqrt(base*base+height*height)
#	print('Base: '+str(base)+',height: '+str(height)+',hyp: '+str(hyp))


#def exp1(a,b):
#	ans=1
#	while (b>0):
#		ans*=a
#		b-=1
#	return ans




#def exp2(a,b):
#	if b==1:
#		return a
#	else:
#		return a*exp2(a,b-1)



#def exp3(a,b):
#	if b==1:
#		return a
#	if (b%2)*2==b:
#		return exp3(a,b/2)
#	else:return a*exp3(a,b-1)





#def Towers(size,fromStack,toStack,spareStack):
#	if size==1:
#		print('Move disk from ',fromStack,'to',toStack)
#	else:
#		Towers(size-1,fromStack,spareStack,toStack)
#		Towers(1,fromStack,toStack,spareStack)
#		Towers(size-1,spareStack,toStack,fromStack)



#def bsearch(s,e,first,last):
#	print(first,last)
#	if (last-first)<2:
#		return s[first]==e or s[last]==e
#	mid=int(first+(last-first)/2)
#	if s[mid]==e:
#		return True
#	if s[mid]>e:
#		return bsearch(s,e,first,mid-1)
#	return bsearch(s,e,mid+1,last)





#def search(s,e):
#	answer=None
#	i=0
#	numCompares=0
#	while i<len(s) and answer==None:
#		numCompares+=1
#		if e==s[i]:
#			answer=True
#		elif e<s[i]:
#			answer=False
#		i+=1
#	print(answer,numCompares)






#def bsearch(s,e,first,last,calls):
#	print(first,last,calls)
#	if (last-first)<2:
#		return s[first]==e or s[last]==e
#	mid=int(first+(last-first)/2)
#	if s[mid]==e:
#		return True
#	if s[mid]>e:
#		return bsearch(s,e,first,mid-1,calls+1)
#	return bsearch(s,e,mid+1,last,calls+1)


#def search(s,e):
#	print(bsearch(s,e,0,len(s)-1,1))







#def selSort(L):
#	for i in range(len(L)-1):
#		print (L)
#		minIndx=i
#		minVal=L[i]
#		j=i+1
#		while j<len(L):
#			if minVal>L[j]:
#				minIndx=j
#				minVal=L[j]
#			j=j+1
#		temp=L[i]
#		L[i]=L[minIndx]
#		L[minIndx]=temp
#	print(L)





#def bubbleSort(L):
#	for j in range(len(L)):
#		print(L)
#		for i in range(len(L)-1):
#			if L[i]>L[i+1]:
#				temp=L[i]
#				L[i]=L[i+1]
#				L[i+1]=temp
#       print(L)



#def bubbleSort1(L):
#	swapped=True
#	while swapped:
#		swapped=False
#		print(L)
#		for i in range(len(L)-1):               
#			if L[i]>L[i+1]:               - - - - 2.内套循环结束点。
#				temp=L[i]
#				L[i]=L[i+1]
#				L[i+1]=temp
#				swapped=True  ----------1.小循环内套循环。
#	print(L)



##2018.5.20总结：1."while not name....",如果"name"为true,   "not name"就为“False";反之类似；
##               2.while后接常量(或true)表示无限循环,要停止需后加“break"(或常量等于“False");
##	       3.例子中有典型的二分法，二分法排序，选择排序法和冒泡排序法。
##












#def merge(left,right):                -----------------两个已排好序列
#	result=[]
#	i,j=0,0
#	while i<len(left) and j<len(right):
#		if left[i]<=right[j]:
#			result.append(left[i])
#			i+=1
#		else:
#			result.append(right[j])
#			j+=1
#	while i<len(left):
#		result.append(left[i])
#		i+=1
#	while j<len(right):
#		result.append(right[j])
#		j+=1
#	return result


#def mergesort(L):                        -------分治法排列
#	print(L)
#	if len(L)<2:
#		return L[:]
#	else:
#		middle=len(L)//2
#		left=mergesort(L[:middle])
#		right=mergesort(L[middle:])
#		together=merge(left,right)
#		print('merged',together)
#		return together



#def readFloat(requestMsg,errorMsg):
#	while True:
#		val=input(requestMsg)
#		try:
#			val=float(val)
#			return val
#		except:
#			print(errorMsg)










#def getGrades(fname):
#	try:
#		gradesFile=open(fname,'w')
#	except IOError:
#		print('Could not open',fname)
#		print('aaaaa')
#	grades=[]
#	for line in gradesFile:
#		grades.append(float(line))
#	return grades









#def silly():                               ---------二分查找错误
#	res=[]
#	done=False
#	while not done:
#		elem=input('Enter element.  Return when done.')
#		if elem=='':
#			done=True
#		else:
#			res.append(elem)
#	#print('res should be,[1,2,3]',res)
#	tmp=res[:]
#	#print('tmp=',tmp,'res=',res)
#	tmp.reverse()
#	isPal=(res==tmp)
#	#print('tmp=',tmp,'res=',res)
#	if isPal:
#		print('is a palindrome')
#	else:
#		print('is not a palindrome')



##def fib(n):                           -------斐波那契函数
##	global numCalls
##	#print('fib called with',n)
##	numCalls+=1
##	if n<=1:
##		return 1
##	else:
##		return fib(n-1)+fib(n-2)
##numCalls=0
##n=30
##res=fib(n)
##print ('fib of',n,'=',res,'numCalls=',numCalls)
##
##	    
##def fastFib(n,memo):                              ------动态规划
##     global numCalls
##     numCalls+=1
##     #print('fib1 called with',n)
##     if not n in memo:
##	     memo[n]=fastFib(n-1,memo)+fastFib(n-2,memo)
##     return memo[n]
##
##def fib1(n):
##	memo={0:1,1:1}
##	return fastFib(n,memo)
##
##numCalls=0
##n=30
##res=fib1(n)
##print ('fib of',n,'=',res,'numCalls=',numCalls)



##def maxVal(w,v,i,aW):                    -----------最优子结构(背包问题）
##    print('maxVal callde with:',i,aW)
##    global numCalls
##    numCalls+=1
##    if i==0:
##        if w[i]<=aW:
##            return v[i]
##        else:
##            return 0
##    without_i=maxVal(w,v,i-1,aW)
##    if w[i]>aW:
##        return without_i
##    else:
##        with_i=v[i]+maxVal(w,v,i-1,aW-w[i])
##    return max(with_i,without_i)
##
##numCalls=0
##w=[5,3,2]
##v=[9,7,8]
##res=maxVal(w,v,len(v)-1,5)
##print('max Val=',res,'number of calls=',numCalls)
##
##
##numCalls=0
##w=[1,5,3,4]
##v=[15,10,9,5]
##res=maxVal(w,v,len(v)-1,8)
##print('max Val=',res,'number of calls=',numCalls)
##
##
##
##numCalls=0
##w=[1,1,5,5,3,3,4,4]
##v=[15,15,10,10,9,9,5,5]
##res=maxVal(w,v,len(v)-1,8)
##print('max Val=',res,'number of calls=',numCalls)




##def fastMaxVal(w,v,i,aW,m):       ---------动态规划（背包问题）
##    global numCalls
##    numCalls+=1
##    try:
##        return m[(i,aW)]
##    except KeyError:
##        if i==0:
##            if w[i]<=aW:
##                m[(i,aW)]=v[i]
##                return v[i]
##            else:
##                m[(i,aW)]=0
##                return 0
##        without_i=fastMaxVal(w,v,i-1,aW,m)
##        if w[i]>aW:
##            m[(i,aW)]=without_i
##            return without_i
##        else:
##            with_i=v[i]+fastMaxVal(w,v,i-1,aW-w[i],m)
##        res=max(with_i,without_i)
##        m[(i,aW)]=res
##        return res
##
##def maxVal0(w,v,i,aW):
##    m={}
##    return fastMaxVal(w,v,i,aW,m)
##
##numCalls=0
##w=[1,1,5,5,3,3,4,4]
##v=[15,15,10,10,9,9,5,5]
##i=len(v)-1
##aW=8
##a=maxVal0(w,v,i,aW)
##print(a,numCalls)



##2018.5.23 总结：1.动态规划问题要找准嵌套中的重复计算部分，将计算过的后面嵌套又要用到的结果归入一个字典，方便套用。
##                2.{1:a,2:b}字典格式为“key+内容”中间用冒号（：）.
##                3.KeyError为字典内无对应key.
##                4.‘global+.....‘为全局定义该函数.
##                5.’try...+except‘为异常处理语句，不会中断程序的进行，过程为：当程序进行到try时,执行try下面的语句，异常时，对应except后的异常状态，执行except.... 后的语句；完毕后再回到try，重复之前的操作。
##                6.IOError为输入输出错误，通常为调用了不存在的文件.
##                7.运用二分法查找出程序中的bug,常用print打出上文结果.
                






##def addPoints(p1,p2):                     -------数据为列表
##    r=[]
##    r.append(p1[0]+p2[0])
##    r.append(p1[1]+p2[1])
##    return r
##p=[1,2]
##q=[3,1]
##r=addPoints(p,q)
##print (r)





##class cartesianPoint:
##    pass
##cp1=cartesianPoint()
##cp2=cartesianPoint()
##cp1.x=1.0
##cp1.y=2.0
##cp2.x=1.0
##cp2.y=3.0
##
##
##
##
##
##def samePoint(p1,p2):
##    return(p1.x==p2.x)and(p1.y==p2.y)
##
##
##import math
##class polarPoint:
##    pass
##pp1=polarPoint()
##pp2=polarPoint()
##pp1.radius=1.0
##pp1.angle=0
##pp2.radius=2.0
##pp2.angle=math.pi/4.0


##import math
##class cPoint:
##    def __init__(self,x,y):
##        self.x=x
##        self.y=y
##        self.radius=math.sqrt(self.x*self.x+self.y*self.y)
##        self.angle=math.atan2(self.y,self.x)
##    def cartesian(self):
##        return (self.x,self.y)
##    def polar(self):
##        return (self.radius,self.angle)
##    def __str__(self):                                     ---重载
##        return '('+str(self.x)+','+str(self.y)+')'                       
##    def __gt__(self,other):                             ---重载
##        return (self.x>other.x)and(self.y>other.y)
##        
##
##a=cPoint(1.0,2.0)
##
##class pPoint:
##    def __init__(self,r,a):
##        self.radius=r
##        self.angle=a
##        self.x=r*math.cos(a)
##        self.y=r*math.sin(a)
##    def cartesian(self):
##        return(self.x,self.y)
##    def polar(self):
##        return (self.radius,self.angle)
##    def __str__(self):
##        return  ('('+str(self.x)+','+str(self.y)+')')
##    def __gt__(self,other):
##        return(self.x>other.x)and(self.y>other.y)
##
##b=pPoint(1.0,2.0)
##
##
##
##class Segment:
##    def __init__(self,start,end):
##        self.start=start
##        self.end=end
##    def length(self):
##        return math.sqrt(((self.start.x-self.end.x)*(self.start.x-self.end.x))
##                         +((self.start.y-self.end.y)*(self.start.y-self.end.y)))
##
##
##p1=cPoint(3.0,4.0)
##p2=cPoint(5.0,7.0)
##s1=Segment(p1,p2)
##print(s1.length())
##
##
##class Rectangle:                                            -----创建实例
##    def __init__(self,width,height,corner):
##        self.width=width
##        self.height=height
##        self.corner=corner
##
##        
##def findCenter(box):                                        -----继承
##    p=cPoint(box.corner.x+box.width/2.0,box.corner.y-box.height/2.0)
##    return p
##box=Rectangle(100,200,p1)
##print(findCenter(box))
##
##def growRect(box,dwidth,dheight):                  -----修改
##    box.width=box.width+dwidth
##    box.height=box.height+dheight
##
##growRect(box,10,20)
##print(findCenter(box))
    





##class newPoint:
##    def __init__(self,x=0,y=0):
##        self.x=x
##        self.y=y
##    def __str__(self):
##        return '('+str(self.x)+','+str(self.y)+')'
##    def __eq__(self,other):
##        return (self.x==other.x)and(self.y==other.y)
##    def __add__(self,other):
##        return newPoint(self.x+other.x,self.y+other.y)
##    def __lt__(self,other):
##        return (self.x<other.x)and(self.y<other.y)
##
##
##origin=newPoint()
##p1=newPoint(3.0,4.0)
##p2=newPoint()
##p3=p1+p2
##print(p3)
##print(p1<p2)



##2018.5.30总结：1.类运算重载：__init__(self)：  ---构造方法；
##                             __add__(self, other): ----加法；
##                             __lt__(self, other):  -----小于比较；
##                             __eq__(self, other): -----全等比较；
##                             __gt__(self, other): -----大于比较；
##                             __str__(self):       -----打印,print()函数的指定输出对象
##               2.继承、修改需在定义函数最后的括号内署名原类（为保持函数清洁，通常需用第二名称代替原类);










import operator

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

per=Person('Frank','Fooba')


class MITPerson(Person):
    nextIdNum=0
    def __init__(self,familyName,firstName):                #-------为子类定义变量
        Person.__init__(self,familyName,firstName)         # -------为子类指定父类中的变量（父类的初始化）       
        self.idNum=MITPerson.nextIdNum
        MITPerson.nextIdNum+=1
    def getIdNum(self):
        return self.idNum
    def __str__(self):
        return ('<MIT Person: %s %s >'%(self.first_name,self.family_name))
    def __eq__(self,other):
        return operator.eq(self.idNum,other.idNum)

p1=MITPerson('Smith','Fred')
p2=MITPerson('Foobar','Jane')
print(p1.getIdNum())
print(p2.getIdNum())

    


class UG(MITPerson):
    def __init__(self,familyName,firstName):
        MITPerson.__init__(self,familyName,firstName)
        self.year=None
    def setYear(self,year):
        if year>5:
            raise OverflowError('Too many')
        self.year=year
    def getYear(self):
        return self.year
    def say(self,toWhom,something):                     #---------修改，模块对应，相当于重载了say函数
        return MITPerson.say(self,toWhom,'Excuse me,but '+something)

me=Person('Grimson','Eric')
ug=UG('Doe','Jane')







class Prof(MITPerson):
    def __init__(self,familyName,firstName,rank):
        MITPerson.__init__(self,familyName,firstName)
        self.rank=rank
        self.teaching={}
    def addTeaching(self,term,subj):
        try:
            self.teaching[term].append(subj)
        except KeyError:
            self.teaching[term]=[subj]
    def getTeaching(self,term):
        try:
            return self.teaching[term]
        except KeyError:
            return None
    def lecture(self,toWhom,something):
        return self.say(toWhom,something+' as it is obvious')
    def say(self,toWhom,something):
        if type(toWhom)==UG:
            return MITPerson.say(self,toWhom,'I do not understand why you say '+something)
        elif type(toWhom)==Prof:
            return MITPerson.say(self,toWhom,'I really liked your paper on '+something)
        else:
            return self.lecture(something)


me=Prof('Grimson','Eric','Full')
me.addTeaching('F08','6.00')
me.addTeaching('S09','6.00')
me.addTeaching('S09','6.xxx')
print(me.getTeaching('F08'))
print(me.getTeaching('S09'))
print(me.getTeaching('S08'))
print(me.teaching)


class Faculty:
    def __init__(self):
        self.names=[]
        self.IDs=[]
        self.members=[]
        self.place=None
    def add(self,who):
        if type(who)!=Prof:
            raise TypeError('not a professor')
        if who.getIdNum() in self.IDs:
            raise ValueError('duplicate ID')
        self.names.append(who.familyName())
        self.IDs.append(who.getIdNum())
        self.members.append(who)
    def __iter__(self):
        self.place=0
        return self
    def __next__(self):
        if self.place>=len(self.names):
            raise StopIteration
        self.place+=1
        return self.members[self.place-1]


