#! /bin/bash
# Declara un arreglo con 4 elementos

ARRAY=( 'Debian linux' 'Redhat linux' Ubuntu linux )

# Obtener el numero de elementos
ELEMENTS=${#ARRAY[@]}

for (( i=0;i<$ELEMENTS;i++)); do
	echo ${ARRAY[${i}]}
done