#    numpy&pandas
#————————————————————————————————————————————





import numpy as np

##array=np.array([[1,2,3],[2,3,4]])  #-----矩阵化（行向量）
##
##
##print(array)
##print('number of dim: ',array.ndim) #-----矩阵的维度
##print('shape: ',array.shape)		#----矩阵的形状 ?x?
##print('size: ',array.size)          #----元素的个数
##print(np.linalg.det(array))	#----矩阵行列式的值
##
##
##a=np.array([2,23,4],dtype=np.float)	#----指定元素的种类
##print(a)
##print(a.dtype)
##b=np.zeros((3,4),dtype=np.int16)
##print(b,b.dtype)
##
##c=np.arange(10,22,2).reshape((2,3))	#---10-22，2步长，重新整理，
##print(c)
##
##
##
##d=np.linspace(1,10,12).reshape((3,4))	#----开始端1，结束端10，且分割成12个数据，生成线段
##print(d)




##a=np.array([10,20,30,40])
##
##b=np.arange(4)            #range(4)
##
##c=10*np.sin(a)            #每个元素求sin
##
##print(c)
##print(b)
##print(b<3)                #每个元素作比较
##print(b==3)





##a=np.array([[1,1],[0,1]])
##b=np.arange(4).reshape((2,2))
##
##
##c=a*b		#错误的做法
##c_dot=np.dot(a,b)             #-----矩阵的乘法
##c_dot2=a.dot(b)
##
##d=np.linalg.inv(a)        #-----求逆
##
##
##print(a)
##print(b)
##print(c)
##print(c_dot)
##print(c_dot2)
##print(d)







##a=np.random.random((2,4))	#生成2行4列的随机元素不大于1的矩阵
##
##
##print(a)
##print(np.sum(a,axis=1))     #-----------axis=1为行；=0为列，将行加起来合并为1行
##print(np.min(a,axis=0))		#----找出每列的最小值
##print(np.max(a,axis=1))		




##A=np.arange(2,14).reshape((3,4))
##
##print(A)
##
##print(np.argmin(A))          #------最小值索引号
##
##print(np.argmax(A))          #-----最大值索引号
##
##print(np.mean(A))             #-----平均值
##print(A.mean())
##
##print(np.average(A,1,[2/5,1/5,1/5,1/5]))         #-----平均值（附加权重，无著名则都为1）
##
##print(np.median(A))           #-----中位数
##
##print(np.cumsum(A))            #----累加
##print(np.reshape(np.cumsum(A),(3,4)))
##
##print(np.diff(A))               #---累差
##
##print(np.nonzero(A))            #---找出非零数（输出为坐标i(前)j(后)）
##
##print(np.sort(A))               #----逐行排序(无变化)
###A.sort()                       #----A=np.sort(A)
##
##print(np.transpose(A))           #-----矩阵的转置
##
##
##print(np.linalg.matrix_rank(A))              #-----矩阵的秩
##
##print(np.clip(A,6,11))                #------边端同化
##
##print(np.mean(A,axis=1))               #-----都可指定行 ，列计算







##A=np.arange(3,15)
##
##print(A)
##print(A[3])
##
##
##
##B=np.arange(3,15).reshape(3,4)  
##
##print(B)
##
##print(B[2])               #----打印第三行
##print(B[2,:])
##
##print(B[1][1])
##print(B[1,1])
##
##print(B[1,1:3])           #打印第二行，第二到第三个数
##
##
##for row in B:          #-------打印B的所有元素(行向量)
##    print(row)
##
##
##
##for column in B.T:
##    print(column)    #------打印B中的所有列向量（行转置）
##
##print(B)
##print(B.flatten())  #-----矩阵归为一行
##for item in B.flatten(): 
##    print(item)






##A=np.array([1,1,1])
##B=np.array([2,2,2])
##
##C=np.vstack((A,B))     #-----竖粘
##D=np.hstack((A,B))     #-----横粘（111222）
##
##print(C)
##
##print(A.shape,C.shape)
##
##print(D)
##
##print(D.shape)     #------单行无法得到转置
##print(D.T)
##print(D.T.shape)
##
##
##print(A[np.newaxis,:].shape)   
##print(A[np.newaxis,:])
##
##print(A[:,np.newaxis].shape)    #----单行转置方法
##print(A[:,np.newaxis])
##
##
##
##
##
##A_=np.array([1,1,1])[:,np.newaxis]
##print(A_)
##
##
##B_=np.array([2,2,2])[:,np.newaxis]
##
##print(np.vstack((A_,B_)))
##print(np.hstack((A_,B_)))
##
##
##
##C_=np.concatenate((A_,B_,B_,A_),axis=1)      #------可改变维度的合并
##
##print(C_)







