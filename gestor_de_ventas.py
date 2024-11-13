import os, customtkinter, mysql.connector, tkinter 
from tkinter import StringVar, messagebox, ttk
from PIL import Image

# Inicializar la ventana principal
ventana_ini = customtkinter.CTk()
ventana_ini.geometry("1000x600")
ventana_ini.title("RopaUrbana")

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
    ventana_ini.destroy()

# Configurar la apariencia y el tema de color para customtkinter
customtkinter.set_appearance_mode("dark")

# Metodos
def boton_salir():
    ventana_ini.destroy()

def boton_ventas():
    f_buttons.place_forget()
    f_b_salir.place_forget()
    fr_marco_ventas.place(relx=0.625, rely= 0.39, anchor="center")
    fr_ventas_volver.place(relx=0.15, rely= 0.55, anchor="center")

def boton_inventario():
    f_buttons.place_forget()
    f_b_salir.place_forget()
    fr_marco_inventario.place(relx=0.675, rely= 0.39, anchor="center")
    fr_agre_volver.place(relx=0.2, rely= 0.55, anchor="center")
    fr_mens_agre.place(relx=0.675, rely=0.84, anchor="center")

def boton_vender():
    f_b_salir.place_forget()
    f_buttons.place_forget()
    fr_marco_vender.place(relx=0.1, rely=0.2)
    fr_compra_reali.place(relx=0.35, rely= 0.8, anchor="center")
    fr_carr_img.place(relx=0.82, rely= 0.33, anchor="center")
    fr_boton_comprar.place(relx=0.77, rely=0.72, anchor="center")

def ven_inicio():
    f_b_salir.place(relx=0.84, rely=0.9, anchor="center")
    f_buttons.place(relx=0.5, rely=0.2, anchor="center")
    f_ven_ini_tit.place(relx=0.5, rely=0.07, anchor="center")
    fr_marco_ventas.place_forget()
    fr_ventas_volver.place_forget()
    FRAME0.destroy()
    FRAME2_copy.destroy()
    FRAME2.destroy()
    FRAME11_copy.destroy()
    FRAME13.destroy()
    FRAME5.destroy()

def volver_ini_ventas():
    f_b_salir.place(relx=0.84, rely=0.9, anchor="center")
    f_buttons.place(relx=0.5, rely=0.2, anchor="center")
    fr_marco_ventas.place_forget()
    fr_ventas_volver.place_forget()

def volver_ini_invertario():
    f_b_salir.place(relx=0.84, rely=0.9, anchor="center")
    f_buttons.place(relx=0.5, rely=0.2, anchor="center")
    fr_marco_inventario.place_forget()
    fr_agre_volver.place_forget()
    fr_mens_agre.place_forget()

def volver_provedores():
    fr_marco_provedores.place_forget()
    fr_agre_provedores.place_forget()
    fr_mens_provedores.place_forget()
    fr_marco_inventario.place(relx=0.675, rely= 0.39, anchor="center")
    fr_agre_volver.place(relx=0.2, rely= 0.55, anchor="center")
    fr_mens_agre.place(relx=0.675, rely=0.84, anchor="center")

def boton_provedores():
    fr_marco_inventario.place_forget()
    fr_agre_volver.place_forget()
    fr_mens_agre.place_forget()
    fr_marco_provedores.place(relx=0.675, rely= 0.39, anchor="center")
    fr_agre_provedores.place(relx=0.2, rely= 0.55, anchor="center")
    fr_mens_provedores.place(relx=0.675, rely=0.84, anchor="center")

def volver_ini():
    fr_marco_vender.place_forget()
    fr_marco_vender.place_forget()
    fr_compra_reali.place_forget()
    fr_carr_img.place_forget()
    fr_boton_comprar.place_forget()
    f_buttons.place(relx=0.5, rely=0.2, anchor="center")
    f_b_salir.place(relx=0.84, rely=0.9, anchor="center")

