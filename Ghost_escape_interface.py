# coding: utf-8

from Ghost_escape_functions import*
from tkinter import*
from functools import*
import sys

class Ghost_escape_interface(Frame):
    Castle_Niveau1=[[0,0,1,1,1,1,1,0,0,0,['heaven'],0,0]
        ,[0,0,1,0,0,0,1,0,0,0,1,0,0]
        ,[[],1,1,1,[],1,1,1,[],1,1,1,[]]
        ,[1,0,1,0,0,0,1,0,0,0,1,0,1]
        ,[[],1,1,1,[],1,1,1,[],1,1,1,[]]
        ,[1,0,1,0,0,0,1,0,0,0,1,0,1]
        ,[[],1,1,1,[],1,1,1,[],1,1,1,[]]
        ,[0,0,1,0,0,0,1,0,0,0,0,0,0]
        ,[0,0,1,1,['reception'],1,1,0,0,0,0,0,0]]
    Castle_Niveau2=[[0,[],0,0,0,0,0,0,0,0,0,0,0]
        ,[0,1,1,[],1,1,[],1,1,[],1,[],0]
        ,[0,1,0,1,0,0,1,0,0,1,0,1,0]
        ,[0,[],1,1,0,0,['heaven'],1,1,[],1,[],0]
        ,[0,0,0,1,0,0,0,0,0,1,0,1,0]
        ,[0,0,0,[],1,1,1,1,[],1,0,1,[]]
        ,[0,[],0,1,0,0,1,0,0,1,1,1,0]
        ,[0,1,1,[],0,0,1,0,0,0,[],0,0]
        ,[0,0,0,0,0,0,['reception'],0,0,0,0,0,0]]
    Castle_Niveau3=[[0,1,1,[],1,0,0,1,1,1,1,1,[]]
        ,[0,[],0,0,[],1,1,['heaven'],0,0,0,0,1]
        ,[0,1,0,0,1,0,0,1,1,1,1,1,[]]
        ,[0,[],1,[],1,1,[],1,1,0,[],0,0]
        ,[0,0,0,1,0,0,0,0,[],0,1,0,0]
        ,[1,1,1,[],1,1,1,0,1,1,1,1,0]
        ,[[],0,0,0,0,0,[],0,0,0,0,1,0]
        ,[1,0,0,0,0,0,1,1,[],0,0,1,0]
        ,[1,[],1,1,[],1,1,0,1,1,1,['reception'],0]]
    Castle_Niveau4=[[0,['reception'],0,0,0,0,0,0,0,0,0,0,0]
        ,[0,1,1,[],1,1,[],1,1,[],1,[],0]
        ,[0,1,0,1,0,0,1,0,0,1,0,1,0]
        ,[0,[],1,1,0,0,[],1,1,[],1,[],0]
        ,[0,0,0,1,0,0,0,0,0,1,0,1,0]
        ,[0,0,0,[],1,1,1,1,[],1,0,1,[]]
        ,[0,[],0,1,0,0,1,0,0,1,1,1,0]
        ,[0,1,1,[],0,0,1,0,0,0,[],0,0]
        ,[0,0,0,0,0,0,['heaven'],0,0,0,0,0,0]]
    Castles={1:Castle_Niveau1,2:Castle_Niveau2,
        3:Castle_Niveau3,4:Castle_Niveau4}
    Castle=Castles[1]
    Gameboard=deepcopy(Castle)
    Player={'pintes':3}
    Gameboard=affectation_of_the_pions(Gameboard)
    position_of_the_reception=where_is_the_reception(Castle)
    Gameboard[position_of_the_reception[0]][
        position_of_the_reception[1]]=Player
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.beginning_labels()
    def beginning_labels(self):
        for each_thing_in_my_window in self.winfo_children():
            each_thing_in_my_window.destroy()
        self.hello=Label(self,text='Welcome on Ghost Escape !')
        self.hello.pack()
        self.start=Button(self,text='Start',
            command=Ghost_escape_interface.beginning_the_game)
        self.start.pack()
        self.dificulty=Button(self,text='Chose the difficulty',
            command=partial(
                Ghost_escape_interface.choice_of_the_difficulty,self))
        self.dificulty.pack()
        self.quit=Button(self,text='Quit',command=self.quit)
        self.quit.pack()
    def choice_of_the_difficulty(Window):
        for each_thing_in_my_window in Window.winfo_children():
            each_thing_in_my_window.destroy()
        Level1=Button(Window,text='Level 1',command=partial(
            Ghost_escape_interface.chose_level,1,Window))
        Level1.pack()
        Level2=Button(Window,text='Level 2',command=partial(
            Ghost_escape_interface.chose_level,2,Window))
        Level2.pack()
        Level3=Button(Window,text='Level 3',command=partial(
            Ghost_escape_interface.chose_level,3,Window))
        Level3.pack()
        Level4=Button(Window,text='Level 4',command=partial(
            Ghost_escape_interface.chose_level,4,Window))
        Level4.pack()
    def chose_level(player_level_choice,Window):
        Ghost_escape_interface.Castle=Ghost_escape_interface.Castles[
            player_level_choice]
        Ghost_escape_interface.Gameboard=deepcopy(
            Ghost_escape_interface.Castle)
        Player={'pintes':3}
        Ghost_escape_interface.Gameboard=affectation_of_the_pions(
            Ghost_escape_interface.Gameboard)
        position_of_the_reception=where_is_the_reception(
            Ghost_escape_interface.Castle)
        Ghost_escape_interface.Gameboard[position_of_the_reception[0]][
            position_of_the_reception[1]]=Player
        Ghost_escape_interface.beginning_labels(Window)
    def beginning_the_game():
        for each_thing_in_my_window in Window.winfo_children():
            each_thing_in_my_window.destroy()
        frame_gameboard=Frame(Window, borderwidth=1)
        frame_gameboard.pack(side=LEFT,padx=10,pady=10)
        frame_text=Text(Window,height=5,width=50,relief=GROOVE)
        Ghost_escape_interface.display_gameboard(Window,frame_gameboard)
        Ghost_escape_interface.display_buttons(
            Window,frame_gameboard,frame_text)
        frame_text.pack(side=RIGHT,padx=10)
    def display_gameboard(Window,frame_gameboard):
        for ligne in range(len(Ghost_escape_interface.Gameboard)):
            for colonne in range(len(
                Ghost_escape_interface.Gameboard[ligne])):
                if Ghost_escape_interface.Gameboard[
                    ligne][colonne]==0:
                    Canvas(frame_gameboard,width=50,height=50,
                        background='black').grid(row=ligne,column=colonne)
                elif Ghost_escape_interface.Gameboard[
                    ligne][colonne]==1:
                    Canvas(frame_gameboard,width=50,height=50,
                        background='white').grid(row=ligne,column=colonne)
                elif type(Ghost_escape_interface.Gameboard[
                    ligne][colonne])==list:
                    Canvas(frame_gameboard,width=50,height=50,
                        background='red').grid(row=ligne,column=colonne)
                elif type(Ghost_escape_interface.Gameboard[
                    ligne][colonne])==dict:
                    canvas=Canvas(frame_gameboard,width=50,height=50,
                        background='white')
                    gf1=PhotoImage(master=canvas,file='casper.png')
                    frame_gameboard.casper=gf1
                    canvas.create_image(0,0,image=gf1,anchor=NW)
                    canvas.grid(row=ligne,column=colonne)
        position_of_the_player=where_is_the_player(
            Ghost_escape_interface.Gameboard)
        energy_of_the_player="%d"%(Ghost_escape_interface.Gameboard[
            position_of_the_player[0]][
                position_of_the_player[1]]['pintes'])
        Label(frame_gameboard,text='Number of\nlifepoints : %s'%(
            energy_of_the_player),justify=CENTER).grid(row=3,column=14)
    def display_buttons(Window,frame_gameboard,frame_text):
        deplacement_buttons=Frame(Window,borderwidth=1)
        deplacement_buttons.pack(side=BOTTOM,padx=10,pady=10)
        left_button=Button(deplacement_buttons,text="Left",
            command=partial(Ghost_escape_interface.move,1,
                Window,frame_gameboard,frame_text))
        left_button.pack(side=LEFT)
        right_button=Button(deplacement_buttons,text="Right",
            command=partial(Ghost_escape_interface.move,2,
                Window,frame_gameboard,frame_text))
        right_button.pack(side=RIGHT)
        bottom_button=Button(deplacement_buttons,text="Bottom",
            command=partial(Ghost_escape_interface.move,4,
                Window,frame_gameboard,frame_text))
        bottom_button.pack(side=BOTTOM)
        top_button=Button(deplacement_buttons,text="Top",
            command=partial(Ghost_escape_interface.move,3,
                Window,frame_gameboard,frame_text))
        top_button.pack(side=TOP)
    def move(choice_of_deplacement,Window,frame_gameboard,frame_text):
        try:
            new_position_of_the_player=deplacement_of_the_player(
                choice_of_deplacement,Ghost_escape_interface.Gameboard,
                    Ghost_escape_interface.Castle)
            Ghost_escape_interface.check_events_for_the_player(
                new_position_of_the_player,
                    Ghost_escape_interface.Gameboard,
                        Ghost_escape_interface.Castle,frame_text,
                            frame_gameboard,Window)
            try:
                Ghost_escape_interface.display_gameboard(
                    Window,frame_gameboard)
            except:
                pass
        except:
            frame_text.delete('1.0',END)
            frame_text.insert(END,
                "This movement is impossible.\n Try again\n")
            Ghost_escape_interface.display_gameboard(Window,
                frame_gameboard)
    def check_events_for_the_player(new_position_of_the_player,
        gameboard,castle,frame_text,frame_gameboard,Window):
        frame_text.delete('1.0',END)
        list_for_text=ennemy(new_position_of_the_player,
            gameboard,castle)
        if list_for_text!=[]:
            position_of_the_player=where_is_the_player(gameboard)
            if list_for_text[0]==4:
                frame_text.insert(END,
                    'You are encounting a Bibbendum Chamallow.\n')
                frame_text.insert(END,'You lose 2 pintes.\n')
                frame_text.insert(END,
                    'You still have %d pintes\n'%(gameboard[
                        position_of_the_player[0]][
                            position_of_the_player[1]]['pintes']))
            elif list_for_text[0]==5:
                frame_text.insert(END,
                    'You are encounting the mad scientist.\n')
                frame_text.insert(END,'You lose 1 pinte.\n')
                frame_text.insert(END,
                    'You still have %d pintes\n'%(gameboard[
                        position_of_the_player[0]][
                            position_of_the_player[1]]['pintes']))
                frame_text.insert(END,'He moves you to an another case !\n')
                magic_deplacement(Ghost_escape_interface.Gameboard,
                    Ghost_escape_interface.Castle,position_of_the_player)
            elif list_for_text[0]==6:
                frame_text.insert(END,
                    'You are encounting the master of the castle.\n')
                frame_text.insert(END,
                    'You are coming back to the start case.\n')
            elif list_for_text[0]==7:
                frame_text.insert(END,
                    'Wondeful, you have just earned %s pintes.\n'%(
                        list_for_text[1]))
                frame_text.insert(END,'You have %s pintes now.\n'%(gameboard[
                    position_of_the_player[0]][
                        position_of_the_player[1]]['pintes']))
            elif list_for_text[0]=='heaven':
                frame_text.insert(END,
                    "You've just reached the ghost heaven's gate.\n")
                frame_text.insert(END,"WONDERFUL, you won.\n")
                Ghost_escape_interface.next_level(castle,frame_text,Window)
            elif list_for_text[0]==0:
                frame_text.insert(END,'You are earing a key noise.\n')
            elif list_for_text[0]==1:
                frame_text.insert(END,'You are earing a sardonic laugh.\n')
            elif list_for_text[0]==2:
                frame_text.insert(END,"You are smelling the attractive\n")
                frame_text.insert(END,
                    "fragrance of the strawberry chamallow.\n")
        check_energy=check_the_energy(gameboard,castle)
        if check_energy=='ko':
            frame_text.insert(END,
                "GAME OVER\nYou lose the game.\nTry again.\n")
            Ghost_escape_interface.Gameboard=deepcopy(
                Ghost_escape_interface.Castle)
            Player={'pintes':3}
            Ghost_escape_interface.Gameboard=affectation_of_the_pions(
                Ghost_escape_interface.Gameboard)
            position_of_the_reception=where_is_the_reception(
                Ghost_escape_interface.Castle)
            Ghost_escape_interface.Gameboard[position_of_the_reception[0]][
                position_of_the_reception[1]]=Player
    def next_level(castle,frame_text,Window):
        if castle==Ghost_escape_interface.Castles[1]:
            level=1
            check_there_is_a_next_level='ok'
        elif castle==Ghost_escape_interface.Castles[2]:
            level=2
            check_there_is_a_next_level='ok'
        elif castle==Ghost_escape_interface.Castles[3]:
            level=3
            check_there_is_a_next_level='ok'
        elif castle==Ghost_escape_interface.Castles[4]:
            check_there_is_a_next_level='ko'
            for each_thing_in_my_window in Window.winfo_children():
                each_thing_in_my_window.destroy()
            end_message=Label(Window,
                text="Congratulation you've finished the entire game !\n")
            end_message.pack()
            quit=Button(Window,text='Quitter',command=sys.exit)
            quit.pack()
        if check_there_is_a_next_level=='ok':
            Ghost_escape_interface.Castle=Ghost_escape_interface.Castles[level+1]
            frame_text.insert(END,'You had achieved the level %d.\n'%(level))
            frame_text.insert(END,'You are at the level %d now.\n'%(level+1))
            frame_text.insert(END,'Good luck.\n')
            Ghost_escape_interface.Gameboard=deepcopy(
                Ghost_escape_interface.Castle)
            Player={'pintes':3}
            Ghost_escape_interface.Gameboard=affectation_of_the_pions(
                Ghost_escape_interface.Gameboard)
            position_of_the_reception=where_is_the_reception(
                Ghost_escape_interface.Castle)
            Ghost_escape_interface.Gameboard[position_of_the_reception[0]][
                position_of_the_reception[1]]=Player

Root=Tk()
Root.title('Ghost escape')
Window=Ghost_escape_interface(Root)
Window.mainloop()
