import tkinter as tk
from tkinter import messagebox
import random

class JuegoAdivina:
    def __init__(self, master):
        self.master = master
        master.title("Adivina el Número")

        self.nombre = ""
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0            else:
                messagebox.showinfo("¡Ganaste!", f"¡Felicidades {self.nombre}! Adivinaste el número en {self.intentos} intentos.")
                self.master.destroy()
        # *** CAMBIO 1: Modificar inicialización de variables ***
        # ANTES: self.numero_secreto = random.randint(1, 100)
        # AHORA:
        self.numero_secreto = 0  # Se generará después de elegir dificultad
        self.intentos = 0
        self.rango_min = 1       # NUEVO: rango mínimo
        self.rango_max = 100     # NUEVO: rango máximo
        # Pantalla inicial
        self.label_bienvenida = tk.Label(master, text="¡Bienvenido al juego!")
        self.label_bienvenida.pack()

        self.label_nombre = tk.Label(master, text="Escribe tu nombre:")
        self.label_nombre.pack()

        self.entry_nombre = tk.Entry(master)
        self.entry_nombre.pack()

        # *** CAMBIO 2: Modificar botón y su comando ***
        # ANTES: self.boton_comenzar = tk.Button(master, text="Comenzar juego", command=self.iniciar_juego)
        # AHORA:
        self.boton_continuar = tk.Button(master, text="Continuar", command=self.mostrar_dificultad)
        self.boton_continuar.pack()

        # *** CAMBIO 3: NUEVOS elementos para pantalla de dificultad ***
        self.label_dificultad = tk.Label(master, text="Elige la dificultad:", font=('Helvetica', 12, 'bold'))
        self.boton_facil = tk.Button(master, text="Fácil (1-50)", command=lambda: self.seleccionar_dificultad(1, 50))
        self.boton_medio = tk.Button(master, text="Medio (1-100)", command=lambda: self.seleccionar_dificultad(1, 100))
        self.boton_dificil = tk.Button(master, text="Difícil (1-200)", command=lambda: self.seleccionar_dificultad(1, 200))

        # Juego
        self.label_indicacion = tk.Label(master, text="", font=('Helvetica', 10, 'bold'))
        self.label_contador = tk.Label(master, text="", font=('Helvetica', 10, 'bold'))
        self.entry_intento = tk.Entry(master)
        self.boton_adivinar = tk.Button(master, text="Adivinar", command=self.verificar_intento)

    # *** CAMBIO 4: NUEVA función mostrar_dificultad (reemplaza la lógica original de iniciar_juego) ***
    def mostrar_dificultad(self):
        self.nombre = self.entry_nombre.get()
        if not self.nombre:
            messagebox.showwarning("Nombre vacío", "Por favor, escribe tu nombre.")
            return

        # Ocultar pantalla inicial
        self.label_bienvenida.pack_forget()
        self.label_nombre.pack_forget()
        self.entry_nombre.pack_forget()
        self.boton_continuar.pack_forget()

        # Mostrar pantalla de dificultad
        self.label_dificultad.pack(pady=10)
        self.boton_facil.pack(pady=5)
        self.boton_medio.pack(pady=5)
        self.boton_dificil.pack(pady=5)

    # *** CAMBIO 5: NUEVA función seleccionar_dificultad ***
    def seleccionar_dificultad(self, min_val, max_val):
        self.rango_min = min_val
        self.rango_max = max_val
        self.numero_secreto = random.randint(min_val, max_val)  # Generar número según dificultad
        
        # Ocultar pantalla de dificultad
        self.label_dificultad.pack_forget()
        self.boton_facil.pack_forget()
        self.boton_medio.pack_forget()
        self.boton_dificil.pack_forget()
        self.label_indicacion.config(text=f"{self.nombre}, adivina un número entre 1 y 100:")
        self.label_contador.config(text=f"intentos: {self.intentos}")
        # Mostrar juego
        self.iniciar_juego()

    # *** CAMBIO 6: Simplificar iniciar_juego (ya no maneja nombre ni oculta elementos) ***
    def iniciar_juego(self):
        # ANTES: Toda la lógica de validar nombre y ocultar elementos
        # AHORA: Solo mostrar el juego
        self.label_indicacion.config(text=f"{self.nombre}, adivina un número entre {self.rango_min} y {self.rango_max}:")
        self.label_indicacion.pack()
        self.label_contador.pack()
        self.entry_intento.pack()
        self.boton_adivinar.pack()

    def verificar_intento(self):
        
        try:
            intento = int(self.entry_intento.get())
            self.intentos += 1
            self.label_contador.config(text=f"intentos: {self.intentos}")
            self.label_contador.pack()

            # *** CAMBIO 7: NUEVA validación de rango ***
            if intento < self.rango_min or intento > self.rango_max:
                messagebox.showwarning("Fuera de rango", f"Por favor, ingresa un número entre {self.rango_min} y {self.rango_max}.")
                return

            if self.intentos == 10:
                messagebox.showinfo("Pista", "Perdiste. Numero de intentos maximo alcanzado")
                self.master.destroy()
            elif intento < self.numero_secreto:
                messagebox.showinfo("Pista", "Demasiado bajo. Intenta otra vez.")
            elif intento > self.numero_secreto:
                messagebox.showinfo("Pista", "Demasiado alto. Intenta otra vez.")
            else:
                messagebox.showinfo("¡Ganaste!", f"¡Felicidades {self.nombre}! Adivinaste el número en {self.intentos} intentos.")
                self.master.destroy()
            
            # *** CAMBIO 8: NUEVO - Limpiar campo después de cada intento ***
            self.entry_intento.delete(0, tk.END)
            
        except ValueError:
            messagebox.showerror("Entrada inválida", "Por favor, ingresa un número válido.")

if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoAdivina(root)
    root.mainloop()