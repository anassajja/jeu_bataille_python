from random import shuffle, randint


class Carte:
    def __init__(self, f, c):
        self.__valeur = f
        self.__couleur = c

    def nom_carte(self):
        s = self.__valeur + " " + self.__couleur
        return s


class JeuDeCartes():
    def __init__(self):
        couleur = [chr(9824), chr(9829), chr(9827), chr(9830)]
        valeur = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi"]

        # Construction de la liste des 32 cartes
        self.__cartes = []
        for coul in couleur:
            for val in valeur:
                self.__cartes.append(Carte(val, coul))
        return

    # Melange des cartes
    def battre(self):
        shuffle(self.__cartes)

    # Afficher du jeu de carte
    def afficher(self):
        for carte in self.__cartes:
            print(carte.nom_carte(), end=" ")
        print()

    # distribuer une carte du jeu
    def distribuer(self):
        if len(self.__cartes) == 0:
            print("Plus aucune carte")
            return
        else:
            t = randint(0, len(self.__cartes) - 1)
            carte = self.__cartes[t]
            del (self.__cartes[t])  ## ou self.__cartes.pop(t)
            return carte

    def jouer_bataille(self, joueur1, joueur2):
        while len(joueur1) > 0 and len(joueur2) > 0:
            # Le code actuel de la fonction
            carte_joueur1 = joueur1.pop()
            carte_joueur2 = joueur2.pop()
            print("Le joueur 1 joue :", carte_joueur1.nom_carte())
            print("Le joueur 2 joue :", carte_joueur2.nom_carte())
            print("Joueur 1 a", len(joueur1), "cartes restantes.")
            print("Joueur 2 a", len(joueur2), "cartes restantes.")
            if carte_joueur1._Carte__valeur == carte_joueur2._Carte__valeur:
                print("Bataille !")
                cartes_bataille = [carte_joueur1, carte_joueur2]
                while carte_joueur1._Carte__valeur == carte_joueur2._Carte__valeur:
                    print("Les joueurs tirent chacun une carte face visible...")
                    for i in range(1):
                        if len(joueur1) == 0 or len(joueur2) == 0:
                            print("Plus assez de cartes pour continuer la bataille !")
                            if len(joueur1) > 0:
                                print("Joueur 1 a gagné le jeu !")
                            else:
                                print("Joueur 2 a gagné le jeu !")
                            return

                    else:
                        carte_joueur1 = joueur1.pop()
                        carte_joueur2 = joueur2.pop()
                        cartes_bataille.append(carte_joueur1)
                        cartes_bataille.append(carte_joueur2)
                    print("Le joueur 1 joue :", carte_joueur1.nom_carte())
                    print("Le joueur 2 joue :", carte_joueur2.nom_carte())
                    print("Joueur 1 a", len(joueur1), "cartes restantes.")
                    print("Joueur 2 a", len(joueur2), "cartes restantes.")

                if carte_joueur1._Carte__valeur > carte_joueur2._Carte__valeur:
                    print("Le joueur 1 remporte la bataille !")
                else:
                    print("Le joueur 2 remporte la bataille !")

                if carte_joueur1._Carte__valeur > carte_joueur2._Carte__valeur:
                    joueur1.extend(cartes_bataille)
                else:
                    joueur2.extend(cartes_bataille)
                print("Joueur 1 a", len(joueur1), "cartes restantes.")
                print("Joueur 2 a", len(joueur2), "cartes restantes.")
                print("**========================================================================================**")
            else:
                if carte_joueur1._Carte__valeur > carte_joueur2._Carte__valeur:
                    joueur1.extend([carte_joueur1, carte_joueur2])
                    print("Le joueur 1 remporte la manche !")
                else:
                    joueur2.extend([carte_joueur1, carte_joueur2])
                    print("Le joueur 2 remporte la manche !")
                print("Joueur 1 a", len(joueur1), "cartes restantes.")
                print("Joueur 2 a", len(joueur2), "cartes restantes.")
                print("**========================================================================================**")

        if len(joueur1) > 0:
            print("Joueur 1 a gagné le jeu !")
        else:
            print("Joueur 2 a gagné le jeu !")


jeu = JeuDeCartes()
cartesJoueur1 = []
cartesJoueur2 = []
print("**========================================================================================**")
print("Affichage Jeu initial :")
print("**========================================================================================**")
jeu.afficher()
print("**========================================================================================**")
input("Taper la touche Entrée pour mélanger le jeu de cartes !")
print("**========================================================================================**")
jeu.battre()
jeu.afficher()
print("**========================================================================================**")
input("Taper la touche Entrée pour distribuer 26 cartes au joueur !")
print("**========================================================================================**")
print("main du joueur 1 :")
for i in range(26):
    c = jeu.distribuer()
    cartesJoueur1.append(c)  # ou remplacer les 2 lignes par cartesJoueur1.append(jeu.tirer())
    print("Carte", i + 1, "\t:\t", (c.nom_carte()), end=" ")
print()
print("**========================================================================================**")
print("main du joueur 2 :")
for i in range(26):
    c = jeu.distribuer()
    cartesJoueur2.append(c)
    print("Carte", i + 1, "\t:\t", (c.nom_carte()), end=" ")
print()
print("**========================================================================================**")
input("Taper la touche Entrée pour tirer une carte pour chaque joueur !")
print("**========================================================================================**")
jeu.jouer_bataille(cartesJoueur1, cartesJoueur2)
print("**========================================================================================**")
