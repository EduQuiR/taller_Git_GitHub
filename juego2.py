import tkinter as tk
from tkinter import messagebox
import random

class JuegoAdivina:
    def __init__(self, master):
        self.master = master
        master.title("Adivina el Número")

        self.nombre = ""
        self.intentos = 0
        self.numero_secreto = 0
        self.rango_min = 1
        self.rango_max = 100



        # Pantalla inicial
        self.label_bienvenida = tk.Label(master, text="¡Bienvenido al juego!")
        self.label_bienvenida.pack()

        self.label_nombre = tk.Label(master, text="Escribe tu nombre:")
        self.label_nombre.pack()

        #Le permito al usuario agregar el nivel
        #Aqui se supone que estaria la solucion no conseguida

        self.entry_nombre = tk.Entry(master)
        self.entry_nombre.pack()

        self.boton_comenzar = tk.Button(master, text="Comenzar juego", command=self.iniciar_juego)
        self.boton_comenzar.pack()

        # Juego
        self.label_indicacion = tk.Label(master, text="", font=('Helvetica', 10, 'bold'))
        self.entry_intento = tk.Entry(master)
        self.boton_adivinar = tk.Button(master, text="Adivinar", command=self.verificar_intento)

    def iniciar_juego(self):
        self.nombre = self.entry_nombre.get()
        if not self.nombre:
            messagebox.showwarning("Nombre vacío", "Por favor, escribe tu nombre.")
            return

        self.label_bienvenida.pack_forget()
        self.label_nombre.pack_forget()
        self.entry_nombre.pack_forget()
        self.boton_comenzar.pack_forget()

        self.label_indicacion.config(text=f"{self.nombre}, adivina un número entre 1 y 100:")
        self.label_indicacion.pack()
        self.entry_intento.pack()
        self.boton_adivinar.pack()

    def verificar_intento(self):
        try:
            intento = int(self.entry_intento.get())
            self.intentos += 1

            if intento < self.numero_secreto:
                messagebox.showinfo("Pista", "Demasiado bajo. Intenta otra vez.")
            elif intento > self.numero_secreto:
                messagebox.showinfo("Pista", "Demasiado alto. Intenta otra vez.")
            else:
                messagebox.showinfo("¡Ganaste!", f"¡Felicidades {self.nombre}! Adivinaste el número en {self.intentos} intentos.")
                self.master.destroy()
        except ValueError:
            messagebox.showerror("Entrada inválida", "Por favor, ingresa un número válido.")

#Realizar cambios

if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoAdivina(root)
    root.mainloop()
