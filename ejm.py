import customtkinter, tkinter
from tkinter import StringVar, messagebox, ttk

customtkinter.set_default_color_theme("green")

# Inicializar la ventana principal
ventana_ini = customtkinter.CTk()
ventana_ini.geometry("1000x600")
ventana_ini.title("RopaUrbana")

def iniciar_sesion():
    any

f_ven_login = customtkinter.CTkFrame(ventana_ini, width=450, height=500, fg_color="transparent", corner_radius=10)
f_ven_login.pack(padx=10, pady=10)

f2_ven_login = customtkinter.CTkFrame(f_ven_login, width=450, height=500, fg_color="gray", corner_radius=10)
f2_ven_login.pack(padx=10, pady=10)

l_login = customtkinter.CTkLabel(f2_ven_login, text="Iniciar sesión", font=("Arial", 50, "bold"), width=1000, height=50, text_color="black")
l_login.place(relx=0.5, rely=0.1, anchor="center")

l_login_name = customtkinter.CTkLabel(f2_ven_login, text="Usuario:", text_color="black", font=("Arial", 30, "bold")) 
l_login_name.place(relx=0.2, rely=0.3, anchor="center")

l_login_pass = customtkinter.CTkLabel(f2_ven_login, text="Contraseña:", text_color="black", font=("Arial", 25, "bold")) 
l_login_pass.place(relx=0.2, rely=0.4, anchor="center")

pass_entry = customtkinter.CTkEntry(f2_ven_login, width=200, height=25, corner_radius=10, text_color="black", font=("Arial", 15, "bold"))
pass_entry.place(relx=0.7, rely=0.4, anchor="center")

user_entry = customtkinter.CTkEntry(f2_ven_login, width=200, height=25, corner_radius=10, text_color="black", font=("Arial", 15, "bold"))
user_entry.place(relx=0.7, rely=0.3, anchor="center")

boton_iniciar = customtkinter.CTkButton(f2_ven_login, width=100, height=50, font=("Arial",40,"bold"),corner_radius=10, text="Enter", command=iniciar_sesion)
boton_iniciar.place(relx=0.3, rely=0.55)

ventana_ini.mainloop()