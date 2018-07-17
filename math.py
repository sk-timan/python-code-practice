import math



P=101.3
E=76.3 #氨气在水中的亨利系数 kPa
m=E/P #相平衡常数
p_L=998.2 #溶剂密度 kg/m^3
H=998.2/(76.3*18.02) #溶解度系数  kmol/(kpa*m^3)
p_Vm=101.3*27.8/(8.314*293.15) #混合气体平均密度 kg/m^3

u_V=0.065 #混合气体粘度 kg/(m*h)
u_L=1 #溶剂粘度 mPa*s












#Y1=0.1/(1-0.1) #进塔气摩尔比
a=float(input('please input Molar mass of ammonia(%):'))
Y1=float(a/(1-a))
Y2=Y1*(1-0.95) #出塔气摩尔比
#Q_N=3000+500*12
Q_N=float(3000+500*int(input('please input your group number:')))
Q_V=Q_N*(0.1013*(273.15+20)/(0.1013*273.15)) #混合气体流量 m^3/h
V=Q_V/22.4*273.15/(273.15+20)*(1-a)  #非反应气体摩尔流量 kmol/h
L_Vmin=(Y1-Y2)/(Y1/m-0) 
L_V=1.3*L_Vmin
L=L_V*V   #溶剂摩尔流量 kmol/h
L_Wmin1=0.08 #最小润湿速率 m^3/(m*h)  d<75mm
L_Wmin2=0.12
X1=V*(Y1-Y2)/L+0      #出塔液相组成














Vs=Q_V/3600  # m^3/s
W_V=Q_V*p_Vm  #气体质量流量 kg/h
W_L=L*18.02   #液体质量流量




##d=38 #填料公称直径 mm
##sita=228 #填料比表面积 m^2*m^(-3)
##fai_f=133 #干填料因子系数 m^(-1)
##Y=.22
d=int(input('please input Nominal diameter of packing(mm):')) 
sita=float(input('please input specific surface area of packing(m^2*m^(-3)):'))
fai_f=float(input('please input dry packing Factor(m^(-1)):'))
def Get_X():
    x=(W_L/W_V)*(p_Vm/p_L)**0.5
    return x
print('X=',Get_X())
Y=float(input("Finding the value of Y based on the Eckert's association diagram:"))













def Tower_diameter(u_f):
    miu=0.7*u_f
    D=math.sqrt(4*Vs/(math.pi*miu))
    return D*1000


def TowerDNorm(D):
    if D<=700:
        if D/100==int (D/100):
            return D
        else:
            D_Nor=(int(D/100))*100+50
            return D_Nor
    elif D>700 and D<=1000:
        D_Nor=math.ceil(D/100)
        return D_Nor
    elif D>1000:
        D_Nor=math.ceil((D-1000)/200)*200+1000
        return D_Nor
    else:
        raise ValueError('the value of D is not suitable')






def Get_X():
    x=(W_L/W_V)*(p_Vm/p_L)**0.5
    return x
def Get_u_f(fai_f):
    u_f=math.sqrt(Y*9.81*p_L/(fai_f*1*u_L**0.2*p_Vm))
    return u_f



def u_check(DN,u_f):
    u=4*Q_V/(3600*(math.pi*(DN/1000)**2))
    if u/u_f<0.5 or u/u_f>0.85:
        print('wrong,the u/u_f=%f is not in the range of 0.5~0.85'%(u/u_f))
        return False
    else:
        print('checked! u/u_f=',u/u_f)
        return True


def DN_check(DN):
    if DN/d>=8:
        print('check! DN/d=',DN/d)
        return True
    else:
        print('wrong,the DN/d=%f must over 8'%(DN/d))
        return False


    
def Liq_check(DN):
    if d<=75:
        Umin=L_Wmin1*sita
    else:
        Umin=L_Wmin2*sita
    U=4*W_L/(p_L*math.pi*(DN/1000)**2)
    if U<Umin:
        print('wrong,U=%f < Umin=%f'%(U,Umin))
        return False
    else:
        print('check!U=%f >= Umin=%f'%(U,Umin))
        return True



    

