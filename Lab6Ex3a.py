from Point import Point
from Rectangle import Rectangle
import matplotlib.pyplot as plt
from matplotlib.patches import Circle as C
import json

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

# pass scale
for i in range(len(pts)):

    pts[i].setX(x[i] * scale)
    pts[i].setY(y[i] * scale)

# centre point
xTranslation = 500 - bbox.centroid().getX() * scale
yTranslation = 500 - bbox.centroid().getY() * scale

# translate coordinates
x_translated = list(range(len(pts)))
y_translated = list(range(len(pts)))
for i in range(len(pts)):

    x_translated[i] = pts[i].getX() + xTranslation
    y_translated[i] = pts[i].getY() + yTranslation

# plot cities
fig, ax = plt.subplots()
ax.plot(1000, 1000)

for i in range(len(pts)):

    plt.plot(x_translated[i], y_translated[i], marker='o', color = 'black')

plt.gca().set_aspect('equal')
plt.show()

