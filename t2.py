import random
"""  
UNIVERSIDAD DE LA COSTA CUC 
FUNDAMENTOS ALGORÍTMICOS 
TALLER DE ALGORITMOS CONDICIONALES 
PROFESOR: Msc. ROBERTO MORALES  

"""
"""los ejercicios estan comentados para que sea mas facil ejecutar uno por uno"""


"""1. Hacer  un  algoritmo  que  calcule  el  total  a  pagar  por  la  compra  de 
camisas.  Si  se  compran  tres  camisas  o  mas  se  aplica  un  descuento 
del  30%  sobre  el  total  de  la  compra  y  si  son  menos  de  tres  camisas 
un descuento del 10%."""
"""print("el precio de las camisas es de 10000")
camisa=int(input("ingrese cuantas camisas desea comprar "))
total=0
if (camisa>=3):
    total=(camisa*10000)-((camisa*10000)*0.3)
    print("el precio total a pagar es de: ", total)
if(camisa<3):
    total=(camisa*10000)-((camisa*10000)*0.1)
    print("el precio total a pagar es de: ", total)"""

"""2. En  un  supermercado  se  hace  una  promoción,  mediante  la  cual  el 
cliente  obtiene  un  descuento  dependiendo  de  un  número  que  se 
escoge al azar. Si el número escogido es menor que 74 el descuento 
es  del  15%  sobre  el  total  de  la  compra,  si  es  mayor  o  igual  a  74  el 
descuento es del 20%. Obtener cuanto dinero se le descuenta. """

"""compra=int(input("ingrese el valor de la compra "))
azar=random.randint(0,100)
print("esto es azar ",azar)
if (azar<74):
    print("el descuento es de: ", (compra*0.15))
if (azar>=74):
    print("el descuento es de: ", (compra*0.20))"""

"""3. Una compañía de seguros está abriendo un departamento de 
finanzas  y  estableció  un  programa  para  captar  clientes,  que  conssite 
en lo siguiente: Si el monto por el que se efectúa la fianza es menor 
que $50.000 la cuota a pagar será por el 3% del monto, y si el monto 
es  mayor  que  $50.000  la  cuota  a  pagar  será  el  2%  del  monto.  La 
afianzadora  desea  determinar  cual  será  la  cuota  que  debe  pagar  al 
cliente."""
"""
fianza=int(input("ingrese el valor de la fianza "))

if (fianza<50000):
    print("la  cuota  que  debe  pagar  al cliente es de: ", (fianza*0.3))
if (fianza>=50000):
    print("la  cuota  que  debe  pagar  al cliente es de: ", (fianza*0.2))"""