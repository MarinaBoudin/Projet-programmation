# coding: utf-8

from copy import *
from random import*

# Classes

class PossibilityError(Exception):
    pass

def deplacement_of_the_player(type_of_deplacement,gameboard,castle):
    position_of_the_player=where_is_the_player(gameboard)
    if type_of_deplacement==1:
        if position_of_the_player[1]-1==-1:
            raise PossibilityError()
        if gameboard[position_of_the_player[0]][
            position_of_the_player[1]-1]==0:
            raise PossibilityError()
        new_position_of_the_player=gameboard[
            position_of_the_player[0]][
                position_of_the_player[1]-1]
        gameboard[position_of_the_player[0]][
            position_of_the_player[1]-1]=gameboard[
                position_of_the_player[0]][position_of_the_player[1]]
        gameboard[position_of_the_player[0]][
            position_of_the_player[1]]=castle[
                position_of_the_player[0]][position_of_the_player[1]]
    elif type_of_deplacement==2:
        if gameboard[position_of_the_player[0]][
            position_of_the_player[1]+1]==0:
            raise PossibilityError()
        new_position_of_the_player=gameboard[position_of_the_player[0]][
            position_of_the_player[1]+1]
        gameboard[position_of_the_player[0]][
            position_of_the_player[1]+1]=gameboard[
                position_of_the_player[0]][position_of_the_player[1]]
        gameboard[position_of_the_player[0]][
            position_of_the_player[1]]=castle[
                position_of_the_player[0]][position_of_the_player[1]]
    elif type_of_deplacement==3:
        if position_of_the_player[0]-1==-1:
            raise PossibilityError()
        if gameboard[position_of_the_player[0]-1][
            position_of_the_player[1]]==0:
            raise PossibilityError()
        new_position_of_the_player=gameboard[position_of_the_player[0]-1][
            position_of_the_player[1]]
        gameboard[position_of_the_player[0]-1][
            position_of_the_player[1]]=gameboard[
                position_of_the_player[0]][position_of_the_player[1]]
        gameboard[position_of_the_player[0]][
            position_of_the_player[1]]=castle[
                position_of_the_player[0]][position_of_the_player[1]]
    elif type_of_deplacement==4:
        if gameboard[position_of_the_player[0]+1][
            position_of_the_player[1]]==0:
            raise PossibilityError()
        new_position_of_the_player=gameboard[position_of_the_player[0]+1][
                position_of_the_player[1]]
        gameboard[position_of_the_player[0]+1][
            position_of_the_player[1]]=gameboard[
                position_of_the_player[0]][position_of_the_player[1]]
        gameboard[position_of_the_player[0]][
            position_of_the_player[1]]=castle[
                position_of_the_player[0]][position_of_the_player[1]]
    return new_position_of_the_player

