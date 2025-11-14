# Sistema Predictivo Basado en Lógica Difusa para la Prevención del Sobrecalentamiento (CIMCYT 2025)

![Licencia](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.x-green.svg)
![Estado](https://img.shields.io/badge/estado-Investigación-yellow.svg)

Un sistema inteligente que utiliza lógica difusa para **predecir** el riesgo de sobrecalentamiento en motores de combustión interna, basado en la investigación presentada en el **CIMCYT 2025**.

[Resumen](#🎯-resumen-del-proyecto) |
[Características](#✨-características-clave) |
[Tecnologías](#🛠️-tecnologías-utilizadas) |
[Instalación](#🚀-instalación) |
[Galería](#📸-galería-del-proyecto) |
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

## 🛠️ Tecnologías utilizadas

* **Lenguaje (Simulador):** Python
* **Librerías (Simulador):** `matplotlib`, `tkinter`
* **Hardware (Protototipo):** NodeMCU (ESP8266)
* **Sensores (Prototipo):** DS18B20 (Temperatura), Anemómetro
* **App Móvil (Prototipo):** MIT App Inventor
* **Modelo de Inferencia:** Lógica Difusa (Takagi-Sugeno)

📸 Galería del Proyecto
<p align="center"> <img src="assets/gui_simulador.png" alt="Interfaz gráfica del simulador en Python" width="600">


<em>Interfaz gráfica del simulador (Tkinter) para probar el sistema de inferencia.</em> </p> <p align="center"> <img src="assets/funciones_membresia.png" alt="Funciones de membresía para temperatura y flujo de aire" width="600">


<em>Funciones de membresía (Temperatura y Flujo de Aire) usadas en el modelo difuso.</em> </p> <p align="center"> <img src="assets/superficie_riesgo_3d.png" alt="Gráfica 3D de la superficie de nivel de riesgo" width="600">


<em>Superficie 3D del sistema Takagi-Sugeno que muestra el nivel de riesgo.</em> </p> <p align="center"> <img src="assets/app_movil.png" alt="App Móvil" width="300">


<em>Interfaz de la App Móvil (App Inventor) para recibir alertas.</em> </p>
