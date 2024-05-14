import tkinter as tk
from tkinter import messagebox
from zeep import Client

# Función para llamar al servicio web y realizar la operación seleccionada
def realizar_operacion(operacion):
    try:
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())

        # Crear un cliente para el servicio web
        client = Client(url)

        # Realizar la operación seleccionada
        if operacion == "suma":
            resultado = client.service.suma(num1, num2)
        elif operacion == "resta":
            resultado = client.service.restar(num1, num2)
        elif operacion == "multiplicacion":
            resultado = client.service.multiplicar(num1, num2)
        elif operacion == "dividir":
            resultado = client.service.dividir(num1, num2)

        # Mostrar el resultado en la etiqueta de resultado
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números válidos.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

# Crear la ventana principal
window = tk.Tk()
window.title("Calculadora")

# URL del servicio web
url = 'http://localhost:8080/Operacion/wsoperaciones?wsdl'

# Etiquetas y entradas para los números
label_num1 = tk.Label(window, text="Número 1:")
label_num1.grid(row=0, column=0)
entry_num1 = tk.Entry(window, width=15)  # Anchura para la entrada
entry_num1.grid(row=0, column=1)

label_num2 = tk.Label(window, text="Número 2:")
label_num2.grid(row=1, column=0)
entry_num2 = tk.Entry(window, width=15)  # Anchura para la entrada
entry_num2.grid(row=1, column=1)

# Botones para realizar las operaciones
button_suma = tk.Button(window, text="Sumar", command=lambda: realizar_operacion("suma"))
button_suma.grid(row=2, column=0)

button_resta = tk.Button(window, text="Restar", command=lambda: realizar_operacion("resta"))
button_resta.grid(row=2, column=1)

button_multiplicacion = tk.Button(window, text="Multiplicar", command=lambda: realizar_operacion("multiplicacion"))
button_multiplicacion.grid(row=2, column=2)

button_multiplicacion = tk.Button(window, text="Dividir", command=lambda: realizar_operacion("dividir"))
button_multiplicacion.grid(row=3, column=0)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(window, text="Resultado:", font=("Arial", 12))
label_resultado.grid(row=3, column=0, columnspan=3)

# Establece un espaciado entre filas para una mejor visualización
for i in range(4):
    window.grid_rowconfigure(i, pad=10)

# Ejecutar la ventana
window.mainloop()
