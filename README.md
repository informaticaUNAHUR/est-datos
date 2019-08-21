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

Por ejemplo, en Gobstones trabajamos un ejercicio:

donde se define:

```
type Tubería is record {
/* PROPÓSITO: Modela una tubería.
INV. DE REP. el largo es mayor a cero. */
field dirección // Dirección
field color  // Color
field largo  // Número
field grosor // Grosor
}

type Grosor is variant {
/* PROPÓSITO: Modela el grosor de una tubería */
case Medio {}
case TresCuartos {}
case Pulgada {}
}

```


Referencia de cómo armar TAD en Python sin tener que meterse demasiado en el concepto de clases:
https://sites.google.com/site/programacioniiuno/temario/unidad-2---tipo-abstracto-de-dato/emulando-un-struct-en-python
(ver apartado: Clase vacía con función constructora)

### OPCIÓN 1 
¿sirve así?

````
class Tuberia:
    pass

def nuevaTuberia(direccion, largo):
    tuberia = Tuberia()
    tuberia.direccion = direccion
    tuberia.largo = largo
    return tuberia

def masLargo(tuberia1,tuberia2):
    return(tuberia1.largo>tuberia2.largo)

tubo1=nuevaTuberia('Oeste', 100)
tubo2=nuevaTuberia('Norte',190)

print('¿es más largo el tubo1 que el tubo2?:', masLargo(tubo1,tubo2))

