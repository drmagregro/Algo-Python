import random
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
            

print(stat(10,20,5,5))