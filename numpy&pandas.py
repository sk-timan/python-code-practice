#    numpy&pandas
#����������������������������������������������������������������������������������������





##import numpy as np

##array=np.array([[1,2,3],[2,3,4]])  #-----���󻯣���������
##
##
##print(array)
##print('number of dim: ',array.ndim)
##print('shape: ',array.shape)
##print('size: ',array.size)
##
##
##a=np.array([2,23,4],dtype=np.float)
##print(a)
##print(a.dtype)
##b=np.zeros((3,4),dtype=np.int16)
##print(b,b.dtype)
##
##c=np.arange(10,22,2).reshape((2,3))
##print(c)
##
##
##
##d=np.linspace(1,10,12).reshape((3,4))
##print(d)




##a=np.array([10,20,30,40])
##b=np.arange(4)
##
##c=10*np.sin(a)
##
##print(c)
##print(b)
##print(b<3)
##print(b==3)





##a=np.array([[1,1],[0,1]])
##b=np.arange(4).reshape((2,2))
##
##c=a*b
##c_dot=np.dot(a,b)             #-----����ĳ˷�
##c_dot2=a.dot(b)
##
##
##print(c)
##print(c_dot)
##print(c_dot2)







##a=np.random.random((2,4))
##
##print(a)
##print(np.sum(a,axis=1))     #-----------axis=1Ϊ�У�=0Ϊ��
##print(np.min(a,axis=0))
##print(np.max(a,axis=1))




##A=np.arange(2,14).reshape((3,4))
##
##print(A)
##
##print(np.argmin(A))          #------��Сֵ������
##
##print(np.argmax(A))          #-----���ֵ������
##
##print(np.mean(A))             #-----ƽ��ֵ
##print(A.mean())
##print(np.average(A))          #-----ƽ��ֵ������Ȩ�أ���������Ϊ1��
##
##print(np.median(A))           #-----��λ��
##
##print(np.cumsum(A))            #----�ۼ�
##
##print(np.diff(A))               #---�۲�
##
##print(np.nonzero(A))            #---�ҳ������������Ϊ����ij��
##
##print(np.sort(A))               #----��������
##
##print(np.transpose(A))           #-----�����ת��
##print(A.T)
##
##print(np.linalg.matrix_rank(A))              #-----�������
##
##print(np.clip(A,5,9))                #------�߶�ͬ��
##
##print(np.mean(A,axis=1))               #-----����ָ���� ���м���






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
##print(B[2])
##print(B[2,:])
##
##print(B[1][1])
##print(B[1,1])
##
##print(B[1,1:3])
##
##
##for row in B:          #-------����������
##    print(row)
##
##
##
##for column in B.T:
##    print(column)    #------��������������ת�ã�
##
##print(B)
##print(B.flatten())  #-----�����Ϊһ��
##for item in B.flatten(): 
##    print(item)






##A=np.array([1,1,1])
##B=np.array([2,2,2])
##
##C=np.vstack((A,B))     #-----��ճ
##D=np.hstack((A,B))     #-----��ճ��111222��
##
##print(C)
##
##print(A.shape,C.shape)
##
##print(D)
##
##print(D.shape)     #------�����޷��õ�ת��
##print(D.T)
##print(D.T.shape)
##
##
##print(A[np.newaxis,:].shape)   
##print(A[np.newaxis,:])
##
##print(A[:,np.newaxis].shape)    #----����ת�÷���
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
##C_=np.concatenate((A_,B_,B_,A_),axis=1)      #------�ɸı�ά�ȵĺϲ�
##
##print(C_)







##A=np.arange(12).reshape((3,4))
##print(A)
##
##print(np.split(A,2,axis=1))                  #-----�ָ�
##print(np.vsplit(A,3))
##print(np.hsplit(A,2))
##
##print(np.array_split(A,2,axis=0))              #----�ǵȷָ�




##a=np.arange(4)
##b=a
##c=a
##d=b
##a[0]=11
##
##b_=a.copy()   # --------�޹�����ֵ





#��������������������������������������������������������������������������������������������������������



##import pandas as pd
##import numpy as np