##A=np.arange(12).reshape((3,4))
##print(A)
##
##print(np.split(A,2,axis=1))                  #-----分割
##print(np.vsplit(A,3))
##print(np.hsplit(A,2))
##
##print(np.array_split(A,2,axis=0))              #----非等分割




##a=np.arange(4)
##b=a
##c=a
##d=b
##a[0]=11
##
##b_=a.copy()   # --------无关联赋值





#————————————————————————————————————————————————————



##import pandas as pd
##import numpy as np


##s=pd.Series([1,3,6,np.nan,44,1])   #------n维数表（带索引值）
##print(s)
##
##
##dates=pd.date_range('20180603',periods=6)   #----日期格式
##print(dates)
##
##
##df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])   #----创建一个二维列表（指定索引号，和列标）
##print(df)
##
##
##
##
##
##df1=pd.DataFrame(np.arange(12).reshape((3,4)))  #-----默认为01234......的索引和列标
##print(df1)
##
##
##df2=pd.DataFrame({'A':1.,
##                  'B':pd.Timestamp('20180603'),
##                  'C':pd.Series(1,index=list(range(4)),dtype='float32'),
##                  'D':np.array([3]*4,dtype='int32'),
##                  'E':pd.Categorical(["test","train","test","train"]),
##                  'F':'foo'})
##print(df2)
##print(df2.dtypes)
##print(df2.index)
##print(df2.columns)
##print(df2.values)  #-----矩阵各值
##print(df2.describe())  #------进行详细计算，自动忽略非数字类型
##print(df2.T)
##print(df2.sort_index(axis=1,ascending=False))
##print(df2.sort_index(axis=0,ascending=False))
##print(df2.sort_values(by='E'))







##dates=pd.date_range('20180603',periods=6)
##df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
##
##print(df)
##print(df['A'])
##print(df.A)
##
##print(df[:3])                  #--------列
##print(df[:'20180605'])
##
##print(df.loc['20180603'])   #----------行
##
##print(df.loc[:,['A','B']])   #----行为[:]所有行；列为['A','B']两列
##
##
##print(df.iloc[3:5,1:3])
##print(df.iloc[[1,3,5],1:3])
##
##
##
##
##print(df.ix[:3,['A','C']])            #----混合输入
##print(df.loc[:,['A','C']])            #----无法通过索引号，只能通过索引值
##print(df.iloc[:3,[0,2]])              #----无法输入索引值
##
##print(df)
##print(df[df.A>8])          #------筛选A列中大于8的，同时去掉所有False行
##print(df.A>8)              #-----输出为布尔值








##dates=pd.date_range('20180603',periods=6)
##df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
##
##df.iloc[2,2]=1111
##df.loc['20180603','B']=222
##
##
##print(df)
##
##df[df.A>4]=5
##
##print(df)
##
##df.A[df.A>4]=0
##print(df)
##
##
##
##df['F']=np.nan
##print(df)
##
##df['E']=pd.Series([1,2,3,4,5,6],index=pd.date_range('20180603',periods=6))        #---添加数据（长度需对齐）
##print(df)







##dates=pd.date_range('20180603',periods=6)
##df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
##df.iloc[0,1]=np.nan
##df.iloc[1,2]=np.nan
##
##print(df)
##print(df.dropna(axis=0,how='any'))#或者'all'    #-----------舍弃任何丢失数据（nan)
##
##print(df.fillna(value=0))           #-----填充nan为...
##
##print(df)
##print(df.isnull())
##
##print(np.any(df.isnull())==True) #-----检测在数据中是否存在 NaN, 如果存在就返回 True
##







##data=pd.read_csv('student.csv')
##print(data)
##
##
##data.to_pickle('student2.pickle')






#合并：

##df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])     #-------ones()指定元素为全同
##df2=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
##df3=pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
##
##
##
##
##print(df1)
##print(df2)
##print(df3)
##
##
##res=pd.concat([df1,df2,df3],axis=0,ignore_index=True)
##
##print(res)




