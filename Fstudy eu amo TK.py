from tkinter import *
from tkinter import ttk
from translate import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil

mu = Tk()
 #paletta de cores
 # preto #000000
 # vermelho #C90324
 #azivis #052875

sty = Translator(from_lang="english", to_lang="pt-br")
class tradutordeenglish():
    def __init__(self):
        self.trad=Toplevel(mu)
        self.trad.geometry('250x400')
        self.texto=Entry(self.trad)
        self.texto.pack()
        self.traducao=Label(self.trad,text='', background='red')
        self.traducao.place(relx=0.4,rely=0.1,relheight=0.05,relwidth=0.3)
        self.tradbotao=Button(self.trad,text='traduzir', command=self.traduzir)
        self.tradbotao.place(relx=0.4,rely=0.2,relheight=0.05,relwidth=0.3)
        self.tradbotao=Button(self.trad,text='tela2', command=self.tela2)
        self.tradbotao.place(relx=0.4,rely=0.3,relheight=0.05,relwidth=0.3)
        self.trad.mainloop()
    def traduzir(self):
        self.traducao.configure(text=(sty.translate(self.texto.get())))

    def tela2(self):
        self.tl2=Toplevel(mu)
        self.tl2.geometry('125x200')
        self.tl2.title('tela222')

        self.eversom=PhotoImage(file='imagens\\eversom125x200.png')
        self.zoio=Label(self.tl2,image=self.eversom)
        self.zoio.pack()

        self.zoeiragarai=Label(self.tl2,text='só pra zoar garai\n kkkkkkkkkkkkkkkkkkkkkkk')
        self.zoeiragarai.place(relx=0,rely=0.7)

        self.botao=Button(self.tl2,text='aaa', background='black')
        self.botao.pack()
        self.tl2.mainloop()

class calculadora():
    def __init__(self):
        self.calc=Toplevel(mu)
        self.tela()
        self.widgets()
        mu.mainloop()
    def tela(self):
        self.calc.title('calculdora da desgraça')
        self.calc.geometry('250x400')
        self.calc.resizable(True,True)
        self.calc.configure(background="#5ce1e6")
    def widgets(self):
        self.calclogo=Label(self.calc,text='calculadora',background='#5ce1e6')
        self.calclogo.place(relx=0.25,rely=0.05,relheight=0.15,relwidth=0.5)

        self.playbutton=Label(self.calc,text='digite sua questão', background='red', highlightbackground='blue', highlightthickness=2)
        self.playbutton.place(relx=0.15,rely=0.24,relwidth=0.7,relheight=0.05)

        self.showmusic=Entry(self.calc,background='red', highlightbackground='blue', highlightthickness=2)
        self.showmusic.place(relx=0.15,rely=0.28, relwidth=0.7,relheight=0.1)


        self.resultadodaop=Label(self.calc,text='', background='blue', highlightbackground='red', highlightcolor='blue', highlightthickness=2)
        self.resultadodaop.place(relx=0.4, rely=0.5, relwidth=0.15, relheight=0.1)

        self.acao=Button(self.calc,text='calcular', command=self.aoclicar)
        self.acao.place(relx=0.9,rely=0.9, relwidth=0.1, relheight=0.1)
    def aoclicar(self):
        self.resultadodaop.configure(text=str(eval(self.showmusic.get())))
class mplayer():
    def __init__(self):
        self.mpl=Toplevel(mu)
        self.tela()
        self.widgets()
        mu.mainloop()
    
    def tela(self):
        self.mpl.title('player de musica')
        self.mpl.geometry('250x400')
        self.mpl.resizable(True,True)
        self.mpl.configure(background="black")

    def widgets(self):
        self.bolso=PhotoImage(file='imagens\Bbombado_250x400.png')
        self.bolsolabel=Label(self.mpl,image=self.bolso)
        self.bolsolabel.pack()

        self.ytlogo=Label(self.mpl,text='logo',background='red', highlightbackground='blue', highlightthickness=2)
        self.ytlogo.place(relx=0.35,rely=0.1,relheight=0.2,relwidth=0.3)

        self.playbutton=Button(self.mpl,text='play msc', background='blue', highlightbackground='red', highlightthickness=2)
        self.playbutton.place(relx=0,rely=0.3,relwidth=0.2,relheight=0.1)

        self.showmusic=Label(self.mpl,text='sua musica', background='white', highlightbackground='blue', highlightthickness=2)
        self.showmusic.place(relx=0.2,rely=0.3, relwidth=0.8,relheight=0.1)
