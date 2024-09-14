import os, customtkinter, mysql.connector, tkinter 
from tkinter import StringVar, messagebox, ttk
from PIL import Image

# Intentar conectar a la base de datos MySQL
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="RopaUrbana"
    )
    cursor = db.cursor()
except mysql.connector.Error as err:
    # Mostrar un mensaje de error si la conexión falla y cerrar la aplicación
    messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {err}")
    app.destroy()

# Configurar la apariencia y el tema de color para customtkinter
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

# Inicializar la ventana principal
ventana_ini = customtkinter.CTk()
ventana_ini.geometry("1000x600")
ventana_ini.title("RopaUrbana")

#ventana inicial
f_ven_ini_tit = customtkinter.CTkFrame(ventana_ini, width=1000, height=50, fg_color="black")
f_ven_ini_tit.pack(padx=10, pady=10)

l_tit = customtkinter.CTkLabel(f_ven_ini_tit, text="RopaUrbana", font=("Arial", 50, "bold"), width=1000, height=50, text_color="white")
l_tit.place(relx=0.5, rely=0.5, anchor="center")

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

f_buttons = customtkinter.CTkFrame(ventana_ini, width=550, corner_radius=10, height=200, fg_color=("black"))
f_buttons.place(relx=0.3, rely=0.4, anchor="center")

b_vender = customtkinter.CTkButton(f_buttons, text="Vender",font=("Arial", 40, "bold"), fg_color="lime", width=200, height=50, corner_radius=10,command=boton_vender,text_color="black")
b_vender.place(relx=0.3, rely=0.3, anchor="center")

b_inventario = customtkinter.CTkButton(f_buttons, text="Inventario",  font=("Arial", 35, "bold"),  width=200, height=50,   corner_radius=10, command=boton_inventario, text_color="black",fg_color="orange")
b_inventario.place(relx=0.7, rely=0.3, anchor="center")

b_ventas = customtkinter.CTkButton(f_buttons, text="Ventas", font=("Arial", 40, "bold"),  command=boton_ventas  ,width=200, height=50, corner_radius=10, fg_color="yellow", text_color="black")
b_ventas.place(relx=0.3, rely=0.7, anchor="center")

b_salir = customtkinter.CTkButton(f_buttons, text="Salir", text_color="black",font=("Arial", 40, "bold"), corner_radius=10, width=200, command=boton_salir, height=50)
b_salir.place(relx=0.7, rely=0.7, anchor="center")

f_autor = customtkinter.CTkFrame(ventana_ini, width=550, corner_radius=10,  height=150, fg_color=("black"))
f_autor.place(relx=0.3, rely=0.8, anchor="center")
l_autor = customtkinter.CTkLabel(f_autor, text="Gabriel Tellez - Javier Murcia", text_color="white" , font=("Arial", 35, "bold"), width=50, height=50)
l_autor.place(relx=0.5, rely=0.5, anchor="center")

ventana_ini.mainloop()
