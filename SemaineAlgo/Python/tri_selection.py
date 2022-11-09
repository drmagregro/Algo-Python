def tri_selection(tab):
    n = len(tab)
    for i in range(n-1):
        pos_min = i
        for j in range(i+1, n):
            if tab[j] < tab[pos_min]:
                pos_min = j
        tmp = tab[i]
        tab[i] = tab[pos_min]
        tab[pos_min] = tmp