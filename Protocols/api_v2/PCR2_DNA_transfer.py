#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 12:02:38 2021

@author: neg
"""
from opentrons import protocol_api

# metadata
metadata = {'apiLevel': '2.8',
            'protocolName': 'DNA transfer to PCR plate',
            'author': 'James Kitson <james.kitson@newcastle.ac.uk>',
            'description': 'A protocol to distribute template DNA into a target PCR plate'}

# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions

def run(protocol: protocol_api.ProtocolContext):
      
    # set up the reagent locations
    DNA_plate = protocol.load_labware('sarstedt_96_unskirted_wellplate_200ul_on_coldblock',5,'Source DNA plate')
    PCR_plate = protocol.load_labware('sarstedt_96_skirted_wellplate_200ul',8,'Target PCR plate')
    
    # set up tip locations
    tiprack_20 = protocol.load_labware('opentrons_96_filtertiprack_20ul', 2)
    
    # set up pipettes
    pipette_10 = protocol.load_instrument('p10_multi', mount='right', tip_racks=[tiprack_20]) 
    pipette_10.well_bottom_clearance.aspirate = 2
    pipette_10.well_bottom_clearance.dispense = 2
  
    Sources = DNA_plate.rows_by_name()['A']
    Dests = PCR_plate.rows_by_name()['A']
  
    pipette_10.transfer(2,
                    Sources,
                    Dests,
                    mix_before=(5,5),
                    disposal_volume=0.5,
                    new_tip='always')

 
          