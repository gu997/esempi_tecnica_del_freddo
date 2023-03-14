
def  Portata(Teva, Tasp, Pgc): #kg/h

    C1 = 647.861333
    C2 = 23.86872574
    C3 = -5.801421663
    C4 = -2.214435806
    C5 = 0.322007965
    C6 = 0.043223774
    C7 = 0.005835259
    C8 = -0.251500262
    C9 = 0.008367634
    C10 = -0.019162208
    
    portata = C1 + C2 * Teva + C3 * Tasp + C4 * Pgc + C5 * Teva ** 2 + C6 * Tasp ** 2 + C7 * Pgc ** 2 + C8 * Teva * Tasp + C9 * Tasp * Pgc + C10 * Pgc * Teva
    
    return portata
    
def Temperatura_mandata(Teva, Tasp, Pgc): #°C
    
    C1 = -40.67055897
    C2 = -2.393127965
    C3 = 1.337595844
    C4 = 1.645149629
    C5 = 0.017090146
    C6 = -0.004564506
    C7 = -0.003450209
    C8 = 0.008756045
    C9 = 0.001345215
    C10 = -0.00611009
    
    T_mandata = C1 + C2 * Teva + C3 * Tasp + C4 * Pgc + C5 * Teva ** 2 + C6 * Tasp ** 2 + C7 * Pgc ** 2 + C8 * Teva * Tasp + C9 * Tasp * Pgc + C10 * Pgc * Teva
    
    return T_mandata
    
def PotenzaE_C(Teva, Tasp, Pgc): 
    
    C1 = -0.75534463
    C2 = -0.161152048
    C3 = 0.000816267
    C4 = 0.110580865
    C5 = -0.00202722
    C6 = 0.00000707504
    C7 = -0.000184898
    C8 = 0.000014234
    C9 = -0.00000885697
    C10 = 0.001775837
    
    potenzaE_C = C1 + C2 * Teva + C3 * Tasp + C4 * Pgc + C5 * Teva ** 2 + C6 * Tasp ** 2 + C7 * Pgc ** 2 + C8 * Teva * Tasp + C9 * Tasp * Pgc + C10 * Pgc * Teva
    
    return potenzaE_C





if __name__=='__main__':
    import numpy as np
    Teva=0
    Tasp= Teva+10
    Pgc =100
    n=10
    m=6
    Teva=np.linspace(-5,5,n)
    Pgc=np.linspace(80,130,m)
    
    M=np.zeros([m,n])
    T_out=np.zeros([m,n])
    P_el=np.zeros([m,n])
    for i in range(m):
        M[i]=Portata(Teva, Tasp, Pgc[i])/3600
        T_out[i]=Temperatura_mandata(Teva, Tasp, Pgc[i])
        P_el[i]=PotenzaE_C(Teva, Tasp, Pgc[i])
        
        
    import matplotlib.pyplot as plt
    plt.figure(dpi=200)
    for i in range(m):
        plt.plot(Teva,M[i],label=str(Pgc[i])+' bar')
    plt.xlabel('$T_{eva}$ [°C]')
    plt.ylabel('m [kg/s]')
    plt.grid()
    plt.legend()
    
    import matplotlib.pyplot as plt
    plt.figure(dpi=200)
    for i in range(m):
        plt.plot(Teva,T_out[i],label=str(Pgc[i])+' bar')
    plt.xlabel('$T_{eva}$ [°C]')
    plt.ylabel('$T_{out}$ [°C]')
    plt.grid()
    plt.legend()
    
    import matplotlib.pyplot as plt
    plt.figure(dpi=200)
    for i in range(m):
        plt.plot(Teva,P_el[i],label=str(Pgc[i])+' bar')
    plt.xlabel('$T_{eva}$ [°C]')
    plt.ylabel('$P_{el}$ [kW]')
    plt.grid()
    plt.legend( loc='upper left')