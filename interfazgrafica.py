import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

estudiantes = {}

def pantalla_inicio():
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="Bienvenido a la aplicacion", font=("Georgia", 14)).pack(pady=10)
    tk.Button(area_dinamica, text="Mostrar mensaje de bienvenida", command=lambda: messagebox.showinfo("Bienvenida", "Holaaaa!")).pack()

def pantalla_datos_alumno():
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="Ingresa los datos del alumno:", font=("Times New Roman", 14)).pack(pady=10)

    tk.Label(area_dinamica, text="Nombre del alumno:").pack()
    campo_nombre = tk.Entry(area_dinamica)
    campo_nombre.pack(pady=5)

    tk.Label(area_dinamica, text="Calificacion:").pack()
    campo_calificacion = tk.Entry(area_dinamica)
    campo_calificacion.pack(pady=5)

    tk.Label(area_dinamica, text="Sexo (M/F):").pack()
    campo_sexo = tk.Entry(area_dinamica)
    campo_sexo.pack(pady=5)

    def guardar_datos():
        nombre = campo_nombre.get()
        try:
            calificacion = float(campo_calificacion.get())
        except ValueError:
            messagebox.showerror("Error", "La calificacion debe ser un numero.")
            return
        sexo = campo_sexo.get().upper()

        if nombre and sexo in ["M", "F"]:
            estudiantes[nombre] = {
                "calificacion": round(calificacion, 2),
                "sexo": sexo
            }
            messagebox.showinfo("Guardado", f"Alumno {nombre} guardado correctamente.")
            campo_nombre.delete(0, tk.END)
            campo_calificacion.delete(0, tk.END)
            campo_sexo.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Datos invalidos. Revisa los campos.")

    def mostrar_estudiantes():
        if not estudiantes:
            messagebox.showinfo("Estudiantes", "No hay estudiantes ingresados.")
            return
        texto = "Lista de estudiantes:\n"
        for nombre, datos in estudiantes.items():
            texto += f"{nombre} - Calificacion: {datos['calificacion']}, Sexo: {datos['sexo']}\n"
        messagebox.showinfo("Estudiantes", texto)

    tk.Button(area_dinamica, text="Guardar datos del alumno", command=guardar_datos).pack(pady=5)
    tk.Button(area_dinamica, text="Ver estudiantes", command=mostrar_estudiantes).pack(pady=5)

def pantalla_configuracion():
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="Configuraciones de fondo", font=("Comic Sans MS", 14)).pack(pady=10)

    colores = ["lightblue", "lightgreen", "lightyellow", "lightgray"]
    tk.Label(area_dinamica, text="Cambiar color de fondo:").pack()

    def cambiar_color(color):
        ventana_principal.config(bg=color)
        menu_lateral.config(bg=color)
        area_dinamica.config(bg=color)

    for c in colores:
        tk.Button(area_dinamica, text=c, bg=c, width=20, command=lambda col=c: cambiar_color(col)).pack(pady=2)

def pantalla_guia_ayuda():
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="Guia para responder", font=("Arial", 14)).pack(pady=10)
    contenido = (
        "Responde con tus palabras:\n\n"
        "- Que hace cada boton?\n"
        "- Que cambias si modificas un texto?\n"
        "- Como cambias un color?\n"
        "- Que debes renombrar?"
    )
    tk.Label(area_dinamica, text=contenido, justify="left").pack(pady=10)

def limpiar_area_dinamica():
    for widget in area_dinamica.winfo_children():
        widget.destroy()

ventana_principal = tk.Tk()
ventana_principal.title("Interfaz de practica")
ventana_principal.geometry("500x400")
ventana_principal.config(bg="lightblue")

menu_lateral = tk.Frame(ventana_principal, bg="lightblue", width=120)
menu_lateral.pack(side="left", fill="y")

area_dinamica = tk.Frame(ventana_principal, bg="white")
area_dinamica.pack(side="right", expand=True, fill="both")

tk.Button(menu_lateral, text="Inicio", command=pantalla_inicio, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Datos del alumno", command=pantalla_datos_alumno, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Configuracion", command=pantalla_configuracion, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Guia de ayuda", command=pantalla_guia_ayuda, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Salir", command=ventana_principal.destroy, width=15).pack(pady=30)

pantalla_inicio()
ventana_principal.mainloop()
