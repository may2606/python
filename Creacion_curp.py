# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 02:22:28 2023

@author: WIN 10
"""
import datetime
import random

# Función para generar el dígito verificador
def generar_digito_verificador(curp_base):
    diccionario = "0123456789ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    suma = 0

    for i, caracter in enumerate(curp_base):
        valor = diccionario.index(caracter)
        suma += (valor * (i + 1))

    digito_verificador = diccionario[suma % 10]
    return digito_verificador

# Función para obtener el siglo asignado
def obtener_siglo(fecha_nacimiento):
    if fecha_nacimiento.year >= 2000:
        return 'A'
    else:
        return '0'

# Función para generar la CURP
def generar_CURP(nombre, apellido_paterno, apellido_materno, sexo, fecha_nacimiento, entidad_nacimiento):
    # Diccionario de vocales a excluir
    vocales = ['A', 'E', 'I', 'O', 'U']

    # Función para encontrar la primera consonante después de la primera letra
    def encontrar_primera_consonante(palabra):
        for i in range(1, len(palabra)):
            if palabra[i].upper() not in vocales:
                return palabra[i].upper()
        return ''

    # Obtener los datos para la CURP
    curp_generada = apellido_paterno[:2].upper() + apellido_materno[0].upper() + nombre[0].upper() + \
                    str(fecha_nacimiento.year)[2:] + str(fecha_nacimiento.month).zfill(2) + \
                    str(fecha_nacimiento.day).zfill(2) + sexo.upper() + entidad_nacimiento[:2].upper() + \
                    encontrar_primera_consonante(apellido_paterno) + \
                    encontrar_primera_consonante(apellido_materno) + \
                    encontrar_primera_consonante(nombre)

    # Carácter 17 - Siglo asignado
    siglo_asignado = obtener_siglo(fecha_nacimiento)
    curp_generada += siglo_asignado

    # Carácter 18 - Dígito verificador aleatorio
    digito_verificador = generar_digito_verificador(curp_generada)
    curp_generada += digito_verificador

    return curp_generada

# Solicitar datos al usuario
nombre = input("Ingresa tu nombre: ")
apellido_paterno = input("Ingresa tu apellido paterno: ")
apellido_materno = input("Ingresa tu apellido materno: ")
sexo = input("Ingresa tu sexo (H/M): ")
fecha_nacimiento_str = input("Ingresa tu fecha de nacimiento (Formato: AAAA-MM-DD): ")
fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento_str, "%Y-%m-%d")
entidad_nacimiento = input("Ingresa la clave de entidad federativa de nacimiento (2 caracteres): ")

# Generar la CURP
curp_generada = generar_CURP(nombre, apellido_paterno, apellido_materno, sexo, fecha_nacimiento, entidad_nacimiento)

# Mostrar la CURP generada
print("Tu CURP generada es:", curp_generada)
 #integrantes : Danae Paloma Hernande Gomez 
#Mayra Galvez Rodriguez