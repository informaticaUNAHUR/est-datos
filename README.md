# Estructuras de Datos - 2019

### Lenguaje propuesto para ejercitar: Python 3
IDE: Spyder del paquete ANCONDA: https://www.anaconda.com/distribution/


## CLASES 1, 2 y 3 - Introducción a Python 

Objetivos: 
* familiarizarse con la sintaxis Python, realizar operaciones y cálculos usando instrucciones, consola, ver resultados
* Construir funciones
* Repasar estructuras de control
* 

**Caso: Ejericio 6 del TP 1**

Propone: 
>Declarar dos variables enteras (con cualquier valor) e informar por pantalla cual es menor de las dos, si son iguales, indicarlo por separado. Cambiar el orden de los valores para comprobar el funcionamiento.


1) Primero la intención es que usen alternativa condicional
```
variable1=10
variable2=1

if (variable1>variable2):
    print('variable1')
elif (variable2>variable1):
    print('variable2')
else:
    print('iguales')
```

2) Sería bueno relacionarlo con las formas y prácticas propuestas en Intro (Gobstones)
Entonces, se podría resolver, por ejemplo así:
```
def mayorOIgual(numero1,numero2):
    return('var1' if numero1>numero2 else ('iguales' if numero1==numero2 else 'var2'))

print('otra forma de hacerlo al estilo Gobstones')
print(mayorOIgual(variable1,variable2))
```

## Clases 4 y 5  - Tipo Abstracto de Datos

Objetivos:
 * Introducir el concepto de TDA

**En la primera clase también se puede trabajar relacionado con Gobstones (registros y variantes)**




