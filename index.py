import random

armas_vikingo = {
    "espada": 12,
    "hacha": 15,
    "garrote": 8
}

arma_actual = "espada"

def mostrar_menu_armas():
    print("\n--- Menú de Armas ---")
    print("Elige tu arma:")
    for arma in armas_vikingo:
        print(f"- {arma.capitalize()}")
    print("---------------------")

def cambiar_arma(nueva_arma):
    global arma_actual
    if nueva_arma in armas_vikingo:
        arma_actual = nueva_arma
        print(f"¡Has cambiado a {arma_actual}!")
    else:
        print("Esa arma no existe. Mantienes tu arma actual:", arma_actual.capitalize())

def atacar_con_arma():
    dano_base = armas_vikingo[arma_actual]
    dano_total = dano_base + random.randint(-2, 5)
    print(f"¡Atacas con tu {arma_actual.capitalize()}! Infliges {dano_total} de daño.")

def iniciar_juego():
    energia_vikingo = 100
    print("¡Bienvenido, valiente guerrero vikingo!")

    while True:
        print("\n--- ¡Elige tu acción! ---")
        print("1. Atacar")
        print("2. Cambiar de arma")
        print("3. Ver estado")
        print("4. Salir")

        eleccion = input("Ingresa tu elección: ").strip()

        if eleccion == '1':
            print(f"Arma equipada: {arma_actual.capitalize()}")
            atacar_con_arma()
        elif eleccion == '2':
            mostrar_menu_armas()
            nueva_arma = input("Escribe el nombre del arma que quieres usar: ").lower().strip()
            cambiar_arma(nueva_arma)
        elif eleccion == '3':
            print(f"\n--- Estado del Vikingo ---")
            print(f"Energía: {energia_vikingo}")
            print(f"Arma equipada: {arma_actual.capitalize()} (Daño: {armas_vikingo[arma_actual]})")
            print("-------------------------")
        elif eleccion == '4':
            print("El vikingo se retira a su aldea. ¡Hasta la próxima aventura!")
            break
        else:
            print("Elección no válida. Por favor, intenta de nuevo.")

iniciar_juego()