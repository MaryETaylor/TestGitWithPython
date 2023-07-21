# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 13:45:48 2023

@author: brave
"""
import gpxpy
import gpxpy.gpx

from math import radians, cos, sin, asin, sqrt

gpx_file = open(r"C:\Users\brave\Downloads\Carr Peak via Old Sawmill Spring Trail.gpx", 'r')

gpx = gpxpy.parse(gpx_file)




def distance(lat1, lat2, lon1, lon2):
     
    # The math module contains a function named
    # radians which converts from degrees to radians.
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
      
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
 
    c = 2 * asin(sqrt(a))
    
    # Radius of earth in kilometers (6371). Use 3956 for miles
    r = 3956
      
    # calculate the result
    return(c * r)
     
     
# driver code
totalDistance = 0
totalDistanceWithElevation= 0
for track in gpx.tracks:
    for segment in track.segments:
        for i in range(len(segment.points)-1):
            firstPoint = segment.points[i]
            secondPoint = segment.points[i+1]
            shortDistance = distance(firstPoint.latitude, secondPoint.latitude, firstPoint.longitude, secondPoint.longitude)
           
            eleDistance = sqrt(shortDistance**2 + ((secondPoint.elevation - firstPoint.elevation)/5280)**2)
            
            totalDistance += shortDistance
            totalDistanceWithElevation += eleDistance

print("Distance without Elevation: ", totalDistance)
print("Distance with Elevation", totalDistanceWithElevation)
print((totalDistanceWithElevation-totalDistance)*5280)
