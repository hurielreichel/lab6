import csv
from City import City
from Rectangle import Rectangle
from Point import Point
import matplotlib.pyplot as plt
from matplotlib.patches import Circle as C
from matplotlib.patches import Rectangle as R
import json

#### CITIES ####

# open the CSV file
with open("data.csv", mode = 'r') as file:
    # read the CSV file
    csvFile = csv.reader(file)

    cities = []
    for lines in csvFile:

        cities.append(City(lines[0], Point(float(lines[1].split()[1]), float(lines[1].split()[0])), lines[2],lines[3],lines[4],lines[5],lines[6]))

#### COAST LINE ####

# open json file
pts = []
with open("europe.geojson", mode = 'r') as file:
    gjFile = json.load(file)
    for entry in gjFile['features']:
        polyline = entry['geometry']['coordinates']
        #print(polyline)

        for i in range(len(polyline)):

            pts.append(Point(polyline[i][0], polyline[i][1]))

#bbox
x = []
y = []
for i in range(len(pts)):
    #minx
    x.append(pts[i].getX())

    #miny
    y.append(pts[i].getY())

bbox = Rectangle(Point(min(x), max(y)), max(x) - min(x), max(y) - min(y))

#scale
scale = 900/max(bbox.getheight(), bbox.getwidth())

# pass scale to cities
for i in range(len(cities)):

    cities[i].setlocation(Point(cities[i].getlocation().getX() * scale, cities[i].getlocation().getY() * scale))

# pass scale to coast line points
for i in range(len(pts)):

    pts[i].setX(x[i] * scale)
    pts[i].setY(y[i] * scale)

# centre point
xTranslation = 500 - bbox.centroid().getX() * scale
yTranslation = 500 - bbox.centroid().getY() * scale

# translate coordinates
x_translated_cities = list(range(len(cities)))
y_translated_cities = list(range(len(cities)))
for i in range(len(cities)):

    x_translated_cities[i] = cities[i].getlocation().getX() + xTranslation
    y_translated_cities[i] = cities[i].getlocation().getY() + yTranslation

# translate coordinates coast line points
x_translated = list(range(len(pts)))
y_translated = list(range(len(pts)))
for i in range(len(pts)):

    x_translated[i] = pts[i].getX() + xTranslation
    y_translated[i] = pts[i].getY() + yTranslation

# plot cities
fig, ax = plt.subplots()
ax.plot(1000, 1000)

for i in range(len(pts)):

    plt.plot(x_translated[i], y_translated[i], marker='.', color = 'black')

for i in range(len(cities)):

    ax.add_patch(C(xy = (x_translated_cities[i], y_translated_cities[i]),
                   radius = 20,
                   facecolor = "blue",
                   linewidth = 1,
                   edgecolor = "gray"))

    plt.text(x_translated_cities[i], y_translated_cities[i], cities[i].getname(), ha = 'center')

plt.gca().set_aspect('equal')
plt.show()
