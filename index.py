#mensaje de bienvenida
print("BIENVENIDO AL SISTEMA DE GESTION 'EL COSTA' "); 
print("\nREGISTRAR VENTAS DE PRODUCTOS")

#definicion de array y variables globales
procesos = True; 
procesos2 = True; 
productos = 0; 
contadorProductos = 0; 
contadorDinero = 0; 
ventas = []; 
totalProductos = []
totalDinero = []

#primera parte
#primer bucle principal
while procesos == True:

    #opciones
    print("\n////////////////\nOPCIONES DISPONIBLES:"); 
    print("1.Agregar gafas."); 
    print("2.Agregar relojes."); 
    print("3.Agregar accesorios para celular."); 
    print("4.Agregar otros productos."); 
    
    opciones = int(input("\n→Ingrese una de las opciones:")); 
    while opciones <1 or opciones >4:
        print("\nALERTA: Opcion no valida"); 
        print("\n////////////////\nOPCIONES DISPONIBLES:"); 
        print("1.Agregar gafas."); 
        print("2.Agregar relojes."); 
        print("3.Agregar accesorios para celular."); 
        print("4.Agregar otros productos."); 
        opciones = int(input("\n→Ingrese una de las opciones:")); 

    #Asignacion de id para tipo de producto    
    if opciones == 1:
        codigo = 1;  
    elif opciones == 2:
        codigo = 2; 
    elif opciones == 3:
        codigo = 3; 
    elif opciones == 4:
        codigo = 4;        
    else:
        print("ALERTA: Eres hacker bro, no deberias de estar aqui"); 
        
    #assignacion de valores por producto
    nombre = input("\n→Ingrese el nombre del producto:");         
    cantidad = int(input("\n→Ingrese la unidades vendidas del producto:")); 
    precio = float(input("\n→Ingrese el precio unitario del articulo:")); 
    descuento = float(input("\n→Ingrese el descuentot total de la factura:")); 
        
    while cantidad <=0 or precio <=0 or descuento <0:
        print("\nALERTA: Uno de los valores ingresados no es valido"); 
        cantidad = int(input("\n→Ingrese la unidades vendidas del producto:")); 
        precio = float(input("\n→Ingrese el precio unitario del articulo:")); 
        descuento = float(input("\n→Ingrese el descuentot total de la factura:")); 
            
    subtotal = cantidad * precio; 
    total = subtotal - descuento;    
            
    #agregar diccionario a matriz
    ventas.append([codigo, nombre, cantidad, precio, descuento, subtotal, total]); 
        
    #continuar agregando producto o no  
    respuesta = input("\n¿DESEAS INGRESAR OTRO PRODUCTO? \n→S[si] | N[no]:"); 
    while respuesta.lower() != "s" and respuesta.lower() != "si" and respuesta.lower() != "n" and respuesta.lower() != "no":
        print("ALERTA: Opcion no valida"); 
        respuesta = input("\n¿DESEAS INGRESAR OTRO PRODUCTO? \n→S[si] | N[no]:"); 
    
    #condicional que cierra el primer bucle principal
    if respuesta.lower() == "s" or respuesta.lower() == "si":
        procesos = True; 
    else:
        print("ALERTA: Ya no se peuden ingresar mas productos"); 
        procesos = False;    

#segunda parte
print("\n////////////////\nCALCULOS"); 

