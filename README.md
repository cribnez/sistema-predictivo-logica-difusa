# Sistema Predictivo Basado en Lógica Difusa para la Prevención del Sobrecalentamiento (CIMCYT 2025)

![Licencia](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.x-green.svg)
![Estado](https://img.shields.io/badge/estado-Investigación-yellow.svg)

Un sistema inteligente que utiliza lógica difusa para **predecir** el riesgo de sobrecalentamiento en motores de combustión interna, basado en la investigación presentada en el **CIMCYT 2025**.

[Resumen](#🎯-resumen-del-proyecto) |
[Características](#✨-características-clave) |
[Tecnologías](#🛠️-tecnologías-utilizadas) |
[Instalación](#🚀-instalación) |
[Uso](#▶️-uso-del-simulador) |
[Autores](#🧑‍🔬-autores)

---

## 🎯 Resumen del proyecto

Este proyecto desarrolla un sistema inteligente para la prevención del sobrecalentamiento en motores de combustión interna. A diferencia de los sistemas de monitoreo tradicionales, que son **reactivos** (alertan cuando el motor *ya* está sobrecalentado), esta solución es **predictiva**.

Utilizando sensores de temperatura (DS18B20) y flujo de aire (anemómetro), junto con un **sistema de inferencia difuso Takagi-Sugeno**, el sistema predice condiciones de riesgo antes de que ocurran fallos críticos. El núcleo del prototipo está implementado en un microcontrolador **NodeMCU (ESP8266)** y envía alertas a una **aplicación móvil** desarrollada en App Inventor.

Este repositorio contiene el código fuente del simulador de escritorio en Python, así como la documentación de la investigación.

## ✨ Características clave

* 🧠 **Modelo Predictivo:** Utiliza lógica difusa (Takagi-Sugeno) para *predecir* el riesgo de sobrecalentamiento, no solo para reaccionar a él.
* 🌡️ **Entradas Múltiples:** Procesa datos de dos variables críticas: temperatura del refrigerante y flujo de aire del ventilador.
* 📱 **Ecosistema Completo:** El proyecto está diseñado en 3 componentes:
    1.  **Hardware:** Un prototipo con NodeMCU y sensores.
    2.  **App Móvil:** Una app en App Inventor para recibir alertas.
    3.  **Simulador:** El script de Python en este repositorio para probar el modelo.
* 📊 **Simulador Interactivo:** Incluye una GUI de Python (Tkinter) para visualizar las funciones de membresía y probar el sistema de inferencia en tiempo real.

## 📸 Vistas Previas

*(Aquí puedes añadir capturas de pantalla de tu simulador, la app móvil y el hardware)*

| Simulador de Python | App Móvil |
| :---: | :---: |
| [Simulador de Python](docs/images/fig_gui_python.png) | [App Móvil](docs/images/fig_app_movil.png) |

## 🛠️ Tecnologías utilizadas

* **Lenguaje (Simulador):** Python
* **Librerías (Simulador):** `matplotlib`, `tkinter`
* **Hardware (Prototipo):** NodeMCU (ESP8266)
* **Sensores (Prototipo):** DS18B20 (Temperatura), Anemómetro
* **App Móvil (Prototipo):** MIT App Inventor
* **Modelo de Inferencia:** Lógica Difusa (Takagi-Sugeno)

## 📂 Estructura del repositorio

```
.
├── 📄 LICENSE
├── 📄 README.md
├── 📄 requirements.txt
├── 📄 .gitignore
│
├── 📂 docs/
│   └── 📑 CIMCYT2025_Ibanez_SistemaPredictivo.docx
│
└── 📂 src/
    ├── 🐍 python_simulator/
    ├── 📟 firmware_nodemcu/
    └── 📱 mobile_app/
```

## 🚀 Instalación (Simulador de Python)

1.  Clona este repositorio:
    ```bash
    git clone [https://github.com/tu_usuario/tu_repositorio.git](https://github.com/tu_usuario/tu_repositorio.git)
    cd tu_repositorio
    ```

2.  (Recomendado) Crea y activa un entorno virtual:
    ```bash
    # En macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # En Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## ▶️ Uso del simulador

Una vez instaladas las dependencias, puedes ejecutar el simulador desde la raíz del proyecto:

```bash
python src/python_simulator/algoritmo.py
```

Esto abrirá una ventana de Tkinter donde puedes:
* Ajustar los deslizadores de **Temperatura** y **Flujo de Aire**.
* Ver el gráfico de las funciones de membresía.
* Observar el **Nivel de Riesgo** calculado en tiempo real por el sistema difuso.

## 🧑‍🔬 Autores y agradecimientos

Este proyecto es el resultado de la investigación presentada en el **Congreso Internacional de Mantenimiento y Confiabilidad (CIMCYT 2025)**.

**Autores del Artículo**:
* Juan Ríos Hernández
* Christian Roberto Ibáñez Nangüelú
* Roberto Ibáñez Córdova
* Manuel Ramos Ponce
* Fredy Martínez Cortez

## ⚖️ Licencia

Este proyecto está distribuido bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.
