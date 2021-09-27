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
   # outplate = protocol.load_labware('sarstedt_96_skirted_wellplate_200ul', 5,
   #                                   label='Cleaned samples')
    waste = protocol.load_labware('starlab_tip_box_waste', 7)
    
    # key labware dimensions
    tip_height = 3
    well_width =8.2
    well_length = 71.2
    
    # magnetic module and labware on it
    mag_mod = protocol.load_module('magdeck', 1)
    magplate = mag_mod.load_labware('sarstedt_96_skirted_wellplate_200ul',
                                      label='Samples')
    
    # pipettes
    # left_pipette = protocol.load_instrument('p50_multi', mount='left', tip_racks=[tiprack_1, tiprack_2, tiprack_3])
    left_pipette = protocol.load_instrument('p300_multi', mount='left', tip_racks=[tiprack_1, tiprack_2,tiprack_3])
    
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
    
    
    ##### Step 1 - Wait for 5 minutes then apply magnets for 5 minutes ####
    #protocol.delay(minutes = 5, msg = 'Binding DNA to SPRI beads')
    mag_mod.engage(height=19.5)
    #protocol.delay(minutes = 5, msg = 'Separating SPRI beads from supernatant')
    
    #### Step 2 - Remove the supernatant ####
    # set pipetting parameters
    left_pipette.flow_rate.aspirate = 10 # slow here as SPRI mix is viscous
    left_pipette.flow_rate.dispense = 150 # this doesn't matter as it's dispensing to 'trash'
    left_pipette.flow_rate.blow_out = 150 # this doesn't matter as it's dispensing to 'trash'
    left_pipette.well_bottom_clearance.dispense = 30 # I just want this a bit down in the 'trash' in case of splattering
    
# =============================================================================
#     # pipette out the bulk of the liquid
#     left_pipette.well_bottom_clearance.aspirate = 1.5 # near the bottom but with a gap
#     left_pipette.consolidate(30, magplate.rows_by_name()['A'], waste['A1'],
#                               blow_out=True)
#     # drop pipette height and aspirate speed then pipette out the remainder of the liquid
#     left_pipette.flow_rate.aspirate = 5
#     left_pipette.well_bottom_clearance.aspirate = 0.5
#     left_pipette.consolidate(30, magplate.rows_by_name()['A'], waste['A1'],
#                               blow_out=True)
# =============================================================================
    left_pipette.pick_up_tip()
    for well in well_name:
        left_pipette.move_to(magplate.wells(well)).bottom(1.5)
        left_pipette.aspirate(50, magplate.wells(well))
        left_pipette.move_to(magplate.wells(well)).bottom(0.3)
        left_pipette.aspirate(30, magplate.wells(well))
        left_pipette.move_to(magplate.wells(well)).bottom(0.5)
        left_pipette.move_to(magplate.wells(well)).bottom(0.7)
        left_pipette.move_to(magplate.wells(well)).bottom(0.9)
        left_pipette.move_to(magplate.wells(well)).bottom(1.1)
        left_pipette.move_to(magplate.wells(well)).top(-2)
        left_pipette.touch_tip(well, radius=0.65,v_offset=-2, speed=25)
        left_pipette.dispense(80,waste['A1'])
        left_pipette.blow_out()
    left_pipette.drop_tip()
        
