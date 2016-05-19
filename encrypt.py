listaABC=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];
def pertenece(listaABC,caracter):
 for i in listaABC:
  if(caracter==i):
   return True;
   break;
 return False;

def posicion(listaABC,caracter):
 for i in range(len(listaABC)):
  if(listaABC[i]==caracter):
   return i;
   break;

def trasladar(listaABC,palabra,numero):
 str0="";
 for i in range(len(palabra)):
  if(pertenece(listaABC,str(palabra[i]))):
   if(posicion(listaABC,str(palabra[i]))+numero>25):
    str0=str0+listaABC[posicion(listaABC,str(palabra[i]))+numero-26];
   else:
    str0=str0+listaABC[posicion(listaABC,str(palabra[i]))+numero];
  else:
   str0=str0+" ";
 return str0;

Encrypt=raw_input("Ingrese una palabra o frase :");
Encrypt.lower();
numero=input("Ingrese numero de traslado :");
print(trasladar(listaABC,Encrypt,int(numero)));  
   
