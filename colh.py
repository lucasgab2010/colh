from tkinter import *

vtn = Tk()
vtn.title("C-NAG200")
vtn.geometry("220x200")
vtn.config(background="blue")


def caudal():

    a = ((((int(txt2.get())) / 10) ** 5) * 10)
    b = (1.3*(int(txt1.get())))
    caudal = (a/b) ** 0.5
    return Resultado.set(caudal)


Resultado = StringVar()


def Salir():
    vtn.destroy()


lbl1 = Label(vtn, text="longitud mts", bg="yellow", fg="black")
lbl1.grid(row=1, column=1)
txt1 = Entry(vtn)
txt1.grid(row=1, column=2)
lbl2 = Label(vtn, text="diametro mm", bg="yellow", fg="black")
lbl2.grid(row=2, column=1)
txt2 = Entry(vtn)
txt2.grid(row=2, column=2)


btnCaudal = Button(vtn, text="Caudal", command=caudal)
btnCaudal.grid(row=4, column=1, columnspan=2)

btnSalir = Button(vtn, text="Salir", bg="yellow", fg="black", command=Salir)
btnSalir.grid(row=3, column=1, columnspan=2)

lblRes = Label(vtn, bg="red", fg="black", width=30, textvariable=Resultado)
lblRes.grid(row=5, column=1, columnspan=2)

vtn.mainloop()
