import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Funciones de membresía trapezoidal y triangular
def trapecio(x, a, b, c, d):
    return max(0, min((x - a) / (b - a), 1, (d - x) / (d - c)))

def triangulo(x, a, b, c):
    return max(0, min((x - a) / (b - a), (c - x) / (c - b)))

# TEMPERATURA
def temperatura_fria(x): return trapecio(x, 70, 80, 85, 90)
def temperatura_media(x): return triangulo(x, 88, 93, 98)
def temperatura_caliente(x): return trapecio(x, 95, 98, 100, 105)

# FLUJO DE AIRE
def flujo_bajo(x): return trapecio(x, 0, 2, 4, 6)
def flujo_regular(x): return triangulo(x, 5, 10, 15)
def flujo_optimo(x): return trapecio(x, 14, 18, 22, 26)

# Inferencia Takagi-Sugeno con 9 reglas
def inferencia_ts_ampliada(t, f):
    tf = {
        'fria': temperatura_fria(t),
        'media': temperatura_media(t),
        'caliente': temperatura_caliente(t)
    }
    ff = {
        'bajo': flujo_bajo(f),
        'regular': flujo_regular(f),
        'optimo': flujo_optimo(f)
    }

    reglas = [
        (tf['fria'], ff['bajo'], 0.5),
        (tf['fria'], ff['regular'], 0.5),
        (tf['fria'], ff['optimo'], 0),
        (tf['media'], ff['bajo'], 1),
        (tf['media'], ff['regular'], 0.5),
        (tf['media'], ff['optimo'], 0),
        (tf['caliente'], ff['bajo'], 1),
        (tf['caliente'], ff['regular'], 1),
        (tf['caliente'], ff['optimo'], 0.5),
    ]

    numerador = sum(min(temp, flujo) * salida for temp, flujo, salida in reglas)
    denominador = sum(min(temp, flujo) for temp, flujo, _ in reglas)
    return numerador / denominador if denominador != 0 else 0

# Actualiza sliders y resultado
def actualizar_valores(val=None):
    t = temp_slider.get()
    f = flujo_slider.get()
    temp_valor.config(text=f"{t:.1f} °C")
    flujo_valor.config(text=f"{f:.1f}")
    riesgo = inferencia_ts_ampliada(t, f)
    resultado.config(text=f"🔎 Riesgo estimado: {riesgo:.2f}")

    # Semáforo de riesgo
    if riesgo < 0.5:
        color = "#ccffcc"
        nivel = "🟢 Bajo"
    elif riesgo < 0.8:
        color = "#fff0b3"
        nivel = "🟡 Moderado"
    else:
        color = "#ff9999"
        nivel = "🔴 Alto"
    indicador.config(bg=color, text=f"🔦 Nivel de riesgo: {nivel}")

# Gráfica de funciones de membresía
def graficar_membresias():
    fig, axs = plt.subplots(1, 2, figsize=(10, 4))

    # Temperatura
    t_vals = list(range(69, 110))
    axs[0].plot(t_vals, [temperatura_fria(t) for t in t_vals], label="Fría")
    axs[0].plot(t_vals, [temperatura_media(t) for t in t_vals], label="Media")
    axs[0].plot(t_vals, [temperatura_caliente(t) for t in t_vals], label="Caliente")
    axs[0].set_title("Temperatura")
    axs[0].legend()
    axs[0].grid(True)

    # Flujo de aire
    f_vals = list(range(00, 30))
    axs[1].plot(f_vals, [flujo_bajo(f) for f in f_vals], label="Bajo")
    axs[1].plot(f_vals, [flujo_regular(f) for f in f_vals], label="Regular")
    axs[1].plot(f_vals, [flujo_optimo(f) for f in f_vals], label="Óptimo")
    axs[1].set_title("Flujo de aire")
    axs[1].legend()
    axs[1].grid(True)

    return fig

# GUI principal
ventana = tk.Tk()
ventana.title("Evaluador de Riesgo Difuso")

# Slider temperatura
tk.Label(ventana, text="Temperatura (°C)").pack()
temp_frame = tk.Frame(ventana)
temp_frame.pack()
temp_slider = ttk.Scale(temp_frame, from_=0, to=110, orient='horizontal', command=actualizar_valores)
temp_slider.pack(side='left')
temp_valor = tk.Label(temp_frame, text="22.0 °C")
temp_valor.pack(side='left', padx=10)

# Slider flujo de aire
tk.Label(ventana, text="Flujo de aire").pack()
flujo_frame = tk.Frame(ventana)
flujo_frame.pack()
flujo_slider = ttk.Scale(flujo_frame, from_=0, to=30, orient='horizontal', command=actualizar_valores)
flujo_slider.pack(side='left')
flujo_valor = tk.Label(flujo_frame, text="40.0")
flujo_valor.pack(side='left', padx=10)

# Reglas difusas visuales
tk.Label(ventana, text="📜 Reglas difusas:").pack()
reglas_frame = tk.Frame(ventana)
reglas_frame.pack(pady=5)

reglas_textos = [
    ("Fría + Bajo → Riesgo MEDIO", "#ffe6cc"),
    ("Fría + Regular → Riesgo MEDIO", "#ffe6cc"),
    ("Fría + Óptimo → Riesgo BAJO", "#ccffcc"),
    ("Media + Bajo → Riesgo ALTO", "#ff9999"),
    ("Media + Regular → Riesgo MEDIO", "#fff0b3"),
    ("Media + Óptimo → Riesgo BAJO", "#ccffcc"),
    ("Caliente + Bajo → Riesgo ALTO", "#ff9999"),
    ("Caliente + Regular → Riesgo ALTO", "#ff9999"),
    ("Caliente + Óptimo → Riesgo MEDIO", "#ffe6cc")
]

for texto, color in reglas_textos:
    tk.Label(reglas_frame, text="🌡️ " + texto, bg=color, fg="black", relief="groove", width=60, anchor="w", padx=10).pack(pady=2)

# Resultado final y semáforo
resultado = tk.Label(ventana, text="🔎 Riesgo estimado:")
resultado.pack(pady=10)

indicador = tk.Label(ventana, text="🔦 Nivel de riesgo", bg="#ccffcc", width=30)
indicador.pack(pady=5)

# Mostrar gráficas
fig = graficar_membresias()
canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas.get_tk_widget().pack()

# Inicializa sliders
temp_slider.set(22.0)
flujo_slider.set(40.0)
actualizar_valores()

ventana.mainloop()