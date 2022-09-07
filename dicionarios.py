#LOS DICCIONARIOS SON VARIABLES ESPECIALES
#QUE ME PERMITEN ALMACENAR MULTIPLES DATOS
#DE DIFERENTE TIPO EN UNA SOLA VARIABLE
#DENTRO DE UN DICCIONARIO YO PEUEDO TENER LISTAS
empleado={
    'nombre': "juan",
    'cedula': 32243630,
    'cargo': "Analista de datos",
    'salario': 8000000,
    'horasTrabajadas': 40,
    'aplicaSubsidioTransporte': False,
    'deducciones':[1500000,800000]

}
print(empleado)
print(empleado['deducciones'][1])

#RECORRIENDO UN DICCIONARIO:
for observadorAtributo,observadorValor in empleado.items():
    print(observadorAtributo)
    print(observadorValor)