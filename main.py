class Match:
    def __init__(self, joueur1=None, joueur2=None):
        self.left = None
        self.right = None
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.gagnant = None
        self.y = 0  # position verticale


def creer_match(j1, j2, gagnant):
    m = Match(j1, j2)
    m.gagnant = gagnant
    return m


# --- Arbre ---
m1 = creer_match("A", "B", "A")
m2 = creer_match("C", "D", "C")
m3 = creer_match("E", "F", "E")
m4 = creer_match("G", "H", "G")
m5 = creer_match("I", "J", "I")
m6 = creer_match("K", "L", "K")
m7 = creer_match("M", "N", "M")
m8 = creer_match("O", "P", "O")

q1 = Match(); q1.left = m1; q1.right = m2
q2 = Match(); q2.left = m3; q2.right = m4
q3 = Match(); q3.left = m5; q3.right = m6
q4 = Match(); q4.left = m7; q4.right = m8

d1 = Match(); d1.left = q1; d1.right = q2
d2 = Match(); d2.left = q3; d2.right = q4

finale = Match(); finale.left = d1; finale.right = d2


# --- Simulation ---
def jouer_tournoi(match):
    if match is None:
        return
    jouer_tournoi(match.left)
    jouer_tournoi(match.right)
    match.gagnant = match.left.gagnant if match.left else match.gagnant

jouer_tournoi(finale)


# --- POSITIONNEMENT ---
def assigner_positions(match, y=0, step=2):
    if match.left is None and match.right is None:
        match.y = y
        return y + step

    y = assigner_positions(match.left, y, step)
    y = assigner_positions(match.right, y, step)

    match.y = (match.left.y + match.right.y) // 2
    return y


assigner_positions(finale)


# --- DESSIN ---
largeur = 80
hauteur = 32
canvas = [[" "]*largeur for _ in range(hauteur)]


def draw(match, x):
    if match is None:
        return

    y = match.y
    texte = match.gagnant or "?"

    # écrire texte
    for i, c in enumerate(texte):
        canvas[y][x+i] = c

    if match.left and match.right:
        y1 = match.left.y
        y2 = match.right.y

        # vertical
        for i in range(min(y1, y2), max(y1, y2)+1):
            canvas[i][x-2] = "│"

        # horizontal
        for i in range(x-6, x-2):
            canvas[y1][i] = "─"
            canvas[y2][i] = "─"

        canvas[y1][x-2] = "┌"
        canvas[y2][x-2] = "└"

        draw(match.left, x-8)
        draw(match.right, x-8)


draw(finale, 70)


# --- AFFICHAGE ---
for ligne in canvas:
    print("".join(ligne))

print("\nVainqueur :", finale.gagnant)
