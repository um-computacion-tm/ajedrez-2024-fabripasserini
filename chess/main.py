from chess.tablero import Tablero
from chess.excepciones import *
from chess.piezas.rey import Rey

class Ajedrez:
    """
    Clase que gestiona el juego de ajedrez, maneja las reglas y el estado del juego,
    incluidos los turnos, el tablero y las condiciones de victoria.
    
    Atributos:
        __tablero__: Instancia de la clase Tablero que representa el tablero del juego.
        __turno__: Color del jugador actual, "BLANCO" o "NEGRO".
        __terminar_partida__: Booleano que indica si la partida ha terminado.
        __ganador__: Color del jugador ganador, o None si no ha terminado el juego.
        __rey_blanco__: Instancia de Rey que representa al rey blanco.
        __rey_negro__: Instancia de Rey que representa al rey negro.
    """
    
    def __init__(self):
        """
        Inicializa el juego de ajedrez con el tablero en su estado inicial, 
        configurando los turnos y el estado de los reyes.
        """
        self.__tablero__ = Tablero()
        self.__turno__ = "BLANCO"
        self.__terminar_partida__ = False
        self.__ganador__ = None
        self.__rey_blanco__ = self.__tablero__.obtener_rey_blanco()  
        self.__rey_negro__ = self.__tablero__.obtener_rey_negro()

    def en_juego(self):
        """
        Indica si el juego está en curso.
        
        Returns:
            bool: Siempre devuelve True para indicar que el juego está activo.
        """
        return True
    
    def en_tablero(self, fila, columna):
        """
        Verifica si una posición está dentro del tablero.

        Args:
            fila (int): La fila a verificar.
            columna (int): La columna a verificar.

        Returns:
            bool: True si la posición está dentro del tablero, False si no.
        """
        return 0 <= fila < 8 and 0 <= columna < 8

    def mover_pieza(self, desde_fila, desde_columna, hasta_fila, hasta_columna):
        """
        Mueve una pieza desde una posición inicial a una posición destino,
        verificando la validez del movimiento según las reglas del juego.

        Args:
            desde_fila (int): Fila de origen de la pieza.
            desde_columna (int): Columna de origen de la pieza.
            hasta_fila (int): Fila de destino de la pieza.
            hasta_columna (int): Columna de destino de la pieza.

        Raises:
            fuera_del_tablero: Si alguna coordenada está fuera del tablero.
            movimiento_sin_pieza: Si no hay ninguna pieza en la posición de origen.
            turno_invalido: Si la pieza a mover no pertenece al jugador cuyo turno es.
            movimiento_inválido: Si el movimiento no es permitido por las reglas de la pieza.
        """
        origen = self.__tablero__.obtener_pieza(desde_fila, desde_columna)
        destino = self.__tablero__.obtener_pieza(hasta_fila, hasta_columna)
        
        if not (self.en_tablero(desde_fila, desde_columna) and self.en_tablero(hasta_fila, hasta_columna)):
            raise fuera_del_tablero
        elif origen is None:
            raise movimiento_sin_pieza
        elif origen.obtener_color() != self.__turno__:
            raise turno_invalido
        elif desde_fila == hasta_fila and desde_columna == hasta_columna:
            raise movimiento_inválido
        elif destino is not None and destino.obtener_color() == self.__turno__:
            raise movimiento_inválido
        
        if (hasta_fila, hasta_columna) not in origen.obtener_posibles_posiciones(desde_fila, desde_columna):
            raise movimiento_inválido

        estado_juego = Tablero.verificar_estado_juego()
        if estado_juego != "CONTINUA":
            print(f"Juego terminado. Ganador: {estado_juego}")
        
        self.__tablero__.poner_pieza(hasta_fila, hasta_columna, origen)
        self.__tablero__.poner_pieza(desde_fila, desde_columna, None)

        if isinstance(destino, Rey):
            self.__terminar_partida__ = True
            self.__ganador__ = self.__turno__
            self.terminar_partida()
        else:
            self.cambiar_turno()
        
    def turnos(self):
        """
        Devuelve el turno actual del juego.

        Returns:
            str: "BLANCO" si es el turno del jugador blanco, "NEGRO" si es el turno del jugador negro.
        """
        return self.__turno__

    def mostrar_tablero(self):
        """
        Muestra el estado actual del tablero imprimiéndolo en la consola.
        """
        print("\nTablero de juego")
        self.__tablero__.imprimir_tablero()

    def cambiar_turno(self):
        """
        Cambia el turno al otro jugador. Si es el turno de las blancas, lo cambia a las negras,
        y viceversa.
        """
        if self.__turno__ == "BLANCO":
            self.__turno__ = "NEGRO"
        else:
            self.__turno__ = "BLANCO"
    
    def ganador(self):
        """
        Determina el ganador del juego si la partida ha terminado.

        Returns:
            str: "BLANCO" si el jugador blanco ha ganado, "NEGRO" si el jugador negro ha ganado,
            o None si la partida aún no ha terminado.
        """
        if self.__terminar_partida__:
            return "NEGRO" if self.__turno__ == "BLANCO" else "BLANCO"
        return None
    
    def terminar_partida(self):
        """
        Termina la partida y anuncia al ganador.
        """
        self.__terminar_partida__ = True
        print("Gana el jugador", self.ganador())

        
    

    

       