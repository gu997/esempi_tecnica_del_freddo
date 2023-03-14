import grafici_termodinamici as gt
import grafico as gr
import numpy as np
import matplotlib.pyplot as plt


from ciclo_CO2_NH3_fun import ciclo2level



class bT:
        pass
class hT:
    pass

'Dati:'
bT.T_eva=-30 #°C
bT.DT_pinch=5
hT.T_cond=40 #°C


bT.fluid='CO2'
hT.fluid='NH3'


'parametro:'
n=50
T_cond_list=np.linspace(-10,20,n)
cop=np.zeros(n)

for i in range(n):
    bT.T_cond=T_cond_list[i]
    cop[i] = ciclo2level(bT,hT)


plt.figure(dpi=200)

plt.plot(T_cond_list,cop)
plt.xlabel("$ P_{gc} $ [bar]")
plt.ylabel("COP []")
plt.title('Curva ottimo $ P_{gc} $ ')
plt.grid()
plt.show()      