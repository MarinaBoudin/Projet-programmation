# coding: utf-8

import random
import sys
from copy import *
from random import*

# Classes

class PossibilityError(Exception):
    pass

class NumberError(Exception):
    pass

def principal(BASE):
    joueur={'pintes':3}
    C=deepcopy(BASE)
    C[8][4]=joueur
    b=begin()
    if b==1:
        piece(C)
        jeu(BASE,C)
    elif b==2:
        print('Au revoir')
        sys.exit()

def begin():
    print("1: Commencer le jeu")
    print("2: Quitter")
    try:
        b=int(input('Votre choix : '))
        if b not in [1,2]:
            raise NumberError()
    except ValueError:
        print('Attention votre réponse doit être 1 ou 2')
        b=begin()
    except NumberError:
        print('Attention votre réponse doit être 1 ou 2')
        b=begin()
    return b

def affichage_plateau(C):
    for k in C:
        for i in k:
            if i==0:
                print('  ',end='')
            elif i==1:
                print(' *',end='')
            elif type(i)==list:
                print(' #',end='')
            elif type(i)==dict:
                print(' X',end='')
        print('',end='\n')

def where(C):
    L=[]
    for k in range(len(C)):
        for i in range(len(C[k])):
            if type(C[k][i])==dict:
                L=L+[k]+[i]
    return L

def deplacement(a,C,BASE):
    L=where(C)
    if a==1:
        try:
            if L[1]-1==-1:
                raise PossibilityError()
            if C[L[0]][L[1]-1]==0:
                raise PossibilityError()
            new=C[L[0]][L[1]-1]
            C[L[0]][L[1]-1]=C[L[0]][L[1]]
            C[L[0]][L[1]]=BASE[L[0]][L[1]]
        except:
            print('Mouvement impossible choisissez un autre mouvement')
            affichage_plateau(C)
            a=choix()
            new=deplacement(a,C,BASE)
    elif a==2:
        try:
            if C[L[0]][L[1]+1]==0:
                raise PossibilityError()
            new=C[L[0]][L[1]+1]
            C[L[0]][L[1]+1]=C[L[0]][L[1]]
            C[L[0]][L[1]]=BASE[L[0]][L[1]]
        except:
            print('Mouvement impossible choisissez un autre mouvement')
            affichage_plateau(C)
            a=choix()
            new=deplacement(a,C,BASE)
    elif a==3:
        try:
            if L[0]-1==-1:
                raise PossibilityError()
            if C[L[0]-1][L[1]]==0:
                raise PossibilityError()
            new=C[L[0]-1][L[1]]
            C[L[0]-1][L[1]]=C[L[0]][L[1]]
            C[L[0]][L[1]]=BASE[L[0]][L[1]]
        except:
            print('Mouvement impossible choisissez un autre mouvement')
            affichage_plateau(C)
            a=choix()
            new=deplacement(a,C,BASE)
    elif a==4:
        try:
            if C[L[0]+1][L[1]]==0:
                raise PossibilityError()
            new=C[L[0]+1][L[1]]
            C[L[0]+1][L[1]]=C[L[0]][L[1]]
            C[L[0]][L[1]]=BASE[L[0]][L[1]]
        except:
            print('Mouvement impossible choisissez un autre mouvement')
            affichage_plateau(C)
            a=choix()
            new=deplacement(a,C,BASE)
    elif a==0:
        c=quitter()
        if c==1:
            print("Au revoir")
            sys.exit()
        elif c==2:
            jeu(BASE,C)
    return new

def magic(C,BASE,L):
    try:
        gauche=int(input('De combien de mouvement vers la gauche voulez vous vous déplacer ?\nVotre réponse : '))
        droite=int(input('De combien de mouvement vers la droite voulez vous vous déplacer ?\nVotre réponse : '))
        haut=int(input('De combien de mouvement vers le haut voulez vous vous déplacer ?\nVotre réponse : '))
        bas=int(input('De combien de mouvement vers le bas voulez vous vous déplacer ?\nVotre réponse : '))
        C[L[0]+bas-haut][L[1]-gauche+droite]=C[L[0]][L[1]]
        C[L[0]][L[1]]=BASE[L[0]][L[1]]
    except:
        print("Ce déplacemenet n'est pas possible. Réessayez.")
        affichage_plateau(C)
        magic(C,BASE,L)

