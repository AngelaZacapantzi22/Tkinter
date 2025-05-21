import tkinter as tk
from tkinter import messagebox
import math


historial_areas = []

def pantalla_inicio():
    limpiar_area_dinamica()
    
    tk.Label(area_dinamica, text="Lado del Cuadrado:", font=("Georgia", 12)).pack(pady=10)
    entrada_lado = tk.Entry(area_dinamica)
    entrada_lado.pack()

    def calcular_area_cuadrado():
        try:
            lado = float(entrada_lado.get())
            area = lado ** 2
            resultado = f"Cuadrado - Lado: {lado} → Área: {area:.2f}"
            historial_areas.append(resultado)
            messagebox.showinfo("Área del Cuadrado", resultado)
        except ValueError:
            messagebox.showerror("Error", "Ingresa un número válido.")

    tk.Button(area_dinamica, text="Calcular Área", command=calcular_area_cuadrado).pack(pady=10)

def pantalla_rectangulo():
    limpiar_area_dinamica()

    tk.Label(area_dinamica, text="Base del Rectángulo:", font=("Arial", 12)).pack(pady=5)
    base = tk.Entry(area_dinamica)
    base.pack()

    tk.Label(area_dinamica, text="Altura del Rectángulo:", font=("Arial", 12)).pack(pady=5)
    altura = tk.Entry(area_dinamica)
    altura.pack()

    def calcular_area_rectangulo():
        try:
            b = float(base.get())
            h = float(altura.get())
            area = b * h
            resultado = f"Rectángulo - Base: {b}, Altura: {h} → Área: {area:.2f}"
            historial_areas.append(resultado)
            messagebox.showinfo("Área del Rectángulo", resultado)
        except ValueError:
            messagebox.showerror("Error", "Ingresa valores válidos.")

    tk.Button(area_dinamica, text="Calcular Área", command=calcular_area_rectangulo).pack(pady=10)

def pantalla_triangulo():
    limpiar_area_dinamica()

    tk.Label(area_dinamica, text="Base del Triángulo:", font=("Arial", 12)).pack(pady=5)
    base = tk.Entry(area_dinamica)
    base.pack()

    tk.Label(area_dinamica, text="Altura del Triángulo:", font=("Arial", 12)).pack(pady=5)
    altura = tk.Entry(area_dinamica)
    altura.pack()

    def calcular_area_triangulo():
        try:
            b = float(base.get())
            h = float(altura.get())
            area = (b * h) / 2
            resultado = f"Triángulo - Base: {b}, Altura: {h} → Área: {area:.2f}"
            historial_areas.append(resultado)
            messagebox.showinfo("Área del Triángulo", resultado)
        except ValueError:
            messagebox.showerror("Error", "Ingresa valores válidos.")

    tk.Button(area_dinamica, text="Calcular Área", command=calcular_area_triangulo).pack(pady=10)

def pantalla_circulo():
    limpiar_area_dinamica()

    tk.Label(area_dinamica, text="Radio del Círculo:", font=("Arial", 12)).pack(pady=10)
    radio = tk.Entry(area_dinamica)
    radio.pack()

    def calcular_area_circulo():
        try:
            r = float(radio.get())
            area = math.pi * r ** 2
            resultado = f"Círculo - Radio: {r} → Área: {area:.2f}"
            historial_areas.append(resultado)
            messagebox.showinfo("Área del Círculo", resultado)
        except ValueError:
            messagebox.showerror("Error", "Ingresa un número válido.")

    tk.Button(area_dinamica, text="Calcular Área", command=calcular_area_circulo).pack(pady=10)

def ver_historial():
    limpiar_area_dinamica()
    if historial_areas:
        historial_texto = "\n".join(historial_areas)
        messagebox.showinfo("Historial de Áreas", historial_texto)
    else:
        messagebox.showinfo("Historial de Áreas", "No hay cálculos aún.")

def limpiar_area_dinamica():
    for widget in area_dinamica.winfo_children():
        widget.destroy()

ventana_principal = tk.Tk()
ventana_principal.title("Calculadora de Áreas")
ventana_principal.geometry("500x400")
ventana_principal.config(bg="lightblue")

menu_lateral = tk.Frame(ventana_principal, bg="lightblue", width=120)
menu_lateral.pack(side="left", fill="y")

area_dinamica = tk.Frame(ventana_principal, bg="white")
area_dinamica.pack(side="right", expand=True, fill="both")

tk.Button(menu_lateral, text="Cuadrado", command=pantalla_inicio, width=15).pack(pady=5)
tk.Button(menu_lateral, text="Rectángulo", command=pantalla_rectangulo, width=15).pack(pady=5)
tk.Button(menu_lateral, text="Triángulo", command=pantalla_triangulo, width=15).pack(pady=5)
tk.Button(menu_lateral, text="Círculo", command=pantalla_circulo, width=15).pack(pady=5)
tk.Button(menu_lateral, text="Ver Historial", command=ver_historial, width=15).pack(pady=20)
tk.Button(menu_lateral, text="Salir", command=ventana_principal.destroy, width=15).pack(pady=30)

pantalla_inicio()

ventana_principal.mainloop()



