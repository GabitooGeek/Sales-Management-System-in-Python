import os
from customtkinter import *

class App(CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Configuración de los frames y etiquetas
        self.FRAME0 = CTkFrame(master=self, fg_color="transparent")
        self.FRAME0.pack_propagate(False)
        self.FRAME0.pack(pady=(5, 5), expand=1, fill="both", padx=(5, 0), side="left")
        self.LABEL18 = CTkLabel(master=self.FRAME0, text="Panel\nAdmin !", justify="left", anchor="w", text_color=("gray10", "#FFFFFF"), font=CTkFont(size=82))
        self.LABEL18.pack(padx=(30, 0), expand=1, fill="x")

        # Marco para el formulario de login
        self.FRAME2_copy = CTkFrame(master=self)
        self.FRAME2_copy.pack_propagate(False)
        self.FRAME2_copy.pack(pady=(20, 20), expand=1, fill="both", padx=(5, 20), side="left")
        self.FRAME2 = CTkFrame(master=self.FRAME2_copy, width=465, height=400, fg_color="transparent")
        self.FRAME2.pack(expand=1, padx=50, pady=100)

        # Título del formulario
        self.LABEL3 = CTkLabel(master=self.FRAME2, text="Login", anchor="w", text_color=("gray10", "#FFFFFF"), font=CTkFont(size=39))
        self.LABEL3.pack(fill="x")

        # Campo de usuario
        self.FRAME5 = CTkFrame(master=self.FRAME2, fg_color="transparent")
        self.FRAME5.pack(pady=(0, 0), fill="x")
        self.LABEL8_copy = CTkLabel(master=self.FRAME5, text="Usuario", anchor="w", text_color=("gray10", "#FFFFFF"), font=CTkFont(size=15))
        self.LABEL8_copy.pack(fill="x")
        self.ENTRY9 = CTkEntry(master=self.FRAME5, placeholder_text="example@gmail.com", height=35, corner_radius=3, text_color=("gray10", "#FFFFFF"), width=222)
        self.ENTRY9.pack(fill="x")

        # Campo de contraseña
        self.FRAME11_copy = CTkFrame(master=self.FRAME2, fg_color="transparent")
        self.FRAME11_copy.pack(pady=(10, 0), fill="x")
        self.LABEL12_copy = CTkLabel(master=self.FRAME11_copy, text="Password", anchor="w", text_color=("gray10", "#FFFFFF"), font=CTkFont(size=15))
        self.LABEL12_copy.pack(fill="x")
        self.ENTRY13_copy = CTkEntry(master=self.FRAME11_copy, placeholder_text="", height=35, corner_radius=3, text_color=("gray10", "#FFFFFF"), show="*")
        self.ENTRY13_copy.pack(fill="x")

        # Botón de login con verificación
        self.FRAME13 = CTkFrame(master=self.FRAME2, fg_color="transparent")
        self.FRAME13.pack(pady=(20, 20), fill="x")
        self.BUTTON16 = CTkButton(master=self.FRAME2, text="Login", height=35, text_color=("gray98", "#FFFFFF"), fg_color=("#8651ff", "#8651ff"), hover_color=("#6940c9", "#6940c9"), width=500, corner_radius=3, command=self.verify_login)
        self.BUTTON16.pack(fill="x")

        # Mensaje de resultado del login
        self.result_label = CTkLabel(master=self.FRAME2, text="", text_color=("red", "#FFFFFF"), font=CTkFont(size=15))
        self.result_label.pack(pady=(10, 0))

    def verify_login(self):
        username = self.ENTRY9.get()
        password = self.ENTRY13_copy.get()
        
        # Verificar si los datos ingresados coinciden con "admin admin"
        if username == "admin" and password == "admin":
            self.result_label.configure(text="¡Inicio de sesión exitoso!", text_color=("green", "#00FF00"))
            self.open_gestor_ventas()  # Llamar a la función para abrir el archivo y cerrar la ventana
        else:
            self.result_label.configure(text="Usuario o contraseña incorrectos", text_color=("red", "#FF0000"))

    def open_gestor_ventas(self):
        # Abrir el archivo gestor_ventas.py y cerrar la ventana de login
        os.system("python3 gestor_de_ventas.py")  # Asegúrate de que el archivo esté en la misma carpeta o especifica la ruta completa
        self.destroy()  # Cerrar la ventana de login después de abrir el archivo

set_default_color_theme("green")
root = App()
root.geometry("1366x768")
root.title("Login")
root.configure(fg_color=['gray92', 'gray14'])
root.mainloop()