#segundo condicional principal
while procesos2 == True:

    #menu de opciones
    print("\nPuedes realizar los siguientes calculos:"); 
    print("1.Listado de productos por categoria."); 
    print("2.Total de dinero por categoria."); 
    print("3.Total de dinero en descuento."); 
    print("4.No realizar ningun calculo"); 
    opciones2 = int(input("\n→Ingrese una de las opciones:")); 
    
    #bucle por si no selecciona una opcion disponible
    while opciones2 <1 or opciones2 >4:
        print("\nALERTA: Opcion no valida"); 
        print("\nPuedes realizar los siguientes calculos:"); 
        print("1.Listado de productos por categoria."); 
        print("2.Total de dinero por categoria."); 
        print("3.Total de dinero en descuento."); 
        print("4.No realizar ningun calculo"); 
        opciones2 = int(input("\n→Ingrese una de las opciones:")); 
    
    #operaciones segun cada opcion
    if opciones2 == 1:

        #se muestran todos lo producto por categoria
        print("\n°GAFAS"); 
        for i in range(0,len(ventas),1):
            if ventas[i][0] == 1:
                print(f"Nombre: {ventas[i][1]} | Cantidad: {ventas[i][2]} | Total: {ventas[i][6]}"); 
                contadorProductos += 1; 
        if contadorProductos == 0:
            print("No hay productos en esta cateogoria")
        totalProductos.append(contadorProductos); 
        contadorProductos = 0; 

        print("\n°RELOJES"); 
        for i in range(0,len(ventas),1):
            if ventas[i][0] == 2:
                print(f"Nombre: {ventas[i][1]} | Cantidad: {ventas[i][2]} | Total: {ventas[i][6]}"); 
                contadorProductos += 1; 
        if contadorProductos == 0:
            print("No hay productos en esta cateogoria")
        totalProductos.append(contadorProductos); 
        contadorProductos = 0; 
                
        print("\n°ACCESORIOS PARA CELULAR"); 
        for i in range(0,len(ventas),1):
            if ventas[i][0] == 3:
                print(f"Nombre: {ventas[i][1]} | Cantidad: {ventas[i][2]} | Total: {ventas[i][6]}"); 
                contadorProductos += 1; 
        if contadorProductos == 0:
            print("No hay productos en esta cateogoria")
        totalProductos.append(contadorProductos); 
        contadorProductos = 0; 

        print("\n°OTROS PRODUCTOS"); 
        for i in range(0,len(ventas),1):
            if ventas[i][0] == 4:
                print(f"Nombre: {ventas[i][1]} | Cantidad: {ventas[i][2]} | Total: {ventas[i][6]}"); 
                contadorProductos += 1; 
        if contadorProductos == 0:
            print("No hay productos en esta cateogoria")
        totalProductos.append(contadorProductos); 
        contadorProductos = 0; 
    
        print("\n°CONTADOR TOTAL"); 
        print(f"1.Gafas:{totalProductos[0]}"); 
        print(f"1.Relojes:{totalProductos[1]}"); 
        print(f"1.Accesorios:{totalProductos[2]}"); 
        print(f"1.Otros:{totalProductos[3]}"); 

    elif opciones2 == 2: 

        #se muestra el total de dinero por categoria y su sumatoria
        for i in range(0,len(ventas),1):
            if ventas[i][0] == 1:
                contadorDinero = contadorDinero + ventas[i][6]; 
        print(f"\n°Gafas:{contadorDinero} COP"); 
        totalDinero.append(contadorDinero); 
        contadorDinero = 0; 
        
        for i in range(0,len(ventas),1): 
            if ventas[i][0] == 2:
                contadorDinero = contadorDinero + ventas[i][6]; 
        print(f"°Relojes:{contadorDinero}COP"); 
        totalDinero.append(contadorDinero); 
        contadorDinero = 0; 

        for i in range(0,len(ventas),1):
            if ventas[i][0] == 3:
                contadorDinero = contadorDinero + ventas[i][6]; 
        print(f"°Accesorios para celular:{contadorDinero}COP"); 
        totalDinero.append(contadorDinero); 
        contadorDinero = 0; 

        for i in range(0,len(ventas),1):
            if ventas[i][0] == 4:
                contadorDinero = contadorDinero + ventas[i][6]; 
        print(f"°Otros:{contadorDinero}COP"); 
        totalDinero.append(contadorDinero); 
        contadorDinero = 0; 

        print(f"\n°Total de dinero:{totalDinero[0]+totalDinero[1]+totalDinero[2]+totalDinero[3]} COP"); 
        
    elif opciones2 == 3:

        #se muestra en su totalidad el dinero de los descuentos
        suma_descuento = 0; 
        
        for i in range(0, len(ventas),1):
            suma_descuento = suma_descuento + ventas[i][4]; 
        print(f"\nTotal de dinero en descuento: {suma_descuento}COP"); 
        suma_descuento = 0; 

    elif opciones2 == 4:

        #finaliza el segundo bucle principal
        procesos2 = False; 
    else:
        print("ALERTA: Eres hacker bro, no deberias de estar aqui"); 