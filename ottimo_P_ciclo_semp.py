import numpy as np
import matplotlib.pyplot as plt

from impianto_senza_eiettore_function import ciclo_semplice


n=50
P_gc=np.linspace(70,150,n)
COP=np.zeros(n)
T_gc=40

for i in range(n):
    T,P,H,S,cop=ciclo_semplice(P_gc[i],T_gc)
    COP[i]=cop
    #print('cop='+str(cop))

plt.figure(dpi=200)

plt.plot(P_gc,COP)
plt.xlabel("$ P_{gc} $ [bar]")
plt.ylabel("COP []")
plt.title('Curva ottimo $ P_{gc} $ ')
plt.grid()
plt.show()  