##s=pd.Series([1,3,6,np.nan,44,1])   #------nά����������ֵ��
##print(s)
##
##
##dates=pd.date_range('20180603',periods=6)   #----���ڸ�ʽ
##print(dates)
##
##
##df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])   #----����һ����ά�б�ָ�������ţ����б꣩
##print(df)
##
##
##
##
##
##df1=pd.DataFrame(np.arange(12).reshape((3,4)))  #-----Ĭ��Ϊ01234......���������б�
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
##print(df2.values)  #-----�����ֵ
##print(df2.describe())  #------������ϸ���㣬�Զ����Է���������
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
##print(df[:3])                  #--------��
##print(df[:'20180605'])
##
##print(df.loc['20180603'])   #----------��
##
##print(df.loc[:,['A','B']])   #----��Ϊ[:]�����У���Ϊ['A','B']����
##
##
##print(df.iloc[3:5,1:3])
##print(df.iloc[[1,3,5],1:3])
##
##
##
##
##print(df.ix[:3,['A','C']])            #----�������
##print(df.loc[:,['A','C']])            #----�޷�ͨ�������ţ�ֻ��ͨ������ֵ
##print(df.iloc[:3,[0,2]])              #----�޷���������ֵ
##
##print(df)
##print(df[df.A>8])          #------ɸѡA���д���8�ģ�ͬʱȥ������False��
##print(df.A>8)              #-----���Ϊ����ֵ








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
##df['E']=pd.Series([1,2,3,4,5,6],index=pd.date_range('20180603',periods=6))        #---������ݣ���������룩
##print(df)







##dates=pd.date_range('20180603',periods=6)
##df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
##df.iloc[0,1]=np.nan
##df.iloc[1,2]=np.nan
##
##print(df)
##print(df.dropna(axis=0,how='any'))#����'all'    #-----------�����κζ�ʧ���ݣ�nan)
##
##print(df.fillna(value=0))           #-----���nanΪ...
##
##print(df)
##print(df.isnull())
##
##print(np.any(df.isnull())==True) #-----������������Ƿ���� NaN, ������ھͷ��� True
##







##data=pd.read_csv('student.csv')
##print(data)
##
##
##data.to_pickle('student2.pickle')






#�ϲ���

##df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])     #-------ones()ָ��Ԫ��Ϊȫͬ
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
##res=pd.concat([df1,df2],axis=1,join_axes=[df1.index])   #-------����df1������������
##print(res_)
##print(res)








##df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])     #-------ones()ָ��Ԫ��Ϊȫͬ
##df2=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
##df3=pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
##
##
##
##
##
##res=df1.append([df2,df3],ignore_index=True)         #-----�ͺϲ������ַ���(appendֻ��һά�ϲ���axis��
##print(res)
##res=pd.concat([df1,df2,df3],axis=0,ignore_index=True)
##print(res)



##df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
##s1=pd.Series([1,2,3,4],index=['a','b','c','d'])   #-----�����Զ���������ֵ
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









#��䣺
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
##res=pd.merge(left,right,on=['key1','key2'])   #-------Ĭ��how='inner'
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
##res=pd.merge(df1,df2,on='col1',how='outer',indicator=True)     #------��䷽ʽ˵��
##print(res)
##
##
##
##res=pd.merge(df1,df2,on='col1',how='outer',indicator='indicator_column')
##print(res)





##left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
##                     'B': ['B0', 'B1', 'B2']},
##                     index=['K0', 'K1', 'K2'])       #-------ָ������ֵ
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
##res=pd.merge(left,right,left_index=True,right_index=True,how='outer') #----��������ֵ�����
##print(res)









##boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
##girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
##
##print(boys)
##print(girls)
##
##res=pd.merge(boys,girls,on='k',suffixes=['_boy','_girl'],how='inner')    #-----������DataFrame������ͬ����ʱ���������渽�Ӻ�׺����
##print(res)
##
##res=pd.merge(boys,girls,on='k',suffixes=['_boy','_girl'],how='outer')
##print(res)






##import matplotlib.pyplot as plt


##data=pd.Series(np.random.randn(10),index=np.arange(10))
##print(data)
##data.cumsum()
##data.plot()    #----��matplottlib�ṩһ��Yֵ
##plt.show()     #----��ͼ


##data=pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=list('ABCD'))#['A','B','C','D'])
##data=data.cumsum()
##print(data.head())   #----ǰ����
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


#����������������������������������������������������������������������������������������������������������������������������

