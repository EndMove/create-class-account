#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Nihart Jérémi 6TB
# Powered By EndMove

# comptes-nihajer.py – date 04.10.2019

from typing import List
from random import randrange


def checkOccurence(liste: List, login: str):
    for i in liste:
        if i == login:
            return True
    return False


def removeSpace(chaine: str):
    return chaine.replace(" ", "")


def removeAccent(chaine: str):
    new_chaine = chaine
    accents = {'a': ['à', 'ã', 'á', 'â'],
               'e': ['é', 'è', 'ê', 'ë'],
               'i': ['î', 'ï'],
               'u': ['ù', 'ü', 'û'],
               'o': ['ô', 'ö']}
    for simple_char, accented_chars in accents.items():
        for accented_char in accented_chars:
            new_chaine = new_chaine.replace(accented_char, simple_char)
    return new_chaine


def createLogin(nom: str, prenom: str):
    nom = removeSpace(nom)
    prenom = removeSpace(prenom)
    login = ""
    for i in range(4):
        login += nom[i % len(nom)].lower()
    for i in range(3):
        login += prenom[i % len(prenom)].lower()
    return removeAccent(login)


def createPassword(lettres=4, chiffres=4):
    password = ""
    for i in range(lettres):
        char = chr(ord('a') + randrange(0, 26))
        password += char
    for i in range(chiffres):
        numb = str(randrange(0, 9))
        password += numb
    return password


def createGroupe(chaine: str):
    return f"classe{chaine.lower()}"


def importEleves(fichier: str):
    eleves = []
    file_content = open(fichier, 'r')
    for i in file_content:
        eleve = i.split(";")
        eleve[-1] = eleve[-1][:3]
        eleves.append(eleve)
    file_content.close()
    return eleves


def exportComptes(listing: List[List[str]], fichier: str):
    file_content = open(fichier, 'w')
    for i in listing:
        ligne = f"{i[0]};{i[1]};{i[2]}\n"
        file_content.write(ligne)
    file_content.close()


if __name__ == '__main__':
    try:
        eleves = []
        accounts = []
        logins = []
        passwords = []
        print("""\
              #===============================#
              |     Welcome to EndAcount      |
              |             v1.0              |
              #===============================#
              """)
        if "n" == input("Use default source file 'eleves.csv' (O/n): "):
            importFile = input(" => Source file: ")
        else:
            importFile = "eleves.csv"
        if "n" == input("Use default output file 'logins.csv' (O/n): "):
            exportFile = input(" => Output file: ")
        else:
            exportFile = "logins.csv"
        nbrL = 4  # input("\nNumber of letter for password (4): ")
        nbrC = 4  # input("Number of digits for password (4): ")
        # -== Traitement des données ==-
        eleves = importEleves(importFile)
        for i in eleves:
            # Groupe:
            group = createGroupe(i[2])
            # Login:
            login = createLogin(i[0], i[1])

            login_ok = 2

            while login_ok > 1:
                if checkOccurence(logins, login):
                    login = f"{login[:7]}{login_ok}"
                    login_ok += 1
                else:
                    login_ok = 0
            logins.append(login)
            # Password:
            password = createPassword(nbrL, nbrC)
            password_ok = True
            while password_ok:
                if checkOccurence(passwords, password):
                    password = createPassword(nbrL, nbrC)
                else:
                    password_ok = False
            passwords.append(password)
            # Ajout utilisateur:
            user = [login, password, group]
            accounts.append(user)
        # Creation nouveau fichier logins:
        exportComptes(accounts, exportFile)
        # Cloturation:
        print("""\n
              #===============================#\n
                   Login users were created
              """)
    except Exception as error:
        print(f"EndAccount Error: {error}")
