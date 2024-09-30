from chess.piezas.pieza import Pieza
from chess.excepciones import *


class Peon(Pieza):
    blanco_str = "♟"
    negro_str = "♙"
    
    def obtener_posibles_posiciones(self, desde_fila, desde_columna): # Devuelve todas las posiciones posibles a las que el peón puede moverse
        posibles = []
        posibles.extend(self.obtener_posiciones_mover(desde_fila, desde_columna))
        posibles.extend(self.obtener_posibles_comer(desde_fila, desde_columna))
        return posibles
    
    def es_posicion_valida(self, fila, columna):# Verifica si la posición está dentro de los límites del tablero.
        
        if not (0 <= fila < 8 and 0 <= columna < 8):
            raise fuera_del_tablero(f"La posición ({fila}, {columna}) está fuera de los límites del tablero.")
        return True
    
    def obtener_posibles_comer(self, desde_fila, desde_columna): # Devuelve las posiciones diagonales donde el peón puede capturar una pieza enemiga.
       
        posiciones_comer = []
        if self.__color__ == "NEGRO":
            direcciones = [(1, 1), (1, -1)]
        else:
            direcciones = [(-1, 1), (-1, -1)]

        for direccion in direcciones:
            nueva_fila = desde_fila + direccion[0]
            nueva_columna = desde_columna + direccion[1]

            if self.es_posicion_valida(nueva_fila, nueva_columna):
                otra_pieza = self.__tablero__.obtener_pieza(nueva_fila, nueva_columna)
                if otra_pieza:
                    if otra_pieza.__color__ != self.__color__:
                        posiciones_comer.append((nueva_fila, nueva_columna))
                    else:
                        raise movimiento_inválido(f"No puedes capturar tu propia pieza en ({nueva_fila}, {nueva_columna}).")

        return posiciones_comer
    
    def obtener_posiciones_mover(self, desde_fila, desde_columna): # Devuelve las posiciones válidas a las que el peón puede moverse 
        posiciones = []

        if self.__color__ == "NEGRO":
            avance = 1
            fila_inicial = 1
        else:
            avance = -1
            fila_inicial = 6

        nueva_fila = desde_fila + avance
        if self.es_posicion_valida(nueva_fila, desde_columna):
            if self.__tablero__.obtener_pieza(nueva_fila, desde_columna) is None:
                posiciones.append((nueva_fila, desde_columna))
            else:
                raise movimiento_inválido(f"Hay una pieza bloqueando el movimiento en ({nueva_fila}, {desde_columna}).")

            if desde_fila == fila_inicial:
                nueva_fila_dos = desde_fila + (2 * avance)
                if self.es_posicion_valida(nueva_fila_dos, desde_columna):
                    if self.__tablero__.obtener_pieza(nueva_fila_dos, desde_columna) is None:
                        posiciones.append((nueva_fila_dos, desde_columna))
                    else:
                        raise movimiento_inválido(f"Hay una pieza bloqueando el movimiento en ({nueva_fila_dos}, {desde_columna}).")

        return posiciones




    
   