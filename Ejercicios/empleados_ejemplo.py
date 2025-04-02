import copy


def mostrar_estado(original, shallow, deep, paso):
    """
    Función de ayuda para mostrar el estado actual de las tres listas
    de manera formateada y clara.
    """
    print(f"\n{'='*60}")
    print(f"Paso {paso}")
    print(f"{'='*60}")
    print("\nLista Original:")
    for empleado in original:
        print(f"  - {empleado[0]}: {empleado[1]}")

    print("\nCopia Superficial (Shallow Copy):")
    for empleado in shallow:
        print(f"  - {empleado[0]}: {empleado[1]}")

    print("\nCopia Profunda (Deep Copy):")
    for empleado in deep:
        print(f"  - {empleado[0]}: {empleado[1]}")

    print("\nAnálisis de IDs:")
    print(f"ID Lista Original: {id(original)}")
    print(f"ID Shallow Copy: {id(shallow)}")
    print(f"ID Deep Copy: {id(deep)}")
    print(f"ID habilidades Pedro Original: {id(original[0][1])}")
    print(f"ID habilidades Pedro Shallow: {id(shallow[0][1])}")
    print(f"ID habilidades Pedro Deep: {id(deep[0][1])}")


def main():
    # Paso 1: Crear la lista original
    print("\n🔹 Creando lista original de empleados...")
    empleados = [
        ["Pedro", ["Python", "SQL"]],
        ["Manolo", ["Java", "C++", "JavaScript"]],
        ["Alejandro", ["HTML", "CSS", "JavaScript"]]
    ]

    # Paso 2: Crear copias superficial y profunda
    print("🔹 Creando copias superficial y profunda...")
    empleados_shallow = empleados.copy()  # Copia superficial
    empleados_deep = copy.deepcopy(empleados)  # Copia profunda

    # Mostrar estado inicial
    mostrar_estado(empleados, empleados_shallow,
                   empleados_deep, "1: Estado Inicial")

    # Paso 3: Modificar la lista de habilidades de Pedro en la lista original
    print("\n🔹 Modificando habilidades de Pedro en la lista original...")
    empleados[0][1].append("Docker")

    # Mostrar estado después de la modificación
    mostrar_estado(empleados, empleados_shallow, empleados_deep,
                   "2: Después de agregar 'Docker' a las habilidades de Pedro")

    # Paso 4: Modificar la lista completa de un empleado
    print("\n🔹 Reemplazando toda la lista de habilidades de Manolo...")
    empleados[1][1] = ["Go", "Rust"]

    # Mostrar estado después de la segunda modificación
    mostrar_estado(empleados, empleados_shallow, empleados_deep,
                   "3: Después de reemplazar las habilidades de Manolo")

    # Explicación final
    print("\n📝 Conclusiones:")
    print("""
1. Shallow Copy (.copy()):
   - Crea una nueva lista de primer nivel
   - Mantiene referencias a los objetos internos (listas de habilidades)
   - Por eso los cambios en las habilidades se reflejan en la copia superficial

2. Deep Copy (deepcopy()):
   - Crea copias nuevas de todos los niveles de objetos
   - Las modificaciones en la lista original no afectan a la copia profunda
   - Es útil cuando necesitamos una copia completamente independiente

3. Comportamiento con modificaciones:
   - Modificar elementos internos (append): afecta a original y shallow copy
   - Reemplazar listas completas: solo afecta a la lista donde se hace el cambio
    """)


if __name__ == "__main__":
    main()
