import numpy as np
from Soluciones.Manager import Actividad

def Ejercicio_1a():
    S1=np.load("./Soluciones/sol01.npy")
    Actividad("F",S1).Ejercicio()

def Ejercicio_1b():
    S2=np.load("./Soluciones/sol02.npy")
    Actividad("G",S2).Ejercicio()

def Ejercicio_2a():
    S3=np.load("./Soluciones/sol03.npy")
    Actividad("F",S3).Ejercicio()
    
def Ejercicio_2b():
    S4=np.load("./Soluciones/sol04.npy")
    Actividad("G",S4).Ejercicio()