#! /bin/bash
#pone todos los argumentos en el arreglo direc
direc=("$@")
#cambiamos a la posicion de fuente
cd "${direc[0]}" 
#obtenemos el nombre de la carpeta donde estamos
FUENTE="${PWD##*/}"
#salimos al directorio que contiene la carpeta que vamos a copiar
cd ..
#asignamos la direccion de destino
DESTINO=${direc[1]}
#variables de la fecha
D=$(date +%d)
M=$(date +%m)
Y=$(date +%Y)
#creamos el nombre del archivo con la fecha y el nombre de la carpeta a respaldar
FILENAME=$Y"_"$M"_"$D"_"$FUENTE
#creamos el zip y lo enviamos a la direccion de destino
zip -r $DESTINO/$FILENAME.zip $FUENTE
