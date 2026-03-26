class Match:
  def __init__(self):
    self.left = None
    self.right = None
    self.joueur1 = None
    self.joueur2 = None
    self.gagnant = None

  def est_jouable(self):
    return self.left and self.right and \
      self.left.gagnant and self.right.gagnant

  def mettre_a_jour(self):
    if self.est_jouable():
      self.joueur1 = self.left.gagnant
      self.joueur2 = self.right.gagnant
          
  def est_jouable(self):
    return (
      self.left is not None and
      self.right is not None and
      self.left.gagnant is not None and
      self.right.gagnant is not None and
      self.gagnant is None
    )

  def matchs_jouables(noeud):
    if noeud is None:
      return []

    jouables = []

    if noeud.est_jouable():
      jouables.append(noeud)

    jouables += matchs_jouables(noeud.left)
    jouables += matchs_jouables(noeud.right)

    return jouables


# feuilles (16e de finale)
m1 = Match()
m1.gagnant = "Equipe A"

m2 = Match()
m2.gagnant = "Equipe B"

# match suivant (8e)
m3 = Match()
m3.left = m1
m3.right = m2

m3.mettre_a_jour()

print(m3.joueur1, "vs", m3.joueur2)

