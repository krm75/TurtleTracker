# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 12:52:09 2019

@author: krm75
"""


# Copy and paste a line of data as the lineString variable value
lineString = "20616	29051	7/3/2003 9:13	3	66	33.898	-77.958	27.369	-46.309	6	0	-126	529	3	401 651134.7	0"

# Use the split command to parse the items in lineString into a list object
lineData = lineString.split("\t")

# Assign variables to specfic items in the list
recordID = lineData[0]              # ARGOS tracking record ID
obsDateTime = lineData[2]           # Observation date and time (combined)
obsDate = obsDateTime.split()[0]    # Observation date - first item in obsDateTime list object
obsTime = obsDateTime.split()[1]    # Observation time - second item in obsDateTime list object
obsLC = lineData[3]                 # Observation Location Class
obsLat = lineData[5]                # Observation Latitude
obsLon = lineData[6]                # Observation Longitude

# Print information to the use
print ("Record {0} indicates Sara was seen at {1}N and {2}W on {3}".format(recordID, obsLat,obsLon,obsDate))

#.readline() is a function to read the next line
#.readlines() is a function to read all lines at or below the cursor
#.seek(0) to bring the cursor back up to the top
#open('filename', 'r' (read-mode) or 'w' (write-mode)) pulls in a file
