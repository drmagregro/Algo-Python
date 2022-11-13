def tri_selection(tab):
    n = len(tab)
    cpt=0
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
    print(cpt)
    return(tab)

# tab=[0,1,2,3,4,5,6,7,8,9]
tab=[9,8,7,6,5,4,3,2,1,0]
print(tri_selection(tab))