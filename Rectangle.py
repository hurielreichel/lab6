from Point import Point
from Shape import Shape

class Rectangle(Shape):

    def __init__(self, topLeftPoint, width, height):

        self.topLeftPoint = topLeftPoint
        self.width = float(width)
        self.height = float(height)
        
    def gettopLeftPoint(self):

        return(self.topLeftPoint)

    def getwidth(self):

        return(self.width)

    def getheight(self):

        return(self.height)

    def settopLeftPoint(self, topLeftPoint):

        self.topLeftPoint = topLeftPoint

        return(topLeftPoint)

    def setwidth(self, width):

        self.width = width

        return(width)

    def setheight(self, height):

        self.height = height

        return(height)

    def area(self):

        a = float( round(self.width * self.height, 1) )

        return a

    def perimeter(self):

        p = float( round(self.width * 2 + self.height * 2, 1) )

        return p

    def contains(self, point):

        xmin = self.topLeftPoint.getX()

        xmax = xmin + self.width

        ymax = self.topLeftPoint.getY()

        ymin = ymax + self.height

        if point.getX() >= xmin and point.getX() <= xmax and point.getY() >= ymax and point.getY() <= ymin :

            return True

        else:

            return False

    def centroid(self):

        return Point(self.topLeftPoint.getX()+(self.getwidth()/2), self.topLeftPoint.getY() - (self.getheight() / 2))

    def toString(self):

        xmin = self.topLeftPoint.getX()

        xmax = xmin + self.width

        ymax = self.topLeftPoint.getY()

        ymin = ymax - self.height

        return "The Rectangle [topLeftPoint = " + self.topLeftPoint.toString() + ", width = " + str(self.width) + \
            ", height = " + str(self.height) + "]"
    
