import tkinter,requests
from tkinter import messagebox
from datetime import datetime

API_KEY="3b3ddc5f98b8f6502b43eea92f40a73d"
BASE_URL="http://api.openweathermap.org/data/2.5/weather"



def dadosweather(cidade):
    params={
        'q':cidade,
        'appid':API_KEY,
        'units':'metric',
        'lang':'pt'
    }

    response=requests.get(BASE_URL,params=params)

    return response.json()

def guardarhistorico(cidade,temperatura):
    with open('histórico','a') as ficheiro:
        data_hora=datetime.now().strftime('%Y-&m-%d %H:%M:%S')
        ficheiro.write(f'{data_hora} - {cidade}: {temperatura}ºC\n')

class AppMeteorologia:
    def __init__(self,root):
        self.root=root
        self.root.title('App de metereologia')
        self.root.geometry('480x300')
        self.root.config(bg='gray')
        self.labeltittle=tkinter.Label(root,text='Cidade/País'
                                       ,bg='gray'
                                       ,font=('Arial',24,'bold'))
        self.labeltittle.place(x=150,y=25)

        self.entry=tkinter.Entry(root)
        self.entry.place(x=150,y=100)

        self.butao=tkinter.Button(root,text='Search',command=self.search)
        self.butao.place(x=285,y=100)

        self.label=tkinter.Label(root,text='Não há nada para ver aqui',bg='gray',font=('Arial',12))
        self.label.place(x=150,y=150)

    def search(self):
        cidade=self.entry.get()
        
        if cidade:
            dados=dadosweather(cidade)

def main():
    root=tkinter.Tk()
    app=AppMeteorologia(root)
    root.mainloop()

if __name__=='__main__':
    main()