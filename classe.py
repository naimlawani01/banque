class Vehicule:
    def __init__(self,nom, vitesse):
        self.nom_vehicule=nom
        self.vitesse_vehicule=vitesse


v1=Vehicule("Avion", "2000km/s")
print(v1.nom_vehicule)
print(v1.vitesse_vehicule)

