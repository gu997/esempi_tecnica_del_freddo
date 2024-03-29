import CoolProp.CoolProp as CP

lib="HEOS"
#lib="REFPROP"

fluidname= "CO2"
#fluidname= "Helium"


fluid   = CP.AbstractState(lib, fluidname )

P_tot=30*10**5
Q=0.6
fluid.update(CP.PQ_INPUTS, P_tot, Q)
fluid.update(CP.PT_INPUTS, 517685.170540156, 278.15)
fluid.update(CP.QT_INPUTS, 0.27193457276482425, 278.15)


fluid.p()
fluid.Q()
fluid.T()
fluid.hmass()
fluid.smass()


'esempio:'
#lib="HEOS"
lib="REFPROP"

fluidname= "R1233ZD(E)"

fluid   = CP.AbstractState(lib, fluidname )

T=30
fluid.update(CP.QT_INPUTS, 0, T+273.15)
fluid.p()
