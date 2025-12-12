# Bot de Telegram con Gemini AI

Bot de Telegram que responde preguntas usando Google Gemini AI. Perfecto para grupos donde los usuarios pueden hacer preguntas y el bot responde automáticamente.

## Características

- ✅ Responde automáticamente a todas las preguntas en grupos
- ✅ Usa Gemini AI para generar respuestas inteligentes
- ✅ Muestra indicador "escribiendo..." mientras procesa
- ✅ Manejo de errores robusto
- ✅ Fácil de desplegar en Railway, Render o Replit

## Configuración

### 1. Crear el bot en Telegram

1. Abre Telegram y busca **@BotFather**
2. Envía `/newbot`
3. Sigue las instrucciones y guarda el TOKEN que te da
4. Envía `/setprivacy` a @BotFather
5. Selecciona tu bot y elige **Disable** (para que reciba todos los mensajes del grupo)

### 2. Obtener API Key de Gemini

1. Ve a [Google AI Studio](https://aistudio.google.com/apikey)
2. Crea una API Key
3. Guarda la API Key

### 3. Desplegar en Railway (GRATIS)

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/telegram-gemini-bot)

1. Haz clic en el botón de arriba
2. Ingresa tus variables de entorno:
   - `TELEGRAM_TOKEN`: El token de @BotFather
   - `GEMINI_API_KEY`: Tu API key de Google AI Studio
3. Haz clic en "Deploy"
4. ¡Listo! Tu bot está funcionando 24/7

### Alternativa: Desplegar en Render

1. Crea cuenta en [Render.com](https://render.com)
2. Crea un nuevo "Web Service"
3. Conecta este repositorio de GitHub
4. Configura las variables de entorno:
   - `TELEGRAM_TOKEN`
   - `GEMINI_API_KEY`
5. Despliega

## Usar el Bot

1. Añade el bot a tu grupo de Telegram
2. Dale permisos de administrador (para leer mensajes)
3. ¡Cualquier mensaje que envíen los usuarios será respondido por el bot!

## Variables de Entorno

```bash
TELEGRAM_TOKEN=tu_token_de_botfather
GEMINI_API_KEY=tu_api_key_de_gemini
```

## Desarrollo Local

```bash
# Clonar repositorio
git clone https://github.com/nms20152009-netizen/telegram-gemini-bot.git
cd telegram-gemini-bot

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
export TELEGRAM_TOKEN="tu_token"
export GEMINI_API_KEY="tu_api_key"

# Ejecutar
python bot.py
```

## Estructura del Proyecto

```
telegram-gemini-bot/
├── bot.py              # Código principal del bot
├── requirements.txt    # Dependencias Python
├── Procfile           # Configuración para Railway/Render
└── README.md          # Este archivo
```

## Solución de Problemas

### El bot no responde en el grupo

- Verifica que desactivaste el "privacy mode" en @BotFather (`/setprivacy` → Disable)
- Asegúrate de que el bot tenga permisos de administrador en el grupo
- Revisa los logs en Railway/Render para ver si hay errores

### Error de API Key

- Verifica que la API key de Gemini sea válida
- Verifica que las variables de entorno estén configuradas correctamente

## Créditos

Creado por [tu nombre] usando:
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [Google Gemini AI](https://ai.google.dev/)

## Licencia

MIT
