class Auto(object):
 def __init__(self,kilometraje,bencina,rendimiento,encendido):
  self.kilometraje=kilometraje;
  self.bencina=bencina;
  self.rendimiento=rendimiento; #km x 1lt de bencina
  self.encendido=encendido;
 def encender(self):
  self.encendido=True;
 def apagar(self):
  self.encendido=False;
 def mover(self):
  while(self.bencina>0 and self.encendido):
   self.bencina-=1;
   self.kilometraje+=self.rendimiento;
  if(self.bencina>0 or not self.encendido):
   print("no hay bencina o no esta encendido");
 def obtenerKilometraje(self):
  return self.kilometraje;
 def obtenerBencina(self):
  return self.bencina;
 def cargarBencina(self,bencina):
  if(not self.encendido):
   self.bencina+=bencina;
  else:
   print("se debe apagar el auto");

auto1=Auto(0,0,13,False);
auto1.mover();
auto1.encender();
print(auto1.obtenerBencina());
auto1.cargarBencina(0);
auto1.apagar();
auto1.cargarBencina(20);
auto1.encender();
auto1.mover();
print(auto1.obtenerKilometraje());

