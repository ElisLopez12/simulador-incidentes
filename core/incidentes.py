INCIDENTES = [
    # 1️⃣ Acceso no autorizado
    {
        "tipo": "Acceso no autorizado",
        "descripcion": "Se detectó un intento de acceso sospechoso al sistema.",
        "pasos": [
            {
                "mensaje": "¿Cuál es la primera acción a tomar?",
                "acciones": ["Bloquear acceso", "Ignorar", "Reiniciar sistema"],
                "correcta": "Bloquear acceso",
            },
            {
                "mensaje": "El acceso fue bloqueado. ¿Qué hacer ahora?",
                "acciones": ["Notificar al administrador", "Ignorar"],
                "correcta": "Notificar al administrador",
            },
        ],
    },
    # 2️⃣ Caída del sistema
    {
        "tipo": "Caída del sistema",
        "descripcion": "El sistema principal ha dejado de responder.",
        "pasos": [
            {
                "mensaje": "¿Cómo responder al incidente?",
                "acciones": [
                    "Reiniciar sistema",
                    "Ignorar",
                    "Notificar al administrador",
                ],
                "correcta": "Reiniciar sistema",
            },
            {
                "mensaje": "El sistema fue reiniciado. ¿Qué hacer ahora?",
                "acciones": ["Verificar logs", "Ignorar"],
                "correcta": "Verificar logs",
            },
        ],
    },
    # 3️⃣ Malware detectado
    {
        "tipo": "Malware detectado",
        "descripcion": "Se detectó software malicioso en un equipo.",
        "pasos": [
            {
                "mensaje": "¿Qué acción tomar primero?",
                "acciones": ["Aislar equipo", "Ignorar", "Reiniciar sistema"],
                "correcta": "Aislar equipo",
            },
            {
                "mensaje": "El equipo fue aislado. ¿Siguiente paso?",
                "acciones": ["Ejecutar análisis", "Ignorar"],
                "correcta": "Ejecutar análisis",
            },
        ],
    },
    # 4️⃣ Phishing reportado
    {
        "tipo": "Correo de phishing",
        "descripcion": "Un usuario reportó un correo sospechoso.",
        "pasos": [
            {
                "mensaje": "¿Cómo responder?",
                "acciones": ["Bloquear remitente", "Ignorar", "Reenviar correo"],
                "correcta": "Bloquear remitente",
            },
            {
                "mensaje": "Remitente bloqueado. ¿Qué hacer después?",
                "acciones": ["Notificar usuarios", "Ignorar"],
                "correcta": "Notificar usuarios",
            },
        ],
    },
    # 5️⃣ Uso excesivo de recursos
    {
        "tipo": "Uso excesivo de recursos",
        "descripcion": "Un servidor está consumiendo demasiados recursos.",
        "pasos": [
            {
                "mensaje": "¿Qué acción tomar?",
                "acciones": ["Ejecutar análisis", "Ignorar", "Reiniciar sistema"],
                "correcta": "Ejecutar análisis",
            },
            {
                "mensaje": "Análisis completado. ¿Siguiente paso?",
                "acciones": ["Reiniciar sistema", "Notificar al administrador"],
                "correcta": "Reiniciar sistema",
            },
        ],
    },
    # 6️⃣ Intentos de fuerza bruta
    {
        "tipo": "Fuerza bruta detectada",
        "descripcion": "Múltiples intentos fallidos de inicio de sesión.",
        "pasos": [
            {
                "mensaje": "¿Acción inmediata?",
                "acciones": ["Bloquear acceso", "Ignorar"],
                "correcta": "Bloquear acceso",
            },
            {
                "mensaje": "Acceso bloqueado. ¿Qué sigue?",
                "acciones": ["Notificar al administrador", "Ignorar"],
                "correcta": "Notificar al administrador",
            },
        ],
    },
    # 7️⃣ Servicio detenido
    {
        "tipo": "Servicio detenido",
        "descripcion": "Un servicio crítico se ha detenido inesperadamente.",
        "pasos": [
            {
                "mensaje": "¿Cómo proceder?",
                "acciones": ["Reiniciar sistema", "Ignorar"],
                "correcta": "Reiniciar sistema",
            },
            {
                "mensaje": "Servicio reiniciado. ¿Qué hacer ahora?",
                "acciones": ["Verificar logs", "Notificar usuarios"],
                "correcta": "Verificar logs",
            },
        ],
    },
    # 8️⃣ Configuración alterada
    {
        "tipo": "Configuración alterada",
        "descripcion": "Se detectaron cambios no autorizados en la configuración.",
        "pasos": [
            {
                "mensaje": "¿Acción recomendada?",
                "acciones": ["Restaurar configuración", "Ignorar"],
                "correcta": "Restaurar configuración",
            },
            {
                "mensaje": "Configuración restaurada. ¿Qué hacer ahora?",
                "acciones": ["Notificar equipo", "Ignorar"],
                "correcta": "Notificar equipo",
            },
        ],
    },
    # 9️⃣ Tráfico sospechoso
    {
        "tipo": "Tráfico sospechoso",
        "descripcion": "Se detectó tráfico inusual en la red.",
        "pasos": [
            {
                "mensaje": "¿Qué hacer primero?",
                "acciones": ["Ejecutar análisis", "Ignorar"],
                "correcta": "Ejecutar análisis",
            },
            {
                "mensaje": "Análisis completado. ¿Siguiente acción?",
                "acciones": ["Bloquear IP sospechosa", "Notificar administrador"],
                "correcta": "Bloquear IP sospechosa",
            },
        ],
    },
    # 🔟 Evento normal
    {
        "tipo": "Evento normal",
        "descripcion": "El sistema funciona dentro de los parámetros normales.",
        "pasos": [
            {
                "mensaje": "¿Acción a tomar?",
                "acciones": ["Ignorar", "Ejecutar análisis"],
                "correcta": "Ignorar",
            },
            {
                "mensaje": "¿Desea realizar alguna verificación adicional?",
                "acciones": ["Ejecutar análisis", "No hacer nada"],
                "correcta": "No hacer nada",
            },
        ],
    },
    # 1️⃣1️⃣ Fallo de backup
    {
        "tipo": "Fallo de backup",
        "descripcion": "El proceso de backup ha fallado.",
        "pasos": [
            {
                "mensaje": "¿Qué acción tomar primero?",
                "acciones": [
                    "Verificar logs de backup",
                    "Ignorar",
                    "Reiniciar sistema",
                ],
                "correcta": "Verificar logs de backup",
            },
            {
                "mensaje": "Logs revisados. ¿Siguiente paso?",
                "acciones": ["Reintentar backup", "Notificar administrador"],
                "correcta": "Reintentar backup",
            },
        ],
    },
    # 1️⃣2️⃣ Error en aplicación crítica
    {
        "tipo": "Error en aplicación crítica",
        "descripcion": "Una aplicación crítica dejó de funcionar.",
        "pasos": [
            {
                "mensaje": "¿Qué hacer primero?",
                "acciones": ["Reiniciar aplicación", "Ignorar"],
                "correcta": "Reiniciar aplicación",
            },
            {
                "mensaje": "Reinicio completado. ¿Qué sigue?",
                "acciones": ["Verificar funcionalidad", "Notificar equipo"],
                "correcta": "Verificar funcionalidad",
            },
        ],
    },
    # 1️⃣3️⃣ Contraseña comprometida
    {
        "tipo": "Contraseña comprometida",
        "descripcion": "Se detectó que una contraseña de usuario fue comprometida.",
        "pasos": [
            {
                "mensaje": "Primera acción a tomar?",
                "acciones": ["Forzar cambio de contraseña", "Ignorar"],
                "correcta": "Forzar cambio de contraseña",
            },
            {
                "mensaje": "Sesiones activas revocadas. ¿Qué más hacer?",
                "acciones": ["Notificar usuario afectado", "Ignorar"],
                "correcta": "Notificar usuario afectado",
            },
        ],
    },
    # 1️⃣4️⃣ Intrusión física
    {
        "tipo": "Intrusión física",
        "descripcion": "Se detectó acceso físico no autorizado a instalaciones.",
        "pasos": [
            {
                "mensaje": "Acción inmediata?",
                "acciones": ["Verificar cámaras", "Ignorar"],
                "correcta": "Verificar cámaras",
            },
            {
                "mensaje": "Cámaras verificadas. ¿Qué hacer ahora?",
                "acciones": ["Alertar seguridad", "Registrar incidente"],
                "correcta": "Alertar seguridad",
            },
            {
                "mensaje": "Seguridad alertada. Próximo paso?",
                "acciones": ["Registrar incidente", "Ignorar"],
                "correcta": "Registrar incidente",
            },
        ],
    },
    # 1️⃣5️⃣ Actualización fallida
    {
        "tipo": "Actualización fallida",
        "descripcion": "Una actualización crítica no se aplicó correctamente.",
        "pasos": [
            {
                "mensaje": "Primera acción?",
                "acciones": ["Detectar fallo", "Ignorar"],
                "correcta": "Detectar fallo",
            },
            {
                "mensaje": "Fallo identificado. ¿Siguiente paso?",
                "acciones": ["Revertir cambios", "Intentar actualizar de nuevo"],
                "correcta": "Revertir cambios",
            },
            {
                "mensaje": "Cambios revertidos. ¿Qué hacer después?",
                "acciones": ["Intentar actualizar de nuevo", "Notificar administrador"],
                "correcta": "Intentar actualizar de nuevo",
            },
        ],
    },
    # 1️⃣6️⃣ Falla de red
    {
        "tipo": "Falla de red",
        "descripcion": "Se detectó pérdida de conectividad en un segmento de la red.",
        "pasos": [
            {
                "mensaje": "Primer paso?",
                "acciones": ["Identificar nodo afectado", "Ignorar"],
                "correcta": "Identificar nodo afectado",
            },
            {
                "mensaje": "Nodo identificado. ¿Siguiente acción?",
                "acciones": ["Reiniciar router", "Notificar usuarios"],
                "correcta": "Reiniciar router",
            },
            {
                "mensaje": "Router reiniciado. ¿Qué más hacer?",
                "acciones": ["Verificar conectividad", "Ignorar"],
                "correcta": "Verificar conectividad",
            },
        ],
    },
    # 1️⃣7️⃣ Correo no entregado
    {
        "tipo": "Correo no entregado",
        "descripcion": "Un correo crítico no fue entregado.",
        "pasos": [
            {
                "mensaje": "Primer paso?",
                "acciones": ["Verificar servidor de correo", "Ignorar"],
                "correcta": "Verificar servidor de correo",
            },
            {
                "mensaje": "Servidor revisado. ¿Qué sigue?",
                "acciones": ["Reenviar correo", "Notificar usuario"],
                "correcta": "Reenviar correo",
            },
        ],
    },
    # 1️⃣8️⃣ Error en base de datos
    {
        "tipo": "Error en base de datos",
        "descripcion": "Se detectó un error crítico en la base de datos.",
        "pasos": [
            {
                "mensaje": "Primer paso?",
                "acciones": ["Revisar logs", "Ignorar"],
                "correcta": "Revisar logs",
            },
            {
                "mensaje": "Logs revisados. ¿Qué acción tomar?",
                "acciones": ["Reiniciar servicio", "Notificar DBA"],
                "correcta": "Reiniciar servicio",
            },
            {
                "mensaje": "Servicio reiniciado. Próximo paso?",
                "acciones": ["Probar consultas", "Ignorar"],
                "correcta": "Probar consultas",
            },
        ],
    },
    # 1️⃣9️⃣ Ransomware detectado
    {
        "tipo": "Ransomware detectado",
        "descripcion": "Se detectó ransomware en un equipo.",
        "pasos": [
            {
                "mensaje": "Primera acción?",
                "acciones": ["Aislar máquina", "Ignorar"],
                "correcta": "Aislar máquina",
            },
            {
                "mensaje": "Máquina aislada. ¿Qué hacer después?",
                "acciones": ["Analizar ransomware", "Notificar equipo de seguridad"],
                "correcta": "Analizar ransomware",
            },
            {
                "mensaje": "Ransomware analizado. Próximo paso?",
                "acciones": ["Restaurar backup", "Ignorar"],
                "correcta": "Restaurar backup",
            },
        ],
    },
    # 2️⃣0️⃣ Alerta de IDS
    {
        "tipo": "Alerta de IDS",
        "descripcion": "El sistema de detección de intrusos generó una alerta.",
        "pasos": [
            {
                "mensaje": "Primera acción?",
                "acciones": ["Verificar alerta", "Ignorar"],
                "correcta": "Verificar alerta",
            },
            {
                "mensaje": "Alerta verificada. ¿Qué hacer después?",
                "acciones": ["Correlacionar eventos", "Notificar administrador"],
                "correcta": "Correlacionar eventos",
            },
            {
                "mensaje": "Eventos correlacionados. Próximo paso?",
                "acciones": ["Investigar origen", "Ignorar"],
                "correcta": "Investigar origen",
            },
        ],
    },
]
