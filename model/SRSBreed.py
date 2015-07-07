
class SRSBreed:    
    __name = ""
    __synonyms = []
    __locations = []
    __breeds = []

    def __init__(self, name, species):
        self.__name = name
        self.__species = species

    def name (self):
        return self.__name

    def synonyms (self):
        return self.__synonyms

    def locations (self):
        return self.__locations

