import utils as u
def menu_1():
    print("1- Ouvrir un compte")
    print("2- Fermeture d'un compte")
    print("3- Effectuer une operation")
    choix = int(input("--> "))
    return choix
# ................................................................................................
def get_ligne_fichier(nom_fichier):
    fichier_clients = open(nom_fichier, "r")
    lignes = fichier_clients.readlines() #On lit le contenu du fichier et on le stock dans une variable (lignes)
    fichier_clients.close()
    return lignes
# ................................................................................................
def menu_2():
    print("1- Deposer de l'argent sur le compte")
    print("2- Retirer de l'argent du compte")
    print("3- Afficher le solde du compte")
    print("4- Afficher les 10 dernieres operations(achats)sur un compte")
    print("5- Changement du NIP")
    print("6- Faire un achat")
    choix=int(input("--> "))
    return choix
# ................................................................................................
def fermeture_compte():
    print('Suppression du compte')
    #Ouvert le fichier en mode lecture
    lignes=get_ligne_fichier("clients.txt")
    compte = input("Entrer le numero de compte: ")
    pass_word=verification_nip()
    if check_password(compte,pass_word):

        #On ouvre le fichier en mode ecriture w(ecrase l'ancien conntenu)
        fichier_clients = open("clients.txt", "w")
        #une boucle qui va remplir a nouveau le fichier sans le compte a supprimer
        for ligne in lignes:
            list_ligne= ligne.split()
            if compte != list_ligne[0]: # SANS LE COMPTE DU CLIENT  A SUPPRIMER
                fichier_clients.write(ligne)
        fichier_clients.close()
        print("Le numero de compte {} a ete supprime de la banque.\n".format(compte))
    else:
        print("La suppression a echoue")
        print("Numero du compte ou mot de passe incorrect.")
# .....................................................................................................
def retirer_argent(compte,somme_a_retirer):
    # somme_a_retirer = float(input("Montant a retirer: "))
    lignes=get_ligne_fichier("clients.txt")
    fichier_clients = open("clients.txt", "w")
    for ligne in lignes:
        list_ligne= ligne.split()
        if compte != list_ligne[0]: # SANS LE COMPTE DU CLIENT  A SUPPRIMER
            fichier_clients.write(ligne)
        else:
            if somme_a_retirer>float(list_ligne[-1]):
                print("Votre solde est insuffisant pour effectuer cette operation.")
                fichier_clients.write(ligne)
            else:
                nouveau_solde = str(float(list_ligne[-1]) - somme_a_retirer)
                fichier_clients.write(list_ligne[0]+" "+list_ligne[1]+" "+list_ligne[2]+" "+list_ligne[3]+" "+list_ligne[4]+" "+list_ligne[5]+" "+nouveau_solde +"\n")
                print("Votre nouveau solde est: {} dollars".format(nouveau_solde))
    fichier_clients.close()
# ................................................................................................
def effectuer_operation(compte, marchand, produit):
    quantite=float(input("Tu veux pour combien de quantite? "))
    prix_unitaire=u.MARCHANT[marchand][produit]["prix"]
    prix_total=quantite*prix_unitaire
    fichier_achat=open("achat.txt","a")
    fichier_achat.write("{} {} {} {} {}\n".format(compte, marchand, produit, quantite, prix_total))
    retirer_argent(compte, prix_total)
    fichier_achat.close()
# ................................................................................................
def verification_nip():
    verifier_nip = False
    while verifier_nip == False:
        NIP = input('Code PIN: ') # On le gere dans une fonction
        if NIP.isnumeric():
            if len(NIP) ==4:
                verifier_nip = True
            else:
                print('NIP invalide doit etre de 4 chiffres')
        else: 
            print('NIP invalide (des chiffres)')
    return NIP
# ...................................................................................................
def deposer_argent(compte):
    somme_a_deposer = float(input("Montant a deposer: "))
    lignes=get_ligne_fichier("clients.txt")
    fichier_clients = open("clients.txt", "w")
    for ligne in lignes:
        list_ligne= ligne.split()
        if compte != list_ligne[0]: # SANS LE COMPTE DU CLIENT  A SUPPRIMER
            fichier_clients.write(ligne)
        else:
            nouveau_solde = str(somme_a_deposer + float(list_ligne[-1]))
            fichier_clients.write(list_ligne[0]+" "+list_ligne[1]+" "+list_ligne[2]+" "+list_ligne[3]+" "+list_ligne[4]+" "+list_ligne[5]+" "+nouveau_solde +"\n")
            print("Votre nouveau solde est: {} dollars".format(nouveau_solde))
    fichier_clients.close()
# ......................................................................................................
def afficher_solde(compte):
    fichier_clients = open("clients.txt", "r")
    lignes = fichier_clients.readlines() #On lit le contenu du fichier et on le stock dans une variable (lignes)
    fichier_clients.close()
    for ligne in lignes:
        list_ligne= ligne.split()
        if compte == list_ligne[0]: # SANS LE COMPTE DU CLIENT  A SUPPRIMER
            solde  = list_ligne[-1]
            print("Votre solde est de: {} $".format(solde))
    fichier_clients.close()
# ................................................................................................
def changement_pin(compte):
    print("Changement du NIP")
    NIP=verification_nip()
    lignes=get_ligne_fichier("clients.txt")
    fichier_clients = open("clients.txt", "w")
    for ligne in lignes:
        list_ligne= ligne.split()
        if compte != list_ligne[0]: # SANS LE COMPTE DU CLIENT  A SUPPRIMER
            fichier_clients.write(ligne)
        else:
            # NIP = str(NIP)
            fichier_clients.write(list_ligne[0]+" "+list_ligne[1]+" "+list_ligne[2]+" "+list_ligne[3]+" "+list_ligne[4]+" "+NIP+" "+list_ligne[6] +"\n")
            print("NIP modifie avec succes")
    fichier_clients.close()
# ................................................................................................

def affiche_marchant():
    print("Liste des marchands ")
    for marchant in u.LISTE_MARCHANDS:
        print("{}.{}".format(marchant, u.LISTE_MARCHANDS[marchant]))
# .......................................................................................................
def recup_option():
    return int(input("Selectionner votre option: "))
# ................................................................................................
def affiche_produit(marchand):
    print("La liste des produits de {} :".format(marchand))
    for produit in u.MARCHANT[marchand]:
        print(" {}: {}$/{}".format(produit,u.MARCHANT[marchand][produit]["prix"],u.MARCHANT[marchand][produit]["unite"]))

# ................................................................................................
def check_password(compte, code_pin):
    lignes=get_ligne_fichier("clients.txt")
    ligne_chaine=[]
    for ligne in lignes:
        ligne_chaine.append(ligne.split())
    dico={}
    for x in ligne_chaine:
        dico[x[0]]=x[-2]
    if compte in dico and dico[compte]==code_pin:
        return True
    else:
        return False
# ................................................................................................
         
