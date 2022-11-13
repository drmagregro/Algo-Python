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
    print("le nombre de comparaisons et d'affectations est égale à: ") 
    print(cpt)           
    return(t)

def stat(min,max,step,nbr):
    compteur=0
    for a in range(min,max+1,step):
        for p in range(nbr):
            t=a*[0]
            for q in range(a):
                t[q]=random.randint(0,100)
            cpt=0
            for i in range(len(t)-1,0,-1):
                for j in range(0,i):
                    cpt=cpt+1
                    if(t[j+1]<t[j]):
                        temporaire = t[j+1]
                        t[j+1] = t[j]
                        t[j] = temporaire
                        cpt=cpt+3
            compteur=compteur+cpt
        print(a,compteur/nbr)
            
            # print("le nombre de comparaisons et d'affectations est égale à: ") 
            # print(cpt)           
            # print(t)



    
# p=[9,8,7,6,5,4,3,2,1,0]
# p=[0,1,2,3,4,5,6,7,8,9]
# print(triabulopti(p))

print(stat(10,20,5,5))