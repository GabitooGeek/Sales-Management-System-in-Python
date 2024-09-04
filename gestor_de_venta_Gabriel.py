import customtkinter, tkinter, os
from tkinter import *
from PIL import Image

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")

# Main Window
ventana_ini = customtkinter.CTk()
ventana_ini.geometry("1000x500")
ventana_ini.title("RopaUrbana")

# Title Frame
f_ven_ini_tit = customtkinter.CTkFrame(ventana_ini, width=1000, height=50, fg_color="black")
f_ven_ini_tit.pack(padx=10, pady=10)

l_tit = customtkinter.CTkLabel(f_ven_ini_tit, text="RopaUrbana", font=("Arial", 50, "bold"), width=1000, height=50, text_color="white")
l_tit.place(relx=0.5, rely=0.5, anchor="center")

# Image Display
image_path_ves_verde = os.path.join(os.path.dirname(__file__), "ves_verde.jpg")
image_ves_verde = customtkinter.CTkImage(light_image=Image.open(image_path_ves_verde), size=(150, 250))
l_image_vestido_ver = customtkinter.CTkLabel(ventana_ini, image=image_ves_verde, text="")
l_image_vestido_ver.place(relx=0.8, rely=0.45, anchor="center")

image_path_ves_negro = os.path.join(os.path.dirname(__file__), "ves_negro.jpg")
image_ves_negro = customtkinter.CTkImage(light_image=Image.open(image_path_ves_negro), size=(150, 250))
l_image_vestido_neg = customtkinter.CTkLabel(ventana_ini, image=image_ves_negro, text="")
l_image_vestido_neg.place(relx=0.9, rely=0.55, anchor="center")

image_path_ves_naranja = os.path.join(os.path.dirname(__file__), "con_blan.jpg")
image_ves_naranja = customtkinter.CTkImage(light_image=Image.open(image_path_ves_naranja), size=(150, 250))
l_image_vestido_nar = customtkinter.CTkLabel(ventana_ini, image=image_ves_naranja, text="")
l_image_vestido_nar.place(relx=0.7, rely=0.65, anchor="center")

# Button Frame
f_buttons = customtkinter.CTkFrame(ventana_ini, width=550, corner_radius=10, height=200, fg_color=("black"))
f_buttons.place(relx=0.3, rely=0.4, anchor="center")

# Button Functions (Open new windows)
def boton_vender():
    ventana_vender = customtkinter.CTk()
    ventana_vender.geometry("1000x500")  
    ventana_vender.title("Vender Producto")

    f_ven_vender_tit = customtkinter.CTkFrame(ventana_vender, width=1000, height=50, fg_color="black")
    f_ven_vender_tit.pack(padx=10, pady=10)

    l_ven_tit = customtkinter.CTkLabel(f_ven_vender_tit, text="Vender", font=("Arial", 50, "bold"), width=1000, height=50, text_color="white")
    l_ven_tit.place(relx=0.5, rely=0.5, anchor="center")

    f_vender = customtkinter.CTkFrame(ventana_vender, width=900, height=400,corner_radius=10, fg_color="gray")
    f_vender.pack(padx=10, pady=10)

    l_id = customtkinter.CTkLabel(f_vender, text="Producto:", font=("Arial", 30, "bold"), width=200, height=30, text_color="white")
    l_id.place(relx=0.2, rely=0.2, anchor="center")

    l_cant = customtkinter.CTkLabel(f_vender, text="Cantidad:", font=("Arial", 30, "bold"), width=200, height=30, text_color="white")
    l_cant.place(relx=0.2, rely=0.4, anchor="center")

    l_precio = customtkinter.CTkLabel(f_vender, text="Precio", font=("Arial", 30, "bold"), width=200, height=30, text_color="white")
    l_precio.place(relx=0.2, rely=0.6, anchor="center")

    l_total = customtkinter.CTkLabel(f_vender, text="Total", font=("Arial", 30, "bold"), width=200, height=30, text_color="white")
    l_total.place(relx=0.2, rely=0.8, anchor="center")

    idp_entry = customtkinter.CTkEntry(f_vender, width=200, height=30, text_color="black", fg_color="white", border_color="gray")
    idp_entry.place(relx=0.4, rely=0.2, anchor="center")

    cant_entry = customtkinter.CTkEntry(f_vender, width=200, height=30, text_color="black", fg_color="white", border_color="gray")
    cant_entry.place(relx=0.4, rely=0.4, anchor="center")

    def vender_productos():
        pass

    b_vender = customtkinter.CTkButton(f_vender, text="Vender", font=("Arial", 30, "bold"), corner_radius=10,width=200, height=30, command=vender_productos)
    b_vender.place(relx=0.8, rely=0.6, anchor="center")

    def ventana_atras():
        ventana_vender.destroy()

    b_atras_vend = customtkinter.CTkButton(f_vender, text="Atrás",corner_radius=10, font=("Arial", 30, "bold"), width=200, height=30, command=ventana_atras)
    b_atras_vend.place(relx=0.8, rely=0.8, anchor="center")

    image_path_car = os.path.join(os.path.dirname(__file__), "car.jpg")
    image_car = customtkinter.CTkImage(light_image=Image.open(image_path_car), size=(150, 250))
    l_image_car = customtkinter.CTkLabel(f_vender, image=image_car, text="")
    l_image_car.place(relx=0.7, rely=0.65, anchor="center")

    ventana_vender.mainloop()

