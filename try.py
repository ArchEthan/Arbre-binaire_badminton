# feuilles
m1 = Match(); m1.gagnant = "A"
m2 = Match(); m2.gagnant = "B"
m3 = Match(); m3.gagnant = "C"
m4 = Match(); m4.gagnant = None  # pas encore joué

# niveau au-dessus
m5 = Match(); m5.left = m1; m5.right = m2
m6 = Match(); m6.left = m3; m6.right = m4

# finale
finale = Match(); finale.left = m5; finale.right = m6

# trouver matchs jouables
jouables = matchs_jouables(finale)

print(len(jouables))
