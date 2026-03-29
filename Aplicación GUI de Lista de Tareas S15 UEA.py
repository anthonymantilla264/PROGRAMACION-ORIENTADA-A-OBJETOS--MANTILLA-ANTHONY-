import tkinter as tk


def agregar(event=None):
    texto = entrada.get()
    # Si hay texto escrito, lo meto a la lista
    if texto != "":
        lista.insert(tk.END, texto)
        entrada.delete(0, tk.END)


def completar(event=None):
    seleccion = lista.curselection()
    # Solo hago algo si hay una tarea seleccionada
    if seleccion:
        indice = seleccion[0]
        tarea = lista.get(indice)

        # Le agrego la etiqueta de listo si no la tiene
        if not "(LISTO)" in tarea:
            lista.delete(indice)
            lista.insert(indice, tarea + " (LISTO)")


def borrar():
    seleccion = lista.curselection()
    if seleccion:
        lista.delete(seleccion[0])


# --- Ventana principal ---
ventana = tk.Tk()
ventana.title("Tareas UEA")
ventana.geometry("400x450")

# Caja de texto
entrada = tk.Entry(ventana, width=35, font=("Arial", 12))
entrada.pack(pady=10)
entrada.bind('<Return>', agregar)  # Para que funcione con la tecla Enter

# Marco para poner los botones en fila
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=5)

# Botones simples con colores básicos
btn1 = tk.Button(frame_botones, text="Agregar", command=agregar, bg="lightgreen")
btn1.grid(row=0, column=0, padx=5)

btn2 = tk.Button(frame_botones, text="Completada", command=completar, bg="lightblue")
btn2.grid(row=0, column=1, padx=5)

btn3 = tk.Button(frame_botones, text="Borrar", command=borrar, bg="#ff9999")
btn3.grid(row=0, column=2, padx=5)

# Lista de tareas
lista = tk.Listbox(ventana, width=40, height=15, font=("Arial", 12))
lista.pack(pady=10)
lista.bind('<Double-Button-1>', completar)  # Doble clic para completar

# Agregué unas tareas de prueba para ir avanzando
lista.insert(tk.END, "Registrar mi marca")
lista.insert(tk.END, "Pedir mercadería para la Distribuidora")

ventana.mainloop()