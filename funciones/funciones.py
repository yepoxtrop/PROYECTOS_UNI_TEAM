def codigoProducto(opciones):
    if opciones == 1:
        return 1;  
    elif opciones == 2:
        return 2; 
    elif opciones == 3:
        return 3;  
    elif opciones == 4:
        return 4; 
    else:
        print("ALERTA: Eres hacker bro, no deberias de estar aqui"); 
    
def arregloProducto(codigo, nombre, cantidad, precio, descuento):
    subtotal = cantidad * precio; 
    total = subtotal - descuento;    
    return [codigo, nombre, cantidad, precio, descuento, subtotal, total]; 

def encontrarDatosProducto(codigo,ventas):
    contadorProductos = 0;
    productos = []
    texto = ""
    for i in range(0,len(ventas),1):
        if ventas[i][0] == codigo:
            contadorProductos += 1;
            productos.append(f"Nombre: {ventas[i][1]} | Cantidad: {ventas[i][2]} | Total: {ventas[i][6]}"); 
    
    if contadorProductos == 0:
        productos.append("No hay productos en esta cateogoria"); 
    
    for i in range(0,len(productos),1):
        texto += productos[i] + "\n";
    
    return texto; 

def contadorTotalProductos(ventas):
    gafas = 0;
    relojes = 0;
    accesorios = 0;
    otrosProd = 0;
    
    for i in range(0,len(ventas),1):
        if ventas[i][0] == 1:
            gafas += 1;
        elif ventas[i][0] == 2:
            relojes += 1;
        elif ventas[i][0] == 3:
            accesorios += 1;
        elif ventas[i][0] == 4:
            otrosProd += 1;
        else:
            print("ALERTA: Eres hacker bro, no deberias de estar aqui"); 
    
    return f"1.Gafas:{gafas} \n2.Relojes:{relojes} \n3.Accesorios:{accesorios} \n4.Otros:{otrosProd}"; 
        
    # totalProductos.append(contadorProductos); 
    # contadorProductos = 0;
    
def contadorTotalDinero(ventas):
    gafas = 0;
    relojes = 0;
    accesorios = 0;
    otrosProd = 0;
    total = 0; 
    
    for i in range(0,len(ventas),1):
        if ventas[i][0] == 1:
            gafas += ventas[i][6]; 
        elif ventas[i][0] == 2:
            relojes += ventas[i][6]; 
        elif ventas[i][0] == 3:
            accesorios += ventas[i][6]; 
        elif ventas[i][0] == 4:
            otrosProd += ventas[i][6]; 
        else:
            print("ALERTA: Eres hacker bro, no deberias de estar aqui");
    
    total = gafas + relojes + accesorios + otrosProd; 
    
    return f"1.Gafas:{gafas}COP \n 2.Relojes:{relojes}COP \n 3.Accesorios:{accesorios}COP \n 4.Otros:{otrosProd}COP \n Total: {total}COP"; 