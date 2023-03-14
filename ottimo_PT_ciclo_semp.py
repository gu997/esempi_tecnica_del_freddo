import CoolProp.CoolProp as CP
import numpy as np
import matplotlib.pyplot as plt

from impianto_senza_eiettore_function import ciclo_semplice

lib='HEOS'
fluid='CO2'
fld = CP.AbstractState(lib, fluid)

p_crit = fld.p_critical()*1e-5
t_crit= fld.T_critical()-273.15

n=50
m=6

T_gc=np.linspace(20,50,m-1)
T_gc= np.append(T_gc,t_crit)
T_gc=np.sort(T_gc)

P_gc=np.linspace(50,150,n)
COP=np.zeros((m,n))

for j in range(m):
    for i in range(n):
        T,P,H,S,cop=ciclo_semplice(P_gc[i],T_gc[j])
        COP[j,i]=cop
        #print('cop='+str(cop))


plt.figure(dpi=200)
for j in range(m):    
    plt.plot(P_gc,COP[j,:],label='$T_{gc}$ = '+str( np.round ( T_gc[j],2 )))


plt.plot([p_crit,p_crit], [COP.min(),COP.max()],'--',linewidth=1)

plt.xlabel("$ P_{gc} $ [bar]")
plt.ylabel("COP []")
plt.title('Curva ottimo $ P_{gc} $ ')
plt.grid()
plt.legend()
plt.show()  


