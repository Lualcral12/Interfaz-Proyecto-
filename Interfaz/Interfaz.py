import Operaciones as op
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

RutaImagen = None

def SeleccionarImagen(EtiquetaIma):
    global RutaImagen
    RutaImagen = filedialog.askopenfilename(
        initialdir="~/Desktop", 
        title="Seleccionar imagen",
        filetypes=[("Archivos de imagen", "*.png *.jpg *.jpeg *.bmp *.gif")]
    )
    if RutaImagen: 
        op.CargarImagen(RutaImagen, EtiquetaIma)
        CargarImagen.place_forget()

def InterpolarYGuardar():
    
    ImagenNueva = op.AumentarResolucion(RutaImagen)
    ImagenNueva.save('C:/Users/ALONSO/Desktop/foto.jpg')
    ImagenNueva.show()

def MostrarInicio(CargarImagen):
    CargarImagen.place(relx = 0.5, rely = 0.5, anchor = "center")


Ventana = Tk()
Ventana.title("Interpolación en Imágenes")
Ventana.geometry("1200x600")
Ventana.config(bg = "Black")
Ventana.resizable(False, False)

ImagenCargada = Frame(Ventana, bg = "Black", width = 1000, height = 600)
ImagenCargada.place(relx = 0.5, rely = 0.5, anchor = "center")

EtiquetaImagen = Label(ImagenCargada, text="La imagen seleccionada se mostrará aquí")
EtiquetaImagen.place(relx = 0.5, rely = 0.5, anchor = "center")

BTNInicio = Button(ImagenCargada, text = "Interpolar Imagen", font = ("Segoe UI", 24, "normal" ), fg = "white", relief="flat", bg = "#FC922F", command = lambda:InterpolarYGuardar())
BTNInicio.place(relx = 0.5, rely = 0.9, anchor="center", width=400, height=60)

#-----------------------------------------------------------------------------------------------

CargarImagen = Frame(Ventana, bg = "Black", width = 1000, height = 600)
CargarImagen.place(relx = 0.5, rely = 0.5, anchor = "center")

Titulo = Label(CargarImagen, text = "Interpolación en Imágenes.", fg = "White", bg = "Black", font = ("Segoe UI", 36, "bold"))
Titulo.place(relx = 0.5, rely = 0.3, anchor = "center")

Titulo = Label(CargarImagen, text = "Selecciona una imagen para duplicar su resolución.", fg = "White", bg = "Black", font = ("Segoe UI", 28, "normal"))
Titulo.place(relx = 0.5, rely = 0.43, anchor = "center")

BTNSeleccion = Button(CargarImagen, text = "Seleccionar", font = ("Segoe UI", 24, "normal" ), fg = "white", relief="flat", bg = "#FC922F", command =lambda:SeleccionarImagen(EtiquetaImagen) )
BTNSeleccion.place(relx = 0.5, rely = 0.7, anchor="center", width=200, height=60)

#-------------------------------------------------------------------------------------------------------
BTNBorrar = Button(ImagenCargada, text = "--", fg = "Black", command= lambda:MostrarInicio(CargarImagen))
BTNBorrar.place(relx = 0.8, rely = 0.2, anchor="center", width=50, height=50)


Ventana.mainloop()

