import random

def triabulopti(t):
    cpt=0
    for i in range(len(t)-1,0,-1):
        for j in range(0,i):
            cpt=cpt+1
            if(t[j+1]<t[j]):
                temporaire = t[j+1]
                t[j+1] = t[j]
                t[j] = temporaire
                cpt=cpt+3
    print("le nombre de comparaisons et d'affectations est égale à: ",cpt)           
    return(t)





    
p=[9,8,7,6,5,4,3,2,1,0]
# p=[0,1,2,3,4,5,6,7,8,9]
print(triabulopti(p))

