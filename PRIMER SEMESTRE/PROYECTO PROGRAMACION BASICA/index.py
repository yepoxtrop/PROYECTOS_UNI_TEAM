print("BIENVENIDO AL SISTEMA DE GESTION \nEL COSTA"); 

print("\nREGISTRAR VENTAS DE PRODUCTOS")
procesos = True; 
procesos2 = True; 
productos = 0; 
ventas = {}; 

while procesos == True:
    print("\n→Ingrese una de las opciones:"); 
    print("1. Agregar gafas."); 
    print("2. Agregar relojes."); 
    print("3. Agregar accesorios para celular."); 
    print("4. Agregar otros productos."); 
    
    opciones = int(input("\n→Ingrese una de las opciones: ")); 
    while opciones <1 or opciones >4:
        print("\nALERTA: Opcion no valida"); 
        print("\nIngrese una de las opciones:"); 
        print("1. Agregar gafas."); 
        print("2. Agregar relojes."); 
        print("3. Agregar accesorios para celular."); 
        print("4. Agregar otros productos."); 
        opciones = int(input("\nEscoja alguna de las opciones: ")); 
        
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
        
        #
        nombre = input("\nIngrese el nombre del producto:");     
        
        cantidad = int(input("\nIngrese la unidades vendidas del producto:")); 
        precio = float(input("\nIngrese el precio unitario del articulo:")); 
        descuento = float(input("\nIngrese el descuentot total de la factura:")); 
        
        while cantidad <=0 or precio <=0 or descuento <=0:
            print("\nALERTA: Uno de los valores ingresados no es valido"); 
            cantidad = int(input("\nIngrese la unidades vendidas del producto:")); 
            precio = float(input("\nIngrese el precio unitario del articulo:")); 
            descuento = float(input("\nIngrese el descuentot total de la factura:"));      
            
        subtotal = cantidad * precio; 
        total = subtotal - descuento;    
            
        ventas.append({"Codigo": codigo, 
                        "Nombre":nombre, 
                       "Cantidad": cantidad, 
                       "Precio": precio, 
                       "Descuento": descuento, 
                       "Subtotal": subtotal, 
                       "Total": total
        }); 
        
        #  
        respuesta = input("\n¿DESEAS INGRESAR OTRO PRODUCTO? \nS[si] | N[no]:"); 
        while respuesta.lower() != "s" and respuesta.lower() != "si" and respuesta.lower() != "n" and respuesta.lower() != "no":
            print("ALERTA: Opcion no valida");
            respuesta = input("\n¿DESEAS INGRESAR OTRO PRODUCTO? \nS[si] | N[no]:"); 
        
        if respuesta.lower() == "s" or respuesta.lower() == "si":
            procesos = True; 
        else:
            print("ALERTA: Ya no se peuden ingresar mas productos"); 
            procesos = False;    
            
print("\nCALCULOS"); 
print("\nPuedes realizar los siguientes calculos:"); 

while procesos2 == True:
    print("1.Listado de productos por categoria."); 
    print("2.Total de dinero por categoria."); 
    print("3.Total de dinero en descuento."); 
    print("4.No realizar ningun calculo"); 
    opciones2 = int(input("\nIngrese una de las opciones: ")); 
    
    while opciones2 <1 or opciones2 >4:
        print("\nALERTA: Opcion no valida"); 
        print("\nPuedes realizar los siguientes calculos:"); 
        print("1.Listado de productos por categoria."); 
        print("2.Total de dinero por categoria."); 
        print("3.Total de dinero en descuento."); 
        print("4.No realizar ningun calculo"); 
        opciones2 = int(input("\nIngrese una de las opciones: ")); 
        
    if opciones2 == 1:
        print("\nGAFAS"); 
        for i in ventas:
            if i["Codigo"] == 1:
                print(f"Nombre: {i["Nombre"]} | Cantidad: {i["Cantidad"]} | Total: {i["Total"]}"); 
                
        print("\nRELOJES"); 
        for i in ventas:
            if i["Codigo"] == 2:
                print(f"Nombre: {i["Nombre"]} | Cantidad: {i["Cantidad"]} | Total: {i["Total"]}"); 
                
        print("\nACCESORIOS PARA CELULAR"); 
        for i in ventas:
            if i["Codigo"] == 3:
                print(f"Nombre: {i["Nombre"]} | Cantidad: {i["Cantidad"]} | Total: {i["Total"]}"); 
                
        print("\nOTROS PRODUCTOS"); 
        for i in ventas:
            if i["Codigo"] == 4:
                print(f"Nombre: {i["Nombre"]} | Cantidad: {i["Cantidad"]} | Total: {i["Total"]}"); 
                
    elif opciones2 == 2: 
        total_gafas = 0;
        for i in ventas:
            if i["Codigo"] == 1:
                total_gafas = i["Total"] + total_gafas; 
        print(f"\nGafas:{total_gafas}COP"); 
        
        total_relojes = 0;
        for i in ventas:
            if i["Codigo"] == 2:
                total_relojes = i["Total"] + total_relojes; 
        print(f"\nRelojes:{total_relojes}COP"); 
                
        total_accesorios = 0;
        for i in ventas:
            if i["Codigo"] == 3:
                total_accesorios = i["Total"] + total_accesorios; 
        print(f"\nAccesorios para celular:{total_accesorios}COP"); 
        
        total_otros = 0;
        for i in ventas:
            if i["Codigo"] == 4:
                total_otros = i["Total"] + total_otros;
        print(f"\nOtros:{total_otros}COP"); 
        
        print(f"\nTotal de dinero:{total_gafas+total_relojes+total_accesorios+total_otros}COP"); 
        
        total_gafas = 0;
        total_relojes = 0;
        total_accesorios = 0;
        total_otros = 0; 
        
    elif opciones2 == 3:
        suma_descuento = 0;
        
        for i in ventas:
            suma_descuento = suma_descuento + i["Descuento"]; 
        
        print(f"\nTotal de dinero en descuento: {suma_descuento}COP"); 
        
    elif opciones2 == 4:
        break;
    else:
        print("ALERTA: Eres hacker bro, no deberias de estar aqui"); 
        
    