def boton_inventario():
    ventana_inventario = customtkinter.CTk()
    ventana_inventario.geometry("1000x500")
    ventana_inventario.title("Inventario")
    # Add content for "Inventario" window here
    ventana_inventario.mainloop()

def boton_agregar_prod():
    ventana_agregar = customtkinter.CTk()
    ventana_agregar.geometry("1000x500")
    ventana_agregar.title("Agregar Producto")
    # Add content for "Agregar Producto" window here
    ventana_agregar.mainloop()

def boton_ventas():
    ventana_ventas = customtkinter.CTk()
    ventana_ventas.geometry("1000x500")
    ventana_ventas.title("Ventas")
    # Add content for "Ventas" window here
    ventana_ventas.mainloop()

def boton_salir():
    ventana_ini.destroy()  

# Buttons
b_vender = customtkinter.CTkButton(f_buttons, text="Vender", 
                                    font=("Arial", 40, "bold"), width=200,
                                    height=50, corner_radius=10, 
                                    command=boton_vender)
b_vender.place(relx=0.3, rely=0.3, anchor="center")

b_inventario = customtkinter.CTkButton(f_buttons, text="Inventario", 
                                        font=("Arial", 40, "bold"), 
                                        width=100, height=50, 
                                        corner_radius=10, command=boton_inventario)
b_inventario.place(relx=0.7, rely=0.3, anchor="center")

b_agregar_prod = customtkinter.CTkButton(f_buttons, text="Agregar", 
                                            font=("Arial", 40, "bold"), command=boton_agregar_prod,
                                            corner_radius=10, 
                                            width=200, height=50)
b_agregar_prod.place(relx=0.3, rely=0.7, anchor="center")

b_ventas = customtkinter.CTkButton(f_buttons, text="Ventas", font=("Arial", 40, "bold"), 
                                    command=boton_ventas 
                                    ,width=200, height=50, corner_radius=10)
b_ventas.place(relx=0.7, rely=0.7, anchor="center")

# Author Frame
f_autor = customtkinter.CTkFrame(ventana_ini, width=550, corner_radius=10, 
                                    height=150, fg_color=("black"))
f_autor.place(relx=0.3, rely=0.8, anchor="center")

l_autor = customtkinter.CTkLabel(f_autor, text="Gabriel Tellez", text_color="white" , font=("Arial", 40, "bold"), width=50, height=50)
l_autor.place(relx=0.3, rely=0.5, anchor="center")

b_salir = customtkinter.CTkButton(f_autor, text="Salir", font=("Arial", 40, "bold"), corner_radius=10, width=100, command=boton_salir, height=50)
b_salir.place(relx=0.8, rely=0.6, anchor="center")

ventana_ini.mainloop()