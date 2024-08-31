Datos = {
    "Alumnos": []
}

def mostrar_datos(datos):
    if not datos["Alumnos"]:
        print("No se registró ningun alumno")
        return

    i = 1
    for alumno in datos["Alumnos"]:
        print(f"\nAlumno {i}:")
        for clave, valor in alumno.items():
            print(f"  {clave}: {valor}")
        i += 1

def agregar_alumno(datos):
    nombre = input("Nombre del alumno: ")
    apellido = input("Apellido del alumno: ")
    dni = input("DNI: ")
    fecha_nacimiento = input("Fecha de nacimiento (DD/MM/AAAA): ")
    tutor = input("Nombre del tutor: ")
    

    notas = input("Notas del alumno (separadas por comas): ").split(',')
    notas = [float(nota.strip()) for nota in notas]
    
    faltas = int(input("Faltas: "))
    amonestaciones = int(input("amonestaciones: "))

    alumno = {
        "Nombre": nombre,
        "Apellido": apellido,
        "DNI": dni,
        "Fecha de nacimiento": fecha_nacimiento,
        "Tutor": tutor,
        "Notas": notas,
        "Faltas": faltas,
        "Amonestaciones": amonestaciones
    }

    datos["Alumnos"].append(alumno)
    print("Alumno agregado")

def modificar_datos(datos):
    dni = input("DNI del alumno a modificar: ")
    alumno = None
    for a in datos["Alumnos"]:
        if a["DNI"] == dni:
            alumno = a
            break

    if alumno is None:
        print("Alumno no encontrado.")
        return

    print("Datos actuales del alumno:")
    for clave, valor in alumno.items():
        print(f"  {clave}: {valor}")

    print("Ingrese los nuevos datos:")

    nuevo_nombre = input(f"Nuevo Nombre (actual: {alumno['Nombre']}): ")
    if nuevo_nombre:
        alumno["Nombre"] = nuevo_nombre

    nuevo_apellido = input(f"Nuevo Apellido (actual: {alumno['Apellido']}): ")
    if nuevo_apellido:
        alumno["Apellido"] = nuevo_apellido

    nuevo_dni = input(f"Nuevo DNI (actual: {alumno['DNI']}): ")
    if nuevo_dni:
        alumno["DNI"] = nuevo_dni

    nueva_fecha_nacimiento = input(f"Fecha de nacimiento (actual: {alumno['Fecha de nacimiento']}): ")
    if nueva_fecha_nacimiento:
        alumno["Fecha de nacimiento"] = nueva_fecha_nacimiento

    nuevo_tutor = input(f"Nombre y apellido del tutor (actual: {alumno['Tutor']}): ")
    if nuevo_tutor:
        alumno["Tutor"] = nuevo_tutor

    nueva_nota = input(f"Notas (actual: {alumno['Notas']}): ")
    if nueva_nota:
        notas = nueva_nota.split(',')
        notas = [float(nota.strip()) for nota in notas]
        alumno["Notas"] = notas

    nuevas_faltas = input(f"Cantidad de faltas (actual: {alumno['Faltas']}): ")
    if nuevas_faltas:
        alumno["Faltas"] = int(nuevas_faltas)

    nuevas_amonestaciones = input(f"Cantidad de amonestaciones (actual: {alumno['Amonestaciones']}): ")
    if nuevas_amonestaciones:
        alumno["Amonestaciones"] = int(nuevas_amonestaciones)

    print("Datos del alumno modificados")

def expulsar_alumno(datos):
    dni = input("DNI del alumno a expulsar: ")
    nueva_lista = []
    for alumno in datos["Alumnos"]:
        if alumno["DNI"] != dni:
            nueva_lista.append(alumno)
    datos["Alumnos"] = nueva_lista
    print("Alumno expulsado exitosamente.")

def menu():
    while True:
        print("\nGestión de Datos de Alumnos")
        print("1. Mostrar datos de los alumnos")
        print("2. Agregar un nuevo alumno")
        print("3. Modificar datos de un alumno")
        print("4. Expulsar un alumno")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_datos(Datos)
        elif opcion == "2":
            agregar_alumno(Datos)
        elif opcion == "3":
            modificar_datos(Datos)
        elif opcion == "4":
            expulsar_alumno(Datos)
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

menu()


