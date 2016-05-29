echo "Escriba la direccion de directorio"
read fuente
echo "Escriba la direccion del destino de la carpeta comprimida"
read destino
day=$(date +%A)
month=$(date +%B)
year=$(date +%Y)
tar -zcvf $year"_"$month"_"$day"_tarea".tar.gz $fuente
mv  $year"_"$month"_"$day"_"$fuente.tar.gz $destino
