from tkinter import *   #import du module tkinter qui permet de creer des interfaces graphiques basiques
from tkinter import filedialog, colorchooser, PhotoImage #sous modules de tkinter

import pygame #import du module pygame qui permet la gestion de fichiers audio
from pygame.locals import *

from random import randint #import du module random qui permet de tirer des nombres au hasard

from PIL import Image, ImageTk #import du module Python Image Library qui offre une extension des formats d'image supportés


pygame.mixer.pre_init(44100, 16, 2, 4096) #initialisation du sous module mixer de pygame (frequence, resolution, cannaux, "buffersize")
pygame.init()

backup = 0
backuptemp = 0

def initialisation(backup): #choix de la musique à charger au lancement du programme
    nummusic = randint(0,19) #20 correspond au nombre de musique présentes dans la playlist / Choix au hasard d'un nombre qui dertermine quelle musique charger
    backup = nummusic
                             #suite de comparaison pour déterminer quelle musique charger
    if nummusic==0:
        pygame.mixer.music.load("all.mp3") #charge la musique

    if nummusic==1:
        pygame.mixer.music.load("aventure.mp3") #charge la musique

    if nummusic==2:
        pygame.mixer.music.load("bal.mp3")

    if nummusic==3:
        pygame.mixer.music.load("chill.mp3")

    if nummusic==4:
        pygame.mixer.music.load("dreams.mp3")

    if nummusic==5:
        pygame.mixer.music.load("free.mp3")

    if nummusic==6:
        pygame.mixer.music.load("good.mp3")

    if nummusic==7:
        pygame.mixer.music.load("happy.mp3")

    if nummusic==8:
        pygame.mixer.music.load("high.mp3")

    if nummusic==9:
        pygame.mixer.music.load("instru.mp3")

    if nummusic==10:
        pygame.mixer.music.load("kittar.mp3")

    if nummusic==11:
        pygame.mixer.music.load("lights.mp3")

    if nummusic==12:
        pygame.mixer.music.load("paradise.mp3")

    if nummusic==13:
        pygame.mixer.music.load("pnl.mp3")

    if nummusic==14:
        pygame.mixer.music.load("ride.mp3")

    if nummusic==15:
        pygame.mixer.music.load("silence.mp3")

    if nummusic==16:
        pygame.mixer.music.load("tease.mp3")

    if nummusic==17:
        pygame.mixer.music.load("vibes.mp3")

    if nummusic==18:
        pygame.mixer.music.load("war.mp3")

    if nummusic==19:
        pygame.mixer.music.load("baybreeze.mp3")

    pygame.mixer.music.play(-1) #Lancement de la musique / le paramètre -1 caractérise une lecture en boucle
    pygame.mixer.music.pause() #mise en pause de la musique pour pouvoir la lancer qu'une fois le programme lancé
    print('b1=',backup)
    return backup



def play(): #permet de sortir de la pause
    pygame.mixer.music.unpause() #sortie de pause
    print('play') #[DEBUG]affichage dans la commande pour confirmer que l'action a été prise en compte

def pause(): #permet de mettre la pause
    pygame.mixer.music.pause() #mise en pause
    print('pause') #[DEBUG]affichage dans la commande pour confirmer que l'action a été prise en compte

def stop(): #permet de couper la musique et de repartir du début de la musique coupée
    pygame.mixer.music.stop() #arret de la musique
    pygame.mixer.music.play(-1) #lancement de la musique
    pygame.mixer.music.pause() #mise en pause
    print('stop') #[DEBUG]affichage dans la commande pour confirmer que l'action a été prise en compte

def next(): #permet de passer à la musique suivante
    global backuptemp
    nummusic = randint(0,19) #choix au hasard d'un nombre qui dertermine quelle musique charger
    while nummusic == backuptemp:
        nummusic = randint(0,19)
    backuptemp = nummusic
    print('b2=',backuptemp)
                                #suite de comparaison pour déterminer quelle musique charger
    if nummusic==0:
        pygame.mixer.music.load("all.mp3")#charge la musique

    if nummusic==1:
        pygame.mixer.music.load("aventure.mp3")#charge la musique

    if nummusic==2:
        pygame.mixer.music.load("bal.mp3")

    if nummusic==3:
        pygame.mixer.music.load("chill.mp3")

    if nummusic==4:
        pygame.mixer.music.load("dreams.mp3")

    if nummusic==5:
        pygame.mixer.music.load("free.mp3")

    if nummusic==6:
        pygame.mixer.music.load("good.mp3")

    if nummusic==7:
        pygame.mixer.music.load("happy.mp3")

    if nummusic==8:
        pygame.mixer.music.load("high.mp3")

    if nummusic==9:
        pygame.mixer.music.load("instru.mp3")

    if nummusic==10:
        pygame.mixer.music.load("kittar.mp3")

    if nummusic==11:
        pygame.mixer.music.load("lights.mp3")

    if nummusic==12:
        pygame.mixer.music.load("paradise.mp3")

    if nummusic==13:
        pygame.mixer.music.load("pnl.mp3")

    if nummusic==14:
        pygame.mixer.music.load("ride.mp3")

    if nummusic==15:
        pygame.mixer.music.load("silence.mp3")

    if nummusic==16:
        pygame.mixer.music.load("tease.mp3")

    if nummusic==17:
        pygame.mixer.music.load("vibes.mp3")

    if nummusic==18:
        pygame.mixer.music.load("war.mp3")

    if nummusic==19:
        pygame.mixer.music.load("baybreeze.mp3")

    pygame.mixer.music.play(-1) #Lancement de la musique / le paramètre -1 caractérise une lecture en boucle

