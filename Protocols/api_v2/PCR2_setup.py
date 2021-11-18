#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 12:02:38 2021

@author: neg
"""
from opentrons import protocol_api

# metadata
metadata = {'apiLevel': '2.8',
            'protocolName': 'mastermix multiplate dispense',
            'author': 'James Kitson <james.kitson@newcastle.ac.uk>',
            'description': 'A protocol to distribute mastermix beads to multiple PCR plates'}

# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions

def run(protocol: protocol_api.ProtocolContext):
      
    # key labware dimensions
    tip_height = 3.5
    well_width =8.3
    well_length = 8.3
    
    # key liquid volumes
    mastermix_vol = 10
    fudge_factor=1.2
    
    # work out the initial mastermix volume per well on the 2.2ml plate
    mastermix_start_vol = round((mastermix_vol*96*fudge_factor),1)
       
    # create a function that works out the starting liquid height
    def start_height(start_vol, tip_height, well_width, well_length):
        # define the volume of the tip of the well tip
        #tip_vol = ((tip_height*well_width)/2)*well_length
        tip_vol = (2/3)*3.14159*tip_height**3
        # if the start volume > tip volume, work out the residual height, add it to the tip height and subrtact it from the total height of the tube
        if start_vol > tip_vol:
            return round(tip_height+((start_vol-tip_vol)/(well_width*well_length)),1)
        # if the starting volume is less than the tip volume, work out the total height and subrtact it from the total height of the tube
        else:
            return (3*start_vol/(2*3.14159))**(1/3)


    # set up the reagent locations
    reservoir = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap',9)
    mastermix = reservoir['A1']
    
    # set up tip locations
    tiprack_200 = protocol.load_labware('opentrons_96_filtertiprack_200ul', 3)
    
    # set up the destination PCR plates
    #PCR_plate_name = 'sarstedt_96_skirted_wellplate_200ul'
    #dest_plates = [protocol.load_labware(PCR_plate_name, str(slot))
     #          for slot in [available_slots[i] for i in range(number_of_destination_plates)]]
    
    PCR_plate = protocol.load_labware('sarstedt_96_skirted_wellplate_200ul', 1)
    
    # generate a list of detinations to target for the primer distribute command
    #all_dests = [well for plate in dest_plates for well in plate.rows('A')] 
    
    # calculate a step number for pipette changes and aspirate heights
    #steps=len(dest_plates)      
    steps=8
    
   
    # set up pipettes
    pipette_300 = protocol.load_instrument('p300_single', mount='left', tip_racks=[tiprack_200]) 
 
    # set pipetting parameters for mastermix distribution
    pipette_300.flow_rate.aspirate = 50
    initial_mastermix_height = start_height(mastermix_start_vol, tip_height, well_width, well_length)
  
    print("The initial mastermix volume is: ", mastermix_start_vol)
    print("The initial mastermix height is: ", initial_mastermix_height)
    
    # Define initial pipetting height that deals with workng on single rows
    if round(initial_mastermix_height-(initial_mastermix_height/steps),1) > 0:
        pipette_300.well_bottom_clearance.aspirate = round(initial_mastermix_height-(initial_mastermix_height/steps),1)
    elif round(initial_mastermix_height-(initial_mastermix_height/steps),1) == 0:
        pipette_300.well_bottom_clearance.aspirate = 0.3
    print("The initial mastermix pipetting height is: ", pipette_300.well_bottom_clearance.aspirate)
    
    ######################################
    ### ROUND 1 the first four plates ####
    ######################################
    
    # # Set some really slow pipetting rates for the viscous mastermix    
    pipette_300.flow_rate.dispense = 10
    pipette_300.well_bottom_clearance.dispense = 5
    pipette_300.flow_rate.blow_out = 10

    # Start a ticker to track pipetting operations
    ticker = 1
    
      
    # distribute mastermix using distribute command and well referencing - may need replacing with aspirate and dispense if I need waiting times etc
    pipette_300.pick_up_tip() 
    for row in ['A','B','C','D','E','F','G','H']:
        print('Round', ticker, 'pipetting height', pipette_300.well_bottom_clearance.aspirate)
        pipette_300.aspirate((mastermix_vol*12)+5, mastermix)
        pipette_300.touch_tip(mastermix, radius=0.75,v_offset=-2, speed=25)
        for well in PCR_plate.rows_by_name()[row]:
            pipette_300.dispense(mastermix_vol,
                                 well)    
        pipette_300.blow_out(mastermix.top(-2))
        # tasks done so add one to the ticker to calulate new pipette heights.
        ticker = ticker+1
                  
        # change the aspirate height on the mastermix to move down a bit, if it is the last step, set a special heigh that isn't zero and slow the aspirate right down
        if ticker < steps:
            pipette_300.well_bottom_clearance.aspirate = round((initial_mastermix_height)-((initial_mastermix_height/steps)*(ticker*0.9)),1)
        elif ticker == steps:
            pipette_300.well_bottom_clearance.aspirate = round((initial_mastermix_height)-((initial_mastermix_height/steps)*(ticker*0.9)),1)
            pipette_300.flow_rate.aspirate = 5
    pipette_300.drop_tip()
    