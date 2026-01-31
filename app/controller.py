import random
from core.incidentes import INCIDENTES
from datetime import datetime
import os


class SimuladorController:
    def __init__(self):
        self.incidente_actual = None
        self.paso_actual = 0
        self.puntaje = 0

        # Estadísticas
        self.inicio_simulacion = datetime.now()
        self.incidentes_generados = 0
        self.acciones_correctas = 0
        self.acciones_incorrectas = 0

    # -------------------------------------------------
    # Generar un nuevo incidente
    # -------------------------------------------------
    def generar_incidente(self):
        self.incidente_actual = random.choice(INCIDENTES)
        self.paso_actual = 0
        self.incidentes_generados += 1

        descripcion = self.incidente_actual["descripcion"]
        mensaje_paso = self.incidente_actual["pasos"][self.paso_actual]["mensaje"]

        return f"{descripcion}\n\n{mensaje_paso}"

    # -------------------------------------------------
    # Obtener acciones del paso actual
    # -------------------------------------------------
    def obtener_acciones(self):
        if not self.incidente_actual:
            return []

        pasos = self.incidente_actual["pasos"]

        if self.paso_actual >= len(pasos):
            return []

        return pasos[self.paso_actual]["acciones"]

    # -------------------------------------------------
    # Evaluar acción del usuario
    # -------------------------------------------------
    def evaluar_accion(self, accion):
        if not self.incidente_actual:
            return "⚠ No hay incidente activo."

        paso = self.incidente_actual["pasos"][self.paso_actual]
        accion_correcta = paso["correcta"]

        if accion == accion_correcta:
            self.puntaje += 10
            self.acciones_correctas += 1
            self.paso_actual += 1

            # ¿Quedan más pasos?
            if self.paso_actual < len(self.incidente_actual["pasos"]):
                siguiente_mensaje = self.incidente_actual["pasos"][self.paso_actual][
                    "mensaje"
                ]
                return f"✅ Acción correcta.\n\n{siguiente_mensaje}"
            else:
                return "✅ Incidente resuelto correctamente."
        else:
            self.puntaje -= 5
            self.acciones_incorrectas += 1
            return "❌ Acción incorrecta. Intente otra respuesta."

    # -------------------------------------------------
    # Obtener puntaje
    # -------------------------------------------------
    def obtener_puntaje(self):
        return self.puntaje

    def finalizar_simulacion(self):
        """
        Registra el cierre de la simulación con puntaje final.
        """
        self.guardar_resumen()

    def guardar_resumen(self):
        os.makedirs("logs", exist_ok=True)
        ruta_log = "logs/historial.log"

        fin_simulacion = datetime.now()

        with open(ruta_log, "a", encoding="utf-8") as archivo:
            archivo.write("\n===== RESUMEN DE SIMULACIÓN =====\n")
            archivo.write(
                f"Inicio: {self.inicio_simulacion.strftime('%Y-%m-%d %H:%M:%S')}\n"
            )
            archivo.write(f"Fin:    {fin_simulacion.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            archivo.write(f"Incidentes generados: {self.incidentes_generados}\n")
            archivo.write(f"Acciones correctas: {self.acciones_correctas}\n")
            archivo.write(f"Acciones incorrectas: {self.acciones_incorrectas}\n")
            archivo.write(f"Puntaje final: {self.puntaje}\n")
            archivo.write("================================\n\n")
