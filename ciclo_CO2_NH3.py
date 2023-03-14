
''' 
ciclo sottoposto a CO2,
ciclo ad alta temperatura ad ammoniaca
    
    '''
from impianto_senza_eiettore_function import ciclo_semplice_subcritico
from ciclo_frigo_fun import ciclo_no_rig
import grafici_termodinamici as gt
import grafico as gr

class bT:
    pass
class hT:
    pass

'Dati:'
bT.T_eva=-30 #°C
bT.T_cond=5 #°C
DT_pinch=5
hT.T_cond=40 #°C


bT.fluid='CO2'
hT.fluid='NH3'

'prima risolvo il ciclo a bassa temperatura'
bT.T,bT.P,bT.H,bT.S,bT.cop=ciclo_semplice_subcritico(bT.T_cond,bT.T_eva,bT.fluid)

'poi risolvo il ciclo ad alta temperatura'
hT.T_eva = bT.T_cond-DT_pinch


hT.T,hT.P,hT.H,hT.S,hT.cop=ciclo_no_rig(hT.fluid,hT.T_cond,hT.T_eva)


bT.m=1
hT.m= bT.m*(bT.H[2]- bT.H[3]) / (hT.H[0]- hT.H[3])

cop= bT.m*(bT.H[0]- bT.H[5]) / ( bT.m*(bT.H[2]- bT.H[1])   + hT.m*(hT.H[1]- hT.H[0]) )
print('cop tot =',cop)


gt.grafico_PH_semplice(bT.P/100000,bT.H/1000)

gr.grafico_PH(hT.P*1e-5,hT.H*1e-3,'red',1,hT.fluid,xlim=[500, 2000],ylim=[0, 40])

