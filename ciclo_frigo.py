
''' 
    Ciclo termodinamico:
    si danno come note le temperature all'evaporatore ed al condensatore
    Punto 0 : ingresso compressore
    Punto 1 : ingresso condensatore
    Punto 2 : ingresso valvola laminazione
    Punto 3 : ingresso evaporatore
    
    '''
    
import numpy as np 
import matplotlib.pyplot as plt
import CoolProp.CoolProp as CP
import grafico as gr


lib="HEOS"

fluidname= "R1234YF"

fluid   = CP.AbstractState(lib, fluidname )


"inizializzo i vettori"
T=np.zeros(4)
P=np.zeros(4)
H=np.zeros(4)
S=np.zeros(4)

"dati:"
T_ref=273.15
T_cond=40 #°C
T_eva=0   #°C
eta_comp=0.8

"Punto 0:"
T[0]=T_eva + T_ref

fluid.update(CP.QT_INPUTS, 1, T[0])

P[0]=fluid.p()
H[0]=fluid.hmass()
S[0]=fluid.smass()

"Punto 2:"
T[2]=T_cond + T_ref

fluid.update(CP.QT_INPUTS, 0, T[2])

P[2]=fluid.p()
H[2]=fluid.hmass()
S[2]=fluid.smass()

"Punto 3:"
P[3]=P[0]
H[3]=H[2]

fluid.update(CP.HmassP_INPUTS, H[3], P[3])

T[3]=fluid.T()
S[3]=fluid.smass()
Q=fluid.Q()

"Punto 1:"
P[1]=P[2]
'calcolo il caso isoentropico'
fluid.update(CP.PSmass_INPUTS, P[1], S[0])
H1_id=fluid.hmass()
"formula rendimento"
H[1]=H[0]+(H1_id-H[0])/eta_comp

fluid.update(CP.HmassP_INPUTS, H[1], P[1])
T[1]=fluid.T()
S[1]=fluid.smass()


"grafico:"
P=P*10**-5
H=H*10**-3
# =============================================================================
# 
# plt.plot(H,P,'r')
# plt.plot((H[3],H[0]),(P[3],P[0]),'r')
# 
# =============================================================================

gr.grafico_PH(P,H,'red',1,fluidname)
