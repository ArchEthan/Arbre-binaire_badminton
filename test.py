class Match:
    def __init__(self, joueur1=None, joueur2=None):
        self.left = None
        self.right = None
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.gagnant = None

    # Met à jour les joueurs à partir des sous-matchs
    def mettre_a_jour(self):
        if self.left and self.right:
            self.joueur1 = self.left.gagnant
            self.joueur2 = self.right.gagnant

    # Simule le match
    def jouer(self):
        self.mettre_a_jour()  # s'assure que les joueurs sont à jour
        if self.joueur1 and self.joueur2 and not self.gagnant:
            # Logique simple : joueur1 gagne
            self.gagnant = self.joueur1

# Affiche l'arbre
def afficher_arbre_graphique(match, prefix="", is_left=True):
    if match.right:
        afficher_arbre_graphique(match.right, prefix + ("│   " if is_left else "    "), False)
    print(prefix + ("└── " if is_left else "┌── ") + f"[{match.joueur1 or '-'} vs {match.joueur2 or '-'}] -> {match.gagnant or '-'}")
    if match.left:
        afficher_arbre_graphique(match.left, prefix + ("    " if is_left else "│   "), True)

# --- 16e de finale ---
m1 = Match("Equipe A", "Equipe B"); m1.gagnant = "Equipe A"
m2 = Match("Equipe C", "Equipe D"); m2.gagnant = "Equipe C"
m3 = Match("Equipe E", "Equipe F"); m3.gagnant = "Equipe E"
m4 = Match("Equipe G", "Equipe H"); m4.gagnant = "Equipe G"
m5 = Match("Equipe I", "Equipe J"); m5.gagnant = "Equipe I"
m6 = Match("Equipe K", "Equipe L"); m6.gagnant = "Equipe K"
m7 = Match("Equipe M", "Equipe N"); m7.gagnant = "Equipe M"
m8 = Match("Equipe O", "Equipe P"); m8.gagnant = "Equipe O"

# --- Quarts ---
q1 = Match(); q1.left = m1; q1.right = m2
q2 = Match(); q2.left = m3; q2.right = m4
q3 = Match(); q3.left = m5; q3.right = m6
q4 = Match(); q4.left = m7; q4.right = m8

# --- Demi-finales ---
d1 = Match(); d1.left = q1; d1.right = q2
d2 = Match(); d2.left = q3; d2.right = q4

# --- Finale ---
finale = Match(); finale.left = d1; finale.right = d2

# Fonction récursive pour jouer tous les matchs
def jouer_tournoi(match):
    if match is None:
        return
    jouer_tournoi(match.left)
    jouer_tournoi(match.right)
    match.jouer()

# Jouer le tournoi complet
jouer_tournoi(finale)

# Affichage
print("Arbre complet du tournoi :")
afficher_arbre(finale)
print("\nVainqueur du tournoi :", finale.gagnant)
