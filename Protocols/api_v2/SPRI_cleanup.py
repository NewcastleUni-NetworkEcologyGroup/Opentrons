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
    reservoir = protocol.load_labware('nest_12_reservoir_15ml',2)
    tiprack_1 = protocol.load_labware('opentrons_96_filtertiprack_200ul', 3)
    tiprack_2 = protocol.load_labware('opentrons_96_filtertiprack_200ul', 6)
    tiprack_3 = protocol.load_labware('opentrons_96_filtertiprack_200ul', 9)
    outplate = protocol.load_labware('sarstedt_96_unskirted_wellplate_200ul', 5,
                                      label='Cleaned samples')
    
    # magnetic module and labware on it
    mag_mod = protocol.load_module('magdeck', 1)
    magplate = mag_mod.load_labware('sarstedt_96_skirted_wellplate_200ul',
                                      label='Samples')
    
    # pipettes
    left_pipette = protocol.load_instrument('p50_multi', mount='left', tip_racks=[tiprack_1, tiprack_2, tiprack_3])
    right_pipette = protocol.load_instrument('p300_multi', mount='right', tip_racks=[tiprack_1, tiprack_2,tiprack_3])
    
    # Create a list of target wells  and step numbers to iterate across so we can change aspirate heights when needed
    well_name = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12']
    steps=len(well_name)
    
    # Set liquid starting heights
    Ethanol_start_height = 30
    Tris_start_height = 20
    
    ##### Step 1 - Wait for 5 minutes then apply magnets for 5 minutes ####
    #protocol.delay(minutes = 5, msg = 'Binding DNA to SPRI beads')
    mag_mod.engage(height=18.5)
    #protocol.delay(minutes = 5, msg = 'Separating SPRI beads from supernatant')
    
    #### Step 2 - Remove the supernatant ####
    # set pipetting parameters
    right_pipette.flow_rate.aspirate = 10 # slow here as SPRI mix is viscous
    right_pipette.flow_rate.dispense = 150 # this doesn't matter as it's dispensing to 'trash'
    right_pipette.flow_rate.blow_out = 150 # this doesn't matter as it's dispensing to 'trash'
    right_pipette.well_bottom_clearance.dispense = 30 # I just want this a bit down in the 'trash' in case of splattering
    
    # pipette out the bulk of the liquid
    right_pipette.well_bottom_clearance.aspirate = 1.5 # near the bottom but with a gap
    right_pipette.consolidate(30, magplate.rows_by_name()['A'], protocol.fixed_trash['A1'],
                              blow_out=True)
    # drop pipette height and aspirate speed then pipette out the remainder of the liquid
    right_pipette.flow_rate.aspirate = 5
    right_pipette.well_bottom_clearance.aspirate = 0.1 # as close as we can get to the bottom and half the previous speed
    right_pipette.consolidate(30, magplate.rows_by_name()['A'], protocol.fixed_trash['A1'],
                              blow_out=True)
    
    #### Step 3 - Ethanol wash 1 ####
    # Set the dispense height and rate to a reasonable gentle height that doesn't end up with too much tip in the liquid
    right_pipette.well_bottom_clearance.dispense = 5 # near the bottom but not too near to make sure the tip doesn't block
    ######## fix aspirate heights, all above well top!! - could be cghange from 2.2ml plate to nest 12
    ######## !!set fast aspirate here
    ######## all of this can be much faster
    right_pipette.flow_rate.dispense = 50 # gentle dispense rate to preserve beads
    # Set the aspirate height to the starting ethanol height
    right_pipette.well_bottom_clearance.aspirate = Ethanol_start_height
    # Distribute Ethanol to all columns dropping the aspirate height after every transfer
    right_pipette.pick_up_tip()
    for well in well_name:
        print(right_pipette.well_bottom_clearance.aspirate) # this is just a sense check and can go once the protocol is tested
        right_pipette.transfer(150, reservoir['A1'],
                               magplate.wells_by_name()[well],
                               air_gap = 10,
                               blow_out=True,
                               blowout_location='source well',
                               new_tip = 'never')
        right_pipette.well_bottom_clearance.aspirate = round(right_pipette.well_bottom_clearance.aspirate-(Ethanol_start_height/steps),1)
    right_pipette.drop_tip() 
    
    # Pause briefly for ethanol wash
    ##protocol.delay(seconds = 10, msg = 'Washing beads')
    
    # Remove the bulk of the ethanol
    right_pipette.flow_rate.aspirate = 100 # the first aspirate can be quite fast
    right_pipette.well_bottom_clearance.aspirate = 3 # not right at the bottom to keep liquid flow around the beads gentle
    right_pipette.consolidate(100, magplate.rows_by_name()['A'], protocol.fixed_trash['A1'],
                              blow_out=True)
    # drop pipette height and aspirate speed then pipette out the remainder of the ethanol
    right_pipette.flow_rate.aspirate = 10 # slowing right down as we're pipetting very close to the bottom and don't want to disturb the beads
    right_pipette.well_bottom_clearance.aspirate = 0.1
    right_pipette.consolidate(100, magplate.rows_by_name()['A'], protocol.fixed_trash['A1'],
                              blow_out=True)
       
        
    #### Step 4 - Ethanol wash 2 ####
    # Set the dispense height and rate to a reasonable gentle height that doesn't end up with too much tip in the liquid
    right_pipette.well_bottom_clearance.dispense = 5 # near the bottom but not too near to make sure the tip doesn't block
    right_pipette.flow_rate.dispense = 50 # gentle dispense rate to preserve beads
    # Set the aspirate height to the starting ethanol height
    right_pipette.well_bottom_clearance.aspirate = Ethanol_start_height
    # Distribute Ethanol to all columns dropping the aspirate height after every transfer
    right_pipette.pick_up_tip()
    for well in well_name:
        print(right_pipette.well_bottom_clearance.aspirate) # this is just a sense check and can go once the protocol is tested
        right_pipette.transfer(150, reservoir['A2'],
                               magplate.wells_by_name()[well],
                               air_gap = 10,
                               blow_out=True,
                               blowout_location='source well',
                               new_tip = 'never')
        right_pipette.well_bottom_clearance.aspirate = round(right_pipette.well_bottom_clearance.aspirate-(Ethanol_start_height/steps),1)
    right_pipette.drop_tip() 
    
    # Pause briefly for ethanol wash
    #protocol.delay(seconds = 10, msg = 'Washing beads')
    
    # Remove the bulk of the ethanol
    right_pipette.flow_rate.aspirate = 100 # the first aspirate can be quite fast
    right_pipette.well_bottom_clearance.aspirate = 3 # not right at the bottom to keep liquid flow around the beads gentle
    right_pipette.consolidate(100, magplate.rows_by_name()['A'], protocol.fixed_trash['A1'],
                              blow_out=True)
    # drop pipette height and aspirate speed then pipette out the remainder of the ethanol
    right_pipette.flow_rate.aspirate = 10 # slowing right down as we're pipetting very close to the bottom and don't want to disturb the beads
    right_pipette.well_bottom_clearance.aspirate = 0.1
    right_pipette.consolidate(100, magplate.rows_by_name()['A'], protocol.fixed_trash['A1'],
                              blow_out=True)
    
    #### Step 5 - Dry SPRI beads ####
    mag_mod.engage(height=13.5)
    #protocol.delay(minutes = 2, msg = 'Pulling beads down')
    mag_mod.disengage()
    #protocol.delay(minutes = 8, msg = 'Drying beads')
    
    #### Step 5 - Elute ####
    # Add water ot 10mM Tris-HCl
    # Set the dispense height and rate to a reasonable gentle height that doesn't end up with too much tip in the liquid
    left_pipette.well_bottom_clearance.dispense = 5 # near the bottom but not too near to make sure the tip doesn't block
    left_pipette.flow_rate.dispense = 150 # doesn't really matter and a good rate will help mix beads
    # Set the aspirate height to the starting ethanol height
    left_pipette.well_bottom_clearance.aspirate = Tris_start_height
    # Distribute Ethanol to all columns dropping the aspirate height after every transfer
    left_pipette.pick_up_tip()
    for well in well_name:
        print(left_pipette.well_bottom_clearance.aspirate) # this is just a sense check and can go once the protocol is tested
        left_pipette.transfer(22, reservoir['A3'],
                               magplate.wells_by_name()[well],
                               air_gap = 5,
                               blow_out=True,
                               blowout_location='source well',
                               new_tip = 'never')
        left_pipette.well_bottom_clearance.aspirate = round(left_pipette.well_bottom_clearance.aspirate-(Tris_start_height/steps),1)
    left_pipette.drop_tip() 
    
    #### Step 6 - pause, cover and shake ####
    protocol.pause(
            "Remove skirted plate from magdeck, cover with PCR film and shake on plate shaker for 2 minutes at 1400 rpm, take of lid, return to magdeck and resume protocol")
    
    # Wait 5 min
    #protocol.delay(minutes = 5, msg = 'Waiting for DNA to elute')
    
    # Engage magnets for 5 min
    mag_mod.engage(height=18.5)
    #protocol.delay(minutes = 5, msg = 'Separating SPRI beads')
    
    #### Step 7 - Transfer to unskirted plate for genetic analyser ####
    left_pipette.transfer(20, magplate.rows_by_name()['A'],
                       outplate.rows_by_name()['A'],
                       air_gap = 5,
                       blow_out=False,
                       new_tip = 'always')