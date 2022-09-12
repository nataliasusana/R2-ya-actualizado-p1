from IPython.display import display, Latex
from termcolor import colored
import numpy as np

class Actividad:
    def __init__(self,Funcion,S):
        self.Funcion=Funcion
        self.S=S
    
    def Respuesta(self):
        display(Latex(f'${self.Funcion}\'(x)$'))
        R1 = input("=")
        return R1
    
    def Ejercicio(self):
        R1 = self.Respuesta()
        
        for i in range(len(self.S)):
            self.S[i]=self.S[i].replace(" ","")

        aux=False
        for i in self.S:
            if R1.replace(" ","") == i:
                aux=True
        if aux:
            print(colored("-"*100,"green"))
            print(colored("Correcto","green"))
        else:
            print(colored("-"*100,"red"))
            print(colored("Tu respuesta es incorrecta, verifica las reglas de la derivacion y vuelve a intentar","red"))
            
