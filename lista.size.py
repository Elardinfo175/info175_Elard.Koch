def multiplos_3_7(size):
 lista_de_multiplos_3_7=[];
 for i in range(int(size)):
  j=i+1;
  if(j%3==0 and j%7==0):
   lista_de_multiplos_3_7.append(j);
 return lista_de_multiplos_3_7;

size=raw_input("Ingrese un numero para size: ");
print("Los multiplos de 3 y 7 que estan entre 1 y size son: \n");
print(multiplos_3_7(size));

