from Point import Point
class City():

    def __init__(self, name, location, area, population, density, gdp, elevation):

        self.__name = str(name)
        self.__location = location
        self.__area = float(area)
        self.__population = int(population)
        self.__density = int(density)
        self.__gdp = float(gdp)
        self.__elevation = int(elevation)

    def getname(self):

        return self.__name
        
    def getlocation(self):

        return self.__location

    def getarea(self):

        return self.__area

    def getpopulation(self):

        return self.__population

    def getdensity(self):

        return self.__density
        
    def getgdp(self):

        return self.__gdp
        
    def getelevation(self):

        return self.__elevation

    def setname(self, name):

        self.__name = name

        return self.__name

    def setlocation(self, location):

        self.__location = location

        return self.__location

    def setarea(self, area):

        self.__area = area
        
        return self.__area
    
    def setpopulation(self, population):

        self.__population = population

        return self.__population

    def setdensity(self, density):

        self.__density = density
        
        return self.__density
        
    def setgdp(self, gdp):

        self.__gdp = gdp
        
        return self.__gdp
        
    def setelevation(self, elevation):

        self.__elevation = elevation
        	
        return self.__elevation
