#_*_coding:utf-8_*_

import os

def comprobarFichero(d) :
	if (d, os.W_OK) :
		print 'Fichero OK, Escritura OK'
	elif (d, os.R_OK) :
		print 'Fichero OK, Lectura OK'
	else :
		print 'Fichero no OK'

def escribirPares(d) :
	for i in range(100) :
		if i % 2 == 0 :
			d.write(str(i))

# main

# Escribimos en el fichero
escribir = open('numeros.txt','w')
comprobarFichero(escribir)

escribirPares(escribir)

escribir.close()
comprobarFichero(escribir)

# Leemos del fichero
leer = open ('numeros.txt','r')
comprobarFichero(leer)

print leer.read()

leer.close()
comprobarFichero(leer)