# =============================================================================
# 
#     #### Step 3 - Ethanol wash 1 ####
#     # Set the dispense height and rate to a reasonable gentle height that doesn't end up with too much tip in the liquid
#     left_pipette.well_bottom_clearance.dispense = 10 # near the bottom but not too near to make sure the tip doesn't block
#     left_pipette.flow_rate.aspirate = 100
#     left_pipette.flow_rate.dispense = 50 # gentle dispense rate to preserve beads
#     # Set the aspirate height to the starting ethanol height
#     left_pipette.well_bottom_clearance.aspirate = round(Ethanol_start_height-(Ethanol_start_height/steps),1)
#     # Distribute Ethanol to all columns dropping the aspirate height after every transfer
#     left_pipette.pick_up_tip()
#     for ind, well in enumerate(well_name):
#         print(left_pipette.well_bottom_clearance.aspirate) # this is just a sense check and can go once the protocol is tested
#         left_pipette.transfer(Ethanol_wash_vol, reservoir['A1'],
#                                magplate.wells_by_name()[well],
#                                air_gap = 10,
#                                blow_out=False,
#                                new_tip = 'never')
#         left_pipette.well_bottom_clearance.aspirate = round(Ethanol_start_height-((Ethanol_start_height/steps)*(ind+2)),1)+0.2
#     left_pipette.drop_tip() 
#     
#     # Pause briefly for ethanol wash
#     protocol.delay(seconds = 10, msg = 'Washing beads')
#     left_pipette.well_bottom_clearance.dispense = 25 # raise it up so the tips don't dip in the waste
#     # Remove the bulk of the ethanol
#     left_pipette.flow_rate.aspirate = 100 # the first aspirate can be quite fast
#     left_pipette.well_bottom_clearance.aspirate = 3 # not right at the bottom to keep liquid flow around the beads gentle
#     left_pipette.consolidate(100, magplate.rows_by_name()['A'], waste['A1'],
#                               blow_out=True)
#     # drop pipette height and aspirate speed then pipette out the remainder of the ethanol
#     left_pipette.flow_rate.aspirate = 20 # slowing right down as we're pipetting very close to the bottom and don't want to disturb the beads
#     left_pipette.well_bottom_clearance.aspirate = 0.5 
#     left_pipette.consolidate(50, magplate.rows_by_name()['A'], waste['A1'],
#                               blow_out=True)
#         
#         
#     #### Step 4 - Ethanol wash 2 ####
#     # Set the dispense height and rate to a reasonable gentle height that doesn't end up with too much tip in the liquid
#     left_pipette.well_bottom_clearance.dispense = 10 # near the bottom but not too near to make sure the tip doesn't block
#     left_pipette.flow_rate.aspirate = 100
#     left_pipette.flow_rate.dispense = 50 # gentle dispense rate to preserve beads
#     # Set the aspirate height to the starting ethanol height
#     left_pipette.well_bottom_clearance.aspirate = round(Ethanol_start_height-(Ethanol_start_height/steps),1)
#     # Distribute Ethanol to all columns dropping the aspirate height after every transfer
#     left_pipette.pick_up_tip()
#     for ind, well in enumerate(well_name):
#         print(left_pipette.well_bottom_clearance.aspirate) # this is just a sense check and can go once the protocol is tested
#         left_pipette.transfer(Ethanol_wash_vol, reservoir['A2'],
#                                magplate.wells_by_name()[well],
#                                air_gap = 10,
#                                blow_out=False,
#                                new_tip = 'never')
#         left_pipette.well_bottom_clearance.aspirate = round(Ethanol_start_height-((Ethanol_start_height/steps)*(ind+2)),1)+0.2
#     left_pipette.drop_tip() 
#     
#     # Pause briefly for ethanol wash
#     protocol.delay(seconds = 10, msg = 'Washing beads')
#     left_pipette.well_bottom_clearance.dispense = 25 # raise it up so the tips don't dip in the waste
#     # Remove the bulk of the ethanol
#     left_pipette.flow_rate.aspirate = 100 # the first aspirate can be quite fast
#     left_pipette.well_bottom_clearance.aspirate = 3 # not right at the bottom to keep liquid flow around the beads gentle
#     left_pipette.consolidate(100, magplate.rows_by_name()['A'], waste['A1'],
#                               blow_out=True)
#     # drop pipette height and aspirate speed then pipette out the remainder of the ethanol
#     left_pipette.flow_rate.aspirate = 20 # slowing right down as we're pipetting very close to the bottom and don't want to disturb the beads
#     left_pipette.well_bottom_clearance.aspirate = 0.5
#     left_pipette.consolidate(50, magplate.rows_by_name()['A'], waste['A1'],
#                               blow_out=True)
#     
#     #### Step 5 - Dry SPRI beads ####
#     mag_mod.engage(height=13.5)
#     #protocol.delay(minutes = 2, msg = 'Pulling beads down')
#     mag_mod.disengage()
#     #protocol.delay(minutes = 8, msg = 'Drying beads')
#     
#     #### Step 5 - Elute ####
#     # Add water or 10mM Tris-HCl
#     # Set the dispense height and rate to a reasonable gentle height that doesn't end up with too much tip in the liquid
#     left_pipette.well_bottom_clearance.dispense = 5 # near the bottom but not too near to make sure the tip doesn't block
#     left_pipette.flow_rate.aspirate = 100
#     left_pipette.flow_rate.dispense = 150 # doesn't really matter and a good rate will help mix beads
#     # Set the aspirate height to the starting ethanol height
#     left_pipette.well_bottom_clearance.aspirate = round(Tris_start_height-(Tris_start_height/steps),1)
#     # Distribute Ethanol to all columns dropping the aspirate height after every transfer
#     left_pipette.pick_up_tip()
#     for ind, well in enumerate(well_name):
#         print(left_pipette.well_bottom_clearance.aspirate) # this is just a sense check and can go once the protocol is tested
#         left_pipette.transfer(Tris_elute_vol, reservoir['A10'],
#                                 magplate.wells_by_name()[well],
#                                 air_gap = 5,
#                                 blow_out=True,
#                                 blowout_location='source well',
#                                 new_tip = 'never')
#         left_pipette.well_bottom_clearance.aspirate = round(Tris_start_height-((Tris_start_height/steps)*(ind+2)),1)+0.2
#     left_pipette.drop_tip() 
# 
# =============================================================================
    
    #### Step 6 - pause, cover and shake this is only required if you are sanger ####
    #### sequencing and need to move the suprenatant into a new plate ####
# =============================================================================
#     protocol.pause(
#             "Remove skirted plate from magdeck, cover with PCR film and shake on plate shaker for 2 minutes at 1400 rpm, take of lid, return to magdeck and resume protocol")
#     
#     # Wait 5 min
#     protocol.delay(minutes = 5, msg = 'Waiting for DNA to elute')
#     
#     # Engage magnets for 5 min
#     mag_mod.engage(height=18.5)
#     protocol.delay(minutes = 5, msg = 'Separating SPRI beads')
#     
#     #### Step 7 - Transfer to skirted plate for storage ####
#     left_pipette.well_bottom_clearance.aspirate = 0.1
#     left_pipette.transfer(Tris_elute_vol-2, magplate.rows_by_name()['A'],
#                        outplate.rows_by_name()['A'],
#                        air_gap = 5,
#                        blow_out=False,
#                        touch_tip=False,
#                        new_tip = 'always')
# =============================================================================
