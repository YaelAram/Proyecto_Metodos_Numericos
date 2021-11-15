class Recta:
    __pendiente = 0.0
    __ordenada_origen = 0.0

    def __init__(self, x1, y1, x2, y2):
        if x2 is None and y2 is None:
            self.__pendiente = x1
            self.__ordenada_origen = y1
        else:
            self.__pendiente = (y2 - y1) / (x2 - x1)
            self.__ordenada_origen = y1 - (self.__pendiente * x1)

    def evaluar(self, x):
        return (self.__pendiente * x) + self.__ordenada_origen

    def __str__(self):
        return f"y(x) = {self.__pendiente}x {'' if self.__ordenada_origen <= 0 else '+'}" \
               f" {self.__ordenada_origen if self.__ordenada_origen != 0 else ''}"
