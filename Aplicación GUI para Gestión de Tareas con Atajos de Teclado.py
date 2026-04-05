import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas UEA 4.0")
        self.root.geometry("480x600")
        self.root.configure(bg="#ffffff")  # Fondo blanco puro para resaltar el negro

        # --- Colores ---
        self.col_btn_bg = "#000000"  # Negro
        self.col_btn_hover = "#333333"  # Gris oscuro para el efecto de vida
        self.col_btn_text = "#ffffff"  # Blanco

        # --- Título ---
        tk.Label(root, text="MIS TAREAS", font=("Impact", 24),
                 bg="#ffffff", fg="#000000").pack(pady=20)

        # --- Área de Entrada ---
        input_frame = tk.Frame(root, bg="#ffffff")
        input_frame.pack(pady=5, padx=30, fill=tk.X)

        self.task_entry = tk.Entry(input_frame, font=("Arial", 12), bd=1, relief="solid")
        self.task_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8, padx=(0, 10))
        self.task_entry.focus_set()

        # Botón Añadir Negro
        self.add_button = self.create_black_button(input_frame, text="AÑADIR", command=self.add_task)
        self.add_button.pack(side=tk.RIGHT)

        # --- Lista de Tareas ---
        list_frame = tk.Frame(root, bg="#ffffff", bd=2, relief="flat")
        list_frame.pack(pady=20, padx=30, fill=tk.BOTH, expand=True)

        self.tasks_listbox = tk.Listbox(list_frame, font=("Courier", 11), bd=1, relief="solid",
                                        selectbackground="#000000", selectforeground="#ffffff",
                                        highlightthickness=0, activestyle="none")
        self.tasks_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # --- Botones Inferiores ---
        controls_frame = tk.Frame(root, bg="#ffffff")
        controls_frame.pack(pady=20)

        self.complete_button = self.create_black_button(controls_frame, text="COMPLETAR (C)",
                                                        command=self.complete_task)
        self.complete_button.pack(side=tk.LEFT, padx=10)

        self.delete_button = self.create_black_button(controls_frame, text="ELIMINAR (DEL)",
                                                      command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=10)

        # --- Atajos ---
        self.task_entry.bind('<Return>', lambda e: self.add_task())
        self.root.bind('<c>', lambda e: self.complete_task())
        self.root.bind('<C>', lambda e: self.complete_task())
        self.root.bind('<Delete>', lambda e: self.delete_task())
        self.root.bind('<d>', lambda e: self.delete_task())
        self.root.bind('<Escape>', lambda e: self.root.destroy())

    def create_black_button(self, container, text, command):
        """Crea un botón negro con letras blancas y efecto hover."""
        btn = tk.Button(container, text=text, command=command,
                        bg=self.col_btn_bg, fg=self.col_btn_text,
                        font=("Arial", 9, "bold"),
                        relief="flat", padx=15, pady=8, cursor="hand2",
                        activebackground=self.col_btn_hover, activeforeground="white")

        # Efecto visual al pasar el mouse
        btn.bind("<Enter>", lambda e: btn.config(bg=self.col_btn_hover))
        btn.bind("<Leave>", lambda e: btn.config(bg=self.col_btn_bg))

        return btn

    def add_task(self):
        task = self.task_entry.get()
        if task.strip():
            self.tasks_listbox.insert(tk.END, f" > {task}")
            self.task_entry.delete(0, tk.END)

    def complete_task(self):
        try:
            index = self.tasks_listbox.curselection()[0]
            task = self.tasks_listbox.get(index)
            if "[OK]" not in task:
                self.tasks_listbox.delete(index)
                self.tasks_listbox.insert(index, f"{task} [OK]")
                self.tasks_listbox.itemconfig(index, fg="#aaaaaa")
        except:
            pass

    def delete_task(self):
        try:
            index = self.tasks_listbox.curselection()[0]
            self.tasks_listbox.delete(index)
        except:
            pass


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()