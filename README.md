# 🛺 Urban Routes – Automatización de pruebas con Selenium

## 📌 Descripción del proyecto

Este proyecto forma parte del **Sprint 9 del Bootcamp de QA Engineer de TripleTen**. Consiste en desarrollar pruebas automatizadas para validar el flujo completo de solicitud de taxi en la aplicación web **Urban Routes**, utilizando el patrón **Page Object Model (POM)** y buenas prácticas de automatización.

El objetivo principal es simular el comportamiento de un usuario que realiza una solicitud de taxi, incluyendo selección de tarifa, ingreso de datos personales, configuración de preferencias y validación del proceso de asignación de conductor.

---
## ⚠️ Aviso de atribución

Este proyecto fue desarrollado como parte del programa educativo de **TripleTen**.  
El contenido, estructura y objetivos del ejercicio fueron proporcionados por TripleTen con fines formativos.  
**Todos los derechos sobre el diseño original de la plataforma y los escenarios de prueba pertenecen a TripleTen.**
---

## 🧪 Tecnologías y técnicas utilizadas

- **Lenguaje:** Python 3  
- **Framework de pruebas:** Pytest  
- **Automatización web:** Selenium WebDriver  
- **Patrón de diseño:** Page Object Model (POM)  
- **Gestión de entorno:** Entorno virtual `.venv`  
- **Intercepción de datos:** `retrieve_phone_code()` para capturar códigos de confirmación  
- **Validación de modales y elementos dinámicos:** uso de `WebDriverWait` y condiciones explícitas

---

## 📦 Requisitos previos

Antes de ejecutar las pruebas, asegúrate de tener instalado lo siguiente:

- Python 3.12+
- Google Chrome y ChromeDriver compatibles
- Entorno virtual (`.venv`) recomendado
- Dependencias listadas en `requirements.txt`

---

## ▶️ Pasos para ejecutar las pruebas

1. Clona el repositorio o descarga los archivos del proyecto.
2. Crea y activa un entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Linux/macOS
   .venv\Scripts\activate     # En Windows
    ```
3. Instala las dependencias:

   ```bash  
   pip install -r requirements.txt
    ```
4. Verifica que el entorno virtual esté activo y que las dependencias estén disponibles:

    * Asegúrate de ver el prefijo (venv) en la terminal:
    ```bash
   (venv) usuario@equipo:~/a-project-Urban-Routes-es$
    ```
    *  Ejecuta:
    ```bash
    pip list
    ```
   Debes ver selenium y pytest en la lista de paquetes instalados.
    * Si usas PyCharm u otro IDE, asegúrate de que el intérprete seleccionado sea el entorno virtual ubicado en:
    ```bash
   /home/usuario/a-project-Urban-Routes-es/venv/bin/python
    ```
   Si el entorno ya existe, selecciónalo en lugar de crear uno nuevo.
5. Ejecuta las pruebas con Pytest:
    ```bash
   pytest main.py
6. Revisa los resultados en la terminal para verificar qué casos pasaron y cuáles fallaron.

---

## 🧭 Flujo de pruebas automatizadas

Las pruebas cubren el siguiente flujo completo:

1. Configurar dirección de origen
2. Seleccionar tarifa Comfort
3. Ingresar número de teléfono
4. Agregar tarjeta de crédito (simulación de enfoque perdido en campo CVV)
5. Interceptar código de confirmación con `retrieve_phone_code()`
6. Escribir mensaje para el conductor
7. Solicitar manta y pañuelos
8. Pedir 2 helados
9. Validar aparición del modal de búsqueda de taxi
10. (Opcional) Esperar aparición de información del conductor

---
## ✍️ Autor

**Erick Jiménez del Río**  
QA Engineer en transición a SDET   
📍 CDMX, México  
🔗 [GitHub](https://github.com/erjimrio)  
🔗 [LinkedIn](https://www.linkedin.com/in/erjimrio)