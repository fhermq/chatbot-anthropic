# A LLM Chatbot 🤖

Un chatbot interactivo basado en Claude (Anthropic) con múltiples personalidades. El proyecto demuestra cómo usar system prompts para cambiar el comportamiento y estilo de respuesta del modelo.

## 🎯 Características

- **Múltiples personalidades**: 8 personalidades diferentes para elegir
  - 📚 **Helpful** - Asistente amable y profesional
  - 💻 **Technical** - Ingeniero de software experimentado
  - 🎓 **Teacher** - Profesor paciente con método socrático
  - 🏴‍☠️ **Pirate** - Capitán pirata entretenido
  - 🔬 **Scientist** - Científico riguroso y preciso
  - 🎭 **Poet** - Poeta filosófico con metáforas
  - 👔 **Interviewer** - Entrevistador técnico
  - 🔍 **Code Reviewer** - Revisor de código senior

- **Historial de conversación persistente**: Mantiene el contexto entre mensajes
- **Cambio de personalidad dinámico**: Cambia de personalidad sin perder el historial
- **Comandos útiles**:
  - `quit/exit/bye` - Salir del chatbot
  - `reset` - Limpiar el historial de conversación
  - `switch` - Cambiar a otra personalidad

## 📋 Requisitos

- Python 3.8+
- `anthropic` - SDK de Anthropic
- `python-dotenv` - Para manejo de variables de entorno

## 🚀 Instalación

1. Clona el repositorio o descarga los archivos

2. Configura el virtual environment:
```bash
# Crear virtual environment
python -m venv venv

# Activar virtual environment
source venv/bin/activate  # Mac/Linux
# o: venv\Scripts\activate  # Windows
```

3. Instala las dependencias:
```bash
pip install anthropic python-dotenv
```

4. Obtén tu API key de Anthropic:
   - Ve a: https://console.anthropic.com/
   - Regístrate (¡GRATIS con $5 de crédito - suficiente para 1000+ conversaciones!)
   - Copia tu API key

5. Configura tu API key:
   - Crea un archivo `.env` en la raíz del proyecto
   - Añade tu clave API:
   ```
   ANTHROPIC_API_KEY=tu_clave_aqui
   ```

## 💻 Uso

Ejecuta la versión más reciente (v3):

```bash
python chatbotv3.py
```

El programa:
1. Muestra las personalidades disponibles
2. Te pide elegir una (número del 1 al 8)
3. Inicia una conversación interactiva

### Ejemplo de sesión:

```
============================================================
Simple LLM Chatbot v3 (with personalities)
============================================================

Available personalities:
1. HELPFUL: You are a helpful and friendly assistant...
2. TECHNICAL: You are a senior software engineer with...
[...]

Choose a personality (1-6): 2

✓ You selected: TECHNICAL
============================================================
Commands:
  'quit' - Exit the chatbot
  'reset' - Clear conversation history
  'switch' - Change personality
============================================================

You: Explícame qué es una arquitectura de microservicios

Technical: [Respuesta detallada como ingeniero senior...]

[Messages: 2]
```

## 📁 Estructura del Proyecto

```
simple-llm-chatbot/
├── chatbot.py           # Versión inicial para validar conexión
├── chatbotV1.py         # Versión 1 - Primeras mejoras
├── chatbotV2.py         # Versión 2 - Iteración intermedia
├── chatbotv3.py         # Versión 3 - Actual (RECOMENDADA)
├── .env                 # Configuración (no incluido en git)
├── .gitignore           # Archivos a ignorar
└── README.md            # Este archivo
```

## 🔧 Cómo Funciona

El proyecto utiliza el concepto de **system prompts** para controlar el comportamiento del modelo:

```python
# El system prompt define la personalidad
system_prompt = """You are a senior software engineer with 15+ years experience...
You explain technical concepts clearly with practical examples and code snippets."""

# Se pasa a Claude en cada llamada
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1000,
    system=system_prompt,  # ← Esto cambia el comportamiento
    messages=conversation_history
)
```

### Flujo de Conversación:

1. Usuario elige personalidad
2. Se establece el `system_prompt` correspondiente
3. En cada mensaje:
   - Se añade el mensaje del usuario al historial
   - Se envía a Claude con el sistema_prompt
   - Se recibe y almacena la respuesta
   - Se muestra al usuario

## 🎓 Aprendizajes Clave

Este proyecto demuestra:
- Uso de la API de Anthropic
- Importancia de los system prompts
- Manejo de historial de conversación
- Diseño interactivo en línea de comandos
- Patrones recursivos para cambio de estado

## 🤝 Características Avanzadas Posibles

- Guardar conversaciones en archivo
- Exportar conversaciones a PDF
- Historial persistente entre sesiones
- Más personalidades personalizables
- Integración con web (FastAPI/Flask)
- Análisis de sentimiento
- Logging de sesiones

## ⚠️ Notas Importantes

- Requiere conexión a Internet para usar la API de Anthropic
- Cada llamada consume tokens y tiene costo
- El modelo usado es `claude-sonnet-4-20250514`
- El límite de tokens por respuesta es 1000

## 📝 Licencia

Proyecto personal de demostración

## 👤 Autor

Fernando Mirasol

Proyecto creado como ejercicio de integración con LLMs