def comprar_pro():
    try:
        producto_id = int(id_prod_entry.get())
        cantidad = int(can_prod_entry.get())

        cursor.execute("SELECT precio, stock FROM Productos WHERE id = %s", (producto_id,))
        producto = cursor.fetchone()

        if producto:
            precio, stock = producto
            if cantidad <= stock:
                total = precio * cantidad
                cursor.execute("INSERT INTO Ventas (producto_id, cantidad, total) VALUES (%s, %s, %s)",
                               (producto_id, cantidad, total))
                cursor.execute("UPDATE Productos SET stock = stock - %s WHERE id = %s", (cantidad, producto_id))
                db.commit()
                compra_detalle.set(f"Venta realizada:\n{cantidad} unidades\nTotal: ${total:.2f}")
                obtener_producto_info()
                mostrar_productos()
                mostrar_ventas() 
            else:
                messagebox.showwarning("Stock insuficiente", "No hay suficiente stock del producto seleccionado.")
        else:
            messagebox.showerror("Error", "Producto no encontrado.")
    except ValueError:
        messagebox.showerror("Error", "Ingrese un ID de producto y cantidad válidos.")

def obtener_producto_info():
    try:
        producto_id = int(id_prod_entry.get())
        cantidad = int(can_prod_entry.get())
        cursor.execute("SELECT nombre, precio, stock FROM Productos WHERE id = %s", (producto_id,))
        producto = cursor.fetchone()

        if producto:
            nombre, precio, stock = producto
            nombre_del_producto.set(nombre)
            precio_producto.set(f"${precio:.2f}")
            total_precio = precio * cantidad
            total_compra.set(f"${total_precio:.2f}")
        else:
            nombre_del_producto.set("Producto no encontrado")
            precio_producto.set("$0.00")
            total_compra.set("$0.00")
    except ValueError:
        messagebox.showerror("Error", "Ingrese un ID y cantidad de producto válido.")

def borrar_celda():
    id_prod_entry.delete(0, "end")
    can_prod_entry.delete(0, "end")
    nombre_del_producto.set("Nombre del producto")
    precio_producto.set("$0.00")
    compra_detalle.set("Detalle de venta")

def agregar_producto():
    name = nombre_entry.get()
    price = precio_entry.get()
    stock = cant_entry.get()

    if not name or not price or not stock:
        messagebox.showerror("Error", "Porfavor ingresa bien los datos.")
        return

    try:
        price = float(price)
        stock = int(stock)
    except ValueError:
        messagebox.showerror("Error", "Precio y cantidad son números.")
        return

    query = "INSERT INTO Productos (nombre, precio, stock) VALUES (%s, %s, %s)"
    values = (name, price, stock)
    cursor.execute(query, values)
    db.commit()

    producto_agregado.set(f"Producto agregado:")
    nombre_pro_agre.set(name)
    cant_prod_agre.set(stock)
    precio_agre.set(price)
    update_products()

def enter_but_agregar_borr():
    nombre_entry.delete(0, "end")
    cant_entry.delete(0, "end")
    precio_entry.delete(0, "end")
    id_entry.delete(0, "end")
    producto_agregado.set("Producto agregado")
    cant_prod_agre.set("1")
    nombre_pro_agre.set("Nombre")
    precio_agre.set("$0.0")

def borrar_ventas():
    try:
        cursor.execute("DELETE FROM Ventas")
        db.commit()
        messagebox.showinfo("Éxito", "¡Ventas eliminadas correctamente!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo eliminar las ventas: {err}")
    update_ventas()

def boton_eliminar_prove():
    id_proveedor = id_entry_pro.get()
    if not id_proveedor:
        messagebox.showwarning("Advertencia", "Ingrese el ID del proveedor.")
        return

    try:
        id_proveedor = int(id_proveedor)
        cursor.execute("DELETE FROM Proveedores WHERE id = %s", (id_proveedor,))
        db.commit()
        messagebox.showinfo("Éxito", "Proveedor eliminado correctamente.")
        id_entry.delete(0, "end")
        update_proveedores()
    except ValueError:
        messagebox.showerror("Error", "ID de proveedor inválido.")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al eliminar el proveedor: {err}")
    
