#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 12:02:38 2021

@author: neg
"""
from opentrons import protocol_api

# metadata
metadata = {'apiLevel': '2.8',
            'protocolName': 'SPRI multiplate dispense',
            'author': 'James Kitson <james.kitson@newcastle.ac.uk>',
            'description': 'A protocol to distribute SPRI beads to multiple PCR plates'}

# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions

def run(protocol: protocol_api.ProtocolContext):
      
    # key labware dimensions
    tip_height = 3.5
    well_width =8.3
    well_length = 8.3
    
    # check for labware space
    available_slots = [1,2,4,5,6,7,8,10,11,12] # this order minimises pipette travel over non-target wells
    number_of_destination_plates: int = 4
    max_destination_plates = 4
    if number_of_destination_plates > max_destination_plates:
        raise Exception('Please specify 4 or fewer destination plates, you do not have enough space in a reservoir well')
   
    # key liquid volumes
    SPRI_vol = 30
    water_vol = 20
    
    # work out the initial SPRI volume per well on the 2.2ml plate
    SPRI_start_vol = round((SPRI_vol*number_of_destination_plates*108)/8,1)
    water_start_vol = round((water_vol*number_of_destination_plates*108)/8,1)
       
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
    reservoir = protocol.load_labware('sarstedt_96_wellplate_2200ul',9)
    SPRI = reservoir['A3']
    water = reservoir['A4']
    
    # set up tip locations
    tiprack_200 = protocol.load_labware('opentrons_96_filtertiprack_200ul', 3)
    
    # set up the destination PCR plates
    PCR_plate_name = 'sarstedt_96_skirted_wellplate_200ul'
    dest_plates = [protocol.load_labware(PCR_plate_name, str(slot))
               for slot in [available_slots[i] for i in range(number_of_destination_plates)]]
    
    # generate a list of detinations to target for the primer distribute command
    #all_dests = [well for plate in dest_plates for well in plate.rows('A')] 
    
    # calculate a step number for pipette changes and aspirate heights
    #steps=len(dest_plates)      
    steps=len(dest_plates)*2
    
   
    # set up pipettes
    pipette_300 = protocol.load_instrument('p300_multi', mount='left', tip_racks=[tiprack_200]) 
 
    # set pipetting parameters for SPRI distribution
    pipette_300.flow_rate.aspirate = 10
    initial_SPRI_height = start_height(SPRI_start_vol, tip_height, well_width, well_length)
    initial_water_height = start_height(water_start_vol, tip_height, well_width, well_length)
    print("The initial SPRI volume per reservoir well is: ", SPRI_start_vol)
    print("The initial SPRI height is: ", initial_SPRI_height)
    print("The initial water volume per reservoir well is: ", water_start_vol)
    print("The initial water height is: ", initial_water_height)
    
    protocol.pause("Put 400 microlitres of SPRI beads in wells A1-H1 of the reservoir per plate being set up and 300ul of water in wells A2-H2 per plate being set up")
    
    # Define initial pipetting height that deals with workng on single rows
    if round(initial_SPRI_height-(initial_SPRI_height/steps),1) > 0:
        pipette_300.well_bottom_clearance.aspirate = round(initial_SPRI_height-(initial_SPRI_height/steps),1)
    elif round(initial_SPRI_height-(initial_SPRI_height/steps),1) == 0:
        pipette_300.well_bottom_clearance.aspirate = 0.3
    print("The initial SPRI pipetting height is: ", pipette_300.well_bottom_clearance.aspirate)
    
    ######################################
    ### ROUND 1 the first four plates ####
    ######################################
    
    # # Set some really slow pipetting rates for the viscous SPRI    
    pipette_300.flow_rate.dispense = 10
    pipette_300.well_bottom_clearance.dispense = 5
    pipette_300.flow_rate.blow_out = 10

    # Start a ticker to track pipetting operations
    ticker = 1
    
    # distribute SPRI using distribute command and well referencing - may need replacing with aspirate and dispense if I need waiting times etc
    pipette_300.pick_up_tip()
    for d in dest_plates:
      print('Round', ticker, 'pipetting height', pipette_300.well_bottom_clearance.aspirate)
      # move to SPRI reservoir and aspirate then wait for viscous fluid to catch up
      pipette_300.aspirate(((SPRI_vol*6)+5),SPRI)
      protocol.delay(seconds=1)
      # move to the top of the reservoir and let the SPRI form a drip then touch it off gently to the well wall 
      pipette_300.move_to(SPRI.top(-2))
      protocol.delay(seconds=4)
      pipette_300.touch_tip(SPRI, radius=0.65,v_offset=-2, speed=25)
        
      for well in ['A1', 'A2', 'A3', 'A4', 'A5', 'A6']:
            # dispence the SPRI in the tip into the target well and wait for the viscous fluid to catch up
            pipette_300.dispense(SPRI_vol,d[well])
            protocol.delay(seconds=2)
            # move to the top of the target well and let the SPRI form a drip then touch it off gently to the well wall 
      pipette_300.move_to(d[well].top(-2))
      protocol.delay(seconds=2)
      pipette_300.touch_tip(d[well], radius=0.65,v_offset=-2, speed=25)
      pipette_300.blow_out(SPRI)
      pipette_300.touch_tip(SPRI, radius=0.65,v_offset=-2, speed=25)
      
      # tasks done so add one to the ticker to calulate new pipette heights.
      ticker = ticker+1
                
      # change the aspirate height on the SPRI to move down a bit, if it is the last step, set a special heigh that isn't zero and slow the aspirate right down
      if ticker < steps:
          pipette_300.well_bottom_clearance.aspirate = round((initial_SPRI_height)-((initial_SPRI_height/steps)*(ticker*0.9)),1)
      elif ticker == steps:
          pipette_300.well_bottom_clearance.aspirate = round((initial_SPRI_height)-((initial_SPRI_height/steps)*(ticker*0.9)),1)
          pipette_300.flow_rate.aspirate = 5
          
      print('Round', ticker, 'pipetting height', pipette_300.well_bottom_clearance.aspirate)
      # move to SPRI reservoir and aspirate then wait for viscous fluid to catch up
      pipette_300.aspirate(((SPRI_vol*6)+5),SPRI)
      protocol.delay(seconds=1)
      # move to the top of the reservoir and let the SPRI form a drip then touch it off gently to the well wall 
      pipette_300.move_to(SPRI.top(-2))
      protocol.delay(seconds=4)
      pipette_300.touch_tip(SPRI, radius=0.65,v_offset=-2, speed=25)
      
      for well in ['A7', 'A8', 'A9', 'A10', 'A11', 'A12']:
            # dispence the SPRI in the tip into the target well and wait for the viscous fluid to catch up
            pipette_300.dispense(SPRI_vol,d[well])
            protocol.delay(seconds=2)
            # move to the top of the target well and let the SPRI form a drip then touch it off gently to the well wall 
      pipette_300.move_to(d[well].top(-2))
      protocol.delay(seconds=2)
      pipette_300.touch_tip(d[well], radius=0.65,v_offset=-2, speed=25)
      pipette_300.blow_out(SPRI)
      pipette_300.touch_tip(SPRI, radius=0.65,v_offset=-2, speed=25)
      
      # tasks done so add one to the ticker to calulate new pipette heights.
      ticker = ticker+1
                
      # change the aspirate height on the SPRI to move down a bit, if it is the last step, set a special heigh that isn't zero and slow the aspirate right down
      if ticker < steps:
          pipette_300.well_bottom_clearance.aspirate = round((initial_SPRI_height)-((initial_SPRI_height/steps)*(ticker*0.9)),1)
      elif ticker == steps:
          pipette_300.well_bottom_clearance.aspirate = round((initial_SPRI_height)-((initial_SPRI_height/steps)*(ticker*0.9)),1)
          pipette_300.flow_rate.aspirate = 5    
    pipette_300.drop_tip()            
        
        
    water_steps=len(dest_plates)
    
    # Define initial pipetting height that deals with workng on single rows
    if round(initial_water_height-(initial_water_height/water_steps),1) > 0:
        pipette_300.well_bottom_clearance.aspirate = round(initial_water_height-(initial_water_height/water_steps),1)
    elif round(initial_water_height-(initial_water_height/water_steps),1) == 0:
        pipette_300.well_bottom_clearance.aspirate = 0.3
    print("The initial water pipetting height is: ", pipette_300.well_bottom_clearance.aspirate)
    
    # set remaining pipetting parameters
    pipette_300.well_bottom_clearance.dispense = 8
    pipette_300.flow_rate.dispense = 50
    pipette_300.flow_rate.aspirate = 50

    # distribute water using distribute command and well referencing
    pipette_300.pick_up_tip()
    for ind, d in enumerate(dest_plates):
        print('Round', ind+1, 'pipetting height', pipette_300.well_bottom_clearance.aspirate)
        pipette_300.distribute(water_vol,water,d.wells(),
                                #touch_tip=True,
                                #radius=0.8,
                                new_tip='never',
                                blow_out=True,
                                blow_out_location='source well',
                                disposal_volume=2)
        pipette_300.well_bottom_clearance.aspirate = round(initial_water_height-(initial_water_height/water_steps)*((ind+2)*0.95),1)
    pipette_300.drop_tip() 
            
