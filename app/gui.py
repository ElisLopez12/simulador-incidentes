import tkinter as tk
from app.controller import SimuladorController


class SimuladorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Incidentes de Seguridad")
        self.root.geometry("650x500")

        self.controller = SimuladorController()

        # ----------------------------
        # Título
        # ----------------------------
        self.label_titulo = tk.Label(
            root,
            text="Simulador de Incidentes de Seguridad",
            font=("Arial", 16, "bold"),
        )
        self.label_titulo.pack(pady=10)

        # ----------------------------
        # Puntaje
        # ----------------------------
        self.label_puntaje = tk.Label(
            root, text="Puntaje: 0", font=("Arial", 12, "bold")
        )
        self.label_puntaje.pack(pady=5)

        # ----------------------------
        # Botón generar incidente
        # ----------------------------
        self.btn_incidente = tk.Button(
            root, text="Generar incidente", width=25, command=self.generar_incidente
        )
        self.btn_incidente.pack(pady=10)

        # ----------------------------
        # Botón finalizar simulación
        # ----------------------------
        self.btn_finalizar = tk.Button(
            root,
            text="Finalizar simulación",
            width=25,
            fg="white",
            bg="red",
            command=self.finalizar_simulacion,
        )
        self.btn_finalizar.pack(pady=5)

        # ----------------------------
        # Texto del incidente / pasos
        # ----------------------------
        self.texto_incidente = tk.Label(
            root, text="", justify="left", wraplength=600, font=("Arial", 12)
        )
        self.texto_incidente.pack(pady=15)

        # ----------------------------
        # Frame para acciones
        # ----------------------------
        self.frame_acciones = tk.Frame(root)
        self.frame_acciones.pack(pady=10)

        # ----------------------------
        # Resultado de acción
        # ----------------------------
        self.texto_resultado = tk.Label(root, text="", font=("Arial", 12), fg="blue")
        self.texto_resultado.pack(pady=10)

    # ==================================================
    # Generar incidente
    # ==================================================
    def generar_incidente(self):
        texto = self.controller.generar_incidente()
        self.texto_incidente.config(text=texto)
        self.texto_resultado.config(text="")

        self.actualizar_puntaje()
        self.mostrar_acciones()

    # ==================================================
    # Mostrar acciones del paso actual
    # ==================================================
    def mostrar_acciones(self):
        # Limpiar botones previos
        for widget in self.frame_acciones.winfo_children():
            widget.destroy()

        acciones = self.controller.obtener_acciones()

        for accion in acciones:
            btn = tk.Button(
                self.frame_acciones,
                text=accion,
                width=30,
                command=lambda a=accion: self.ejecutar_accion(a),
            )
            btn.pack(pady=5)

    # ==================================================
    # Ejecutar acción
    # ==================================================
    def ejecutar_accion(self, accion):
        mensaje = self.controller.evaluar_accion(accion)
        self.texto_resultado.config(text=mensaje)

        self.actualizar_puntaje()

        # Actualizar texto principal
        if "Incidente resuelto" in mensaje:
            self.texto_incidente.config(
                text="🟢 Incidente finalizado.\n\nPodés generar un nuevo incidente."
            )
            self.limpiar_acciones()
        else:
            # Mostrar siguiente paso
            self.texto_incidente.config(text=mensaje)
            self.mostrar_acciones()

    # ==================================================
    # Puntaje
    # ==================================================
    def actualizar_puntaje(self):
        puntaje = self.controller.obtener_puntaje()
        self.label_puntaje.config(text=f"Puntaje: {puntaje}")

    # ==================================================
    # Limpiar acciones
    # ==================================================
    def limpiar_acciones(self):
        for widget in self.frame_acciones.winfo_children():
            widget.destroy()

    def finalizar_simulacion(self):
        # Registrar cierre en el controller
        self.controller.finalizar_simulacion()

        # Cerrar ventana
        self.root.destroy()
