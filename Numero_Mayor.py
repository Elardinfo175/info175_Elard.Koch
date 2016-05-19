numero1=raw_input("ingrese numero 1: ");
numero2=raw_input("ingrese numero 2: ");
def comparador(x,y):
 a=x<y;
 b=x>y;
 c=x==y;
 if(a):
  print(str(y)+" es mayor");
 if(b):
  print(str(x)+" es mayor");
 if(c):
  print("son iguales");
comparador(numero1,numero2);
  
