import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import google.generativeai as genai

# Configurar logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Configurar Gemini AI
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY no configurada")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# Token del bot de Telegram
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
if not TELEGRAM_TOKEN:
    raise ValueError("TELEGRAM_TOKEN no configurado")

async def responder_pregunta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Responde preguntas usando Gemini AI"""
    try:
        # Obtener el mensaje del usuario
        pregunta = update.message.text
        user = update.effective_user.first_name
        
        logger.info(f"Pregunta de {user}: {pregunta}")
        
        # Enviar "escribiendo..." mientras procesa
        await update.message.chat.send_action(action="typing")
        
        # Generar respuesta con Gemini
        response = model.generate_content(pregunta)
        respuesta = response.text
        
        # Enviar respuesta
        await update.message.reply_text(respuesta)
        
        logger.info(f"Respuesta enviada a {user}")
        
    except Exception as e:
        logger.error(f"Error al procesar pregunta: {e}")
        await update.message.reply_text(
            "Lo siento, hubo un error al procesar tu pregunta. Intenta de nuevo."
        )

if __name__ == '__main__':
    # Crear aplicación
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    
    # Agregar manejador para mensajes de texto (no comandos)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder_pregunta))
    
    logger.info("Bot iniciado. Esperando mensajes...")
    
    # Iniciar bot
    app.run_polling()
