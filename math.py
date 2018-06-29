import math



P=101.3
E=76.3 #氨气在水中的亨利系数 kPa
m=E/P #相平衡常数
p_L=998.2 #溶剂密度 kg/m^3
H=998.2/(76.3*18.02) #溶解度系数  kmol/(kpa*m^3)
p_Vm=101.3*29.27/(8.314*293.15) #混合气体平均密度 kg/m^3

u_V=0.065 #混合气体粘度 kg/(m*h)
u_L=1 #溶剂粘度 mPa*s












Y1=0.1/(1-0.1) #进塔气摩尔比
Y2=Y1*(1-0.98) #出塔气摩尔比
Q_N=3000+500*12
Q_V=Q_N*(0.1013*(273.15+20)/(0.1013*273.15)) #混合气体流量 m^3/h
V=Q_V/22.4*273.15/(273.15+20)*(1-0.1)  #非反应气体摩尔流量 kmol/h
L_Vmin=(Y1-Y2)/(Y1/m-0) 
L_V=1.3*L_Vmin
L=L_V*V   #溶剂摩尔流量 kmol/h
L_Wmin=0.08 #最小润湿速率 m^3/(m*h)
X1=V*(Y1-Y2)/L+0      #出塔液相组成














Vs=Q_V/3600  # m^3/s
W_V=Q_V*p_Vm  #气体质量流量 kg/h
W_L=L*18.02




d=38 #填料公称直径 mm
sita=228 #填料比表面积 m^2*m^(-3)
fia_f=133 #干填料因子系数 m^(-1)



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
    Y=0.25
    u_f=math.sqrt(Y*9.81*p_L/(fai_f*1*u_L**0.2*p_Vm))
    return u_f



def u_check(DN,u_f):
    u=4*Q_V/(3600*(math.pi*(DN/1000)**2))
    print(u)
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
    Umin=L_Wmin*sita
    U=4*W_L/(p_L*math.pi*(DN/1000)**2)
    if U<Umin:
        print('wrong,U=%f < Umin=%f'%(U,Umin))
        return False
    else:
        print('check!U=%f >= Umin=%f'%(U,Umin))
        return True


def main():
    print('D='+str(Tower_diameter(Get_u_f(fai_f))/1000)+'m')
    print('normalize diameter='+str(TowerDNorm(Tower_diameter(Get_u_f(fai_f))))+'mm')
    
















