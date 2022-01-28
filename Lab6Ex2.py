import csv
from City import City
from Rectangle import Rectangle
from Point import Point
import matplotlib.pyplot as plt
from matplotlib.patches import Circle as C
from matplotlib.patches import Rectangle as R

# open the CSV file
with open("data.csv", mode = 'r') as file:
    # read the CSV file
    csvFile = csv.reader(file)

    cities = []
    for lines in csvFile:

        cities.append(City(lines[0], Point(float(lines[1].split()[1]), float(lines[1].split()[0])), lines[2],lines[3],lines[4],lines[5],lines[6]))

#bbox
x = []
y = []
for i in range(len(cities)):
    #minx
    x.append(cities[i].getlocation().getX())

    #miny
    y.append(cities[i].getlocation().getY())

bbox = Rectangle(Point(min(x), max(y)), max(x) - min(x), max(y) - min(y))

#scale
scale = 900/max(bbox.getheight(), bbox.getwidth())

# pass scale
for i in range(len(cities)):

    cities[i].setlocation(Point(cities[i].getlocation().getX() * scale, cities[i].getlocation().getY() * scale))

# centre point
xTranslation = 500 - bbox.centroid().getX() * scale
yTranslation = 500 - bbox.centroid().getY() * scale

# translate coordinates
x_translated = list(range(len(cities)))
y_translated = list(range(len(cities)))
for i in range(len(cities)):

    x_translated[i] = cities[i].getlocation().getX() + xTranslation
    y_translated[i] = cities[i].getlocation().getY() + yTranslation

# plot cities
fig, ax = plt.subplots()
ax.plot(1000, 1000)

for i in range(len(cities)):

    ax.add_patch(C(xy = (x_translated[i], y_translated[i]),
                   radius = 50,
                   facecolor = "blue",
                   linewidth = 1,
                   edgecolor = "gray"))

    plt.text(x_translated[i], y_translated[i], cities[i].getname(), ha = 'center')

plt.gca().set_aspect('equal')
plt.show()
