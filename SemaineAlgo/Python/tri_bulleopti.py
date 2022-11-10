def triabulopti(t):
    cpt=0
    for i in range(len(t)-1,0,-1):
        for j in range(0,i):
            if(t[j+1]<t[j]):
                temporaire = t[j+1]
                t[j+1] = t[j]
                t[j] = temporaire
    return(t)
    
o=[7,8,5,2,3]
print(triabulopti(o))