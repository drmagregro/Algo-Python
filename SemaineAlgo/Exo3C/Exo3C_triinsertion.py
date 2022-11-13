import random
def stat(min,max,step,nbr):
    compteur=0
    for a in range(min,max+1,step):
        for p in range(nbr):
            tab=a*[0]
            for q in range(a):
                tab[q]=random.randint(0,100)
            cpt=0
            n = len(tab)
            for i in range(1, n):
                cle = tab[i]
                j = i - 1
                while j >= 0 and cle < tab[j]:
                    cpt=cpt+3
                    tab[j+1] = tab[j]
                    j = j - 1
                tab[j + 1] = cle
                cpt=cpt+1
        compteur=compteur+cpt
        print(a,compteur/nbr)

print(stat(10,20,5,5))