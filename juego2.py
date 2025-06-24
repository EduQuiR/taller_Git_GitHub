import tkinter as tk
from tkinter import messagebox
import random

class JuegoAdivina:
    def __init__(self, master):
        self.master = master
        master.title("Adivina el Número")

        self.nombre = ""
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0

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
        self.boton_reiniciar = tk.Button(master, text="Reiniciar juego", command=self.reiniciar_juego)

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
        self.boton_reiniciar.pack()

    def verificar_intento(self):
        try:
            intento = int(self.entry_intento.get())
            self.intentos += 1

            if intento < self.numero_secreto:
                messagebox.showinfo("Pista", "Demasiado bajo. Intenta otra vez.")
                self.entry_intento.delete(0, tk.END)
            elif intento > self.numero_secreto:
                messagebox.showinfo("Pista", "Demasiado alto. Intenta otra vez.")
                self.entry_intento.delete(0, tk.END)
            else:
                messagebox.showinfo("¡Ganaste!", f"¡Felicidades {self.nombre}! Adivinaste el número en {self.intentos} intentos.")
                self.entry_intento.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Entrada inválida", "Por favor, ingresa un número válido.")

    def reiniciar_juego(self):
        # Restablecer variables del juego
        self.nombre = ""
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0
        
        # Ocultar elementos del juego
        self.label_indicacion.pack_forget()
        self.entry_intento.pack_forget()
        self.boton_adivinar.pack_forget()
        self.boton_reiniciar.pack_forget()
        
        # Limpiar campos de entrada
        self.entry_nombre.delete(0, tk.END)
        self.entry_intento.delete(0, tk.END)
        
        # Mostrar pantalla inicial
        self.label_bienvenida.pack()
        self.label_nombre.pack()
        self.entry_nombre.pack()
        self.boton_comenzar.pack()

#Realizar cambios

if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoAdivina(root)
    root.mainloop()
