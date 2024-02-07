import Actions.tools as tool

while True:
    print("------ MENU ------")
    print("1. Agregar venta")
    print("2. Modificar venta")
    print("3. Listar ventas por compañía")
    print("4. Salir")
    
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        tool.agregar_venta()
    elif opcion == 2:
        tool.modificar_venta()
    elif opcion == 3:
        tool.listar_ventas()
    elif opcion == 4:
        break
    else:
        print("Opción inválida. Intente nuevamente.")