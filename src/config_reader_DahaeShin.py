#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅

# ˄
import config

class ConfigReader(object):
    # ˅
    def __init__ (self, filename):
        self.config = config.ConfigParser()
        self.config.read(filename)
    # ˄

    def getDistance(self):
        # ˅
        return float(self.config(['projector_distance']['between_projector_distance']))
        # ˄

    def getWidth(self):
        # ˅
        return float(self.config(['projector_distance']['half_projector_distance']))
        # ˄

    def getIMGWidth(self):
        # ˅
        return int(self.config(['image']['img_width']))
        # ˄

    def getIMGHeight(self):
        # ˅
        return int(self.config(['image']['img_height']))
        # ˄

    def getImageName(self):
        # ˅
        return int(self.config(['image']['img_name']))
        # ˄

    def getGamma(self):
        # ˅
        return float(self.config(['gamma_correction']['gamma']))
        # ˄

    def getProjectionType(self):
        # ˅
        return int(self.config(['projection_type']['projector1']))
        # ˄

    def Update(self):
        # ˅
        pass
        # ˄

    # ˅
    # ˄


# ˅
# ˄
