import sympy as sy

def whatis(expr):
    if isinstance(expr, sy.Basic): # verificar que la expresión sea una expresión de SymPy
        if expr.atoms(sy.Derivative): # verificar si la expresión contiene una derivada
            return True # es una ODE/PDE
        else:
            return False # es una expresión/ecuación
    else:
        return False # es un sistema de ecuaciones

def verificar_sympy(problema, solucion):
    # Caso para ODEs/PDEs
    if whatis(problema):
        # Caso para ODEs
        try:
            # Se intenta clasificar la ODE (PDEs no pasan esta prueba), por lo
            # que se realiza esta prueba primero. Además, las soluciones de PDEs
            # pasan la prueba de checkodesol, pero con resultado False
            sy.classify_ode(problema)
            # Se verifica la solución de la ODE. En caso de existir algún error con
            # la entrada, entrará el except del bloque anidado, dado que si el 
            # problema fuese una PDE, la línea anterior habría entrado al except 
            # de este bloque
            if not sy.checkodesol(problema, solucion)[0]:
                return print('Revisa tu solución')
            else:
                return print('¡Excelente! Tu solución es correcta')
        except Exception:
            # Caso para PDEs
            try:
                # Se intenta clasificar la PDE (ODEs no pasan esta prueba)
                # Contrario al caso anterior, las soluciones de ODEs no pasan
                # la prueba de checkpdesol.
                sy.classify_pde(problema)
                # Se intenta verificar la solución de la PDE. En caso de existir
                # algún error en la entrada, entrará el except
                if not sy.checkpdesol(problema, solucion)[0]:
                    return print('Revisa tu solución')
                else:
                    return print('¡Excelente! Tu solución es correcta')
            except Exception:
                # La entrada presenta un error, se debe revisar por el usuario
                print('Ha ocurrido un error. Revisa tu entrada')
    # Caso para ecuaciones/sistemas de ecuaciones
    else:
        try:
            # Para pasar el bloque try, debe cumplirse el siguiente caso:
            # - El problema depende de sólo n variables, es un problema lineal y
            #   existe sólo una solución
            # Esto dado a que la verificación asume que la solución que recibe es
            # un diccionario. En caso de que la solución sea una lista de diccionarios
            # entrará en el bloque except
            if sy.checksol(problema, solucion):
                return print('¡Excelente! Tu solución es correcta')
            else:
                return print('Revisa tu solución')
        except Exception:
            # Para entrar al bloque except, debe presentarse el siguiente caso:
            # - El problema depende de n variables, pero no es un problema lineal por lo
            #   que existe más de una solución
            # Por ende, se revisa primero que la solución sea una lista (los diccionarios
            # tienen len(dict) = 1). En dicho caso, se almacena el resultado de todas las
            # soluciones en una lista y después se verifica que todos los elementos de la
            # lista tengan valor True.
            if len(solucion) > 1:
                resultado = [sy.checksol(problema, sol) for sol in solucion]
                if all(resultado):
                    return print('¡Excelente! Tu solución es correcta')
                else:
                    return print('Revisa tu solución')
            else:
                # Si se entra a este caso, existe un error en la entrada y esta debe ser
                # revisada por el usuario
                return print('Ha ocurrido un error. Revisa tu entrada')