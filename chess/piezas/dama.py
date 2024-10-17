from chess.piezas.pieza import Pieza  # Importamos la clase Pieza
from chess.excepciones import *  # Importamos las excepciones


class Dama(Pieza):
    blanco_str = "♛"
    negro_str = "♕"

    def __init__(self, color, tablero):
        super().__init__(color, tablero)

    def obtener_posibles_posiciones(self, desde_fila, desde_columna):
        # Combina los movimientos en todas las direcciones posibles (diagonales, verticales, horizontales)
        posibles = []
        posibles.extend(self.obtener_posiciones_mover(desde_fila, desde_columna))
        return posibles

    def es_casilla_vacia(self, fila, columna):
        return self.__tablero__.obtener_pieza(fila, columna) is None
    
    def es_posicion_valida(self, fila, columna):
        if not (0 <= fila < 8 and 0 <= columna < 8):
            raise fuera_del_tablero(f"La posición ({fila}, {columna}) está fuera de los límites del tablero.")
        return True

    def obtener_posiciones_mover(self, desde_fila, desde_columna):
        posiciones = []
        posiciones.extend(self.obtener_posiciones_diagonales(desde_fila, desde_columna))
        posiciones.extend(self.obtener_posiciones_verticales(desde_fila, desde_columna))
        posiciones.extend(self.obtener_posiciones_horizontales(desde_fila, desde_columna))
        return posiciones
    
    def obtener_posiciones_diagonales(self, desde_fila, desde_columna):
        posiciones = []
        direcciones = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Las 4 direcciones diagonales
    
        for direccion in direcciones:
            nueva_fila = desde_fila
            nueva_columna = desde_columna
            
            while True:
                nueva_fila += direccion[0]
                nueva_columna += direccion[1]
                
                if not self.es_posicion_valida(nueva_fila, nueva_columna):
                    break
                
                otra_pieza = self.__tablero__.obtener_pieza(nueva_fila, nueva_columna)
                if otra_pieza is None: 
                    posiciones.append((nueva_fila, nueva_columna))  # Casilla vacía, sigue avanzando
                elif otra_pieza.__color__ != self.__color__:  
                    posiciones.append((nueva_fila, nueva_columna))  # Captura y se detiene
                    break
                else:
                    break  # Si hay una pieza aliada, se detiene
    
        return posiciones

    def obtener_posiciones_verticales(self, desde_fila, desde_columna):
        posiciones = []
        # Movimiento vertical hacia arriba y hacia abajo
        for desplazamiento in [-1, 1]:  
            nueva_fila = desde_fila
            while True:
                nueva_fila += desplazamiento
                if not self.es_posicion_valida(nueva_fila, desde_columna):
                    break
                
                otra_pieza = self.__tablero__.obtener_pieza(nueva_fila, desde_columna)
                if otra_pieza is None:
                    posiciones.append((nueva_fila, desde_columna))  # Casilla vacía
                elif otra_pieza.__color__ != self.__color__:
                    posiciones.append((nueva_fila, desde_columna))  # Captura y se detiene
                    break
                else:
                    break  # Bloqueado por pieza aliada

        return posiciones

    def obtener_posiciones_horizontales(self, desde_fila, desde_columna):
        posiciones = []
    
    # Recorremos todas las columnas hacia la derecha
        for nueva_columna in range(desde_columna + 1, 8):
            if not self.es_posicion_valida(desde_fila, nueva_columna):
                break  # Si no es válida (fuera del tablero), se detiene
            otra_pieza = self.__tablero__.obtener_pieza(desde_fila, nueva_columna)
            if otra_pieza is None:
                posiciones.append((desde_fila, nueva_columna))  # Casilla vacía
            elif otra_pieza.__color__ != self.__color__:
                posiciones.append((desde_fila, nueva_columna))  # Captura
                break  # Detiene después de capturar
            else:
                break  # Detiene si encuentra una pieza aliada

    # Recorremos todas las columnas hacia la izquierda
        for nueva_columna in range(desde_columna - 1, -1, -1):
            if not self.es_posicion_valida(desde_fila, nueva_columna):
                break  # Si no es válida, se detiene
            otra_pieza = self.__tablero__.obtener_pieza(desde_fila, nueva_columna)
            if otra_pieza is None:
                posiciones.append((desde_fila, nueva_columna))  # Casilla vacía
            elif otra_pieza.__color__ != self.__color__:
                posiciones.append((desde_fila, nueva_columna))  # Captura
                break  # Detiene después de capturar
            else:
                break  # Detiene si encuentra una pieza aliada

        return posiciones