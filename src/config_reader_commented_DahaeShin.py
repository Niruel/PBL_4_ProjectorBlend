#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅

# ˄
"""
@brief
Config Reader class
"""
import config
"""
@brief       main function
@attention   configuration of the main function
"""
class ConfigReader(object):
    # ˅
    def __init__ (self, filename):
        self.config = config.ConfigParser()
        """
        @brief the configure type that puts
        """
        self.config.read(filename)
        """
        @brief this is a configure type variable that reads the file's name.
        """
    # ˄

    def getDistance(self):
        """
        @brief      defining the method that is used to return int value assigned to variable 'projector_distance' which holds the distance value between the projectors
        @param[in]  float 'between_projector_distance' imported from config file
        @param[out] returns value of 'between_projector_distance'
        """
        # ˅
        return float(self.config(['projector_distance']['between_projector_distance']))
        # ˄

    def getWidth(self):
        """
        @brief      defining the method that os used to get the width of the image
        @param[in]  float 'half_projector_distance' imported from config file
        @param[out] returns value of 'half_projector_distance'
        """
        # ˅
        return float(self.config(['projector_distance']['half_projector_distance']))
        # ˄

    def getIMGWidth(self):
        """
        @brief      definig the method that returns the int value assigned to variable 'img_width'  which holds the pixel value of width of
                    the image/Users/jaketian/Desktop/pbl4 respository/trunk/src/sally's part/config_DahaeShin.py
                    @param[in]  int 'img_width' imported from config file
        @param[out] returns value of 'img_width'
        """
        # ˅
        return int(self.config(['image']['img_width']))
        # ˄

    def getIMGHeight(self):
        """
        @brief      defining the method that returns the int value assigned to variable 'img_height' which holds the pixel value of height of the image
        @param[in]  int 'img_height' imported from config file
        @param[out] returns value of 'img_height'
        """
        # ˅
        return int(self.config(['image']['img_height']))
        # ˄

    def getImageName(self):
        """
        @brief      defining the method that returns the string value assigned to variable 'image_name' which holds the name of the iamge
        @param[in]  string 'img_name' imported from config file
        @param[out] returns value of 'img_name'
        """
        # ˅
        return int(self.config(['image']['img_name']))
        # ˄

    def getGamma(self):
        """
        @brief      defining the method that corrects the gamma value(brightness of the iamge)
        @param[in]  float 'gamma' imported from config file
        @param[out] returns value of 'gamma'
        """
        # ˅
        return float(self.config(['gamma_correction']['gamma']))
        # ˄

    def getProjectionType1(self):
        """
        @brief      defining the method that returns the assigned value of the variable 'projection_type'
        @param[in]  int 'projector1' imported from config file
        @param[out] returns value of 'projector1'
        """
        # ˅
        return int(self.config(['projection_type']['projector1']))
        # ˄
        
    def getProjectionType2(self):
        """
        @brief      defining the method that returns the assigned value of the variable 'projection_type'
        @param[in]  int 'projector2' imported from config file
        @param[out] returns value of 'projector2'
        """
        # ˅
        return int(self.config(['projection_type']['projector2']))
        # ˄

    def Update(self):
        """
        @breif      defining the method that updates the arrangement
        """
        # ˅
        pass
        # ˄

    # ˅
    # ˄


# ˅
# ˄
