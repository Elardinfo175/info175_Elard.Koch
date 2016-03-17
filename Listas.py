lista_de_palabras=raw_input("Escriba una lista de palabras separadas por coma: ");
if(lista_de_palabras[len(lista_de_palabras)-1]!=","):
 lista_de_palabras=lista_de_palabras+",";

def convertir_lista(lista): 
 lis=[];
 j=0;
 for i in range(len(lista)):
  str0="";
  if lista[i]==",":
   str0=lista[j:i];
   lis.append(str0);
   j=i+1;
 return lis;

def crear_string(lista): 
 cadena="";
 for i in range(len(lista)):
  if(cadena!=""):
   cadena=cadena+","+lista[i];
  else:
   cadena=cadena+lista[i]; 
 return cadena;

lista=convertir_lista(lista_de_palabras);
cadena=crear_string(lista.sort());
print(cadena);
