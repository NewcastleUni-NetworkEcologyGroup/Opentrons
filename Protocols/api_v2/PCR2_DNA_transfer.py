#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 12:02:38 2021

@author: neg
"""
from opentrons import protocol_api

# metadata
metadata = {'apiLevel': '2.8',
            'protocolName': 'PCR1 to PCR2 transfer',
            'author': 'James Kitson <james.kitson@newcastle.ac.uk>',
            'description': 'A protocol to distribute template DNA into a target PCR plate'}

# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions

def run(protocol: protocol_api.ProtocolContext):
      
    # set up the reagent locations
    PCR2_plate = protocol.load_labware('sarstedt_96_unskirted_wellplate_200ul_on_coldblock',7,'Destination PCR2 plate')
    
    # magnetic module and labware on it
    mag_mod = protocol.load_module('magdeck', 1)
    PCR1_plate = mag_mod.load_labware('sarstedt_96_skirted_wellplate_200ul',
                                      label='Source PCR1 plate')
    
    # set up tip locations
    tiprack_20 = protocol.load_labware('opentrons_96_filtertiprack_20ul', 10)
    
    # set up pipettes
    pipette_10 = protocol.load_instrument('p10_multi', mount='left', tip_racks=[tiprack_20]) 
    pipette_10.well_bottom_clearance.aspirate = 2
    pipette_10.well_bottom_clearance.dispense = 2
    
    # Separate the beads from the cleaned PCR1
    mag_mod.engage(height=19)
    protocol.delay(minutes = 2, msg = 'Separating SPRI beads from PCR1')
    
    # set up sources and destinations then do DNA transfer
    Sources = PCR1_plate.rows_by_name()['A']
    Dests = PCR2_plate.rows_by_name()['A']
    
    pipette_10.transfer(5,
                    Sources,
                    Dests,
                    disposal_volume=0.5,
                    new_tip='always')

 
          