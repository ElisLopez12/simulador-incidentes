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
            }
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
            }
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
            }
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
            }
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
            }
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
            }
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
            }
        ],
    },
]
