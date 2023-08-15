import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')  # Descarga los datos necesarios para tokenización
# Definimos los patrones y respuestas para el chatbot
pares = [
    [
        r"¿Cómo está el clima hoy\?",
        ["El clima está soleado y cálido.", "Hoy está soleado y la temperatura es agradable."]
    ],
    [
        r"¿Qué tiempo hace afuera\?",
        ["El clima está bastante bueno.", "Está soleado y agradable."]
    ],
    [
        r"¿Va a llover hoy\?",
        ["No, no se espera lluvia hoy.", "No hay pronóstico de lluvia para hoy."]
    ],
    [
        r"¿Cuándo empieza el verano\?",
        ["El verano generalmente comienza en junio.", "El verano comienza en el mes de junio."]
    ],
    [
        r"(Adiós|Hasta luego)",
        ["Hasta luego. ¡Que tengas un buen día!", "Adiós. ¡Cuídate!"]
    ]
]
# Creamos el chatbot
chatbot = Chat(pares, reflections)

# Bucle principal para interactuar con el chatbot
print("Hola, soy un chatbot de clima. Puedes preguntarme sobre el clima actual. Para salir, escribe 'Adiós'.")
while True:
    mensaje = input("Tú: ")
    if mensaje.lower() == "adiós":
        print("Chatbot: ¡Hasta luego!")
        break
    respuesta = chatbot.respond(mensaje)
    print("Chatbot:", respuesta)
