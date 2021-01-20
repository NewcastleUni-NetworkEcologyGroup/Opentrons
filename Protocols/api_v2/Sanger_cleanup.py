#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 11:53:00 2019

@author: neg
"""

from opentrons import protocol_api

# metadata
metadata = {'apiLevel': '2.8',
            'protocolName': 'SPRI Sanger cleanup',
            'author': 'James Kitson',
            'description': 'SPRI cleanups for Sanger Seq'}

# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions

def run(protocol: protocol_api.ProtocolContext):

    # labware for protocol
    reservoir = protocol.load_labware('sarstedt_96_wellplate_2200ul',2)
    tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', 3)
    tiprack_200 = protocol.load_labware('opentrons_96_filtertiprack_200ul', 6)
    
    # magnetic module and labware on it
    mag_mod = protocol.load_module('magdeck', 1)
    magplate = mag_mod.load_labware('sarstedt_96_wellplate_200ul',
                                      label='Samples')
    
    # pipettes
    left_pipette = protocol.load_instrument('p50_multi', mount='left', tip_racks=[tiprack_300])
    right_pipette = protocol.load_instrument('p300_multi', mount='right', tip_racks=[tiprack_200])
    
    ##### Step 1 - Wait for 5 minutes then apply magnets for 5 minutes
    protocol.delay(minutes = 5, msg = 'Binding DNA to SPRI beads')
    mag_mod.engage(height=18.5)
    protocol.delay(minutes = 5, msg = 'Separating SPRI beads from supernatant')
    
    #### Step 2 - Remove the supernatant
    # set pipetting parameters
    right_pipette.flow_rate.aspirate = 10
    right_pipette.flow_rate.dispense = 150
    right_pipette.flow_rate.blow_out = 150
    right_pipette.well_bottom_clearance.dispense = 30
    
    # pipette out the bulk of the liquid
    right_pipette.well_bottom_clearance.aspirate = 1.5
    right_pipette.consolidate(30, magplate.rows_by_name()['A'], protocol.fixed_trash['A1'],
                              blow_out=True)
    # drop pipette height and aspirate speed then pipette out the remainder of the liquid
    right_pipette.flow_rate.aspirate = 5
    right_pipette.well_bottom_clearance.aspirate = 0.1
    right_pipette.consolidate(30, magplate.rows_by_name()['A'], protocol.fixed_trash['A1'],
                              blow_out=True)
    
    #### Step 3 - Ethanol wash 1
    # Set the pipetting parameters back to normal and distribute the ethanol - this needs some liquid tracking
    right_pipette.distribute(150, reservoir['A1'],magplate.rows_by_name()['A'],
                             air_gap = 10,
                             blow_out=True,
                             blowout_location='source well')
    
    #### Step 4 - Ethanol wash 2
    
    #### Step 5 - Dry SPRI beads
    
    #### Step 5 - Elute
    # Disengage magnets
    # Add water ot 10mM Tris-HCl