def boton_agre_prove():
    name = nombre_prove_entry.get()
    contac = con_entry.get()

    if not name or not contac:
        messagebox.showerror("Error", "Porfavor ingrese un nombre y contacto.")
        return

    try: 
        query = "INSERT INTO Proveedores (nombre, contacto) VALUES (%s, %s)"
        values = (name, contac)
        cursor.execute(query, values)
        db.commit()

        provedor_agregado.set("Proveedor agregado correctamente.")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo agregar el proveedor: {err}")
    update_proveedores()

def boton_borrar_prove():
    nombre_prove_entry.delete(0, "end")
    con_entry.delete(0, "end")
    provedor_agregado.set("Provedor")

def eliminar_inve():
    id_producto = id_entry.get()
    if not id_producto:
        messagebox.showwarning("Advertencia", "Ingrese el ID del producto.")
        return

    try:
        id_producto = int(id_producto)
        cursor.execute("DELETE FROM Productos WHERE id = %s", (id_producto,))
        db.commit()
        messagebox.showinfo("Éxito", "Producto eliminado correctamente.")
        id_entry.delete(0, "end")
        update_products()
    except ValueError:
        messagebox.showerror("Error", "ID de producto inválido.")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al eliminar el producto: {err}")

def mostrar_ventas():
    for item in ventas_treeview.get_children():
        ventas_treeview.delete(item)

    cursor.execute("SELECT v.id, p.nombre, v.cantidad, v.total "
                   "FROM Ventas v "
                   "JOIN Productos p ON v.producto_id = p.id")  
    ventas = cursor.fetchall()

    for venta in ventas:
        ventas_treeview.insert("", "end", values=venta)

def mostrar_productos():
    for item in productos_treeview.get_children():
        productos_treeview.delete(item)

    cursor.execute("SELECT * FROM Productos")
    productos = cursor.fetchall()

    for producto in productos:
        productos_treeview.insert("", "end", values=producto)

def update_ventas():
    mostrar_ventas()
    ventana_ini.after(1000, update_ventas)

def update_products():
    mostrar_productos()
    ventana_ini.after(1000, update_products)

def update_proveedores():
    mostrar_proveedores()
    ventana_ini.after(1000, update_proveedores)

def mostrar_proveedores():
    for item in proveedores_treeview.get_children():
        proveedores_treeview.delete(item)

    cursor.execute("SELECT * FROM Proveedores")
    proveedores = cursor.fetchall()

    for proveedor in proveedores:
        proveedores_treeview.insert("", "end", values=proveedor)

def verify_login():
        username = ENTRY9.get()
        password = ENTRY13_copy.get()
        
        # Verificar si los datos ingresados coinciden con "admin admin"
        if username == "admin" and password == "admin":
            result_label.configure(text="¡Inicio de sesión exitoso!", text_color=("green", "#00FF00"))
            ven_inicio()  # Llamar a la función para abrir el archivo y cerrar la ventana
        else:
            result_label.configure(text="Usuario o contraseña incorrectos", text_color=("red", "#FF0000"))

FRAME0 = customtkinter.CTkFrame(ventana_ini, fg_color="transparent")
FRAME0.pack_propagate(False)
FRAME0.pack(pady=(5, 5), expand=1, fill="both", padx=(5, 0), side="left")
LABEL18 = customtkinter.CTkLabel(FRAME0, text="Panel\nAdmin !", justify="left", anchor="w", text_color=("gray10", "#FFFFFF"), font=("Arial", 82, "bold"),)
LABEL18.pack(padx=(30, 0), expand=1, fill="x")

