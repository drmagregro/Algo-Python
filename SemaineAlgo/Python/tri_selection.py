def tri_selection(tab):

    cpt = 0
    n = len(tab)
    for i in range(n-1):
        pos_min = i
        for j in range(i+1, n):
            cpt += 1 ## Comparaison donc on ajt 3
            if tab[j] < tab[pos_min]:
                pos_min = j
                cpt += 3 ## Echanges donc on ajt 3
        tmp = tab[i]
        tab[i] = tab[pos_min]
        tab[pos_min] = tmp
    print(cpt)
    return tab
    


tab = [9,7,6]
print(tri_selection(tab))
