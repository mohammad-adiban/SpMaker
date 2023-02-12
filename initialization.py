import requests
import json
import mysql.connector
import geopandas as gpd
from shapely.geometry import Point, LineString, Polygon, MultiPolygon
from shapely.ops import cascaded_union
import fiona

def assign_values(url):
    response = requests.get(url)
    inputs = response.json()
    building_limits_coordinates = inputs['building_limits']['features'][0]['geometry']['coordinates'][0]
    height_plateaus_coordinates = []
    height_plateaus_elevations = []
    labels = ['Building Limits']
    polys = [Polygon(building_limits_coordinates)]
    hareas = 0
    hpolys = []

    reqs = inputs['request']
    inputId = inputs['inputID']
    for i in range(len(inputs['height_plateaus']['features'])):
        height_plateaus_coordinates.append(inputs['height_plateaus']['features'][i]['geometry']['coordinates'][0])
        height_plateaus_elevations.append(inputs['height_plateaus']['features'][i]['properties']['elevation'])
        labels.append("Height Plateaus , "+"elevations: "+ str(height_plateaus_elevations[i]))
        #Each Height Plateaus Coordinate MUST NOT exceed the Bulding Area Limitations
        polys.append(polys[0].intersection(Polygon(height_plateaus_coordinates[i])))
        hareas += polys[i+1].area
        hpolys.append(polys[i+1])
    
    return building_limits_coordinates, height_plateaus_coordinates, height_plateaus_elevations, labels, polys, hareas, hpolys,reqs, inputId

class Initialization():
    def __init__(self, url):
        self.url = url
        
    def values (self):   
        bh_vals = assign_values(self.url)
        self.building_limits_coordinates = bh_vals[0]
        self.height_plateaus_coordinates = bh_vals[1]
        self.height_plateaus_elevations = bh_vals[2]
        self.labels = bh_vals[3]
        self.polys = bh_vals[4]
        self.hareas = bh_vals[5]
        self.hpolys = bh_vals[6]
        self.reqs = bh_vals[7]
        self.inputId = bh_vals[8]