FRAME2_copy = customtkinter.CTkFrame(ventana_ini)
FRAME2_copy.pack_propagate(False)
FRAME2_copy.pack(pady=(20, 20), expand=1, fill="both", padx=(5, 20), side="left")
FRAME2 = customtkinter.CTkFrame(FRAME2_copy, width=465, height=400, fg_color="transparent")
FRAME2.pack(expand=1, padx=50, pady=100)

# Título del formulario
LABEL3 = customtkinter.CTkLabel(FRAME2, text="Login", anchor="w", text_color=("gray10", "#FFFFFF"), font=("Arial", 40, "bold"),)
LABEL3.pack(fill="x")

# Campo de usuario
FRAME5 = customtkinter.CTkFrame(FRAME2, fg_color="transparent")
FRAME5.pack(pady=(0, 0), fill="x")
LABEL8_copy = customtkinter.CTkLabel(FRAME5, text="Usuario", anchor="w", text_color=("gray10", "#FFFFFF"), font=("Arial", 15, "bold"),)
LABEL8_copy.pack(fill="x")
ENTRY9 = customtkinter.CTkEntry(FRAME5, placeholder_text="example@gmail.com", height=35, corner_radius=3, text_color=("gray10", "#FFFFFF"), width=222)
ENTRY9.pack(fill="x")

# Campo de contraseña
FRAME11_copy = customtkinter.CTkFrame(FRAME2, fg_color="transparent")
FRAME11_copy.pack(pady=(10, 0), fill="x")
LABEL12_copy = customtkinter.CTkLabel(FRAME11_copy, text="Password", anchor="w", text_color=("gray10", "#FFFFFF"), font=("Arial", 15, "bold"))
LABEL12_copy.pack(fill="x")
ENTRY13_copy = customtkinter.CTkEntry(FRAME11_copy, placeholder_text="", height=35, corner_radius=3, text_color=("gray10", "#FFFFFF"), show="*")
ENTRY13_copy.pack(fill="x")

FRAME13 = customtkinter.CTkFrame(FRAME2, fg_color="transparent")
FRAME13.pack(pady=(20, 20), fill="x")
BUTTON16 = customtkinter.CTkButton(FRAME2, text="Login", height=35, text_color=("gray98", "#FFFFFF"), fg_color=("#8651ff", "#8651ff"), hover_color=("#6940c9", "#6940c9"), width=500, corner_radius=3, command=verify_login)
BUTTON16.place(relx=0.5, rely= 0.6, anchor="center")

result_label = customtkinter.CTkLabel(FRAME2, text="", text_color=("red", "#FFFFFF"), font=("Arial", 15, "bold"))
result_label.pack(pady=(10, 0))

#ventana inicial
f_ven_ini_tit = customtkinter.CTkFrame(ventana_ini, width=1000, height=50, fg_color="black")

l_tit = customtkinter.CTkLabel(f_ven_ini_tit, text="RopaUrbana", font=("Arial", 50, "bold"), width=1000, height=50, text_color="white")
l_tit.place(relx=0.5, rely=0.5, anchor="center")

f_buttons = customtkinter.CTkFrame(ventana_ini, width=980,  height=80, fg_color=("black"))

b_vender = customtkinter.CTkButton(f_buttons, text="Vender",font=("Arial", 40, "bold"), fg_color="gray", width=200, height=50, command=boton_vender,text_color="black")
b_vender.place(relx=0.12, rely=0.5, anchor="center")

b_inventario = customtkinter.CTkButton(f_buttons, text="Inventario",  font=("Arial", 35, "bold"),  width=200, height=50, command=boton_inventario, text_color="black",fg_color="gray")
b_inventario.place(relx=0.35, rely=0.5, anchor="center")

b_ventas = customtkinter.CTkButton(f_buttons, text="Ventas", font=("Arial", 40, "bold"),  command=boton_ventas  ,width=200, height=50, fg_color="gray", text_color="black")
b_ventas.place(relx=0.58, rely=0.5, anchor="center")