class musica():
        def __init__(self):
            self.mp=Toplevel(mu)
            self.tela()
            self.labels()
            self.mp.mainloop()
        
        def tela(self):
            self.mp.title('dowlader de musica')
            self.mp.geometry('250x400')
            self.mp.resizable(True, True)
            self.mp.configure(background='black')

        def selecionardiretorio(self):
            diretoriopath= filedialog.askdirectory()
            self.diretorio.configure(text=diretoriopath)

        def baixarvideo(self):
            self.getlink = self.linkentry.get()
            self.dowdir= self.diretorio.cget('text')
            self.mp.title('baixando...')

            self.vid = YouTube(self.getlink).streams.get_highest_resolution().download()
            self.vid_clip= VideoFileClip(self.vid)
            self.vid_clip.close()
            self.mp.title('movendo..')
            shutil.move(self.vid,self.dowdir)
            self.mp.title('manda que o pai tá on')

        def labels(self):

            self.fundo=PhotoImage(file="imagens\\lula250x400.png")
            self.fundoimg=Label(self.mp,image=self.fundo)
            self.fundoimg.pack()

            self.logo=Label(self.mp,text='youtube', background='green')
            self.logo.place(relx=0.35, rely=0.05, relwidth=0.3,relheight=0.2)

            self.linkentry=Entry(self.mp, background='green')
            self.linkentry.place(relx=0.15,rely=0.25, relwidth=0.7, relheight=0.05)

            self.diretorio=Label(self.mp, text='seu diretorio aparecerá aqui')
            self.diretorio.place(relx=0,rely=0.35, relwidth=1,relheight=0.05)
            self.askdir=Button(self.mp, text='diretório',command=self.selecionardiretorio)
            self.askdir.place(relx=0.3,rely=0.4, relwidth=0.3,relheight=0.05)

            self.labellink=Label(self.mp, text='link')
            self.labellink.place(relx=0,rely=0.25, relwidth=0.1,relheight=0.05)

            self.titulolab=Label(self.mp, background='red',text='')
            self.titulolab.place(relx=0.15,rely=0.45, relwidth=0.7, relheight=0.05)
            self.titulolab2=Label(self.mp, text='titulo')
            self.titulolab2.place(relx=0,rely=0.45, relwidth=0.1,relheight=0.05)


            self.viewlab=Label(self.mp, background='red',text='')
            self.viewlab.place(relx=0.15,rely=0.55, relwidth=0.7, relheight=0.05)
            self.viewlab2=Label(self.mp, text='views')
            self.viewlab2.place(relx=0,rely=0.55, relwidth=0.1,relheight=0.05)

            self.tamlab=Label(self.mp, background='blue',text='')
            self.tamlab.place(relx=0.15,rely=0.65, relwidth=0.7, relheight=0.05)
            self.tamlab2=Label(self.mp, text='tamanho')
            self.tamlab2.place(relx=0,rely=0.65, relwidth=0.1,relheight=0.05)

            self.likeslab=Label(self.mp, background='orange',text='')
            self.likeslab.place(relx=0.15,rely=0.75, relwidth=0.7, relheight=0.05)
            self.likeslab2=Label(self.mp, text='likes')
            self.likeslab2.place(relx=0,rely=0.75, relwidth=0.1,relheight=0.05)

            self.botaodowoad=Button(self.mp, text='dowload', background='white', command=self.baixarvideo)
            self.botaodowoad.place(relx=0.7,rely=0.9, relheight=0.1, relwidth=0.3)

            self.getinfo=Button(self.mp, text='get info', background='white')
            self.getinfo.place(relx=0.4,rely=0.9, relheight=0.1, relwidth=0.3)

class fs(musica,mplayer, calculadora):
    def __init__(self):
        self.mu = mu
        self.tela()
        self.frame()
        mu.mainloop()

    def tela(self):
        self.mu.title('facility study')
        self.mu.geometry('250x400')
        self.mu.resizable(False,False)
        self.mu.configure(background='black')

    def frame(self):
        self.frame1=Frame(self.mu,bd=4,bg='black', highlightbackground='grey', highlightthickness=2)
        self.frame1.place(relx=0.0, rely=0.05, relheight=1,relwidth=1)

        self.frame2=Frame(self.mu,bd=1,bg='black', highlightbackground='black', highlightthickness=1)
        self.frame2.place(relx=0.0,rely=0.0, relwidth=1,relheight=0.05)

        self.botao1=Button(self.frame1, text='tradutor', command= tradutordeenglish)
        self.botao1.place(relx=0.01, rely=0.01, relheight=0.15,relwidth=0.3)

        self.botao2=Button(self.frame1, text='cronograma')
        self.botao2.place(relx=0.35, rely=0.01, relheight=0.15,relwidth=0.3)

        self.botao3=Button(self.frame1, text='calc. notas')
        self.botao3.place(relx=0.7, rely=0.01, relheight=0.15,relwidth=0.3)


        self.botao4=Button(self.frame1, text='calculadora', command= calculadora)
        self.botao4.place(relx=0.01, rely=0.2, relheight=0.15,relwidth=0.3)

        self.botao5=Button(self.frame1, text='player \n musica', command= mplayer)
        self.botao5.place(relx=0.35, rely=0.2, relheight=0.15,relwidth=0.3)

        self.botao6=Button(self.frame1, text='dow. musica', command=musica)
        self.botao6.place(relx=0.7, rely=0.2, relheight=0.15,relwidth=0.3)


        self.nomeapp=Label(self.frame2, text = 'facility study')
        self.nomeapp.place(relx=0.35, rely= 0.0)

        self.delbotao= Button(self.frame1, command=mu.destroy, text='fechar tela')
        self.delbotao.place(relx=0,rely=0.9,relwidth=0.3,relheight=0.1)

fs()