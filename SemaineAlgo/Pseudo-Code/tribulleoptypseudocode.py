# Début
#     fonction triabulleopti(tableau)
#         variable longueur_de_tableau
#         variable(temporaire) 
#         variable premiereitération
#         variable deuxiemeiteration
#         pour "premiereiteration" allant de la longueur_de_tableau-1 à 0 par pas de -1
#             pour "deuxiemeiteration" allant de 0 à "premiereiteration"
#                 si tableau["deuxiemeiteration"+1] > tableau["deuxiemeiteration"]
#                     "temporaire" <- tableau("deuxiemeiteration"+1)
#                     tableau("deuximeiteration"+1) <- tableau("deuximeiteration")
#                     tableau("deuximeiteration") <- "temporaire"
#                 fin si
#             fin pour
#         fin pour
#     afficher tableau
# fin 
