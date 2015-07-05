class SRSAnimal:
    # __animalcode = 0
    #    assert (type(__animalcode) == object)
    #    __sex = 0
    #    assert (type(__sex) == object)
    #    __breed = 0
    #    assert (type(__breed) == object)
    #    __species = 0
    #    assert (type(__species) == object)
    #    __territory = 0
    #    assert (type(__territory) == object)
    #    __father = 0
    #    assert (type(__father) == object)
    #    __mother = 0
    #    assert (type(__mother) == object)
    #    __srsIndividuals = 0
    #    assert (type(__srsIndividuals) == SRSRequestSample)
    #    __animals = 0
    #    assert (type(__animals) == SRSBreed)
    #    __animals = 0
    #    assert (type(__animals) == SRSApplication)

    def __init__(self, animalcode, sex, bornDate, species, breed, territory):
        self.__animalcode = animalcode
        self.__sex = sex
        self.__bornDate = bornDate
        self.__species = species
        self.__breed = breed
        self.__territory = territory

    def animalcode(self, animalcode):
        self.__animalcode = animalcode

    def sex(self):
        return self.__sex

    def borndate(self):
        return self.__bornDate

    def species(self):
        return self.__species

    def breed(self):
        return self.__breed

    def territory(self):
        return self.__territory