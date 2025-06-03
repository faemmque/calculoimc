

while True:
    # Se capturan los datos de la persona
    nombre = input("Escriba su nombre(s) por favor: ")
    ap_paterno = input("Escriba su apellido paterno: ")
    ap_materno = input("Escriba su apellido materno: ")
    edad = input("Escriba su edad: ")
    peso = input("Escriba su peso (kg): ")
    estatura = input("Escriba su estatura (m): ")

    # Validacion de los campos
    if not nombre:
        print("\nEl campo nombre no puede quedar vacio.\n")
    elif not ap_paterno:
        print("\nEl campo apellido paterno no puede quedar vacio.\n")
    elif not ap_materno:
        print("\nEl campo apellido materno no puede quedar vacio.\n")
    elif not edad or not edad.isdigit():
        print("\nEl campo edad no es valido.\n")
    elif not peso or not peso.strip().replace(".","").isdigit():
        print("\nEl campo edad no es valido.\n")
    elif not estatura or not estatura.strip().replace(".","").isdigit():
        print("\nEl campo edad no es valido.\n")
    else:
        # Se calcula el IMC
        imc = float(peso) / (float(estatura) ** 2)
        
        # Se imprimen en pantalla los datos capturados junto con el calculo del IMC
        print("\nHola {0} {1} {2}, a tu edad de {3} años tu Índice de Masa Corporal (IMC) es de : {4:.2f}".format(nombre,ap_paterno,ap_materno,edad,imc))
        print("El IMC se te calculó de la siguiente manera:")
        print("IMC = {0} kg / ({1} m * {1} m) = {2:.2f} \n".format(peso,estatura,imc))
        break
    
    print("Intentemos de nuevo")
