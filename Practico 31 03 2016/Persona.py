import time;

hoy=time.localtime(time.time());

class Persona(object):
 def __init__(self,rut,nombre,fecha_nacimiento,genero):
 self.nombre=nombre;
 self.rut=rut;
 self.fecha_nacimiento=[]; #[0]año,[1]meses,[2]dias
 self.genero=genero;

 def obtener_edad(self):
  edad=hoy[0]-self.fecha_nacimiento[0];
  if(hoy[1]-self.fecha_nacimiento[1]<0):
   edad-=1;
  elif(hoy[1]==self.fecha_nacimiento[1]):
   if(hoy[2]-self.fecha_nacimiento[2]<0):
    edad-=1;
  return edad;

class nota(object):
 def __init__(self,valor,ponderacion,ramo,carrera):
  self.valor=valor;
  self.ponderacion=ponderacion;#diccionario
  self.ramo=ramo;
  self.carrera=carrera;
 def obtener_valor(self):
  return self.valor;

 def obtener_ponderacion(self):
  return self.ponderacion;

 def modificar(self):

class alumno(Persona,nota):

 def __init__(self,correo,carrera,promocion,notas):
  self.correo=correo;
  self.carrera=carrera;
  self.promocion=promocion;
  self.notas=[];
 def agregar_nota(self,nota):
  self.notas.append(nota);
 def PGA(self):
  ponderacion=super(self,alumno).obtener_ponderacion();
  promedio=0;
  for key in ponderacion:
   promedio+=ponderacion[key]*self.notas[int(key)];
  return promedio;
 def promedio_por_ramo(self):
  
 
