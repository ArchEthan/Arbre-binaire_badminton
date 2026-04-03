import random

class Match:
    def __init__(self, joueur1=None, joueur2=None, proba_j1=0.5):
        self.left = None
        self.right = None
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.gagnant = None
        self.proba_j1 = proba_j1
        self.y = 0


def creer_match(j1, j2, proba_j1=0.5):
    return Match(j1, j2, proba_j1)


# --- Arbre ---
m1 = creer_match("A", "B", 0.7)
m2 = creer_match("C", "D", 0.6)
m3 = creer_match("E", "F", 0.5)
m4 = creer_match("G", "H", 0.8)
m5 = creer_match("I", "J", 0.4)
m6 = creer_match("K", "L", 0.3)
m7 = creer_match("M", "N", 0.9)
m8 = creer_match("O", "P", 0.2)

q1 = Match(); q1.left = m1; q1.right = m2
q2 = Match(); q2.left = m3; q2.right = m4
q3 = Match(); q3.left = m5; q3.right = m6
q4 = Match(); q4.left = m7; q4.right = m8

d1 = Match(); d1.left = q1; d1.right = q2
d2 = Match(); d2.left = q3; d2.right = q4

finale = Match(); finale.left = d1; finale.right = d2


# --- Simulation probabiliste ---
def jouer_tournoi(match):
    if match is None:
        return None
    if match.left is None and match.right is None:
        # feuille : tirage avec proba
        match.gagnant = match.joueur1 if random.random() < match.proba_j1 else match.joueur2
        return match.gagnant

    g1 = jouer_tournoi(match.left)
    g2 = jouer_tournoi(match.right)

    match.joueur1 = g1
    match.joueur2 = g2
    match.proba_j1 = 0.5  # par défaut, on peut changer
    match.gagnant = match.joueur1 if random.random() < match.proba_j1 else match.joueur2
    return match.gagnant


jouer_tournoi(finale)


# --- Positionnement ---
def assigner_positions(match, y=0, step=2):
    if match.left is None and match.right is None:
        match.y = y
        return y + step
    y = assigner_positions(match.left, y, step)
    y = assigner_positions(match.right, y, step)
    match.y = (match.left.y + match.right.y) // 2
    return y

assigner_positions(finale)


# --- Dessin ---
largeur = 80
hauteur = 32
canvas = [[" "]*largeur for _ in range(hauteur)]

def draw(match, x):
    if match is None:
        return
    y = match.y
    texte = match.gagnant or "?"
    for i, c in enumerate(texte):
        canvas[y][x+i] = c

    if match.left and match.right:
        y1 = match.left.y
        y2 = match.right.y

        for i in range(min(y1, y2), max(y1, y2)+1):
            canvas[i][x-2] = "│"

        for i in range(x-6, x-2):
            canvas[y1][i] = "─"
            canvas[y2][i] = "─"

        canvas[y1][x-2] = "┌"
        canvas[y2][x-2] = "└"

        draw(match.left, x-8)
        draw(match.right, x-8)

draw(finale, 70)

# --- Affichage ---
for ligne in canvas:
    print("".join(ligne))

print("\nVainqueur :", finale.gagnant)
