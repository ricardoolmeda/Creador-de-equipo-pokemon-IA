import openai
from config import *

def preguntas_pokemon():
    preguntas = [
        "¿Cuál es tu Pokémon favorito?",
        "Si pudieras vivir en una región del mundo Pokémon, ¿cuál elegirías?",
        "¿Tipo favorito?",
        "¿Prefieres entrenar Pokémon de un tipo específico o te gusta tener un equipo variado?",
        "¿Cuál es tu juego de Pokémon favorito?",
        "¿Te identificas con algún entrenador o personaje de la serie Pokémon?",
        "¿Tienes algún recuerdo especial relacionado con Pokémon? ¿Qué pasó?",
        "¿Prefieres batallar en gimnasios o participar en concursos Pokémon?",
        "Si pudieras tener un Pokémon en la vida real, ¿cuál escogerías y por qué?"
    ]
    
    respuestas = []
    
    for pregunta in preguntas:
        respuesta = input(pregunta + " ")
        respuestas.append(respuesta)
    
    return respuestas

def menu_recomendaciones():
    print("1. Recomendar equipo")
    print("2. Volver al menú principal")
    return input("Selecciona una opción: ")

def main():
    openai.api_key = MY_KEY # Cambiar la key por la propia
    print("💬 ChatGPT API en Python")

    # Contexto del asistente
    context = {"role": "system", "content": "Eres un asistente muy útil y amigable, siempre dispuesto a ayudar y a hacer la conversación más entretenida."}
    messages = [context]

    # Preguntas de Pokemon
    respuestas_usuario = preguntas_pokemon()
    print("\nTus respuestas:")
    for i, respuesta in enumerate(respuestas_usuario, 1):
        print(f"Pregunta {i}: {respuesta}")

    while True:
        option = menu_recomendaciones()

        if option == "1":
            # Recomendamos el equipo segun las preguntas
            content = "Basado en mis respuestas: " + str(respuestas_usuario) + ". ¿Cuál sería un buen equipo Pokémon?"
            messages.append({"role": "user", "content": content})
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            response_content = response.choices[0].message.content
            messages.append({"role": "assistant", "content": response_content})
            print(f"> {response_content}")
        elif option == "2":
            # Volver al menu principal
            print("Volviendo al menú principal.")
            break
        else:
            print("Opción no válida, por favor selecciona una opción del menú.")

if __name__ == "__main__":
    main()
