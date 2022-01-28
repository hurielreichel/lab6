import csv
from City import City

# open the CSV file
with open("data.csv", mode = 'r') as file:
    # read the CSV file
    csvFile = csv.reader(file)

    cities = []
    for lines in csvFile:

        cities.append(City(lines[0],lines[1],lines[2],lines[3],lines[4],lines[5],lines[6]))

    for i in range(len(cities)):

        print(cities[i].getname())
        print(cities[i].getlocation())
        print(cities[i].getarea())
        print(cities[i].getpopulation())
        print(cities[i].getdensity())
        print(cities[i].getgdp())
        print(cities[i].getelevation())
        print("\n")
