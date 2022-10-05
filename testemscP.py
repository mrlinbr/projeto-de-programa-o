from tkinter import filedialog
from tkinter import *
import pygame
import os
class playerdmusica():
    def __init__(self):
        self.mu=Tk()
        self.tela()
        self.widgets()
        self.lista()
        self.carregarmusica()
        self.mu.mainloop()

    def tela(self):
        self.mu.geometry('250x400')
        self.mu.configure(background='grey')

    '''def lista(self):
        self.songs = []
        self.current_song= ''
        self.paused = False

    def carregarmusica(self):
        self.diretorio = filedialog.askdirectory()

        for song in os.listdir(self.diretorio):
            name,ext = os.path.splitext(song)
            if ext == '.mp3':
                self.songs.append(song)

        for song in self.songs:
            self.songlist.insert('end', song)

        self.songlist.selection_set(0)
        self.current_song= self.songs[self.songlist.curselection()[0]]'''''

    def widgets(self):


        self.menubar=Menu(self.mu)
        self.mu.config(menu=self.menubar)

        self.organise_menu = Menu(self.menubar, tearoff=False)
        self.organise_menu.add_command(Label='selecionar diretorio')
        self.menubar.add_cascade(Label='organise', menu=self.organise_menu)

        listamusica=Listbox(self.mu,background='black',width=10,height=5)
        listamusica.pack()

        self.play_btnimg=PhotoImage(file='imagens\play.png')
        self.pause_btnimg=PhotoImage(file='imagens\pause.png')
        self.next_btnimg=PhotoImage(file='imagens\\previous.png')
        self.prev_btnimg=PhotoImage(file='imagens\\next.png')

        self.controlframe=Frame(self.mu)
        self.controlframe.pack()

        self.play_btn=Button(self.controlframe, image= self.play_btnimg, borderwidth=0)
        self.pause_btn=Button(self.controlframe, image= self.pause_btnimg, borderwidth=0)
        self.next_btn=Button(self.controlframe, image= self.next_btnimg, borderwidth=0)
        self.prev_btn=Button(self.controlframe, image= self.prev_btnimg, borderwidth=0)

        self.play_btn.grid(row=0, column=0, padx=7,pady=10)
        self.pause_btn.grid(row=0, column=1, padx=7,pady=10)
        self.next_btn.grid(row=0, column=2, padx=7,pady=10)
        self.prev_btn.grid(row=0, column=3, padx=7,pady=10)
playerdmusica()