def ennemy(b,C,BASE):
    L=where(C)
    if type(b)==list:
        for k in b:
            print(k)
            if k==4:
                C[L[0]][L[1]]['pintes']=C[L[0]][L[1]]['pintes']-2
                print('Mouahahahah vous ètes tombé sur un Bibbendum Chamallow.\nVous perdez 2 pintes.\nIl vous reste %d pintes'%(C[L[0]][L[1]]['pintes']))
            elif k==5:
                C[L[0]][L[1]]['pintes']=C[L[0]][L[1]]['pintes']-1
                print('Vous tombez nez à nez avec le savant fou.\nVous perdez une pinte.\nIl vous reste %d pintes\nMais il vous transporte dans la case de votre choix.\nOù voulez vous aller ?'%(C[L[0]][L[1]]['pintes']))
                affichage_plateau(C)
                magic(C,BASE,L)
            elif k==6:
                print('Mouahahahah vous ètes tombé sur le maître du château.\nVous retournez à la case départ.')
                C[8][4]=C[L[0]][L[1]]
                C[L[0]][L[1]]=BASE[L[0]][L[1]]
            elif k==7:
                for i in range(len(b)):
                    C[L[0]][L[1]]['pintes']=C[L[0]][L[1]]['pintes']+1
                print('Youpi vous venez de gagner %s pintes.\nVous avez donc %s pintes.'%(len(b),C[L[0]][L[1]]['pintes']))
            elif k=='paradice':
                print('BRAVO vous avez atteint la porte vers le paradis des fantômes')
                C[8][4]=C[L[0]][L[1]]
                C[L[0]][L[1]]=BASE[L[0]][L[1]]
                principal(BASE)
    else:
        around=[]
        try:
            around=around+[C[L[0]-1][L[1]]]
        except:
            around=around+[0]
        try:
            around=around+[C[L[0]+1][L[1]]]
        except:
            around=around+[0]
        try:
            around=around+[C[L[0]][L[1]-1]]
        except:
            around=around+[0]
        try:
            around=around+[C[L[0]][L[1]+1]]
        except:
            around=around+[0]
        for k in around:
            if (type(k)==list and k!=[]):
                if k[0]==6:
                    print('Vous entendez un bruit de clé')
                elif k[0]==5:
                    print('Vous entendez un rire sardonique')
                elif k[0]==4:
                    print("Vous sentez l'odeur alléchante du chamallow fraise")

def jeu(BASE,C):
    while(True):
        energy(C,BASE)
        affichage_plateau(C)
        a=choix()
        b=deplacement(a,C,BASE)
        ennemy(b,C,BASE)

def quitter():
    try:
        c=int(input(("Voulez vous vraiment quitter le jeu ?\n1: Oui\n2: Non\nVotre choix : ")))
        if c not in [1,2]:
            raise NumberError
    except ValueError:
        print('Attention votre réponse doit être 1 ou 2')
        c=quitter()
    except NumberError:
        print("Attention votre réponse n'est pas une des possibilités.\nRecommencez.")
        c=quitter()
    return c

def choix():
    print("1: Aller vers la GAUCHE")
    print("2: Aller vers la DROITE")
    print("3: Aller vers le HAUT")
    print("4: Aller vers le BAS")
    print("0: QUITTER")
    try:
        a=int(input("Votre choix : "))
        if a not in [0,1,2,3,4]:
            raise NumberError()
    except ValueError:
        print('Attention votre réponse doit être 0,1,2,3 ou 4')
        a=choix()
    except NumberError:
        print("Attention votre réponse n'est pas une des possibilités.\nRecommencez.")
        a=choix()
    return a

def piece(C):
    pions=[4,4,4,5,6,7,7,7,7,7]
    while pions!=[]:
        x=int(9*random())
        y=int(13*random())
        pintes=0
        for k in pions:
            if k==7:
                pintes=pintes+1
        z=int(len(pions)*random())
        if pions[z]==7:
            w=int((pintes+1)*random())
            if w>3:
                w=3
            if C[x][y]==[]:
                C[x][y]=C[x][y]+w*[7]
                for i in range(w):
                    pions.pop()
        else:
            if C[x][y]==[]:
                C[x][y]=C[x][y]+[pions[z]]
                pions.pop(z)
    return C

def energy(C,BASE):
    L=where(C)
    if C[L[0]][L[1]]['pintes']<=0:
        print("GAME OVER, vous n'avez plus d'énergie.\nVous avez perdu la partie.")
        principal(BASE)

# Main program
if __name__=='__main__':
    chateau=[[0,0,1,1,1,1,1,0,0,0,['paradice'],0,0],[0,0,1,0,0,0,1,0,0,0,1,0,0],[[],1,1,1,[],1,1,1,[],1,1,1,[]],[1,0,1,0,0,0,1,0,0,0,1,0,1],[[],1,1,1,[],1,1,1,[],1,1,1,[]],[1,0,1,0,0,0,1,0,0,0,1,0,1],[[],1,1,1,[],1,1,1,[],1,1,1,[]],[0,0,1,0,0,0,1,0,0,0,0,0,0],[0,0,1,1,['reception'],1,1,0,0,0,0,0,0]]
    principal(chateau)
