##
#Documentation for the main class
#The whole class is to read the configuration from init

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
## importing external libraries
import configparser

## Main class is config_reader
# The class is for reading the values of the image
class ConfigReader(object):

    ## main class
    # The constructor, defining all the methods of the main class(configure values of the image)
    # @param self object pointer
    def __init__ (self, filename):
        self.config = configparser.ConfigParser()
        self.config.read(filename)
        
## The class is used to retrieve the distance between the projectors
# @param self is the object pointer, points to the class itself
    def getDistance(self):
        return float(self.config['projector_distance']['between_projector_distance'])

## The class is used to retrieve width of the image being projected on the screen
# @param self is the object pointer, points to the class itself
    def getWidth(self):
        return float(self.config['projector_distance']['projector_image_width'])

## The class is used to retrieve the actual width value of the image( how many pixels is the iamge width comprised of)
# @param self is the object pointer, points to the class itself
    def getIMGWidth(self):
        return int(self.config['image']['img_width'])

## The class is used to retrieve the actual height value of the image( how many pixels is the iamge height comprised of)
# @param self is the object pointer, points to the class itself
    def getIMGHeight(self):
        return int(self.config['image']['img_height'])

## The class is used to retrieve the name of the image ( assigned string value of the image name variable)
# @param self is the object pointer, points to the class itself
    def getIMGName(self):
        return self.config['image']['img_name']

## The class is used to retrieve the gamma value of image, used for gamma correction
# @param self is the object pointer, points to the class itself
    def getGamma(self):
        return float(self.config['gamma_correction']['gamma'])
