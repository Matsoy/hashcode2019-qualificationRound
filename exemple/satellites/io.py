"""
    Extrait du code qui permet de faire les I/O
"""


def lectureFichier(self):
    """
    Lit le fichier et en extrait:
    le temps de la simulation
    le nombre de satellites
    les parametres initiaux des satellites:
        latitude de depart
        longitude de depart
        vitesse de depart
        changement d'orientation max d'un tour a l'autre
        orientation max
    le nombre d'images dans la collection
    les points d'interet:
        score rapporte pour la prise d'un point d'interet
        latitude
        longitude
        intervals de prise de vue requis
    """

    with open(self.nomFichier,'r') as f:
        #Premiere ligne pour le temps
        self.temps = Temps(int(f.readline()))
        #On creer les satellites
        for i in range(0, int(f.readline())):
            coord = f.readline().split(" ")
            self.listeSatellite.append(Satellite(int(coord[0]),int(coord[1]),float(coord[2]),int(coord[3]),int(coord[4]),i))
        #Ajout des collections d images
        for i in range(0, int(f.readline())):
            #line contient 1) Points 2) Nombre d images 3) Nombre d intervalles de temps
            line = f.readline().split(" ")
            images = []
            temps = []
            #Ajoute les coordonnees des images
            for p in range(0, int(line[1])):
                images.append([int(j) for j in f.readline().strip('\n').split(" ")])
                #Parcours de images pour initialiser listeCoordonneesTriees
                for coord in images:
                    #Si la coordonnees n'est pas deja dans listeCoordonneesTriees, alors on l'ajoute
                    if(coord not in self.listeCoordonneesTriees):
                        self.listeCoordonneesTriees.append(coord)
            #Ajoute les intervalles de temps
            for p in range(0, int(line[2])):
                temps.append(f.readline().strip('\n').split(" "))
            #Ajoute la collection
            self.listeCollection.append(Collection(line[0], images, temps))
        #Tri par latitude croissante et, si meme latitude par longitude decroissante
        self.trierListeCoordonneesTriees()
        #Initialise la liste des photos sur la trajectoire des satellites

def fichierSortie(self):
    """
    Ecrit le fichier de sortie contenant:
        le nombre de photos prises
        pour chaque photo prise:
            latitude du point d'interet
            longitude du point d'interet
            tour de la prise de vue
            numero du satellite ayant pris la prise de vue
    """
    # Pour eviter les duplications dans le fichier de sortie, dans le cas ou une seule prise de photo a permis d'avancer plusieurs collections
    listePointsPris = []
    # Parcours de toutes les coordonnees des collections validees
    for collect in self.listeCollectionValidee:
        for coord in collect.listeCoordonneesReussies:
            # Si les coordonnees du point ne sont pas dans listePointsPris, alors on les rajoute a la liste
            if not coord in listePointsPris:
                listePointsPris.append(coord)

    fichier = open("output.out", "w")
    # Ecriture du nombre total de coordonnees
    fichier.write(str(len(listePointsPris))+"\n")
    for coord in listePointsPris:
        fichier.write(str(coord[0])+ " " + str(coord[1]) + " " + str(coord[2]) + " " + str(coord[3]) + "\n")
    fichier.close()