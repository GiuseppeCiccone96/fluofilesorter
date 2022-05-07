"""
Created on Thu Dec 17 15:04:33 2020

@author: giuseppeciccone
"""
import os
from os import listdir
from os.path import isfile, join


#Path where images are saved (ie folder)
path="/Users/giuseppeciccone/Desktop/Pos0/" 
#Name of the sample imaged
condition = "glass"
#Name of channels (example)
channel_1 = "_Phalloidin"
channel_2 = "_Yap"
channel_3 = "_Dapi"

#Ignore the following lines
files  = [f for f in listdir(path) if isfile(join(path, f))]
files.sort() #Sorting important for indexing later
channel1 = files[0::3] #every thrird element starting from 0 is channel1
channel2 = files[1::3] #every thrird element starting from 1 is channel2
channel3 = files[2::3] #every thrird element starting from 2 is channel3

#renaming channel 1
for index, filename in enumerate(channel1): 
        if filename.endswith(".tif"):
                my_dest = condition + channel_1  + str(index) + ".tif"
                my_source = path + filename
                my_dest = path + my_dest
                # rename() function will
                # rename all the files
                os.rename(my_source, my_dest)

#renaming channel 2
for index, filename in enumerate(channel2): 
        if filename.endswith(".tif"):
                my_dest =condition + channel_2 + str(index) + ".tif"
                my_source = path + filename
                my_dest =path + my_dest
                # rename() function will
                # rename all the files
                os.rename(my_source, my_dest)
        
#renaming channel 3
for index, filename in enumerate(channel3): 
        if filename.endswith(".tif"):
                my_dest =condition + channel_3 + str(index) + ".tif"
                my_source = path + filename
                my_dest =path + my_dest
                # rename() function will
                # rename all the files
                os.rename(my_source, my_dest)

