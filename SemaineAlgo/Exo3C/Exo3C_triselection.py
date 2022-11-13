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
            for i in range(n-1):
                pos_min = i
                for j in range(i+1, n):
                    if tab[j] < tab[pos_min]:
                        cpt=cpt+1
                        pos_min = j
                cpt=cpt+3
                tmp = tab[i]
                tab[i] = tab[pos_min]
                tab[pos_min] = tmp
        compteur=compteur+cpt
        print(a,compteur/nbr)

print(stat(10,20,5,5))