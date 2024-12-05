def origen_y_destino():
    origen = input("Ingrese su punto de origen ('Miami', 'Florida' o 'Texas'): ").capitalize()
    destino = input("Ingrese su destino ('Miami', 'Florida' o 'Texas'): ").capitalize()
    return origen, destino


def mostrar_vuelos(origen, destino):
    vuelos_disponibles = {
        "Miami": [("9:00am", "#MK4143"), ("3:30pm", "#ML8452"), ("7:20pm", "#MA0745")],
        "Florida": [("8:00am", "#FS6432"), ("5:30pm", "#FV1412"), ("11:10pm", "#FB2352")],
        "Texas": [("7:00am", "#TS9418"), ("2:00pm", "#TH7852"), ("6:30pm", "#TC4814")]
    }

    if origen not in vuelos_disponibles:
        print("Origen no válido.")
        return None

    print(f"Vuelos de {origen} a {destino}:")
    vuelos = vuelos_disponibles[origen]
    for i, (hora, codigo) in enumerate(vuelos, 1):
        print(f"Vuelo {i}: {origen} - {destino} {hora} - {codigo}")
    return vuelos


def seleccionar_vuelo(vuelos):
    while True:
        try:
            seleccion = int(input("Seleccione el número de vuelo (1, 2 o 3): "))
            if 1 <= seleccion <= len(vuelos):
                return seleccion - 1
            else:
                print("Número inválido. Intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Ingrese un número entre 1 y 3.")


def solicitar_datos_vuelo():
    asiento = input("Seleccione su asiento (Ejemplo: A12): ")
    fecha = input("Ingrese la fecha de su vuelo (DD/MM/AAAA): ")
    return asiento, fecha


def mostrar_reservacion(vuelo, asiento, fecha, origen, destino):
    costos = {"Miami": [421, 356, 112], "Florida": [226, 181, 352], "Texas": [163, 257, 382]}
    costo = costos[origen][vuelo]
    print(f"\nDetalles de la reservación:\nVuelo: {origen} - {destino}, Asiento: {asiento}, Fecha: {fecha}")
    print(f"Costo: ${costo}")
    return costo


def confirmar_reservacion():
    while True:
        confirmar = input("¿Desea confirmar su reservación? (Si/No): ").capitalize()
        if confirmar in ("Si", "No"):
            return confirmar == "Si"
        print("Respuesta no válida. Responda 'Si' o 'No'.")


def solicitar_datos_pago():
    print("---- DATOS DE PAGO ----")
    nombre = input("Ingrese el titular de la tarjeta: ")
    tarjeta = input("Ingrese los números de la tarjeta: ")
    vencimiento = input("Ingrese la fecha de vencimiento (MM/AA): ")
    codigo = input("Ingrese el código de seguridad: ")
    return nombre, tarjeta, vencimiento, codigo


def generar_factura(nombre, costo, vuelo, asiento, fecha, origen, destino):
    factura = (
        f"\nFactura para {nombre}\nMonto: ${costo:.2f}\nVuelo: {origen} - {destino}\n"
        f"Asiento: {asiento}\nFecha: {fecha}\n¡Gracias por su compra!"
    )
    print(factura)


def atencion_cliente():
    respuesta = input("¿Desea ingresar al servicio de atención al cliente? (Si/No): ").capitalize()
    if respuesta == "Si":
        print("\nElija una opción de contacto:")
        print("1. Llamar al 123-456-789")
        print("2. Enviar un correo a soporte@aerolinea.com")
        opcion = input("Ingrese el número de la opción: ")
        if opcion == "1":
            print("Está en la cola de espera. Un representante se comunicará pronto.")
        elif opcion == "2":
            consulta = input("Escriba su consulta: ")
            print("Gracias. Le contactaremos pronto.")
        else:
            print("Opción no válida.")
    elif respuesta == "No":
        print("Gracias por preferirnos.")
    else:
        print("Respuesta no válida.")


def aviones_y_tripulaciones():
    aviones = ["Avianca", "Boeing", "DHL"]
    tripulaciones = [
        "1 Capitán, 1 copiloto y 2 aeromozas",
        "1 Capitán, 1 copiloto y 3 aeromozas",
        "1 Capitán, 1 copiloto y 1 aeromoza"
    ]
    print("Aviones y Tripulaciones:")
    for avion, tripulacion in zip(aviones, tripulaciones):
        print(f"{avion}: {tripulacion}")


def mantenimiento():
    aviones_y_tripulaciones()
    avion = input("Escriba el nombre del avión para programar mantenimiento: ")
    if avion in ["Avianca", "Boeing", "DHL"]:
        print(f"Mantenimiento programado para el {avion}.")
    else:
        print("Avión no encontrado.")


def menu_mantenimiento():
    while True:
        print("\nMenú de Mantenimiento:")
        print("1. Mostrar aviones y tripulaciones")
        print("2. Programar mantenimiento")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            aviones_y_tripulaciones()
        elif opcion == "2":
            mantenimiento()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")


def main():
    print("Bienvenido a Aerolíneas Recope!")
    print("Contamos con viajes a Miami, Florida y Texas.")
    
    tipo_usuario = input("Si eres técnico, presiona 2; si eres usuario de vuelo, presiona 1: ")

    if tipo_usuario == "1":
        origen, destino = origen_y_destino()
        vuelos = mostrar_vuelos(origen, destino)
        
        if vuelos:
            vuelo_seleccionado = seleccionar_vuelo(vuelos)
            asiento, fecha = solicitar_datos_vuelo()
            costo = mostrar_reservacion(vuelo_seleccionado, asiento, fecha, origen, destino)

            if confirmar_reservacion():
                nombre, tarjeta, vencimiento, codigo = solicitar_datos_pago()
                generar_factura(nombre, costo, vuelo_seleccionado, asiento, fecha, origen, destino)
                print("¡Pago confirmado! Gracias por su compra.")
            else:
                print("Reservación cancelada.")
        
        atencion_cliente()

    elif tipo_usuario == "2":
        menu_mantenimiento()
    else:
        print("Opción no válida. Reinicie el programa.")


if __name__ == "__main__":
    main()
