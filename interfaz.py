import tkinter as tk
from tkinter import messagebox
from juego import JuegoAdivina

class InterfazJuego:
    def __init__(self, master):
        self.master = master
        self.master.title("Adivina el Número")

        self.juego = JuegoAdivina()

        # Pantalla inicial
        self.label_bienvenida = tk.Label(master, text="¡Bienvenido al juego!")
        self.label_bienvenida.pack()

        self.label_nombre = tk.Label(master, text="Escribe tu nombre:")
        self.label_nombre.pack()

        self.entry_nombre = tk.Entry(master)
        self.entry_nombre.pack()

        self.boton_comenzar = tk.Button(master, text="Comenzar juego", command=self.iniciar_juego)
        self.boton_comenzar.pack()

        # Juego
        self.label_indicacion = tk.Label(master, text="", font=('Helvetica', 10, 'bold'))
        self.entry_intento = tk.Entry(master)
        self.boton_adivinar = tk.Button(master, text="Adivinar", command=self.verificar_intento)

    def iniciar_juego(self):
        nombre = self.entry_nombre.get()
        try:
            self.juego.iniciar(nombre)
        except ValueError:
            messagebox.showwarning("Nombre vacío", "Por favor, escribe tu nombre.")
            return

        self.label_bienvenida.pack_forget()
        self.label_nombre.pack_forget()
        self.entry_nombre.pack_forget()
        self.boton_comenzar.pack_forget()

        self.label_indicacion.config(text=f"{self.juego.nombre}, adivina un número entre 1 y 100:")
        self.label_indicacion.pack()
        self.entry_intento.pack()
        self.boton_adivinar.pack()

    def verificar_intento(self):
        try:
            intento = int(self.entry_intento.get())
            resultado = self.juego.verificar_intento(intento)
            if resultado == "Demasiado bajo":
                messagebox.showinfo("Pista", "Demasiado bajo. Intenta otra vez.")
            elif resultado == "Demasiado alto":
                messagebox.showinfo("Pista", "Demasiado alto. Intenta otra vez.")
            else:
                messagebox.showinfo("¡Ganaste!", f"¡Felicidades {self.juego.nombre}! Adivinaste el número en {self.juego.intentos} intentos.")
                self.master.destroy()
        except ValueError:
            messagebox.showerror("Entrada inválida", "Por favor, ingresa un número válido.")
