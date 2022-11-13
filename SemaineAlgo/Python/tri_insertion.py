def tri_insertion(tab):
    n = len(tab)
    cpt=0
    for i in range(1, n):
        cle = tab[i]
        j = i - 1
        while j >= 0 and cle < tab[j]:
            cpt=cpt+3
            tab[j+1] = tab[j]
            j = j - 1
        tab[j + 1] = cle
        cpt=cpt+1
    print(cpt)
    return(tab)

# tab=[0,1,2,3,4,5,6,7,8,9]
tab=[9,8,7,6,5,4,3,2,1,0]
print(tri_insertion(tab))