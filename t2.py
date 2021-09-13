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

"""4. una fábrica ha sido sometida a un programa de control de 
contaminación  para  lo  cual  se  efectúa  una  revisión  de  los  puntos  de 
contaminación  generados  por  la  fábrica.  El  programa  de  control  de 
contaminación  consiste  en  medir  los  puntos  que  emite  la  fábrica  en 
cinco  días  de  una  semana  y  si  el  promedio  es  superior  a  los  170 
puntos  entonces  tendrá  la  sanción  de  parar  su  producción  por  una 
semana  y  una  multa  del  50%  de  las  ganancias  diarias  cuando  no  se 
detiene la producción. Si el promedio obtenido de puntos es de 170 o 
menos entonces no tendrá ni sanción ni multa. El dueño de la fábrica 
desea  saber  cuanto  dinero  perderá  después  de  ser  sometido  a  la 
revisión."""
"""
def promedio (a=[]):
    i=0
    promedioo=0
    for i in range(len(a)):
        promedioo+=a[i]
    promedioo=promedioo/len(a)
    return promedioo
ganancias=int(input("ingrese las ganancias por dia "))
lista=[]
i=0
for i in range(5):
    print("ingrese los puntos del dia: ", (i+1))
    lista.append(int(input()))
print("el promedio es de: ", promedio(lista))
if (promedio(lista)>170):
    print("el promedio excede los 170 por lo tanto la multa es de: ", (ganancias*5)*0.5)
if (promedio(lista)<=170):
    print("el promedio no excede los 170 por lo tanto no merece multa")"""

"""5. Una persona se encuentra con un problema de comprar un automóvil 
o  un  terreno,  los  cuales  cuestan  exactamente  lo  mismo.  Sabe  que 
mientras  el  automóvil  se  devalúa,  con  el  terreno  sucede  lo  contrario. 
Esta  persona  comprará  el  automóvil  si  al  cabo  de  tres  años  la 
devaluación  de  este  no  es  mayor  que  la  mitad  del  incremento  del valor  del  terreno.  Ayúdale  a  esta  pesona  a  determinar  si  debe  o  no 
comprar el automóvil. """
"""
precio=int(input("ingrese el precio del auto y del terreno "))
devaluación=int(input("ingrese cuanto se devalua el auto en 3 años "))
incremento=int(input("ingrese cuanto incrementa el precio del terreno cada 3 años "))
if (devaluación<=(incremento*0.5)):
    print("el hombre debe comprar el auto")
if (devaluación>(incremento*0.5)):
    print("el hombre debe comprar el terreno")"""

""" 6. En  una  fábrica  de  computadoras  se  planea  ofrecer  a  los  clientes  un 
descuento que dependerá del número de computadoreas que 
compre. Si las computadoras son menos de cinco se les dará un 10% 
de descuento sobre el total de la compra; si el número de 
computadoras  es  mayor  o  igual  a  cinco  pero  menos  de  diez  se  le 
otorga un 20% de descuento; y si son 10 o más se les da un 40%. El 
precio de cada computadora es de $11.000. """
"""
computadora=int(input("ingrese el numero de computadoras a comprar "))

if (computadora<5):
    print("el descuento es de: ", ((computadora*11000)*0.1), " y el valor total a pagar es: ", 11000-(computadora*0.1))
if (computadora>=5 and computadora<10):
    print("el descuento es de: ", ((computadora*11000)*0.2), " y el valor total a pagar es: ", 11000-(computadora*0.2))
if (computadora>=10):
    print("el descuento es de: ", ((computadora*11000)*0.4), " y el valor total a pagar es: ", 11000-(computadora*0.4))"""

"""7. Un  proveedor  de  estéreos  ofrece  un  descuento  del  10%  sobre  el 
precio sin IVA, de algún aparato si este cuesta $2000 o más. Además, 
independientemente de esto, ofrece un 5% de descuento si la marca 
es  NOSY.  Determinar  cuanto  pagará,  con  IVA  incluido,  un  cliente 
cualquiera por la compra de su aparato. IVA es del 16%."""
"""
aparato=int(input("ingrese el precio del aparato "))
marca=input("ingrese la marca del aparato ")

if (aparato>=2000):
    aparato=aparato-(aparato*0.1)
if (marca=="NOSY" or marca=="nosy"):
    aparato=aparato-(aparato*0.05)
print("el total a pagar es de: ", aparato+(aparato*0.16))"""