f_b_salir = customtkinter.CTkFrame(ventana_ini, width=300, corner_radius=10,  height=100, fg_color=("black"))

b_salir = customtkinter.CTkButton(f_b_salir, text="Salir", fg_color="gray",text_color="black",font=("Arial", 40, "bold"), width=200, command=boton_salir, height=50)
b_salir.place(relx=0.5, rely=0.5, anchor="center")


# Crear y configurar la ventana de venta
fr_marco_vender = customtkinter.CTkFrame(ventana_ini, width=500, height=250, fg_color="black", corner_radius=10)

lb_id_producto = customtkinter.CTkLabel(fr_marco_vender, text="ID Producto:", text_color="white", font=("Arial", 30, "bold")) 
lb_id_producto.place(relx=0.3, rely=0.1, anchor="center")

lb_cant_producto = customtkinter.CTkLabel(fr_marco_vender, text="Cantidad:", text_color="white", font=("Arial", 30, "bold"))
lb_cant_producto.place(relx=0.3, rely=0.3, anchor="center")

nombre_del_producto = tkinter.StringVar(value="Nombre")
lb_nombre_producto = customtkinter.CTkLabel(fr_marco_vender, textvariable= nombre_del_producto, text_color="white", font=("Arial", 25, "bold"))
lb_nombre_producto.place(relx=0.3, rely=0.5, anchor="center")

precio_producto = tkinter.StringVar(value="Precio: $0.0")
lb_precio = customtkinter.CTkLabel(fr_marco_vender, textvariable=precio_producto, text_color="white", font=("Arial", 30, "bold")) 
lb_precio.place(relx=0.3, rely=0.7, anchor="center")

total_compra = tkinter.StringVar(value="Total: $0.0")
lb_total = customtkinter.CTkLabel(fr_marco_vender, textvariable=total_compra, text_color="white", font=("Arial", 30, "bold"))
lb_total.place(relx=0.3, rely=0.9, anchor="center")

id_prod_entry = customtkinter.CTkEntry(fr_marco_vender, width=150, height=25, corner_radius=10, text_color="white", font=("Arial", 15, "bold"))
id_prod_entry.place(relx=0.75, rely=0.1, anchor="center")

can_prod_entry = customtkinter.CTkEntry(fr_marco_vender, width=150, height=25, corner_radius=10, text_color="white", font=("Arial", 15, "bold"))
can_prod_entry.place(relx=0.75, rely=0.3, anchor="center")

boton_enter_pro = customtkinter.CTkButton(fr_marco_vender,fg_color="gray", width=100, height=50, font=("Arial",40,"bold"),corner_radius=10, text="Enter", command=obtener_producto_info)
boton_enter_pro.place(relx=0.65, rely=0.55)

fr_compra_reali = customtkinter.CTkFrame(ventana_ini, width=500, height=150, fg_color="black", corner_radius=10)

compra_detalle = tkinter.StringVar(value="Detalles de tu compra")

lb_compra_realizada = customtkinter.CTkLabel(fr_compra_reali, textvariable= compra_detalle, font=("Arial",40,"bold"), text_color="white")
lb_compra_realizada.place(relx=0.5, rely= 0.5, anchor="center")

fr_carr_img = customtkinter.CTkFrame(ventana_ini, width= 150, height= 150, corner_radius=10 , fg_color="white")
image_path_carrito = os.path.join(os.path.dirname(__file__), "car.jpg")
image_carrito = customtkinter.CTkImage(light_image=Image.open(image_path_carrito), size=(100, 100))
l_image_car = customtkinter.CTkLabel(fr_carr_img, image=image_carrito, text="")
l_image_car.place(relx=0.5, rely=0.5, anchor="center")

