import os
from openai import OpenAI
import pyttsx3
import speech_recognition as sr
from dotenv import load_dotenv

# Cargar API key desde archivo .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Inicializar cliente de OpenAI
client = OpenAI(api_key=api_key)

# Inicializar TTS (texto a voz)
engine = pyttsx3.init()
engine.setProperty("rate", 170)  # velocidad de habla
engine.setProperty("voice", "spanish")  # intenta seleccionar voz en español

# Inicializar reconocimiento de voz
r = sr.Recognizer()

# Función para escuchar desde el micrófono
def escuchar_microfono():
    try:
        with sr.Microphone() as source:
            print("\n🎤 Habla ahora...")
            audio = r.listen(source)
            print("⏳ Procesando voz...")
            texto = r.recognize_whisper_api(audio, api_key=api_key, language="es")
            print(f"📝 Tú dijiste: {texto}")
            return texto
    except Exception as e:
        print(f"⚠️ No se pudo usar el micrófono: {e}")
        return None

# Función para enviar texto a ChatGPT y obtener respuesta
def responder_con_chatgpt(texto_usuario):
    respuesta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un asistente conversacional en español."},
            {"role": "user", "content": texto_usuario}
        ]
    )
    contenido = respuesta.choices[0].message.content
    print(f"\n🤖 ChatGPT: {contenido}")
    return contenido

# Función para hablar con voz
def hablar(texto):
    engine.say(texto)
    engine.runAndWait()

# Ciclo principal de conversación
while True:
    print("\n📢 ¿Cómo quieres ingresar el mensaje?")
    print("1. Escribir texto manualmente")
    print("2. Usar voz (si tienes micrófono)")
    print("3. Salir")

    opcion = input("Elige una opción (1/2/3): ")

    if opcion == "1":
        entrada = input("\n✏️ Escribe tu mensaje: ")
    elif opcion == "2":
        entrada = escuchar_microfono()
        if entrada is None:
            continue
    elif opcion == "3":
        print("👋 ¡Hasta luego!")
        break
    else:
        print("❌ Opción no válida")
        continue

    respuesta = responder_con_chatgpt(entrada)
    hablar(respuesta)

