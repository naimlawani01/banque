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
        if f.check_nom_prenom(nom, prenom):
            choix_3 = f.menu_3()
            if choix_3 == 1:
                break
            elif choix_3 == 2:
                f.effectuer_operation()
        else:
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
        f.effectuer_operation()
        
    

