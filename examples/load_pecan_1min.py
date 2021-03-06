from __future__ import print_function
from nilmtk.dataset import pecan

pecan_1min = pecan.Pecan_1min()

# Name of buildings
pecan_1min.load_building_names('/home/nipun/Desktop/PECAN/')

# Loading data for Home 01
pecan_1min.load_building('/home/nipun/Desktop/PECAN/', 'Home 01')

# Accessing Home 01 Building
building = pecan_1min.buildings['Home_01']

# Summary of Mains
print("Mains summary")
print(building.utility.electric.mains.describe())

# Summary of appliances
print("Appliances summary")
for appliance in building.utility.electric.appliances:
    print(building.utility.electric.appliances[appliance].describe())

# Loading all buildings data
pecan_1min_complete = pecan.Pecan_1min()
pecan_1min_complete.load('/home/nipun/Desktop/PECAN/')

