import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Requiere: pip install tkcalendar


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mi Agenda Personal Uea")
        self.root.geometry("600x450")

        # --- Contenedores (Frames) ---
        self.frame_entrada = tk.LabelFrame(self.root, text="Nuevo Evento", padx=10, pady=10)
        self.frame_entrada.pack(padx=10, pady=10, fill="x")

        self.frame_lista = tk.Frame(self.root, padx=10, pady=10)
        self.frame_lista.pack(padx=10, pady=5, fill="both", expand=True)

        self.frame_acciones = tk.Frame(self.root, padx=10, pady=10)
        self.frame_acciones.pack(fill="x")

        self.crear_widgets_entrada()
        self.crear_treeview()
        self.crear_botones_accion()

    def crear_widgets_entrada(self):
        # Fecha con DatePicker
        tk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0, sticky="w")
        self.ent_fecha = DateEntry(self.frame_entrada, width=12, background='darkblue',
                                   foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
        self.ent_fecha.grid(row=0, column=1, padx=5, pady=5)

        # Hora
        tk.Label(self.frame_entrada, text="Hora (HH:MM):").grid(row=0, column=2, sticky="w")
        self.ent_hora = tk.Entry(self.frame_entrada, width=10)
        self.ent_hora.grid(row=0, column=3, padx=5, pady=5)

        # Descripción
        tk.Label(self.frame_entrada, text="Descripción:").grid(row=1, column=0, sticky="w")
        self.ent_desc = tk.Entry(self.frame_entrada, width=50)
        self.ent_desc.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

    def crear_treeview(self):
        # Configuración de la tabla (TreeView)
        columnas = ("fecha", "hora", "descripcion")
        self.tree = ttk.Treeview(self.frame_lista, columns=columnas, show="headings")

        # Encabezados
        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("hora", text="Hora")
        self.tree.heading("descripcion", text="Descripción")

        # Ajuste de columnas
        self.tree.column("fecha", width=100, anchor="center")
        self.tree.column("hora", width=80, anchor="center")
        self.tree.column("descripcion", width=300)

        self.tree.pack(side="left", fill="both", expand=True)

        # Scrollbar para la lista
        scrollbar = ttk.Scrollbar(self.frame_lista, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

    def crear_botones_accion(self):
        btn_agregar = tk.Button(self.frame_acciones, text="Agregar Evento",
                                bg="#4CAF50", fg="white", command=self.agregar_evento)
        btn_agregar.pack(side="left", padx=5)

        btn_eliminar = tk.Button(self.frame_acciones, text="Eliminar Seleccionado",
                                 bg="#f44336", fg="white", command=self.eliminar_evento)
        btn_eliminar.pack(side="left", padx=5)

        btn_salir = tk.Button(self.frame_acciones, text="Salir", command=self.root.quit)
        btn_salir.pack(side="right", padx=5)

    # --- Lógica de Manejo de Eventos ---

    def agregar_evento(self):
        fecha = self.ent_fecha.get()
        hora = self.ent_hora.get()
        desc = self.ent_desc.get()

        if hora and desc:
            self.tree.insert("", "end", values=(fecha, hora, desc))
            # Limpiar campos tras agregar
            self.ent_hora.delete(0, tk.END)
            self.ent_desc.delete(0, tk.END)
        else:
            messagebox.showwarning("Campos vacíos", "Por favor, completa la hora y la descripción.")

    def eliminar_evento(self):
        seleccion = self.tree.selection()
        if seleccion:
            # Diálogo de confirmación (Requisito opcional)
            confirmar = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas eliminar este evento?")
            if confirmar:
                for item in seleccion:
                    self.tree.delete(item)
        else:
            messagebox.showwarning("Atención", "Selecciona un evento de la lista para eliminarlo.")


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()