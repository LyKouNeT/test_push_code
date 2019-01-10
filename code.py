#! /usr/bin/python3.5

#-*- coding: utf-8 -*-

#Importer json


#Affiche un message et demande le no
#de l'utilisateur
nom = []
nom.append(input("Ecrivez votre nom SVP : "))
print("Votre nom est : {}".format(nom[len(nom)-1]))


#Enregistre le nom de l'utilisateur dans
#le fichier data.json
