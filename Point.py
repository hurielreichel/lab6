class Point():

    def __init__(self, x, y):

        self.__x = float(x)
        self.__y = float(y)
        
    def getX(self):

        return self.__x

    def getY(self):

        return self.__y

    def setX(self, x):

        self.__x = x

        return x

    def setY(self, y):

        self.__y = y

        return y

    def setPosition(self, x, y):

        self.__x = x

        self.__y = y

        return(self)

    def distance(self, x, y):

        d = ( (x - self.__x) ** 2 + (y - self.__y) ** 2 ) ** 0.5

        return d

    def toString(self):

        return "Point ( " + str(self.__x) + ", " + str(self.__y) + " )"

