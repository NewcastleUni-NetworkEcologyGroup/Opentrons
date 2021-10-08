#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 11:53:00 2019

@author: neg
"""

from opentrons import protocol_api

# metadata
metadata = {'apiLevel': '2.8',
            'protocolName': 'SPRI Normalisations',
            'author': 'James Kitson',
            'description': 'SPRI Normalisations for Illumina sequencing'}

# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions

def run(protocol: protocol_api.ProtocolContext):

    # labware for protocol
    reservoir = protocol.load_labware('nest_12_reservoir_15ml',2)
    tiprack_1 = protocol.load_labware('opentrons_96_filtertiprack_200ul', 3, "Tips for SPRI process")
    tiprack_2 = protocol.load_labware('opentrons_96_filtertiprack_200ul', 6)
    tiprack_3 = protocol.load_labware('opentrons_96_filtertiprack_20ul', 9, "Tips for PCR product transfer")
    source_plate = protocol.load_labware('sarstedt_96_skirted_wellplate_200ul', 10, "PCRs to be cleaned")

    waste = protocol.load_labware('sarstedt_96_wellplate_2200ul', 7, "waste plate")
    
    # key labware dimensions
    tip_height = 3
    well_width =8.2
    well_length = 71.2
    
    # magnetic module and labware on it
    mag_mod = protocol.load_module('magdeck', 1)
    magplate = mag_mod.load_labware('sarstedt_96_skirted_wellplate_200ul',
                                      label='Cleaned samples')
    
    # pipettes
    right_pipette = protocol.load_instrument('p10_multi', mount='right', tip_racks=[tiprack_3])
    left_pipette = protocol.load_instrument('p300_multi', mount='left', tip_racks=[tiprack_1, tiprack_2])
    
    # Create a list of target wells and step numbers to iterate across so we can change aspirate heights when needed
    well_name = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12']
    steps=len(well_name)

    # create a function that works out the starting liquid height
    def start_height(start_vol, tip_height, well_width, well_length):
        # define the volume of the tip of the well tip
        #tip_vol = ((tip_height*well_width)/2)*well_length
        tip_vol = (well_length*well_width*tip_height)/2
        # if the start volume > tip volume, work out the residual height, add it to the tip height and subrtact it from the total height of the tube
        if start_vol > tip_vol:
            return round(tip_height+((start_vol-tip_vol)/(well_width*well_length)),1)
        # if the starting volume is less than the tip volume, work out the total height and subrtact it from the total height of the tube
        else:
            return (2*start_vol)/(well_length*well_width)
    
    # Key reagent volumes
    Ethanol_wash_vol=100
    Ethanol_start_vol=96*Ethanol_wash_vol*1.2
    Tris_elute_vol=22
    Tris_start_vol=96*Tris_elute_vol*1.2
    
    # Set liquid starting heights
    Ethanol_start_height = start_height(Ethanol_start_vol, tip_height, well_width, well_length)
    Tris_start_height = start_height(Tris_start_vol, tip_height, well_width, well_length)

    # Print out the starting volumes and heights as a sense check
    print("The initial ethanol volume in reservoir wells A1 and A2 is: ", end='')
    print(Ethanol_start_vol)
    print("The initial ethanol height in reservoir wells A1 and A2 is: ", end='')
    print(Ethanol_start_height)
    print("The initial tris volume in reservoir well A10 is: ", end='')
    print(Tris_start_vol)
    print("The initial tris height in reservoir well A10 is: ", end='')
    print(Tris_start_height)
    
    # set up pipettes
    right_pipette.well_bottom_clearance.aspirate = 2
    right_pipette.well_bottom_clearance.dispense = 2 
    ticker=0
    
    ##### Step 1 - Transfer PCR products to magdeck and mix ####
    # Using a loop pick up PCR products and mix 
    #for source_well, idx in enumerate(source_plate.rows_by_name()['A']):
    for source_well in source_plate.rows_by_name()['A']:
        right_pipette.pick_up_tip()
        # pipette off most of the ethanol
        right_pipette.aspirate(10, source_well.bottom(0.3))
        # step up releasing any blockages and giving liquid time to flow into the pipette
        protocol.delay(seconds = 1)
        right_pipette.move_to(source_well.bottom(0.5))
        protocol.delay(seconds = 1)
        right_pipette.move_to(source_well.bottom(0.7))
        protocol.delay(seconds = 1)
        right_pipette.move_to(source_well.bottom(0.9))
        protocol.delay(seconds = 1)
        right_pipette.move_to(source_well.bottom(1.1))
        protocol.delay(seconds = 1)
        right_pipette.move_to(source_well.top(-2))
        protocol.delay(seconds = 2)
        right_pipette.touch_tip(source_well, radius=0.75,v_offset=-2, speed=25)
        
        right_pipette.dispense(10, magplate.rows_by_name()['A'][ticker].bottom(2))
        right_pipette.mix(5, 10, magplate.rows_by_name()['A'][ticker].bottom(2))
        right_pipette.mix(5, 10, magplate.rows_by_name()['A'][ticker].bottom(4))
        right_pipette.mix(5, 10, magplate.rows_by_name()['A'][ticker].bottom(6))
        right_pipette.touch_tip(magplate.rows_by_name()['A'][ticker], radius=0.75,v_offset=-5, speed=25)
        right_pipette.drop_tip() 
        ticker = ticker+1
    
    
    ##### Step 2 - Wait for 5 minutes then apply magnets for 5 minutes ####
    protocol.delay(minutes = 5, msg = 'Binding DNA to SPRI beads')
    mag_mod.engage(height=15)
    protocol.delay(minutes = 5, msg = 'Separating SPRI beads from supernatant')
    
    #### Step 2 - Remove the supernatant ####
    # set pipetting parameters
    left_pipette.flow_rate.aspirate = 10 # slow here as SPRI mix is viscous
    left_pipette.flow_rate.dispense = 150 # this doesn't matter as it's dispensing to 'trash'
    left_pipette.flow_rate.blow_out = 150 # this doesn't matter as it's dispensing to 'trash'
    #left_pipette.well_bottom_clearance.dispense = 30 # I just want this a bit down in the 'trash' in case of splattering
    
    # Using a loop pick up supernatant and step the pipette height up in increments to release the pressure on blocked tips
    left_pipette.pick_up_tip()
    for target_well in magplate.rows_by_name()['A']:
        # pipette off most of the supernatant
        left_pipette.aspirate(50, target_well.bottom(1.5))
        # move down and pipette off the rest
        left_pipette.aspirate(30, target_well.bottom(0.3))
        # step up releasing any blockages and giving liquid time to flow into the pipette
        protocol.delay(seconds = 1)
        left_pipette.move_to(target_well.bottom(0.5))
        protocol.delay(seconds = 1)
        left_pipette.move_to(target_well.bottom(0.7))
        protocol.delay(seconds = 1)
        left_pipette.move_to(target_well.bottom(0.9))
        protocol.delay(seconds = 1)
        left_pipette.move_to(target_well.bottom(1.1))
        protocol.delay(seconds = 1)
        left_pipette.move_to(target_well.bottom(1.3))
        protocol.delay(seconds = 1)
        left_pipette.touch_tip(target_well, radius=0.50,v_offset=-5, speed=25)
        # put it all in the waste
        left_pipette.blow_out(waste['A1'].top(-10))
        left_pipette.touch_tip(waste['A1'], radius=0.80,v_offset=-5, speed=25)
    left_pipette.drop_tip()

    #### Step 4 - Ethanol wash 1 ####
    # Set the dispense height and rate to a reasonable gentle height that doesn't end up with too much tip in the liquid
    left_pipette.well_bottom_clearance.dispense = 10 # near the bottom but not too near to make sure the tip doesn't block
    left_pipette.flow_rate.aspirate = 100
    left_pipette.flow_rate.dispense = 50 # gentle dispense rate to preserve beads
    # Set the aspirate height to the starting ethanol height
    left_pipette.well_bottom_clearance.aspirate = round(Ethanol_start_height-(Ethanol_start_height/steps),1)
    # Distribute Ethanol to all columns dropping the aspirate height after every transfer
    left_pipette.pick_up_tip()
    for ind, well in enumerate(magplate.rows_by_name()['A']):
        print(left_pipette.well_bottom_clearance.aspirate) # this is just a sense check and can go once the protocol is tested
        left_pipette.transfer(Ethanol_wash_vol, reservoir['A1'],
                                well,
                                air_gap = 10,
                                blow_out=False,
                                new_tip = 'never')
        left_pipette.well_bottom_clearance.aspirate = round(Ethanol_start_height-((Ethanol_start_height/steps)*(ind+2)),1)+0.2
    left_pipette.drop_tip() 
    
    # Pause briefly for ethanol wash
    protocol.delay(seconds = 10, msg = 'Washing beads')
    left_pipette.well_bottom_clearance.dispense = 25 # raise it up so the tips don't dip in the waste
    
    # Using a loop pick up ethanol and step the pipette height up in increments to release the pressure on blocked tips    
    left_pipette.pick_up_tip()
    for target_well in magplate.rows_by_name()['A']:
        # pipette off most of the ethanol
        left_pipette.aspirate(80, target_well.bottom(1.5))
        # move down and pipette off the rest
        left_pipette.aspirate(40, target_well.bottom(0.3))
        # step up releasing any blockages and giving liquid time to flow into the pipette
        protocol.delay(seconds = 1)
        left_pipette.move_to(target_well.bottom(0.5))
        protocol.delay(seconds = 1)
        left_pipette.move_to(target_well.bottom(0.7))
        protocol.delay(seconds = 1)
        left_pipette.move_to(target_well.bottom(0.9))
        protocol.delay(seconds = 1)
        left_pipette.move_to(target_well.bottom(1.1))
        protocol.delay(seconds = 1)
        left_pipette.move_to(target_well.bottom(1.3))
        protocol.delay(seconds = 1)
        left_pipette.touch_tip(target_well, radius=0.50,v_offset=-5, speed=25)
        # create an air gap for the drippy ethanol
        left_pipette.aspirate(10, target_well.top(-1))
        # put it all in the waste
        left_pipette.blow_out(waste['A2'].top(-10))
        # get rid of the drips
        left_pipette.touch_tip(waste['A2'], radius=0.80,v_offset=-5, speed=25)
    left_pipette.drop_tip()  
        
    #### Step 5 - Ethanol wash 2 ####
    # Set the dispense height and rate to a reasonable gentle height that doesn't end up with too much tip in the liquid
    left_pipette.well_bottom_clearance.dispense = 10 # near the bottom but not too near to make sure the tip doesn't block
    left_pipette.flow_rate.aspirate = 100
    left_pipette.flow_rate.dispense = 50 # gentle dispense rate to preserve beads
    # Set the aspirate height to the starting ethanol height
    left_pipette.well_bottom_clearance.aspirate = round(Ethanol_start_height-(Ethanol_start_height/steps),1)
    # Distribute Ethanol to all columns dropping the aspirate height after every transfer
    left_pipette.pick_up_tip()
    for ind, well in enumerate(magplate.rows_by_name()['A']):
        print(left_pipette.well_bottom_clearance.aspirate) # this is just a sense check and can go once the protocol is tested
        left_pipette.transfer(Ethanol_wash_vol, reservoir['A2'],
                                well,
                                air_gap = 10,
                                blow_out=False,
                                new_tip = 'never')
        left_pipette.well_bottom_clearance.aspirate = round(Ethanol_start_height-((Ethanol_start_height/steps)*(ind+2)),1)+0.2
    left_pipette.drop_tip() 
    
    # Pause briefly for ethanol wash
    protocol.delay(seconds = 10, msg = 'Washing beads')
    left_pipette.well_bottom_clearance.dispense = 25 # raise it up so the tips don't dip in the waste

    # Using a loop pick up ethanol and step the pipette height up in increments to release the pressure on blocked tips    
    left_pipette.pick_up_tip()
    for target_well in magplate.rows_by_name()['A']:
        # pipette off most of the ethanol
        left_pipette.aspirate(80, target_well.bottom(1.5))
        # move down and pipette off the rest
        left_pipette.aspirate(40, target_well.bottom(0.3))
        # step up releasing any blockages and giving liquid time to flow into the pipette
        protocol.delay(seconds = 1)
        left_pipette.move_to(target_well.bottom(0.5))
        protocol.delay(seconds = 1)
        left_pipette.move_to(target_well.bottom(0.7))
        protocol.delay(seconds = 1)
        left_pipette.move_to(target_well.bottom(0.9))
        protocol.delay(seconds = 1)
        left_pipette.move_to(target_well.bottom(1.1))
        protocol.delay(seconds = 1)
        left_pipette.move_to(target_well.bottom(1.3))
        protocol.delay(seconds = 1)
        left_pipette.touch_tip(target_well, radius=0.50,v_offset=-5, speed=25)
        # create an air gap for the drippy ethanol
        left_pipette.aspirate(10, target_well.top(-1))
        # put it all in the waste
        left_pipette.blow_out(waste['A3'].top(-10))
        # get rid of the drips
        left_pipette.touch_tip(waste['A3'], radius=0.80,v_offset=-5, speed=25)
    left_pipette.drop_tip()
    
    # Pull the SPRI beads down a bit to make elution easier
    mag_mod.engage(height=7)
    protocol.delay(seconds = 5, msg = 'Pulling beads down')
    
    # remove the last drips of ethanol from the bead wells
    left_pipette.flow_rate.aspirate = 5
    left_pipette.pick_up_tip()
    for target_well in magplate.rows_by_name()['A']:
        left_pipette.aspirate(10, target_well.bottom(0.3))
        protocol.delay(seconds = 1)
        left_pipette.move_to(target_well.bottom(0.5))
        protocol.delay(seconds = 1)
        left_pipette.move_to(target_well.bottom(0.7))
        protocol.delay(seconds = 1)
        left_pipette.move_to(target_well.bottom(0.9))
        protocol.delay(seconds = 1)
        left_pipette.move_to(target_well.bottom(1.1))
        protocol.delay(seconds = 1)
        left_pipette.move_to(target_well.bottom(1.3))
        protocol.delay(seconds = 1)
    left_pipette.blow_out(waste['A4'].top(-4))
    left_pipette.touch_tip(waste['A4'], radius=0.80,v_offset=-5, speed=25)
    left_pipette.drop_tip() 
    
    #### Step 5 - Dry SPRI beads ####
    mag_mod.disengage()
    protocol.delay(minutes = 10, msg = 'Drying beads')
    
    #### Step 6 - Elute ####
    # Add water or 10mM Tris-HCl
    # Set the dispense height and rate to a reasonable gentle height that doesn't end up with too much tip in the liquid
    left_pipette.well_bottom_clearance.dispense = 12 # near the bottom but not too near to make sure the tip doesn't block
    left_pipette.well_bottom_clearance.aspirate = 1
    left_pipette.flow_rate.aspirate = 100
    left_pipette.flow_rate.dispense = 150 # doesn't really matter and a good rate will help mix beads
    # Distribute Tris-HCl to all columns
    left_pipette.distribute(Tris_elute_vol, reservoir['A10'],
                            magplate.rows_by_name()['A'],
                            new_tip = 'once')