fr_boton_comprar = customtkinter.CTkFrame(ventana_ini, width= 250, height= 250, corner_radius=10 , fg_color="gray")
bt_comprar = customtkinter.CTkButton(fr_boton_comprar, text="Comprar",font=("Arial",40, "bold"), width=185,command=comprar_pro,corner_radius=10)
bt_comprar.place(relx=0.5, rely=0.8, anchor="center")
bt_borrar_c = customtkinter.CTkButton(fr_boton_comprar, command= borrar_celda,text="Borrar",font=("Arial",40, "bold"),width=185 ,corner_radius=10, fg_color="red")
bt_borrar_c.place(relx=0.5, rely=0.2, anchor="center")
bt_volver_ini_vend = customtkinter.CTkButton(fr_boton_comprar, command= volver_ini, text="Volver",font=("Arial",40, "bold"),width=185 ,corner_radius=10)
bt_volver_ini_vend.place(relx=0.5, rely=0.5, anchor="center")

# Crear y configurar la ventana de inventario
fr_marco_inventario = customtkinter.CTkFrame(ventana_ini, width=550, height=300, corner_radius=10, fg_color="gray")

columnas_productos = ("ID", "Nombre", "Precio", "Stock")
productos_treeview = ttk.Treeview(fr_marco_inventario, columns=columnas_productos, show="headings")
productos_treeview.pack()
for col in columnas_productos:
    productos_treeview.heading(col, text=col)
    productos_treeview.column(col, width=150)
mostrar_productos()

fr_agre_volver = customtkinter.CTkFrame(ventana_ini, width=300, height=500, corner_radius=10, fg_color="gray")

l_nombre_pro_ingr = customtkinter.CTkLabel(fr_agre_volver, font=("Arial",30,"bold"), text_color="blue",text="Nombre:")
l_nombre_pro_ingr.place(relx=0.25, rely=0.05, anchor="center") 
nombre_entry = customtkinter.CTkEntry(fr_agre_volver, width=125, height=25, corner_radius=10)
nombre_entry.place(relx=0.75,rely=0.05,anchor="center" )

l_precio_pro_ingr = customtkinter.CTkLabel(fr_agre_volver, font=("Arial",30,"bold"), text_color="blue",text="Precio:")
l_precio_pro_ingr.place(relx=0.25, rely=0.15, anchor="center") 
precio_entry = customtkinter.CTkEntry(fr_agre_volver, width=125, height=25, corner_radius=10)
precio_entry.place(relx=0.75,rely=0.15,anchor="center" )

l_cant_pro_ingr = customtkinter.CTkLabel(fr_agre_volver, font=("Arial",30,"bold"), text_color="blue",text="Cantidad:")
l_cant_pro_ingr.place(relx=0.25, rely=0.25, anchor="center") 
cant_entry = customtkinter.CTkEntry(fr_agre_volver, width=125, height=25, corner_radius=10)
cant_entry.place(relx=0.75,rely=0.25,anchor="center" )

l_eliminar_inventario = customtkinter.CTkLabel(fr_agre_volver, text="Eliminar producto", font=("Arial",30,"bold"), text_color="red")
l_eliminar_inventario.place(relx=0.5, rely=0.35, anchor="center")

l_id_pro_inventario = customtkinter.CTkLabel(fr_agre_volver, font=("Arial",30,"bold"), text_color="blue",text="Id:")
l_id_pro_inventario.place(relx=0.25, rely=0.45, anchor="center") 
id_entry = customtkinter.CTkEntry(fr_agre_volver, width=125, height=25, corner_radius=10)
id_entry.place(relx=0.75,rely=0.45,anchor="center")

boton_agre = customtkinter.CTkButton(fr_agre_volver, width=130, fg_color="blue",height=50, font=("Arial",20,"bold"),corner_radius=10, text="Agregar", command=agregar_producto)
boton_agre.place(relx=0.52, rely=0.69)

boton_bor_agre = customtkinter.CTkButton(fr_agre_volver, fg_color="red",width=130, height=50, font=("Arial",20,"bold"),corner_radius=10, text="Borrar", command=enter_but_agregar_borr)
boton_bor_agre.place(relx=0.05, rely=0.69)