class makeD():
    def __init__(self):
        pass
    
    def Get_u_f(self):
        u_f=math.sqrt(Y*9.81*p_L/(fai_f*1*u_L**0.2*p_Vm))
        return u_f

    def Get_D(self):
            miu=0.7*self.Get_u_f()
            D=math.sqrt(4*Vs/(math.pi*miu))
            return D*1000

    def Get_DN(self):
        D=self.Get_D()
        print(D)
        if D<=700:
            if D/100==int (D/100):
                return D
            else:
                D_Nor=(int(D/100))*100+50
                return D_Nor
        elif D>700 and D<=1000:
            D_Nor=math.ceil(D/100)*100
            print(D_Nor)
            return D_Nor
        elif D>1000:
            D_Nor=math.ceil((D-1000)/200)*200+1000
            return D_Nor
        else:
            raise ValueError('the value of D is not suitable')

    def u_check(self):
        u=4*Q_V/(3600*(math.pi*(self.Get_DN()/1000)**2))
        print(self.Get_DN()/1000)
        print(self.Get_u_f())
        if u/self.Get_u_f()<0.5 or u/self.Get_u_f()>0.85:
            print('wrong,the u/u_f=%f is not in the range of 0.5~0.85'%(u/self.Get_u_f()))
            return False
        else:
            print('checked! u/u_f=',u/self.Get_u_f())
            return True


    def DN_check(self):
        if self.Get_DN()/d>=8:
            print('checked! DN/d=',self.Get_DN()/d)
            return True
        else:
            print('wrong,the DN/d=%f must over 8'%(self.Get_DN()/d))
            return False


    def Liq_check(self):
        if d<=75:
            Umin=L_Wmin1*sita
        else:
            Umin=L_Wmin2*sita
        U=4*W_L/(p_L*math.pi*(self.Get_DN()/1000)**2)
        if U<Umin:
            print('wrong,U=%f < Umin=%f'%(U,Umin))
            return False
        else:
            print('checked!U=%f >= Umin=%f'%(U,Umin))
            return True

##def main():
####    Q_N=float(3000+500*int(input('please input your group number:')))
####    a=float(input('please input Molar mass of ammonia(%):'))
####    Y1=float(a/(1-a))
####    d=int(input('please input Nominal diameter of packing(mm):')) 
####    sita=float(input('please input specific surface area of packing(m^2*m^(-3)):'))
####    fai_f=float(input('please input dry packing Factor(m^(-1)):'))  
####    print('X=',Get_X())
####    Y=float(input("Finding the value of Y based on the Eckert's association diagram:"))
##    makeD()
##    if makeD().u_check()==True and makeD().DN_check()==True and makeD().Liq_check()==True:
##        print('All checked,congratulations!')
##    else:
##        print("srroy,the results show that the date did't pass the test,you can change the data and try again")
##    makeZ()
##    print('The tower diameter(mm):',makeD().Get_DN())
##    print('Height of packing(m):',makeZ().Get_Z())
##    makeZ().Z_check()




Y1_=m*X1  #与X1相平衡的气相摩尔比
S=m*V/L #脱吸因数



def Get_N_OG():
    N_OG=1/(1-S)*math.log((1-S)*(Y1-0)/(Y2-0)+S)
    return N_OG



p_V=p_Vm  #混合气体密度 kg/m^3
u_l=3.6 #液体的粘度 kg/(m*h)
a_t=sita #填料总比表面积 m^2/m^3
U_L=4*W_L/(math.pi*(makeD().Get_DN()/1000)**2) #液体质量通量 kg/(m^2*h)
U_V=4*Q_V*p_V/(math.pi*(makeD().Get_DN()/1000)**2)  #气体质量通量 kg/(m^2*h)
sita_c=972000  #填料材料临界表面张力 kg/h^2
sita_L=940896 #液体表面张力 kg/h^2
g=1.27*10**8  #重力加速度 m/h
D_V=0.06804 #氨气在空气中扩散系数 m^2/h
D_L=6.336*10**(-6)#氨气在水中扩散系数 m^2/h
R=8.314  #气体常数 (m^3*kPa)/(kmol*K)
T=20+273.15 #温度 K
psi=1.45#阶梯环形状系数
u=4*Q_V/(3600*(math.pi*(makeD().Get_DN()/1000)**2))
u_f=makeD().Get_u_f()
omiga=math.pi*(makeD().Get_DN()/2000)**2 #塔截面积 m^2



