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

#Ignore the following lines
files  = [f for f in listdir(path) if isfile(join(path, f))]
files.sort() #Sorting important for indexing later
phall = files[0::3] #every thrird element starting from 0 is phalloidin
yap = files[1::3] #every thrird element starting from 1 is yap
dapi = files[2::3] #every thrird element starting from 2 is dapi

#renaming Phall
for index, filename in enumerate(phall): 
        if filename.endswith(".tif"):
                my_dest = condition + "_Phalloidin" + str(index) + ".tif"
                my_source = path + filename
                my_dest = path + my_dest
                # rename() function will
                # rename all the files
                os.rename(my_source, my_dest)

#Renaming Yap
for index, filename in enumerate(yap): 
        if filename.endswith(".tif"):
                my_dest =condition + "_Yap" + str(index) + ".tif"
                my_source = path + filename
                my_dest =path + my_dest
                # rename() function will
                # rename all the files
                os.rename(my_source, my_dest)
        
#Renaming Dapi
for index, filename in enumerate(dapi): 
        if filename.endswith(".tif"):
                my_dest =condition + "_Dapi" + str(index) + ".tif"
                my_source = path + filename
                my_dest =path + my_dest
                # rename() function will
                # rename all the files
                os.rename(my_source, my_dest)