boton_provedores_ver = customtkinter.CTkButton(fr_agre_volver, width=100, height=50, font=("Arial",20,"bold"),corner_radius=10, text="Provedores", command=boton_provedores)
boton_provedores_ver.place(relx=0.05, rely=0.85)

boton_volver_agre_inv = customtkinter.CTkButton(fr_agre_volver, width=130, height=50, font=("Arial",25,"bold"),corner_radius=10, text="Volver", command= volver_ini_invertario)
boton_volver_agre_inv.place(relx=0.52, rely=0.85)

boton_eli_agre = customtkinter.CTkButton(fr_agre_volver, fg_color="red", width=130, height=50, font=("Arial",20,"bold"),corner_radius=10, text="Eliminar", command= eliminar_inve)
boton_eli_agre.place(relx=0.3, rely=0.55)

fr_mens_agre = customtkinter.CTkFrame(ventana_ini, width=550, height=150, corner_radius=10, fg_color="gray")

producto_agregado = tkinter.StringVar(value="Producto agregado")

l_prod_agre = customtkinter.CTkLabel(fr_mens_agre, font=("Arial",35,"bold"), textvariable= producto_agregado, text_color="MediumSpringGreen")
l_prod_agre.place(relx=0.5, rely=0.2, anchor="center")

cant_prod_agre = tkinter.StringVar(value="1")

l_cant_pro_agre = customtkinter.CTkLabel(fr_mens_agre, font=("Arial",30,"bold"), textvariable=cant_prod_agre)
l_cant_pro_agre.place(relx=0.5, rely=0.45, anchor="center")

nombre_pro_agre = tkinter.StringVar(value="Nombre")

l_nombre_pro_agre = customtkinter.CTkLabel(fr_mens_agre, font=("Arial",30,"bold"), text_color="white",textvariable=nombre_pro_agre)
l_nombre_pro_agre.place(relx=0.5, rely=0.65, anchor="center") 

precio_agre = tkinter.StringVar(value="$0.0")

l_precio_pro_agre = customtkinter.CTkLabel(fr_mens_agre, font=("Arial",30,"bold"), text_color="white",textvariable=precio_agre)
l_precio_pro_agre.place(relx=0.5, rely=0.85, anchor="center")

# Crear y configurar la ventana de provedores
fr_marco_provedores = customtkinter.CTkFrame(ventana_ini, width=550, height=300, corner_radius=10, fg_color="gray")

columnas_proveedores = ("ID", "Nombre", "Contacto")  
proveedores_treeview = ttk.Treeview(fr_marco_provedores, columns=columnas_proveedores, show="headings")
proveedores_treeview.pack()
for col in columnas_proveedores:
    proveedores_treeview.heading(col, text=col)
    proveedores_treeview.column(col, width=150)
mostrar_proveedores()

fr_agre_provedores = customtkinter.CTkFrame(ventana_ini, width=300, height=500, corner_radius=10, fg_color="gray")

l_nombre_pro_ingr = customtkinter.CTkLabel(fr_agre_provedores, font=("Arial",30,"bold"), text_color="blue",text="Nombre:")
l_nombre_pro_ingr.place(relx=0.25, rely=0.15, anchor="center") 
nombre_prove_entry = customtkinter.CTkEntry(fr_agre_provedores, width=125, height=25, corner_radius=10)
nombre_prove_entry.place(relx=0.75,rely=0.15,anchor="center" )

l_contacto = customtkinter.CTkLabel(fr_agre_provedores, font=("Arial",30,"bold"), text_color="blue",text="Contacto:")
l_contacto.place(relx=0.25, rely=0.05, anchor="center") 
con_entry = customtkinter.CTkEntry(fr_agre_provedores, width=125, height=25, corner_radius=10)
con_entry.place(relx=0.75,rely=0.05,anchor="center")

