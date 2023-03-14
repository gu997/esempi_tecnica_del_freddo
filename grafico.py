from CoolProp.CoolProp import PropsSI
import numpy as np
import matplotlib.pyplot as plt

def curva_limitePH(fluidname):
    T_lim=np.linspace(250,PropsSI('Tcrit',fluidname),400)
    l=len(T_lim)
    T_l=np.zeros(2*l)
    H_l=np.zeros(2*l)
    
    for i in range(l):
        H_l[i]=PropsSI('H','Q',0,'T',T_lim[i],fluidname)
        T_l[i]=T_lim[i]
    for j in range(l):
        H_l[j+l]=PropsSI('H','Q',1,'T',T_lim[l-j-1],fluidname)
        T_l[j+l]=T_lim[l-j-1]
            
    P_l=np.zeros(2*l)
        
    for i in range(l):
        P_l[i]=PropsSI('P','Q',0,'T',T_lim[i],fluidname)
        T_l[i]=T_lim[i]
    for j in range(l):
        P_l[j+l]=PropsSI('P','Q',1,'T',T_lim[l-j-1],fluidname)
        T_l[j+l]=T_lim[l-j-1]
    
    plt.plot(H_l/1000,P_l/100000,'k')    

def isoentropiche(fluidname):
    len_s=11
    len_p=100
    S=np.linspace(1,1.7,len_s)*1000
    P=np.linspace(1,40,len_p)*100000
    H=np.zeros(len_p)
    for i in range (len_s):
        for j in range(len_p):
            H[j]=PropsSI('H','P',P[j],'S',S[i],fluidname)
        plt.plot(H/1000,P/100000,'b',linewidth=0.5)
        
def isoterme(fluidname):
    P_min=1
    P_max=40
    passo=10
    len_p=30
    T_crit=PropsSI('Tcrit',fluidname)
    T1=np.arange(T_crit,0+273.15,-passo)
    T2=np.arange(T_crit,T_crit+30,passo)
    P=np.linspace(P_min,P_max,len_p)*100000
    H=np.zeros(len_p)
    for i in range (1,len(T2)):
        for j in range(len_p):
            H[j]=PropsSI('H','P',P[j],'T',T2[i],fluidname)
        plt.plot(H/1000,P/100000,'g',linewidth=0.5)
    
    len_p=200
    P=np.linspace(P_min,P_max,len_p)*100000
    H=np.zeros(len_p)
    for j in range(len_p):      
        H[j]=PropsSI('H','P',P[j],'T',T_crit,fluidname)
    plt.plot(H/1000,P/100000,'g',linewidth=0.5)
        
    for i in range (1,len(T1)):
        P_sat=PropsSI('P','Q',0,'T',T1[i],fluidname)
        len_p=15
        P1=np.linspace(P_min*10**5,P_sat-10,len_p)
        P2=np.linspace(P_sat+10,P_max*10**5,len_p)
        H=np.zeros(len_p)
        for j in range(len_p):
            H[j]=PropsSI('H','P',P1[j],'T',T1[i],fluidname)
        plt.plot(H/1000,P1/100000,'g',linewidth=0.5)
        
        H=np.zeros(len_p)
        for j in range(len_p):
            H[j]=PropsSI('H','P',P2[j],'T',T1[i],fluidname)
        plt.plot(H/1000,P2/100000,'g',linewidth=0.5)
    
        plt.plot(np.array([PropsSI('H','Q',0,'T',T1[i],fluidname),PropsSI('H','Q',1,'T',T1[i],fluidname)])/1000,np.array([P_sat,P_sat])/100000,'g',linewidth=0.5)
       
        

   
    
def grafico_PH(P,H,color,number,fluidname,xlim=[250, 410],ylim=[0, 15]):
    plt.figure(dpi=200)
    curva_limitePH(fluidname)
    isoentropiche(fluidname)
    isoterme(fluidname)
    
    plt.plot(H,P,'--',color=color)
    plt.plot((H[0],H[3]),(P[0],P[3]),'--',color=color)
    
    
    k=0
    xx=np.array([5,5,5,5])
    yy=np.array([0,0,0,0])
    for i,j in zip(H,P):
        if number==1:
            plt.annotate(str(k),xy=(i+xx[k],j+yy[k]))
        plt.plot(i,j,'o',color=color)
        k=k+1
        
   
    plt.xlabel("H [kJ/kg]")
    plt.ylabel("P [bar]")
    plt.title('Diagramma P-H')
    plt.grid()
    plt.xlim(xlim)
    plt.ylim(ylim)
    
    
 