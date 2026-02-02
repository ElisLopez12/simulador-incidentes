import tkinter as tk
from app.controller import SimuladorController


class SimuladorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Incidentes de Seguridad")
        self.root.geometry("700x550")
        self.root.configure(bg="#f5f5f5")  # fondo suave

        self.controller = SimuladorController()

        # ----------------------------
        # Título con fondo oscuro
        # ----------------------------
        self.label_titulo = tk.Label(
            root,
            text="Simulador de Incidentes de Seguridad",
            font=("Segoe UI", 18, "bold"),
            bg="#2c3e50",
            fg="white",
            padx=10,
            pady=10,
        )
        self.label_titulo.pack(fill="x", pady=(0, 10))

        # ----------------------------
        # Puntaje con fondo suave
        # ----------------------------
        self.label_puntaje = tk.Label(
            root,
            text="Puntaje: 0",
            font=("Segoe UI", 12, "bold"),
            bg="#ecf0f1",
            fg="#2c3e50",
            padx=10,
            pady=5,
            relief="groove",
            bd=2,
        )
        self.label_puntaje.pack(pady=5)

        # ----------------------------
        # Botones principales
        # ----------------------------
        btn_style = {
            "width": 25,
            "font": ("Segoe UI", 12, "bold"),
            "bd": 0,
            "fg": "white",
        }

        self.btn_incidente = tk.Button(
            root,
            text="Generar incidente",
            bg="#2980b9",
            activebackground="#3498db",
            command=self.generar_incidente,
            **btn_style,
        )
        self.btn_incidente.pack(pady=10)

        self.btn_finalizar = tk.Button(
            root,
            text="Finalizar simulación",
            bg="#c0392b",
            activebackground="#e74c3c",
            command=self.finalizar_simulacion,
            **btn_style,
        )
        self.btn_finalizar.pack(pady=5)

        # ----------------------------
        # Frame central para incidente
        # ----------------------------
        self.frame_incidente = tk.Frame(
            root, bg="white", bd=2, relief="groove", padx=10, pady=10
        )
        self.frame_incidente.pack(padx=20, pady=15, fill="both", expand=True)

        self.texto_incidente = tk.Label(
            self.frame_incidente,
            text="",
            justify="left",
            wraplength=650,
            font=("Segoe UI", 12),
            bg="white",
            fg="#2c3e50",
        )
        self.texto_incidente.pack(pady=5)

        # ----------------------------
        # Frame para acciones
        # ----------------------------
        self.frame_acciones = tk.Frame(self.frame_incidente, bg="white")
        self.frame_acciones.pack(pady=10)

        # ----------------------------
        # Resultado de acción
        # ----------------------------
        self.texto_resultado = tk.Label(
            root,
            text="",
            font=("Segoe UI", 12, "bold"),
            fg="#27ae60",
            bg="#f5f5f5",
        )
        self.texto_resultado.pack(pady=10)

    # =============================
    # Métodos existentes...
    # =============================
    def generar_incidente(self):
        texto = self.controller.generar_incidente()
        self.texto_incidente.config(text=texto)
        self.texto_resultado.config(text="")
        self.actualizar_puntaje()
        self.mostrar_acciones()

    def mostrar_acciones(self):
        for widget in self.frame_acciones.winfo_children():
            widget.destroy()

        acciones = self.controller.obtener_acciones()
        for accion in acciones:
            btn = tk.Button(
                self.frame_acciones,
                text=accion,
                width=30,
                font=("Segoe UI", 11),
                bg="#3498db",
                fg="white",
                activebackground="#2980b9",
                command=lambda a=accion: self.ejecutar_accion(a),
            )
            btn.pack(pady=5)

    def ejecutar_accion(self, accion):
        mensaje = self.controller.evaluar_accion(accion)
        self.texto_resultado.config(text=mensaje)
        self.actualizar_puntaje()
        if "Incidente resuelto" in mensaje:
            self.texto_incidente.config(
                text="🟢 Incidente finalizado.\n\nPodés generar un nuevo incidente."
            )
            self.limpiar_acciones()
        else:
            self.texto_incidente.config(text=mensaje)
            self.mostrar_acciones()

    def actualizar_puntaje(self):
        puntaje = self.controller.obtener_puntaje()
        self.label_puntaje.config(text=f"Puntaje: {puntaje}")

    def limpiar_acciones(self):
        for widget in self.frame_acciones.winfo_children():
            widget.destroy()

    def finalizar_simulacion(self):
        self.controller.finalizar_simulacion()
        self.root.destroy()
