def tri_insertion(tab):
    
    cpt = 0
    n = len(tab)
    for i in range(1, n):
        cpt += 1 ## Comparaison donc on ajt 3
        cle = tab[i]
        j = i - 1
        while j >= 0 and cle < tab[j]:
            cpt += 3 ## Echanges donc on ajt 3
            tab[j+1] = tab[j]
            j = j - 1
        tab[j + 1] = cle
    print(cpt)
    return tab

tab = [9,7,12]
print(tri_insertion(tab))
