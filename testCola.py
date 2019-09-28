#!/usr/bin/python3

import cola
import numpy as np

cola1 = cola.Cola(5, int)
cola1.queue(3)
cola1.queue(2)
cola1.queue(4)
cola1.queue(7)

print(cola1.dequeue())

cola1.mostrar()
cola2 = cola1.clone()
print(cola2)
