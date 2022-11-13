def tri_bulle(tableau):
    permutation = True
    cpt=0
    passage = 0
    while permutation == True:
        permutation = False
        cpt=cpt+1
        passage = passage + 1
        for en_cours in range(0, len(tableau) - passage):
            if tableau[en_cours] > tableau[en_cours + 1]:
                permutation = True
                cpt=cpt+1
                # On echange les deux elements
                tableau[en_cours], tableau[en_cours + 1] = \
                tableau[en_cours + 1],tableau[en_cours]
                cpt=cpt+3
    print(cpt)
    return tableau  

tableau = [9,8,7,6,5,4,3,2,1,0]
# tableau = [0,1,2,3,4,5,6,7,8,9]
print(tri_bulle(tableau))