##
##df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])     
##df2=pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
##
##print(df1)
##print(df2)
##
##
##res=pd.concat([df1,df2],axis=0,join='outer',ignore_index=True)
##
##print(res)
##
##
##res=pd.concat([df1,df2],axis=0,join='inner',ignore_index=True)
##
##
##print(res)
##




##df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])     
##df2=pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
##
##
##
##res_=pd.concat([df1,df2],axis=1)#,join_axes=[df1.index])
##res=pd.concat([df1,df2],axis=1,join_axes=[df1.index])   #-------按照df1的索引号排列
##print(res_)
##print(res)








##df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])     #-------ones()指定元素为全同
##df2=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
##df3=pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
##
##
##
##
##
##res=df1.append([df2,df3],ignore_index=True)         #-----和合并的两种方法(append只能一维合并无axis）
##print(res)
##res=pd.concat([df1,df2,df3],axis=0,ignore_index=True)
##print(res)



##df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
##s1=pd.Series([1,2,3,4],index=['a','b','c','d'])   #-----数列自动对齐索引值
##res=df1.append(s1,ignore_index=True)
##print(res)
##print(s1)
##








##
##left=pd.DataFrame({'key':['K0','K1','K2','K3'],
##                   'A':['A0','A1','A2','A3'],
##                   'B':['B0','B1','B2','B3']})
##
##right=pd.DataFrame({'key':['K0','K1','K2','K3'],
##                    'C':['C0','C1','C2','C3'],
##                    'D':['D0','D1','D2','D3']})
##
##
##
##print(left)
##print(right)
##
##res=pd.merge(left,right,on='key')
##print(res)









#填充：
##left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
##                      'key2': ['K0', 'K1', 'K0', 'K1'],
##                      'A': ['A0', 'A1', 'A2', 'A3'],
##                      'B': ['B0', 'B1', 'B2', 'B3']})
##right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
##                       'key2': ['K0', 'K0', 'K0', 'K0'],
##                       'C': ['C0', 'C1', 'C2', 'C3'],
##                       'D': ['D0', 'D1', 'D2', 'D3']})
##
##print(left)
##print(right)
##
##
##
##
##res=pd.merge(left,right,on=['key1','key2'])   #-------默认how='inner'
##
##print(res)
##
##
##res=pd.merge(left,right,on=['key1','key2'],how='left')  
##
##
##print(res)
##




##
##df1 = pd.DataFrame({'col1':[0,1], 'col_left':['a','b']})
##df2 = pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
##
##
##
##print(df1)
##print(df2)
##
##
##res=pd.merge(df1,df2,on='col1',how='outer',indicator=True)     #------填充方式说明
##print(res)
##
##
##
##res=pd.merge(df1,df2,on='col1',how='outer',indicator='indicator_column')
##print(res)





##left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
##                     'B': ['B0', 'B1', 'B2']},
##                     index=['K0', 'K1', 'K2'])       #-------指定索引值
##right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
##                      'D': ['D0', 'D2', 'D3']},
##                     index=['K0', 'K2', 'K3'])
##
##
##
##print(left)
##print(right)
##
##
##
##res=pd.merge(left,right,left_index=True,right_index=True,how='outer') #----根据索引值来填充
##print(res)









##boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
##girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
##
##print(boys)
##print(girls)
##
##res=pd.merge(boys,girls,on='k',suffixes=['_boy','_girl'],how='inner')    #-----当左右DataFrame存在相同列名时在列名后面附加后缀名称
##print(res)
##
##res=pd.merge(boys,girls,on='k',suffixes=['_boy','_girl'],how='outer')
##print(res)






##import matplotlib.pyplot as plt


##data=pd.Series(np.random.randn(10),index=np.arange(10))
##print(data)
##data.cumsum()
##data.plot()    #----给matplottlib提供一串Y值
##plt.show()     #----出图


##data=pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=list('ABCD'))#['A','B','C','D'])
##data=data.cumsum()
##print(data.head())   #----前五行
##
##
##
##data.plot()
##plt.show()
##
##
##ax=data.plot.scatter(x='A',y='B',color='DarkBlue',label='Class 1')
##data.plot.scatter(x='A',y='C',color='DarkGreen',label='Class 2',ax=ax)
##
##plt.show()


#——————————————————————————————————————————————————————————————

