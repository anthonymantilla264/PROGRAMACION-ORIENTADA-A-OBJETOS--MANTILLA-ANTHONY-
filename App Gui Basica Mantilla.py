import tkinter as tk
from tkinter import ttk # Esto es para que los botones se vean bien en Mac

# 1. Crear la ventana
ventana = tk.Tk()
ventana.title("Sistema Gui Uea -Mantilla-")
ventana.geometry("350x500")
ventana.configure(bg="#222222") # Color oscuro de fondo

# --- FUNCIONES ---

def guardar_nombre():
    nombre = entrada.get() # Obtener el texto
    if nombre != "":
        lista.insert(tk.END, "-> " + nombre) # Agregarlo a la lista
        entrada.delete(0, tk.END) # Limpiar el cuadrito de escritura

def borrar_lista():
    lista.delete(0, tk.END) # Borrar todo lo de la lista

# --- INTERFAZ ---

# Título
titulo = tk.Label(ventana, text="MIS REGISTROS", bg="#222222", fg="white", font=("Arial", 14))
titulo.pack(pady=20)

# Cuadro para escribir
entrada = tk.Entry(ventana)
entrada.pack(pady=5)

# Botones
boton_guardar = ttk.Button(ventana, text="Guardar", command=guardar_nombre)
boton_guardar.pack(pady=10)

boton_limpiar = ttk.Button(ventana, text="Borrar Todo", command=borrar_lista)
boton_limpiar.pack(pady=5)

# La lista donde se ve todo
lista = tk.Listbox(ventana, bg="#333333", fg="white", font=("Arial", 12))
lista.pack(pady=20, padx=20, fill="both", expand=True)

# Iniciar
ventana.mainloop()