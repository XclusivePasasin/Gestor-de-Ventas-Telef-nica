ventas = []

def agregar_venta():
    numero_telefonico = input("Número telefónico: ")
    nombre_compania = input("Nombre de la compañía Telefónica: ")
    modelo = input("Modelo del teléfono: ")
    propietario = input("Nombre del propietario: ")
    direccion = input("Dirección del propietario: ")
    tipo_pago = input("Tipo de pago mensual (prepago/pospago): ")
    if tipo_pago == "prepago":
        pago_mensual = "$0.00"
    else:
        pago_mensual = "$25.00"
    venta = {
        "numero_telefonico": numero_telefonico,
        "nombre_compania": nombre_compania,
        "modelo": modelo,
        "propietario": propietario,
        "direccion": direccion,
        "tipo_pago": tipo_pago,
        "pago_mensual": pago_mensual
    }
    ventas.append(venta)
    print("Venta agregada con éxito.")
def modificar_venta():
    numero_telefonico = input("Número telefónico de la venta a modificar: ")
    for venta in ventas:
        if venta["numero_telefonico"] == numero_telefonico:
            nombre_compania = input("Nuevo nombre de la compañía Telefónica: ")
            modelo = input("Nuevo modelo del teléfono: ")
            propietario = input("Nuevo nombre del propietario: ")
            direccion = input("Nueva dirección del propietario: ")
            tipo_pago = input("Nuevo tipo de pago mensual (prepago/pospago): ")
            if tipo_pago == "prepago":
                pago_mensual = "$0.00"
            else:
                pago_mensual = "$25.00"
            venta["nombre_compania"] = nombre_compania
            venta["modelo"] = modelo
            venta["propietario"] = propietario
            venta["direccion"] = direccion
            venta["tipo_pago"] = tipo_pago
            venta["pago_mensual"] = pago_mensual
            print("Venta modificada con éxito.")
            return
    print("No se encontró una venta con ese número telefónico.")
def listar_ventas():
    nombre_compania = input("Nombre de la compañía Telefónica: ")
    ventas_filtradas = [venta for venta in ventas if venta["nombre_compania"] == nombre_compania]
    ventas_ordenadas = sorted(ventas_filtradas, key=lambda venta: venta["propietario"])
    if len(ventas_ordenadas) > 0:
        for venta in ventas_ordenadas:
            print('\n============================================')
            print("Número telefónico:", venta["numero_telefonico"])
            print("Nombre de la compañía Telefónica:", venta["nombre_compania"])
            print("Modelo del teléfono:", venta["modelo"])
            print("Nombre del propietario:", venta["propietario"])
            print("Dirección del propietario:", venta["direccion"])
            print("Tipo de pago mensual:", venta["tipo_pago"])
            print('============================================')
    else:
        print("No se encontraron ventas para esa compañía.")