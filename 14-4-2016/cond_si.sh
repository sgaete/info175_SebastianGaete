#! /bin/bash

VALID_PASSWORD="secret"

echo "Ingrese la password"
read PASSWORD
#IMPORTANTE LOS ESPACIOS AL PRINCIPIO Y FINAL DE LOS CORCHETES

if [ "$PASSWORD" == "$VALID_PASSWORD" ];then
	echo "Acceso concedido"
else
	echo "Acceso denegado"
fi