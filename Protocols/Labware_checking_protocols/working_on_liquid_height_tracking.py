#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 13:33:28 2019

@author: neg
"""

distance_from_oil_surface_to_opening_of_trough_in_mm: float = 10
vol_transfer: float = 10
length=6
width=6


# variables for mineral oil height track
h_liquid = -(distance_from_oil_surface_to_opening_of_trough_in_mm + 5)

def height_track():
    global h_liquid
    dh = vol_transfer/(length*width) # should this be 8*volume_of_mineral_oil_in_ul for a trough?
    h_liquid -= dh
    
height_track()

