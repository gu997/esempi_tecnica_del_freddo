from CoolProp.CoolProp import PropsSI
import numpy as np
import compressore as c
import grafici_termodinamici as gt


def ciclo_semplice(P_gc,T_gc, fluidname= "CO2"):
    eps=0.8
    
    
    T=np.zeros(6)
    P=np.zeros(6)
    H=np.zeros(6)
    S=np.zeros(6)
    m=np.zeros(3)
    
    T_ref=273.15
    
    "PUNTI NOTI A PRIORI"
    
    T[3]=T_gc+T_ref
    P[3]=P_gc*10**5   #iperparametro
    H[3]=PropsSI('H','T',T[3],'P',P[3],fluidname)
    
    T[0]=-5+T_ref
    P[0]=PropsSI('P','T',T[0],'Q',1,fluidname)
    H[0]=PropsSI('H','T',T[0],'Q',1,fluidname)
            
     
    
    
    T[1]=T[0] + eps*(T[3]-T[0])
    P[1]=P[0]
    H[1]=PropsSI('H','T',T[1],'P',P[1],fluidname)
    m[1]=c.Portata(T[0], T[1], P[3])
    
    H[4]=H[3]-H[1]+H[0]
    P[4]=P[3]
    T[4]=PropsSI('T','H',H[4],'P',P[4],fluidname)
    S[4]=PropsSI('S','H',H[4],'P',P[4],fluidname)
    
    
    P[5]=P[0]
    H[5]=H[4]
    T[5]=PropsSI('T','H',H[5],'P',P[5],fluidname)
    S[5]=PropsSI('S','H',H[5],'P',P[5],fluidname)
           
    
    T[2]=c.Temperatura_mandata(T[0]-T_ref, T[1]-T_ref, P[3]*10**-5)+T_ref
    P[2]=P[3]
    H[2]=PropsSI('H','T',T[2],'P',P[2],fluidname)
    S[2]=PropsSI('S','T',T[2],'P',P[2],fluidname)
    
    
    cop=(H[1]-H[3])/(H[2]-H[1])
    
    return T,P,H,S,cop


def ciclo_semplice_subcritico(T_gc,T_eva, fluidname= "CO2"):
    eps=0.8
    
    
    T=np.zeros(6)
    P=np.zeros(6)
    H=np.zeros(6)
    S=np.zeros(6)
    m=np.zeros(3)
    
    T_ref=273.15
    
    "PUNTI NOTI A PRIORI"
    
    T[3]=T_gc+T_ref
    H[3]=PropsSI('H','T',T[3],'Q',0,fluidname)
    P[3]=PropsSI('P','T',T[3],'Q',0,fluidname)
    
    T[0]=T_eva+T_ref
    P[0]=PropsSI('P','T',T[0],'Q',1,fluidname)
    H[0]=PropsSI('H','T',T[0],'Q',1,fluidname)
            
     
    
    
    T[1]=T[0] + eps*(T[3]-T[0])
    P[1]=P[0]
    H[1]=PropsSI('H','T',T[1],'P',P[1],fluidname)
    m[1]=c.Portata(T[0], T[1], P[3])
    
    H[4]=H[3]-H[1]+H[0]
    P[4]=P[3]
    T[4]=PropsSI('T','H',H[4],'P',P[4],fluidname)
    S[4]=PropsSI('S','H',H[4],'P',P[4],fluidname)
    
    
    P[5]=P[0]
    H[5]=H[4]
    T[5]=PropsSI('T','H',H[5],'P',P[5],fluidname)
    S[5]=PropsSI('S','H',H[5],'P',P[5],fluidname)
           
    
    T[2]=c.Temperatura_mandata(T[0]-T_ref, T[1]-T_ref, P[3]*10**-5)+T_ref
    P[2]=P[3]
    H[2]=PropsSI('H','T',T[2],'P',P[2],fluidname)
    S[2]=PropsSI('S','T',T[2],'P',P[2],fluidname)
    
    
    cop=(H[1]-H[3])/(H[2]-H[1])
    
    return T,P,H,S,cop
    

if __name__=='__main__':
    
    P_gc=95
    T_gc=40
    T,P,H,S,cop=ciclo_semplice(P_gc,T_gc)
    print('cop='+str(cop))
    
    gt.grafico_PH_semplice(P/100000,H/1000)
    
    T_gc=20
    T_eva=-5
    T,P,H,S,cop=ciclo_semplice_subcritico(T_gc,T_eva)
    print('cop='+str(cop))
    gt.grafico_PH_semplice(P/100000,H/1000)