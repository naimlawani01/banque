import random
import fonctions as f
import utils as u

fichier_clients = open("clients.txt", "r+")

#Ouverture du compte (Nom, Prenom, Date de naissance, age, Et le  NIP)
choix = f.menu_1()
if choix==1:
    #On recupere les info du client et on les met dans le fichier
    nom = input('Nom du client: ')
    prenom = input('Prenom du client: ')
    date_de_naissance = input("Date de naissance (jj/mm/aaaa): ")
    age = input("Age :")
    NIP=f.verification_nip()          
    numero_aleatoire = str(random.randint(100000, 999999))
    position_du_client = str(len(fichier_clients.readlines()) +1)
    # print(position_du_client)
    numero_de_compte = "adama-"+numero_aleatoire+'-'+position_du_client
    solde=float(input("Votre solde($): "))
    # print(numero_de_compte)
    fichier_clients.write(numero_de_compte+ '  '+ nom+ '  '+ prenom +'  '+ date_de_naissance+ '  '+ age+ '  '+ NIP + '  '+ str(solde)+'\n')
fichier_clients.close()
if choix==2:
        f.fermeture_compte() 
if choix==3:
    compte = input("Entrer le numero de compte: ")
    NIP=f.verification_nip()
    while f.check_password(compte,NIP)==False:
        print('Numero de compte ou Mot de passe incorrecte')
        compte = input("Entrer le numero de compte: ")
        NIP=f.verification_nip()
    continuer = True
    liste_choix_continuer=['n','o']
    while continuer:
        if f.check_password(compte,NIP):
            choix_2 = f.menu_2()
            if choix_2 == 1:
                f.deposer_argent(compte)
            if choix_2 == 2:
                somme_a_retirer = float(input("Montant a retirer: "))
                f.retirer_argent(compte,somme_a_retirer)
            if choix_2 == 3:
                f.afficher_solde(compte)
            if choix_2==4:
                liste_achats=f.get_ligne_fichier("achat.txt")
                l=[]
                operations=[]
                for elements in liste_achats:
                    l.append(elements.split())
                for premier_element in l:
                    if compte==premier_element[0]:
                        operations.append(premier_element)
                
                nombre_historique_transaction= int(10)
                a=operations[-nombre_historique_transaction:]
                if len(a)==0:
                    print('Aucune transaction pour ce compte')
                else: 
                    print('Historique des {} deniere(s) operations(achat) sur le compte {}: \n'.format(nombre_historique_transaction,compte))
                    for x in a:
                        print(" ".join(x))
            if choix_2 == 5:
                f.changement_pin(compte)
            if choix_2==6:
                f.affiche_marchant()
                option_choix_marchant=f.recup_option()
                if option_choix_marchant==1:
                    marchand=u.LISTE_MARCHANDS[option_choix_marchant]
                    f.affiche_produit(marchand)
                    produit=input("Qu'est ce que vous voulez acheter? ")
                    if produit in u.MARCHANT[marchand].keys():
                        f.effectuer_operation(compte, marchand, produit)
                elif option_choix_marchant==2:
                    marchand=u.LISTE_MARCHANDS[option_choix_marchant]
                    f.affiche_produit(marchand)
                    produit=input("Qu'est ce que vous voulez acheter? ")
                    if produit in u.MARCHANT[marchand].keys():
                        f.effectuer_operation(compte, marchand, produit)
                elif option_choix_marchant==3:
                    marchand=u.LISTE_MARCHANDS[option_choix_marchant]
                    f.affiche_produit(marchand)
                    produit=input("Qu'est ce que vous voulez acheter? ")
                    if produit in u.MARCHANT[marchand].keys():
                        f.effectuer_operation(compte, marchand, produit)
                    
        else:
            print("Numero du compte ou mot de passe incorrect.")

        choix_continuer = input('Vous voulez effectuer une autre operation ?(o/n): ').lower()
        while choix_continuer not in liste_choix_continuer:
            print("VOUS DEVEZ REPONDRE PAR : (o) OU (n)\n")
            choix_continuer = input('Vous voulez effectuer une autre operation ?(o/n): ').lower()
        if choix_continuer=='n':
            continuer =False
import random
import fonctions as f
import utils as u

