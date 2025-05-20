from funciones.funciones import *;
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
    codigo = codigoProducto(opciones); 
        
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
    
    datosProducto = arregloProducto(codigo, nombre, cantidad, precio, descuento); 
    
    #agregar diccionario a matriz
    ventas.append(datosProducto); 
        
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

#segundo ciclo principal
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
        gafas = encontrarDatosProducto(1, ventas); 
        print(gafas); 

        print("\n°RELOJES"); 
        relojes = encontrarDatosProducto(2, ventas); 
        print(relojes); 
                
        print("\n°ACCESORIOS PARA CELULAR"); 
        accesorios = encontrarDatosProducto(3, ventas); 
        print(accesorios); 

        print("\n°OTROS PRODUCTOS"); 
        otrosProd = encontrarDatosProducto(4, ventas); 
        print(otrosProd); 
        
        print("\n°CONTADOR TOTAL"); 
        listado1 = contadorTotalProductos(ventas); 
        print(listado1); 

    elif opciones2 == 2: 

        listado2 = contadorTotalDinero(ventas); 
        print(listado2);  
        
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