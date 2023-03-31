from CoolProp.CoolProp import PropsSI
import numpy as np
import compressore as c
import grafici_termodinamici as gt

eps=0.8


T=np.zeros(6)
P=np.zeros(6)
H=np.zeros(6)
S=np.zeros(6)
m=np.zeros(3)

T_ref=273.15

"PUNTI NOTI A PRIORI"

T[3]=40+T_ref
P[3]=95*10**5   #iperparametro
H[3]=PropsSI('H','T',T[3],'P',P[3],'CO2')

T[0]=-5+T_ref
P[0]=PropsSI('P','T',T[0],'Q',1,'CO2')
H[0]=PropsSI('H','T',T[0],'Q',1,'CO2')
        
 


T[1]=T[0] + eps*(T[3]-T[0])
P[1]=P[0]
H[1]=PropsSI('H','T',T[1],'P',P[1],'CO2')
#m[1]=c.Portata(T[0], T[1], P[3])

H[4]=H[3]-H[1]+H[0]
P[4]=P[3]
T[4]=PropsSI('T','H',H[4],'P',P[4],'CO2')
S[4]=PropsSI('S','H',H[4],'P',P[4],'CO2')


P[5]=P[0]
H[5]=H[4]
T[5]=PropsSI('T','H',H[5],'P',P[5],'CO2')
S[5]=PropsSI('S','H',H[5],'P',P[5],'CO2')
       

T[2]=c.Temperatura_mandata(T[0]-T_ref, T[1]-T_ref, P[3]*10**-5)+T_ref
P[2]=P[3]
H[2]=PropsSI('H','T',T[2],'P',P[2],'CO2')
S[2]=PropsSI('S','T',T[2],'P',P[2],'CO2')


cop=(H[1]-H[3])/(H[2]-H[1])
print('cop='+str(cop))

gt.grafico_PH_semplice(P/100000,H/1000)