run=True
while run:
    liste_choix=['n','o']
    fichier_clients = open("clients.txt", "r+")

    #Ouverture du compte (Nom, Prenom, Date de naissance, age, Et le  NIP)
    choix = f.menu_1()
    if choix==1:
        #On recupere les info du client et on les met dans le fichier
        nom = input('Nom du client: ')
        prenom = input('Prenom du client: ')
        date_de_naissance = input("Date de naissance (jj/mm/aaaa): ")
        age = input("Age :")
        NIP=f.verification_nip()          
        numero_aleatoire = str(random.randint(100000, 999999))
        position_du_client = str(len(fichier_clients.readlines()) +1)
        # print(position_du_client)
        numero_de_compte = "adama-"+numero_aleatoire+'-'+position_du_client
        solde=float(input("Votre solde($): "))
        # print(numero_de_compte)
        fichier_clients.write(numero_de_compte+ '  '+ nom+ '  '+ prenom +'  '+ date_de_naissance+ '  '+ age+ '  '+ NIP + '  '+ str(solde)+'\n')
    fichier_clients.close()
    if choix==2:
            f.fermeture_compte() 
    if choix==3:
        compte = input("Entrer le numero de compte: ")
        NIP=f.verification_nip()
        while f.check_password(compte,NIP)==False:
            print('Numero de compte ou Mot de passe incorrecte')
            compte = input("Entrer le numero de compte: ")
            NIP=f.verification_nip()
        continuer = True
        liste_choix=['n','o']
        while continuer:
            if f.check_password(compte,NIP):
                choix_2 = f.menu_2()
                if choix_2 == 1:
                    f.deposer_argent(compte)
                if choix_2 == 2:
                    somme_a_retirer = float(input("Montant a retirer: "))
                    f.retirer_argent(compte,somme_a_retirer)
                if choix_2 == 3:
                    f.afficher_solde(compte)
                if choix_2==4:
                    liste_achats=f.get_ligne_fichier("achat.txt")
                    l=[]
                    operations=[]
                    for elements in liste_achats:
                        l.append(elements.split())
                    for premier_element in l:
                        if compte==premier_element[0]:
                            operations.append(premier_element)
                    nombre_historique_transaction=int(input("nombre de n derniere(s) transaction(s)? "))
                    a=operations[-nombre_historique_transaction:]
                    if len(a)==0:
                        print('Aucune transaction pour ce compte')
                    else: 
                        print('Historique des {} deniere(s) operations(achat) sur le compte {}: \n'.format(nombre_historique_transaction,compte))
                        for x in a:
                            print(" ".join(x))
                if choix_2 == 5:
                    f.changement_pin(compte)
                    break
                if choix_2==6:
                    f.affiche_marchant()
                    option_choix_marchant=f.recup_option()
                    if option_choix_marchant==1:
                        marchand=u.LISTE_MARCHANDS[option_choix_marchant]
                        f.affiche_produit(marchand)
                        produit=input("Qu'est ce que vous voulez acheter? ")
                        if produit in u.MARCHANT[marchand].keys():
                            f.effectuer_operation(compte, marchand, produit)
                    elif option_choix_marchant==2:
                        marchand=u.LISTE_MARCHANDS[option_choix_marchant]
                        f.affiche_produit(marchand)
                        produit=input("Qu'est ce que vous voulez acheter? ")
                        if produit in u.MARCHANT[marchand].keys():
                            f.effectuer_operation(compte, marchand, produit)
                    elif option_choix_marchant==3:
                        marchand=u.LISTE_MARCHANDS[option_choix_marchant]
                        f.affiche_produit(marchand)
                        produit=input("Qu'est ce que vous voulez acheter? ")
                        if produit in u.MARCHANT[marchand].keys():
                            f.effectuer_operation(compte, marchand, produit) 
                    else:
                        print("Ce marchant n'existe pas ...")   
            else:
                print("Numero du compte ou mot de passe incorrect.")
            choix_continuer = input('Vous voulez effectuer une autre operation ?(o/n): ').lower()
            while choix_continuer not in liste_choix:
                print("VOUS DEVEZ REPONDRE PAR : (o) OU (n)\n")
                choix_continuer = input('Vous voulez effectuer une autre operation ?(o/n): ').lower()
            if choix_continuer=='n':
                continuer =False
    choix_run = input('Vous voulez quitter le programme ?(o/n): ').lower()

    while choix_run not in liste_choix:
        print("VOUS DEVEZ REPONDRE PAR : (o) OU (n)\n")
        choix_run = input('Vous voulez quitter le programme ?(o/n): ').lower()
    if choix_run=='o':
        run =False
        
    

