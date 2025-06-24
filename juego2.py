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
        self.historial_intentos = []

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
        self.label_historial_intentos = tk.Label(master, text="", font=('Helvetica', 10, 'bold'))

    def iniciar_juego(self):
        self.nombre = self.entry_nombre.get()
        if not self.nombre:
            messagebox.showwarning("Nombre vacío", "Por favor, escribe tu nombre.")
            return

        self.label_bienvenida.pack_forget()
        self.label_nombre.pack_forget()
        self.entry_nombre.pack_forget()
        self.boton_comenzar.pack_forget()

        self.label_indicacion.config(text=f"{self.nombre}, adivina un número entre 1 y 100: tienes {self.intentos} intentos")
        self.label_indicacion.pack()
        self.entry_intento.pack()
        self.boton_adivinar.pack()
        self.label_historial_intentos.pack()


    def verificar_intento(self):
        try:
            intento = int(self.entry_intento.get())
            self.historial_intentos.append(intento)
            historial_texto = ", ".join(str(n) for n in self.historial_intentos)
            self.label_historial_intentos.config(text=f"Intentos anteriores: {historial_texto}")
            self.intentos += 1
            self.label_indicacion.config(text=f"{self.nombre}, adivina un número entre 1 y 100: tienes {self.intentos} intentos")

            if intento < self.numero_secreto:
                messagebox.showinfo("Pista", "Demasiado bajo. Intenta otra vez.")
            elif intento > self.numero_secreto:
                messagebox.showinfo("Pista", "Demasiado alto. Intenta otra vez.")
            else:
                messagebox.showinfo("¡Ganaste!", f"¡Felicidades {self.nombre}! Adivinaste el número en {self.intentos} intentos.")
                self.master.destroy()
            with open("resultados.txt", "a", encoding="utf-8") as archivo:
                archivo.write(f"El nombre del jugador es {self.nombre}\n")
                archivo.write(f"La cantidad de intentos fue de {self.intentos}\n")
                archivo.write(f"Los intentos fueron {self.historial_intentos}\n")
                archivo.write(f"El jugador gano!")
        except ValueError:
            messagebox.showerror("Entrada inválida", "Por favor, ingresa un número válido.")

#Realizar cambios

if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoAdivina(root)
    root.mainloop()
