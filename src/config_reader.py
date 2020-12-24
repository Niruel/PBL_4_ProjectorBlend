#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser
import image_rw

class ConfigReader(object):

    def __init__ (self, filename):
        self.config = configparser.ConfigParser()
        self.config.read(filename)
        
    def getDistance(self):
        return float(self.config['projector_distance']['between_projector_distance'])

    def getWidth(self):
        return float(self.config['projector_distance']['projector_image_width'])

    def getIMGWidth(self):
        return int(self.config['image']['img_width'])

    def getIMGHeight(self):
        return int(self.config['image']['img_height'])

    def getIMGName(self):
        return self.config['image']['img_name']

    def getGamma(self):
        return float(self.config['gamma_correction']['gamma'])