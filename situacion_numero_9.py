lin=["\n--------------------------------",
"\n------------------------------------------------------------------"]

print(lin[1],"\n                       COMPRA DE DISCOS",
     lin[1],"\n       DISCOS DISPONIBLES     |","       NUESTROS DESCUENTOS",lin[1],
     "\n   Marca    | Precio Unitario |","  Cantidad    | Descuento",lin[1],
     "\n1. Salsa    | s/. 56.00       |"," a. 1 a 3     | No hay descuento",
     "\n2. Rock     | s/. 63.00       |"," b. 4         | 6.0%",
     "\n3. Pop      | s/. 87.00       |"," c. 5 a 10    | 8.0%",
     "\n4. Folclore | s/. 120.50      |"," d. Mas de 10 | 10.2%",lin[1],
     "\nSI SE LLEVA MAS DE 6 DISC0S DE ROCK O POP, TE REGALAMOS UN POSTER!",lin[1])

sa=[56,"Salsa"]
fo=[120.5,"Folclore"]
pop=[87,"Pop"]
rk=[63,"Rock"]
tx=["\n Compra:","\n Cantidad:","\n Precio: S/.","\n Descuento","\n Obsequio: Poster",
"\n Obsequio: Ninguno","\n Total a pagar: S/.","(6%): S/","(8%): S/","(10.2%): S/","\n Descuento: Ninguno"]
fi=["\n Muchas gracias por su compra! \n Visitenos pronto!","\n       BOLETA ELECTRONICA"]
print("Qué disco quiere comprar? Salsa(s), Rock(r), Pop(p), Folclore(f)")

try:
  def dsk(bl):
     bl
     lot=int(input(f"Cuántos discos de {bl[1]} desea comprar?: "))
     if 1<=lot<=3:
        print(lin[0],fi[1],lin[0],tx[0],bl[1],tx[1],lot,tx[2],lot*bl[0],tx[5],
        tx[10],tx[6],lot*bl[0],lin[0],fi[0],lin[0])
     elif lot==4:
        print(lin[0],fi[1],lin[0],tx[0],bl[1],tx[1],lot,tx[2],lot*bl[0],tx[5],tx[3],tx[7],
        round((lot*bl[0])*0.04,2),tx[6],round(lot*bl[0]-((lot*bl[0])*0.04),2),lin[0],lin[0],fi[0],lin[0])
     elif 5<=lot<=6:
        print(lin[0],fi[1],lin[0],tx[0],bl[1],tx[1],lot,tx[2],lot*bl[0],tx[5],tx[3],tx[8],
        round((lot*bl[0])*0.08,2),tx[6],round(lot*bl[0]-((lot*bl[0])*0.08),2),lin[0],lin[0],fi[0],lin[0])
     elif 6<lot<=10:
        if bl==sa or bl==fo:
           print(lin[0],fi[1],lin[0],tx[0],bl[1],tx[1],lot,tx[2],lot*bl[0],tx[5],tx[3],tx[8],
           round((lot*bl[0])*0.08,2),tx[6],round(lot*bl[0]-((lot*bl[0])*0.08),2),lin[0],fi[0],lin[0])
        else:
           print(lin[0],fi[1],lin[0],tx[0],bl[1],tx[1],lot,tx[2],lot*bl[0],tx[4],tx[3],tx[8],
           round((lot*bl[0])*0.08,2),tx[6],round(lot*bl[0]-((lot*bl[0])*0.08),2),lin[0],fi[0],lin[0])
     elif lot>10:
        if bl==sa or bl==fo:
           print(lin[0],fi[1],lin[0],tx[0],bl[1],tx[1],lot,tx[2],lot*bl[0],tx[5],tx[3],tx[9],
           round((lot*bl[0])*0.102,2),tx[6],round(lot*bl[0]-((lot*bl[0])*0.102),2),lin[0],fi[0],lin[0])
        else:
           print(lin[0],fi[1],lin[0],tx[0],bl[1],tx[1],lot,tx[2],lot*bl[0],tx[4],tx[3],tx[9],
           round((lot*bl[0])*0.102,2),tx[6],round(lot*bl[0]-((lot*bl[0])*0.102),2),lin[0],fi[0],lin[0])

     else:
        print("Cero??")
  buy=input("Ingrese la letra asignada: ")
  if buy.lower()=="s":
     dsk(sa)
  elif buy.lower()=="f":
     dsk(fo)
  elif buy.lower()=="r":
     dsk(rk)
  elif buy.lower()=="p":
     dsk(pop)
  else:
     print("No hay ese valor")
except ValueError:
  print("Error, solo se admite numeros enteros")
except:
  print("Ocurrio un error :0")
  
  
  
  #no soy autor de este
