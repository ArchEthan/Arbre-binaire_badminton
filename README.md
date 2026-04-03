# Arbre-binaire_badminton
⚙️ Fonctionnalités
🌳 Structure du tournoi

    Représentation du tournoi sous forme d’un arbre binaire

    Chaque nœud contient :
        Informations du match
        Participants
        Résultat

    Les nœuds parents représentent les matchs suivants

🏁 Phases du tournoi

Le système prend en charge les différentes étapes :

    16ème de finale
    8ème de finale
    Quart de finale (1/4)
    Demi-finale (1/2)
    Finale

🥇 Gestion des matchs

    Enregistrement des résultats
    Détermination automatique du gagnant
    Accès au prochain match via la structure de l’arbre
    Mise à jour dynamique des nœuds

💾 Stockage des données

    Les informations sont stockées directement dans les nœuds de l’arbre

    Chaque nœud contient :
        Joueurs
        Gagnant

🔄 Logique de fonctionnement

    Initialisation des matchs (16ème de finale)
    Saisie des résultats
    Propagation des gagnants vers le niveau supérieur
    Construction automatique des phases suivantes
    Accès à la finale via la racine de l’arbre

📅 Exemple d'information de match

    Joueurs : A vs B
    Gagnant : A
