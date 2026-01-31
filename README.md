# 🛡️ Simulador de Incidentes de Seguridad

Proyecto desarrollado en **Python** cuyo objetivo es simular incidentes de seguridad informática para **entrenar la toma de decisiones y la respuesta ante incidentes**.

El sistema presenta distintos tipos de incidentes, permite seleccionar acciones, evalúa las decisiones tomadas y genera un **registro completo (logs y resumen final)** de la simulación.

---

## 🎯 Objetivo del proyecto

* Entrenar la **respuesta a incidentes de seguridad**
* Practicar la **toma de decisiones bajo presión**
* Simular escenarios realistas de seguridad informática
* Registrar acciones, resultados y desempeño final

Este proyecto puede utilizarse con fines **educativos**, **académicos** o de **entrenamiento básico en ciberseguridad**.

---

## 🧩 Funcionalidades principales

* ✅ Generación aleatoria de incidentes de seguridad
* ✅ Incidentes con **múltiples pasos de decisión**
* ✅ Acciones correctas e incorrectas
* ✅ Sistema de **puntaje**
* ✅ Interfaz gráfica con **Tkinter**
* ✅ Registro automático en archivos de log
* ✅ Resumen final de la simulación
* ✅ Cierre controlado de la aplicación

---

## 🖥️ Interfaz gráfica

La aplicación cuenta con una **GUI desarrollada en Tkinter**, que permite:

* Visualizar incidentes y preguntas
* Seleccionar acciones mediante botones
* Ver resultados inmediatos
* Consultar el puntaje actual
* Finalizar la simulación de forma segura

---

## 📁 Estructura del proyecto

```text
simulador_incidentes/
│
├── app/
│   ├── gui.py              # Interfaz gráfica (Tkinter)
│   └── controller.py       # Lógica de control y flujo
│
├── core/
│   └── incidentes.py       # Definición de incidentes y acciones
│
├── logs/
│   └── historial.log       # Registro de la simulación
│
├── requirements.txt        # Dependencias del proyecto
├── main.py                 # Punto de entrada de la aplicación
└── README.md               # Documentación del proyecto
```

---

## ⚙️ Requisitos

* Python **3.10 o superior**
* Sistema operativo: Windows, Linux o macOS

### Dependencias

El proyecto utiliza únicamente librerías estándar de Python:

* `tkinter`
* `datetime`
* `random`
* `os`

---

## ▶️ Cómo ejecutar el proyecto

1. Clonar el repositorio:

```bash
git clone https://github.com/ElisLopez12/simulador-incidentes
```

2. Entrar al directorio del proyecto:

```bash
cd simulador-incidentes
```

3. Ejecutar la aplicación:

```bash
python -m main.py
```

---

## 📝 Registro y logs

Durante la simulación se guarda información en:

```
logs/historial.log
```

El archivo incluye:

* Acciones tomadas
* Resultados (correctas / incorrectas)
* Puntaje acumulado
* Resumen final de la simulación

Ejemplo:

```text
===== RESUMEN DE SIMULACIÓN =====
Inicio: 2026-01-30 20:55:10
Fin:    2026-01-30 21:12:44

Incidentes generados: 4
Acciones correctas: 6
Acciones incorrectas: 3
Puntaje final: 65
================================
```

---

## 🧠 Arquitectura del sistema

El proyecto sigue una arquitectura sencilla y clara:

* **GUI** → Interacción con el usuario
* **Controller** → Lógica del flujo y decisiones
* **Core** → Datos y definición de incidentes
* **Logs** → Persistencia de resultados

Esto permite que el sistema sea **escalable, mantenible y fácil de extender**.

---

## 🚀 Posibles mejoras futuras

* Exportar resumen a CSV
* Modo evaluación / modo entrenamiento
* Límite de intentos por incidente
* Indicador de dificultad del incidente
* Estadísticas visuales

---

## 👤 Autores

**Grupo 10 de la Materia Traductores e interpretes**

**Elis López**
**Bárbara Pedrique**
**Dehinert Moran**
**Brandon Morales**
Proyecto académico – Simulación y seguridad informática

---