def Onde():
    a_W=a_t*(1-math.exp(-1.45*(sita_c/sita_L)**0.75*(U_L/(a_t*u_l))**0.1*
                        (U_L**2*a_t/(p_L**2*g))**(-0.05)*(U_L**2/(p_L*sita_L*a_t))**0.2))
    k_G=0.237*(U_V/(a_t*u_V))**0.7*(u_V/(p_V*D_V))**(1/3)*(a_t*D_V/(R*T))
    k_L=0.0095*(U_L/(a_W*u_l))**(2/3)*(u_l/(p_L*D_L))**(-1/2)*(u_l*g/p_L)**(1/3)
    k_Ga=k_G*a_W*psi**1.1
    print(k_Ga,k_G,k_L)
    k_La=k_L*a_W*psi**0.4
    
    if u/u_f<=0.5:
        K_Ga=1/(1/k_Ga+1/(H*k_La))
    else:
        k_Ga_=(1+9.5*(u/u_f-0.5)**1.4)*k_Ga
        k_La_=(1+2.6*(u/u_f-0.5)**2.2)*k_La
        K_Ga=1/(1/k_Ga_+1/(H*k_La_))
        print(k_Ga_,K_Ga)
    H_OG=V/(K_Ga*101.3*omiga)
    return H_OG

def Get_Z():
    Z=Get_N_OG()*Onde()
    Z_=1.5*Z
    print(Z)
    return Z_

def Z_check():
    k=makeZ().Get_Z/makeD().Get_DN()
    if k>8:
        print('h/D=%f,Packing should be layered'%(k))
    else:
        print("Packing needn't be layered")

class makeZ():
    def __init__(self):
        pass
    def Get_N_OG(self):
        N_OG=1/(1-S)*math.log((1-S)*(Y1-0)/(Y2-0)+S)
        return N_OG
    def Onde(self):
        a_W=a_t*(1-math.exp(-1.45*(sita_c/sita_L)**0.75*(U_L/(a_t*u_l))**0.1*
                            (U_L**2*a_t/(p_L**2*g))**(-0.05)*(U_L**2/(p_L*sita_L*a_t))**0.2))
        k_G=0.237*(U_V/(a_t*u_V))**0.7*(u_V/(p_V*D_V))**(1/3)*(a_t*D_V/(R*T))
        k_L=0.0095*(U_L/(a_W*u_l))**(2/3)*(u_l/(p_L*D_L))**(-1/2)*(u_l*g/p_L)**(1/3)
        k_Ga=k_G*a_W*psi**1.1
        k_La=k_L*a_W*psi**0.4
        
        if u/u_f<=0.5:
            K_Ga=1/(1/k_Ga+1/(H*k_La))
        else:
            k_Ga_=(1+9.5*(u/u_f-0.5)**1.4)*k_Ga
            k_La_=(1+2.6*(u/u_f-0.5)**2.2)*k_La
            K_Ga=1/(1/k_Ga_+1/(H*k_La_))
        print(k_Ga_,K_Ga)
        H_OG=V/(K_Ga*P*omiga)
        return H_OG
    
    def Get_Z(self):
        Z=Get_N_OG()*Onde()
        print(Z)
        Z_=1.5*Z
        return Z_
    def Z_check(self):
        print(makeZ().Get_Z())
        k=makeZ().Get_Z()*1000/makeD().Get_DN()
        if k>8:
            print('h/D=%f,Packing should be layered'%(k))
        else:
            print("Packing needn't be layered")


makeD()
if makeD().u_check()==True and makeD().DN_check()==True and makeD().Liq_check()==True:
        print('All checked,congratulations!')
else:
        print("srroy,the results show that the date did't pass the test,you can change the data and try again")
makeZ()
print('The tower diameter(mm):',makeD().Get_DN())
print('Height of packing(m):',makeZ().Get_Z())
makeZ().Z_check()



































