def ennemy(new_position_of_the_player,gameboard,castle):
    position_of_the_player=where_is_the_player(gameboard)
    list_for_text=[]
    if (type(new_position_of_the_player)==list
        and new_position_of_the_player!=[]):
        list_for_text=new_position_of_the_player
        if new_position_of_the_player[0]==4:
            gameboard[position_of_the_player[0]][position_of_the_player[1]][
                'pintes']=gameboard[position_of_the_player[0]][
                    position_of_the_player[1]]['pintes']-2
        elif new_position_of_the_player[0]==5:
            gameboard[position_of_the_player[0]][position_of_the_player[1]][
                'pintes']=gameboard[position_of_the_player[0]][
                    position_of_the_player[1]]['pintes']-1
        elif new_position_of_the_player[0]==6:
            position_of_the_reception=where_is_the_reception(castle)
            gameboard[position_of_the_reception[0]][
                position_of_the_reception[1]]=gameboard[
                    position_of_the_player[0]][position_of_the_player[1]]
            gameboard[position_of_the_player[0]][
                position_of_the_player[1]]=castle[
                    position_of_the_player[0]][position_of_the_player[1]]
        elif new_position_of_the_player[0]==7:
            gameboard[position_of_the_player[0]][
                position_of_the_player[1]]['pintes']=gameboard[
                    position_of_the_player[0]][position_of_the_player[1]][
                        'pintes']+new_position_of_the_player[1]
        elif new_position_of_the_player[0]=='heaven':
            position_of_the_reception=where_is_the_reception(castle)
            gameboard[position_of_the_reception[0]][
                position_of_the_reception[1]]=gameboard[
                    position_of_the_player[0]][position_of_the_player[1]]
            gameboard[position_of_the_player[0]][
                position_of_the_player[1]]=castle[
                    position_of_the_player[0]][position_of_the_player[1]]
    else:
        things_around_the_player=[]
        try:
            things_around_the_player=things_around_the_player+[gameboard[
                position_of_the_player[0]-1][position_of_the_player[1]]]
        except:
            things_around_the_player=things_around_the_player+[0]
        try:
            things_around_the_player=things_around_the_player+[gameboard[
                position_of_the_player[0]+1][position_of_the_player[1]]]
        except:
            things_around_the_player=things_around_the_player+[0]
        try:
            things_around_the_player=things_around_the_player+[gameboard[
                position_of_the_player[0]][position_of_the_player[1]-1]]
        except:
            things_around_the_player=things_around_the_player+[0]
        try:
            things_around_the_player=things_around_the_player+[gameboard[
                position_of_the_player[0]][position_of_the_player[1]+1]]
        except:
            things_around_the_player=things_around_the_player+[0]
        for thing in things_around_the_player:
            if (type(thing)==list and thing!=[]):
                if thing[0]==6:
                    list_for_text=list_for_text+[0]
                elif thing[0]==5:
                    list_for_text=list_for_text+[1]
                elif thing[0]==4:
                    list_for_text=list_for_text+[2]
    return list_for_text

def affectation_of_the_pions(gameboard):
    pions=[4,4,4,5,6,7,7,7,7,7]
    while pions!=[]:
        lign=int(9*random())
        column=int(13*random())
        pintes=0
        for pion in pions:
            if pion==7:
                pintes=pintes+1
        choice_of_pion=int(len(pions)*random())
        if pions[choice_of_pion]==7:
            number_of_pintes=int(pintes*random()+1)
            if number_of_pintes>3:
                number_of_pintes=3
            if gameboard[lign][column]==[]:
                gameboard[lign][column]=gameboard[
                    lign][column]+[7,number_of_pintes]
                for i in range(number_of_pintes):
                    pions.pop()
        else:
            if gameboard[lign][column]==[]:
                gameboard[lign][column]=gameboard[
                    lign][column]+[pions[choice_of_pion]]
                pions.pop(choice_of_pion)
    return gameboard

def check_the_energy(gameboard,castle):
    position_of_the_player=where_is_the_player(gameboard)
    check_energy='ok'
    if gameboard[position_of_the_player[0]][
        position_of_the_player[1]]['pintes']<=0:
        check_energy='ko'
    return check_energy

def magic_deplacement(gameboard,castle,position_of_the_player):
    check_new_position_of_the_player=0
    while check_new_position_of_the_player==0:
        lign=int(9*random())
        column=int(13*random())
        if gameboard[lign][column]!=0 and gameboard[
            lign][column]!=['heaven']:
            check_new_position_of_the_player=1
            gameboard[lign][column]=gameboard[
                position_of_the_player[0]][
                    position_of_the_player[1]]
            gameboard[position_of_the_player[0]][
                position_of_the_player[1]]=castle[
                    position_of_the_player[0]][position_of_the_player[1]]

def where_is_the_reception(castle):
    position_of_the_reception=[]
    for lign in range(len(castle)):
        for column in range(len(castle[lign])):
            if castle[lign][column]==['reception']:
                position_of_the_reception=position_of_the_reception+[
                    lign]+[column]
    return position_of_the_reception

def where_is_the_player(gameboard):
    position_of_the_player=[]
    for lign in range(len(gameboard)):
        for column in range(len(gameboard[lign])):
            if type(gameboard[lign][column])==dict:
                position_of_the_player=position_of_the_player+[
                    lign]+[column]
    return position_of_the_player
