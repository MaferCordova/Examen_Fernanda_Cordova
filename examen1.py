from tkinter import *
v = Tk()
v.geometry("640x480")
v.title('Menu de seleccion')
def abrir():
    v1=Tk()
    v1.geometry("450x480")
    v1.title('Area y perimetro')
    nl=IntVar()
    vl=IntVar()
    etiqueta1 = Label(v1, text="Ingrese el numero de la dos de la figura geometrica: ").grid(row=0, column=0, sticky=W, pady=4)
    etiqueta2 = Label(v1, text="Ingrese el valor de los lados: ").grid(row=1, column=0, sticky=W, pady=4)
    e1 = Entry(v1,textvariable=nl)
    e2 = Entry(v1,textvariable=vl)
    e1.grid(row=0, column=5)
    e2.grid(row=1, column=5)

    def perimetro():
        if (e1.get()>3):
            p=int(e1.get()*int(e2.get())
            etiqueta3 = Label(v1, text="El perimetro es: ").grid(row=2, column=0, sticky=W, pady=4)
            etiqueta5 = Label(v1, text=p).grid(row=2, column=0, sticky=W, pady=4)
    def area():
        
                          
btn3=Button(v1, text ="Calcular", command=perimetro).grid(row=3, column=5, sticky=W, pady=4)
     
    
    
def abrir2():
    v2=Tk()
    v2.geometry("240x380")
    v2.title('Animacion')

etiqueta = Label(v, text="Seleccione: ").grid(row=0, column=0, sticky=W, pady=4)
btn=Button(v, text ="1. AREA Y PERIMETRO", command=abrir).grid(row=1, column=0, sticky=W, pady=4)
btn1=Button(v, text ="2. ANIMACION", command=abrir2).grid(row=2, column=0, sticky=W, pady=4)



mainloop()


 
#Label(master, text="First Name").grid(row=0)
#Label(master, text="Last Name").grid(row=1)
#e1 = Entry(master)
#e2 = Entry(master)
#e1.grid(row=0, column=1)
#e2.grid(row=1, column=1)
