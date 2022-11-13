import random
def stat(min,max,step,nbr):
    compteur=0
    for a in range(min,max+1,step):
        for p in range(nbr):
            t=a*[0]
            for q in range(a):
                t[q]=random.randint(0,100)
            cpt=0
            permutation = True
            passage = 0
            while permutation == True:
                permutation = False
                cpt=cpt+1
                passage = passage + 1
                for en_cours in range(0, len(t) - passage):
                    if t[en_cours] > t[en_cours + 1]:
                        permutation = True
                        cpt=cpt+1
                        # On echange les deux elements
                        t[en_cours], t[en_cours + 1] = \
                        t[en_cours + 1],t[en_cours]
                        cpt=cpt+3
        compteur=compteur+cpt
        print(a,compteur/nbr)

print(stat(10,20,5,5))