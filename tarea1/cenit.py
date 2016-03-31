listaABC=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
listaPolar=["i","b","p","d","o","f","g","h","a","j","k","n","m","l","p","c","q","t","s","r","u","v","w","x","y","z"]
def pertenece(lista,caracter):
 for i in listaABC:
  if(caracter==i):
   return True;
   break;
 return False;

def posicion(lista,caracter):
 for i in range(len(listaABC)):
  if(lista[i]==caracter):
   return i;
   break;

def cambiar(lista1,lista2,caracter):
 str0="";
 for i in caracter:
  if(pertenece(lista1,i)):
   str0=str0+lista2[posicion(lista1,i)];
  else:
   str0=str0+" ";
 return str0;
