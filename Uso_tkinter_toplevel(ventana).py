import tkinter

def funcion():
    Otraventana.state(newstate = "normal")
    root.state(newstate = "withdraw")

def funcion2():
    Otraventana.state(newstate = "withdraw")
    root.state(newstate = "normal") #state(newstate = "withdraw")root.deiconify, zoomed()


root = tkinter.Tk()
root.state(newstate = "normal")
root.geometry("250x150+300+100")
root.resizable(0, 0)
root.title("Ventana 1")

abrirVentana2 = tkinter.Button(root, text="Abrir ventana 2", bg="green", font= ("Times New Roman", 12), fg="yellow", command=funcion)
abrirVentana2.pack()

Otraventana = tkinter.Toplevel()
Otraventana.state(newstate = "withdraw")
Otraventana.geometry("250x150+300+100")
Otraventana.title("Ventana 2")

miEtiqueta = tkinter.Label(Otraventana, text="Bienvenido a la ventana 2", bg="#252850", font=("Times New Roman", 12), fg="yellow")
miEtiqueta.pack()

abrirVentana1 = tkinter.Button(Otraventana, text="Abrir ventana principal", bg="green", font= ("Times New Roman", 12), fg="yellow", command=funcion2)
abrirVentana1.pack()

Otraventana.mainloop()
root.mainloop()

import tkinter as tk


def createNewWindow():
    newWindow = tk.Toplevel(app)
    labelExample = tk.Label(newWindow, text="New Window")
    buttonExample = tk.Button(newWindow, text="New Window button")

    labelExample.pack()
    buttonExample.pack()


app = tk.Tk()
buttonExample = tk.Button(app, text="Create new window", command=createNewWindow)
buttonExample.pack()

app.mainloop()

