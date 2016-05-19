a=True;
lista=[];
while(a):
 linea=raw_input("ingrese una linea :");
 if len(linea)==0:
  a=False;
 else:
  lista.append(linea);
for i in range(len(lista)):
 linea=lista[i];
 print linea.upper();

