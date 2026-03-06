🚗🔥 Sistema Predictivo Basado en Lógica Difusa para la Prevención del Sobrecalentamiento
Presentado en el Congreso Internacional de Mantenimiento y Confiabilidad

---

## 🎯 Resumen del proyecto

Este proyecto desarrolla un sistema inteligente para la prevención del sobrecalentamiento en motores de combustión interna. A diferencia de los sistemas de monitoreo tradicionales, que son **reactivos** (alertan cuando el motor *ya* está sobrecalentado), esta solución es **predictiva**.

🔍 Utiliza sensores de temperatura (DS18B20) y flujo de aire (anemómetro), junto con un **sistema de inferencia difuso Takagi-Sugeno**, para anticipar condiciones de riesgo antes de que ocurran fallos críticos.

🧩 El núcleo del prototipo está implementado en un microcontrolador **NodeMCU (ESP8266)** y envía alertas a una **aplicación móvil** desarrollada en App Inventor.

📁 Este repositorio contiene el código fuente del simulador de escritorio en Python, así como la documentación de la investigación.

---

## ✨ Características clave

- 🧠 **Modelo Predictivo:** Utiliza lógica difusa (Takagi-Sugeno) para *predecir* el riesgo de sobrecalentamiento, no solo para reaccionar a él.  
- 🌡️ **Entradas Múltiples:** Procesa datos de dos variables críticas: temperatura del refrigerante y flujo de aire del ventilador.  
- 📱 **Ecosistema Completo:** El proyecto está diseñado en 3 componentes:  
  1. 🔧 **Hardware:** Prototipo con NodeMCU y sensores.  
  2. 📲 **App Móvil:** Aplicación en App Inventor para recibir alertas.  
  3. 💻 **Simulador:** Script en Python para probar el modelo.  
- 📊 **Simulador Interactivo:** GUI en Python (Tkinter) para visualizar funciones de membresía y probar el sistema de inferencia en tiempo real.

---

## 🛠️ Tecnologías utilizadas

| Componente        | Tecnología / Herramienta                      |
|-------------------|----------------------------------------------|
| 💻 Simulador      | Python + `matplotlib`, `tkinter`             |
| 🔧 Hardware       | NodeMCU (ESP8266)                             |
| 🌡️ Sensores       | DS18B20 (Temperatura), Anemómetro            |
| 📲 App Móvil      | MIT App Inventor                              |
| 🧠 Modelo Difuso   | Lógica Difusa (Takagi-Sugeno)                |

---

📸 Galería del Proyecto
Visualizaciones clave del sistema desarrollado

<p align="center">
  <img src="assets/gui_simulador.png" alt="Interfaz gráfica del simulador en Python" width="400"><br>
  <em>Interfaz gráfica del simulador (Tkinter) para probar el sistema de inferencia.</em>
</p>

<p align="center">
  <img src="assets/funciones_membresia.png" alt="Funciones de membresía para temperatura y flujo de aire" width="400"><br>
  <em>Funciones de membresía (Temperatura y Flujo de Aire) usadas en el modelo difuso.</em>
</p>

<p align="center">
  <img src="assets/superficie_riesgo_3d.png" alt="Gráfica 3D de la superficie de nivel de riesgo" width="400"><br>
  <em>Superficie 3D del sistema Takagi-Sugeno que muestra el nivel de riesgo.</em>
</p>

<p align="center">
  <img src="assets/app_movil.png" alt="App Móvil" width="400"><br>
  <em>Interfaz de la App Móvil (App Inventor) para recibir alertas.</em>
</p>

---

## 🧑‍🔬 Autores y agradecimientos

Este proyecto es el resultado de la investigación presentada en el Congreso Internacional de Mantenimiento y Confiabilidad (CIMCYT 2025).  
Agradecimientos a todos los colaboradores que hicieron posible esta propuesta.

---

## ⚖️ Licencia

Este proyecto está distribuido bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## 📄 Publicación Académica

Este proyecto fue presentado en el **Congreso Internacional de Mantenimiento y Confiabilidad (CIMCYT 2025)** y documentado en la revista *Tecnología Digital*.  
El documento completo también se encuentra disponible en la carpeta `docs` de este repositorio:

<p align="center">
  <a href="docs/articulo_sobrecalentamiento_fuzzy.pdf" target="_blank">
    <img src="https://upload.wikimedia.org/wikipedia/commons/8/87/PDF_file_icon.svg" alt="Artículo en PDF" width="120">
    <br><em>Sistema predictivo basado en lógica difusa para la prevención del sobrecalentamiento en motores de combustión interna</em>
  </a>
</p>

<p align="center">
  <a href="https://www.revistatecnologiadigital.com/pdf/15_03_013_sistema_predictivo_logica_difusa_prevencion_sobrecalentamiento_motores_combustion_interna.pdf" target="_blank">
    📎 <em>Acceso al artículo original en la revista Tecnología Digital</em>
  </a>
</p>