def getvolume(volume): #permet de modifier le volume
    volume=float(volume)/float(100.0) #divison par 100 de la valeur retournée par le Scale Volume pour rendre la valeur compatible avec la commande pygame.mixer.music.set_volume()
    print(volume) #[DEBUG]affiche du volume entre 0 et 1 dans la console pour vérifier la valeur envoyée
    pygame.mixer.music.set_volume(volume) #applique le changement de volume

def couleur(): #applique une nouvelle couleur à l'arrière plan du lecteur
    color = colorchooser.askcolor() #demande à l'utilisateur de choisir une couleur
    color = str(color) #transforme la variable en chaine de caractères
    couleur1 = color.split("\'") #sépare la chaine en groupe separé par le caractère '
    couleur2 = couleur1[1] #on affecte le groupe 1 à couleur2
    Play["bg"] = couleur2 #application de la nouvelle couleur
    Pause["bg"] = couleur2
    Next["bg"] = couleur2
    Previous["bg"] = couleur2
    Stop["bg"] = couleur2
    Volume["bg"] = couleur2
    Couleur["bg"] = couleur2
    File["bg"] = couleur2

def file(): #permet de choisir une musique dans les dossiers de l'ordinateur
    music = filedialog.askopenfilename(title = "Choisir une musique") #demande à l'utilisateur de choisir une musique
    pygame.mixer.music.load(music) #charge la musique
    pygame.mixer.music.play(-1) #lancement de la musique / le paramètre -1 caractérise une lecture en boucle

def previous():
    global backup, backuptemp
    nummusic = backup
    print('num=',nummusic)
    if nummusic==0:
        pygame.mixer.music.load("all.mp3")#charge la musique

    if nummusic==1:
        pygame.mixer.music.load("aventure.mp3")#charge la musique

    if nummusic==2:
        pygame.mixer.music.load("bal.mp3")

    if nummusic==3:
        pygame.mixer.music.load("chill.mp3")

    if nummusic==4:
        pygame.mixer.music.load("dreams.mp3")

    if nummusic==5:
        pygame.mixer.music.load("free.mp3")

    if nummusic==6:
        pygame.mixer.music.load("good.mp3")

    if nummusic==7:
        pygame.mixer.music.load("happy.mp3")

    if nummusic==8:
        pygame.mixer.music.load("high.mp3")

    if nummusic==9:
        pygame.mixer.music.load("instru.mp3")

    if nummusic==10:
        pygame.mixer.music.load("kittar.mp3")

    if nummusic==11:
        pygame.mixer.music.load("lights.mp3")

    if nummusic==12:
        pygame.mixer.music.load("paradise.mp3")

    if nummusic==13:
        pygame.mixer.music.load("pnl.mp3")

    if nummusic==14:
        pygame.mixer.music.load("ride.mp3")

    if nummusic==15:
        pygame.mixer.music.load("silence.mp3")

    if nummusic==16:
        pygame.mixer.music.load("tease.mp3")

    if nummusic==17:
        pygame.mixer.music.load("vibes.mp3")

    if nummusic==18:
        pygame.mixer.music.load("war.mp3")

    if nummusic==19:
        pygame.mixer.music.load("baybreeze.mp3")

    pygame.mixer.music.play(-1) #Lancement de la musique / le paramètre -1 caractérise une lecture en boucle
    backup = backuptemp
    print('b3=',backup)



initialisation(backup) #lancement de la fonction initialisation au lancement du programme

backup = initialisation(backup)





fen1=Tk() #définition d'une fenêtre tkinter
fen1.geometry("400x345") #dimensions de la fenetre
fen1.title("Lecteur de Musique") #titre de la musique
fen1.resizable(width=False, height=False) #fenêtre non redimensionable

photo= PhotoImage(file="ciel2.gif")
label=Label(image=photo)
Label.image=photo
label.pack()

Play = Button(fen1,width=3, height = 2, text='play', command= play) #définition d'un bouton qui applique la fonction play
Play.place(x=160, y=100) #placement du widget

Pause = Button(fen1, width=3, height = 2,text='pause', command= pause) #définition d'un bouton qui applique la fonction pause
Pause.place(x=200, y=100) #placement du widget

Next = Button(fen1, width=3, height = 2, text='next', command= next) #définition d'un bouton qui applique la fonction next
Next.place(x=260, y=100) #placement du widget

Previous = Button(fen1, width=3, height=2, text='previous', command = previous) #
Previous.place(x=100, y=100) #placement du widget

Stop = Button(fen1, width=3, height=2, text='stop', command= stop) #définition d'un bouton qui applique la fonction stop
Stop.place(x=185, y=235) #placement du widget


volume=DoubleVar() #définition de la variable volume
Volume = Scale(fen1, from_ = 0, to = 100,orient = HORIZONTAL, variable = volume, resolution = 1,tickinterval=10, length=200, label='                        Volume', command= getvolume) #définition d'un widet scale allant de 0 à 100 à l'horizontale, avec une résolution de 1, et une echele de 10
Volume.set(50) #réglage du volume initial à 50%
Volume.place(x=95, y=150) #placement du widget

Couleur = Button(fen1, text="couleur", width=5, height=2,command=couleur) #définition d'un bouton qui applique la fonction couleur
Couleur.place(x=240, y=235) #placement du widget

File = Button(fen1, text="file", width=5, height=2,command=file) #définition d'un bouton qui applique la fonction file
File.place(x=120, y=235) #placement du widget


fen1.mainloop()