boton_eliminar_provedor = customtkinter.CTkButton(fr_agre_provedores, width=130, height=50, fg_color="red",font=("Arial",20,"bold"),corner_radius=10, text="Eliminar", command=boton_eliminar_prove)
boton_eliminar_provedor.place(relx=0.3, rely=0.55)

boton_agre_pro = customtkinter.CTkButton(fr_agre_provedores, width=130, height=50, font=("Arial",20,"bold"),fg_color="blue",corner_radius=10, text="Agregar", command=boton_agre_prove)
boton_agre_pro.place(relx=0.52, rely=0.69)

boton_bor_prov = customtkinter.CTkButton(fr_agre_provedores, width=130, height=50, fg_color="red", font=("Arial",20,"bold"),corner_radius=10, text="Borrar", command=boton_borrar_prove)
boton_bor_prov.place(relx=0.05, rely=0.69)

boton_volver_agre = customtkinter.CTkButton(fr_agre_provedores, width=130, height=50, font=("Arial",25,"bold"),corner_radius=10, text="Volver", command= volver_provedores)
boton_volver_agre.place(relx=0.52, rely=0.85)

l_eliminar_prove = customtkinter.CTkLabel(fr_agre_provedores, text="Eliminar provedor", font=("Arial",30,"bold"), text_color="red")
l_eliminar_prove.place(relx=0.5, rely=0.35, anchor="center")

l_id_pro_ingr = customtkinter.CTkLabel(fr_agre_provedores, font=("Arial",30,"bold"), text_color="blue",text="Id:")
l_id_pro_ingr.place(relx=0.25, rely=0.45, anchor="center") 
id_entry_pro = customtkinter.CTkEntry(fr_agre_provedores, width=125, height=25, corner_radius=10)
id_entry_pro.place(relx=0.75,rely=0.45,anchor="center")

provedor_agregado = tkinter.StringVar(value="Provedor")

fr_mens_provedores = customtkinter.CTkFrame(ventana_ini, width=550, height=150, corner_radius=10, fg_color="gray")
l_agre_prove = customtkinter.CTkLabel(fr_mens_provedores, font=("Arial",30,"bold"), text_color="MediumSpringGreen",textvariable= provedor_agregado)
l_agre_prove.place(relx=0.5, rely= 0.5, anchor="center")

# Crear y configurar la ventana de ventas
fr_marco_ventas = customtkinter.CTkFrame(ventana_ini, width=650, height=300, corner_radius=10, fg_color="gray")

columnas_ventas = ("ID Venta", "Producto", "Cantidad", "Total")
ventas_treeview = ttk.Treeview(fr_marco_ventas, columns=columnas_ventas, show="headings")
ventas_treeview.pack()
for col in columnas_ventas:
    ventas_treeview.heading(col, text=col)
    ventas_treeview.column(col, width=150)
mostrar_ventas()

fr_ventas_volver = customtkinter.CTkFrame(ventana_ini, width=200, height=500, corner_radius=10, fg_color="gray")

boton_volver_ventas = customtkinter.CTkButton(fr_ventas_volver, width=150, height=50, font=("Arial",33,"bold"),corner_radius=10, text="Volver", command= volver_ini_ventas)
boton_volver_ventas.place(relx=0.12, rely=0.85)

image_path_emb = os.path.join(os.path.dirname(__file__), "emb.png")
image_emb = customtkinter.CTkImage(light_image=Image.open(image_path_emb), size=(100, 100))
l_image_emb = customtkinter.CTkLabel(fr_ventas_volver, image=image_emb, text="")
l_image_emb.place(relx=0.5, rely=0.2, anchor="center")

boton_borrar_ventas = customtkinter.CTkButton(fr_ventas_volver,fg_color="red",width=150, height=50, font=("Arial",33,"bold"),corner_radius=10, text="Borrar", command= borrar_ventas)
boton_borrar_ventas.place(relx=0.12, rely=0.65)

ventana_ini.mainloop()