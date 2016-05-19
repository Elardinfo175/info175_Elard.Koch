class Camion(object):
 def __init__(self,peso,ruedas):
  self.peso=peso;
  self.ruedas=ruedas;
  self.acoplados={}; #diccionario
 def agregar_acoplados(self,ruedas,peso,carga):
  self.acoplados["ruedas"]=ruedas;
  self.acoplados["peso"]=peso;
  self.acoplados["carga"]=carga;
 def quitar_acoplados(self):
  self.acoplados["ruedas"]=0;
  self.acoplados["peso"]=0.0;
  self.acoplados["carga"]="";
 def obtener_acoplados(self): 
  return self.acoplados;
 def obtener_ruedas(self):
  return self.acoplados["ruedas"];
 def obtener_peso(self):
  return self.acoplados["peso"];

camion1=Camion(10.0,8);
camion1.agregar_acoplados(4,15.0,"mounstro del lago ness");
print camion1.obtener_acoplados();
print camion1.obtener_ruedas();
print camion1.obtener_peso();
camion1.quitar_acoplados();
print camion1.obtener_acoplados();
