class CasillaDeVotacion:

    def __init__(self, identificador, pais):
        self._identificador = identificador
        self.__pais = pais
        self.region = None

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, region):
        if region in self.__pais:
            self.__region = region
        else:
            raise ValueError(f'la region {region} no es valida es {self.__pais}')



