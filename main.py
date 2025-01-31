import openai
from config import *

def obtener_preguntas_pokemon():
    return [
        "¿Cuál es tu Pokémon favorito?",
        "Si pudieras vivir en una región del mundo Pokémon, ¿cuál elegirías?",
        "¿Tipo favorito?",
        "¿Prefieres entrenar Pokémon de un tipo específico o te gusta tener un equipo variado?",
        "¿Te gusta otro tipo?, ¿cuál?",
        "¿Te gustan los pokemons legendarios para tu equipo?",
        "¿Te gusta tener un equipo pokemon solo de una región?",
        "¿Cuál es tu juego de Pokémon favorito?",
        "¿Te identificas con algún entrenador o personaje de la serie Pokémon?",
        "¿Prefieres batallar en gimnasios o participar en concursos Pokémon?",
        "Si pudieras tener un Pokémon en la vida real, ¿cuál escogerías y por qué?"
    ]

def preguntas_pokemon(preguntas):
    respuestas = []
    for pregunta in preguntas:
        respuesta = input(pregunta + " ")
        respuestas.append(respuesta)
    return respuestas

def sugerir_movimientos_pokemon_especificos():
    pokemon_list = input("Ingresa los nombres de los Pokémon separados por comas: ").split(',')
    pokemon_list = [pokemon.strip() for pokemon in pokemon_list]
    return pokemon_list

def mejor_bot():
    bot =[
        "El cual se llama PokeBot",
        "Este es el enlace para acceder a él",
        "https://t.me/@PokeCalculator_bot"

    ]
    print("\"Claro uno de los bot más completos es un bot de telegram")
    for i, bots in enumerate(bot, 1):
        print(f"Bot {i}: {bots}")

def menu_recomendaciones():
    print("1. Recomendar equipo")
    print("2. Repetir cuestionario")
    print("3. Mostrar respuestas a las preguntas")
    print("4. Sugerir movimientos para el equipo Pokémon recomendado")
    print("5. Sugerir movimientos a Pokémon específicos")
    print("6. Consejos de crianza")
    print("7. Mejor Bot para ver estadísticas")
    print("8. Volver al menú principal")
    
    return input("Selecciona una opción: ")

def main():
    openai.api_key = MY_KEY  # Cambiar la key por la propia
    print("💬 ChatGPT API en Python")

    # Contexto del asistente
    context = {"role": "system", "content": "Eres un asistente muy útil y amigable, siempre dispuesto a ayudar y a hacer la conversación más entretenida."}
    messages = [context]

    # Obtener preguntas de Pokémon
    preguntas = obtener_preguntas_pokemon()

    # Preguntas de Pokémon
    respuestas_usuario = preguntas_pokemon(preguntas)

    equipo_pokemon = None  # Inicializar variable de equipo

    while True:
        option = menu_recomendaciones()

        if option == "1":
            # Recomendamos el equipo según las preguntas
            content = "Basado en mis respuestas: " + str(respuestas_usuario) + ". ¿Cuál sería un buen equipo Pokémon?"
            messages.append({"role": "user", "content": content})
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            response_content = response.choices[0].message.content
            messages.append({"role": "assistant", "content": response_content})
            print(f"> {response_content}")
            equipo_pokemon = response_content  # Guardamos el equipo recomendado
       
        elif option == "2":
            respuestas_usuario = preguntas_pokemon(preguntas)  # Actualizar respuestas
            print("\nTus nuevas respuestas:")
            for i, respuesta in enumerate(respuestas_usuario, 1):
                print(f"Pregunta {i}: {respuesta}")
        
        elif option == "3":
            print("\nTus respuestas:")
            for i, respuesta in enumerate(respuestas_usuario, 1):
                print(f"Pregunta {i}: {respuesta}")

        elif option == "4":
            if equipo_pokemon:
                content = "Sugerir los mejores movimientos para este equipo: " + equipo_pokemon
                messages.append({"role": "user", "content": content})
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages
                )
                response_content = response.choices[0].message.content
                messages.append({"role": "assistant", "content": response_content})
                print(f"> {response_content}")
            else:
                print("Primero debes obtener una recomendación de equipo.")
        
        elif option == "5":
            pokemon_list = sugerir_movimientos_pokemon_especificos()
            content = "Sugerir los mejores movimientos para los siguientes Pokémon: " + str(pokemon_list)
            messages.append({"role": "user", "content": content})
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            response_content = response.choices[0].message.content
            messages.append({"role": "assistant", "content": response_content})
            print(f"> {response_content}")
        
        elif option == "6":
            content = "Dame los mejores consejos para la crianza Pokemon"
            messages.append({"role": "user", "content": content})
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            response_content = response.choices[0].message.content
            messages.append({"role": "assistant", "content": response_content})
            print(f"> {response_content}")
        
        elif option =="7":
            mejor_bot()
        
        elif option == "8":
            # Volver al menú principal
            print("Volviendo al menú principal.")
            break
        else:
            print("Opción no válida, por favor selecciona una opción del menú.")

if __name__ == "__main__":
    main()
