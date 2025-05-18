Algoritmo SISTEMADECALCULOS
	Definir indice, contadorArray, MAX, opciones, opciones2 Como Entero;
	Definir producto Como Entero
    Definir cantidad, precio, subtotal, descuento, total Como Entero
	Definir procesos, procesos2 Como Logico;
	Definir decision, nombre como Caracter;
	Definir count1, count2, count3, count4 Como Entero;
	Definir SumTotal, SumDescuento Como Entero;
	
    producto = 0
	indice = 0;
	contadorArray = 0;
	procesos = Verdadero;
	procesos2 = Verdadero;
	
	count1=0;
	count2=0;
	count3=0;
	count4=0;
	SumTotal=0;
	SumDescuento=0;
	
    MAX<-1000;
	Dimension Nombres[MAX]
	//gafa1(nombre)
	
    Dimension Productos[MAX,7];
	//id, cantidades, precios, subtotal, descuento, total, categoria
	
	Escribir "BIENVENIDO AL SISTEMA DE GESTIÓN EL COSTA";
	Escribir "	";
	
	Mientras contadorArray < MAX y procesos == Verdadero Hacer
		producto = producto +1;
		
		//opciones de agregado de productos
		Escribir "	";
		Escribir "OPCIONES DISPONIBLES:";
        Escribir "1.Agregar gafas.";
        Escribir "2.Agregar relojes.";
        Escribir "3.Agregar accesorios para celular.";
        Escribir "4.Agregar otros productos.";
		Escribir "->Ingrese una de las opciones:";
		Leer opciones;
		
		Mientras opciones < 1 o opciones > 4 Hacer
			Escribir "	";
			Escribir "ALERTA:Valor no aceptado.";
			Escribir "	";
			Escribir "1.Agregar gafas.";
			Escribir "2.Agregar relojes.";
			Escribir "3.Agregar accesorios para celular.";
			Escribir "4.Agregar otros productos.";
			Escribir "->Ingrese una de las opciones:";
			Leer opciones;
		Fin Mientras
		
		Escribir "->Ingrese el nombre del articulo:";
		Leer nombre;
		Escribir "->Ingrese las unidaddes vendidas del producto:";
		Leer cantidad;
		Escribir "->Ingrese el precio unitario del articulo:";
		Leer precio;
		Escribir "->Ingrese el descuento total:";
		Leer descuento;
		
		Mientras cantidad<=0 o precio<=0 o descuento<0 Hacer
			Escribir "	";
			Escribir "ALERTA:Alguno de los valores numericos es menor a cero."
			Escribir "	";
			Escribir "Registra nuevamente los valores."
			Escribir "->Ingrese las unidaddes vendidas del producto:";
			Leer cantidad;
			Escribir "->Ingrese el precio unitario del articulo:";
			Leer precio;
			Escribir "->Ingrese el descuento total:";
			Leer descuento;
		Fin Mientras
		
		Nombres[producto] = nombre;
		Productos[producto, 1] = producto;
		Productos[producto, 2] = cantidad;
		Productos[producto, 3] = precio;
		Productos[producto, 4] = precio*cantidad;
		Productos[producto, 5] = descuento;
		Productos[producto, 6] = (precio*cantidad)-descuento;
		
		Segun opciones Hacer
			1:
				Productos[producto, 7] = 1;
			2:
				Productos[producto, 7] = 2;
			3:
				Productos[producto, 7] = 3;
			4:
				Productos[producto, 7] = 4;
			De Otro Modo:
				Escribir "Eres hacker bro, no deberias de llegar aqui";
		Fin Segun
		
		contadorArray = contadorArray +1;
		
		//Ingresar mas productos
		Si contadorArray < MAX Entonces
			Escribir "¿Deseas ingresar algún porducto?";
			Escribir "->S[si] | N[no]"
			Leer decision;
		Fin Si
		
		Mientras decision <> "S" Y decision <> "N" Y decision <> "s" Y decision <> "n" Hacer
			Escribir "	";
			Escribir "ALERTA:Valor no aceptado.";
			Escribir "	";
			Escribir "¿Deseas ingresar algún porducto?";
			Escribir "->S[si] | N[no]"
			Leer decision;
		Fin Mientras
		
		//condicional de proceso segun el valor de decision
		Si decision == "N" o decision == "n"  Entonces
			Escribir "MENSAJE:Ya no se ingresarán más productos."
			procesos = Falso;
		Fin Si
		
		
	Fin Mientras
	
	Escribir "	"
	Escribir "CALCULOS"
	
	Mientras procesos2 == Verdadero Hacer
		Escribir "	";
		Escribir "Puedes realizar los siguientes calculos:";
		Escribir "1.Listado de productos por categoria.";
		Escribir "2.Total de dinero por categoria.";
		Escribir "3.Total de dinero en descuento.";
		Escribir "4.No realizar ningun calculo";
		Leer opciones2;
		
		Mientras opciones2 <> 1 y opciones2 <> 2 y opciones2 <> 3 y opciones2 <> 4 Hacer
			Escribir "	";
			Escribir "ALERTA:Opción no disponible";
			Escribir "	";
			Escribir "Puedes realizar los siguientes calculos:";
			Escribir "1.Listado de productos por categoria.";
			Escribir "2.Total de dinero por categoria.";
			Escribir "3.Total de dinero en descuento.";
			Escribir "4.No realizar ningun calculo";
			Leer opciones2;
		Fin Mientras
		
		Segun opciones2 Hacer
			1:
				Escribir "///	GAFAS	///"
				Para x=1 Hasta MAX Con Paso 1 Hacer
					Si Productos[x,7] == 1 Entonces
						Escribir "Nombre:",Nombres[x];
						count1 = count1 +1;
					Fin Si
				Fin Para
				Escribir "";
				
				Escribir "///	RELOJES		///"
				Para x=1 Hasta MAX Con Paso 1 Hacer
					Si Productos[x,7] == 2 Entonces
						Escribir "Nombre:",Nombres[x];
						count2 = count2 +1;
					Fin Si
				Fin Para
				Escribir "";
				
				Escribir "///	ACCESORIOS PARA CELULAR		///"
				Para x=1 Hasta MAX Con Paso 1 Hacer
					Si Productos[x,7] == 3 Entonces
						Escribir "Nombre:",Nombres[x];
						count3 = count3 +1;
					Fin Si
				Fin Para
				Escribir "";
				
				Escribir "///	OTROS	///"
				Para x=1 Hasta MAX Con Paso 1 Hacer
					Si Productos[x,7] == 4 Entonces
						Escribir "Nombre:",Nombres[x];
						count4 = count4 +1;
					Fin Si
				Fin Para
				Escribir "";
				
				Escribir "///	CONTEO	///";
				Escribir "1.Gafas:", count1;
				Escribir "2.Relojes:", count2;
				Escribir "3.Accesorios para celular:", count3;
				Escribir "4.Otros:", count4;
				count1 = 0;
				count2 = 0;
				count3 = 0;
				count4 = 0;
				Escribir "";
			2:
				Escribir "///	TOTAL DE DINERO CONSEGUIDO	//";
				Para z=1 Hasta MAX Con Paso 1 Hacer
					SumTotal = SumTotal + Productos[z,6];
				Fin Para
				Escribir "Dinero Total:",SumTotal,"COP";
				Escribir "";
				SumTotal = 0;
				
				Para x=1 Hasta MAX Con Paso 1 Hacer
					Si Productos[x,7] == 1 Entonces
						count1 = count1 + Productos[x,6];
					Fin Si
				Fin Para
				
				Para x=1 Hasta MAX Con Paso 1 Hacer
					Si Productos[x,7] == 2 Entonces
						count2 = count2 + Productos[x,6];
					Fin Si
				Fin Para
				
				Para x=1 Hasta MAX Con Paso 1 Hacer
					Si Productos[x,7] == 3 Entonces
						count3 = count3 + Productos[x,6];
					Fin Si
				Fin Para
				
				Para x=1 Hasta MAX Con Paso 1 Hacer
					Si Productos[x,7] == 4 Entonces
						count4 = count4 + Productos[x,6];
					Fin Si
				Fin Para
				
				Escribir "///	CONTEO	///";
				Escribir "1.Gafas:", count1;
				Escribir "2.Relojes:", count2;
				Escribir "3.Accesorios para celular:", count3;
				Escribir "4.Otros:", count4;
				count1 = 0;
				count2 = 0;
				count3 = 0;
				count4 = 0;
				Escribir "";
			3:
				Escribir "///	TOTAL DE DESCUENTO	//";
				Para w=1 Hasta MAX Con Paso 1 Hacer
					SumDescuento = SumDescuento + Productos[w,5];
				Fin Para
				Escribir "Dinero Total:",SumDescuento,"COP";
				Escribir "";
				SumDescuento = 0;
			4:
				procesos2 = Falso;
			De Otro Modo:
				Escribir "Que haces aquí hijo mio?"
		Fin Segun
	Fin Mientras
	
FinAlgoritmo