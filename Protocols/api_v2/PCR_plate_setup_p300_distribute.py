#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 12:02:38 2021

@author: neg
"""
from opentrons import protocol_api

# metadata
metadata = {'apiLevel': '2.8',
            'protocolName': 'multiPCR plate setup',
            'author': 'James Kitson <james.kitson@newcastle.ac.uk>',
            'description': 'A protocol to distribute PCR master mix and tagged primers to multiple PCR plaes'}

# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions

def run(protocol: protocol_api.ProtocolContext):
   
    # key liquid volumes
    PCR_mastermix_vol = 16
    primer_vol = 2
    fudge_factor = 1.2
    
    # key labware dimensions
    tip_height = 3
    well_width =8.2
    well_length = 71.2
    
    # check for labware space
    available_slots = [1,4,7,10,2,5,11] # this order minimises pipette travel over non-target wells
    number_of_destination_plates: int = 4
    if number_of_destination_plates > 4:
        raise Exception('Please specify 4 or fewer destination plates, the P10 cant carry enough primer in one aspirate. Alternatively remake your primers at a higher concentration to dispense smaller volumes')
    
    # work out the initial master mix volume
    start_vol = round(PCR_mastermix_vol*number_of_destination_plates*96*fudge_factor,1)
    
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


    # set up the reagent locations
    primers = protocol.load_labware('sarstedt_96_skirted_wellplate_200ul',8)
    reservoir = protocol.load_labware('nest_12_reservoir_15ml',9)
    mastermix = reservoir['A1']
    
    # set up tip locations
    tiprack_200 = protocol.load_labware('opentrons_96_filtertiprack_200ul', 3)
    tiprack_10 = protocol.load_labware('opentrons_96_filtertiprack_20ul', 6)
    
    # set up the destination PCR plates
    PCR_plate_name = 'sarstedt_96_skirted_wellplate_200ul'
    dest_plates = [protocol.load_labware(PCR_plate_name, str(slot))
               for slot in [available_slots[i] for i in range(number_of_destination_plates)]]
    
    # generate a list of detinations to target for the primer distribute command
    #all_dests = [well for plate in dest_plates for well in plate.rows('A')] 

    # calculate a step number for pipette changes and aspirate heights
    steps=len(dest_plates)      
    
    # set up pipettes
    pipette_300 = protocol.load_instrument('p300_multi', mount='left', tip_racks=[tiprack_200]) 
    pipette_multi10 = protocol.load_instrument('p10_multi', mount='right', tip_racks=[tiprack_10]) 
    
    # set pipetting parameters for mastermix distribution
    pipette_300.flow_rate.aspirate = 25
    initial_mastermix_height = start_height(start_vol, tip_height, well_width, well_length)
    print("The initial mastermix volume is: ", end='')
    print(start_vol)
    print("The initial mastermix height is: ", end='')
    print(initial_mastermix_height)
    pipette_300.well_bottom_clearance.aspirate = round(initial_mastermix_height-(initial_mastermix_height/steps),1)
    pipette_300.flow_rate.dispense = 50
    pipette_300.well_bottom_clearance.dispense = 5
    pipette_300.flow_rate.blow_out = 10

    # set pipetting parameters for primer distribution
    pipette_multi10.flow_rate.aspirate = 25
    pipette_multi10.well_bottom_clearance.aspirate = 2
    pipette_multi10.flow_rate.dispense = 50
    pipette_multi10.well_bottom_clearance.dispense = 2
    pipette_multi10.flow_rate.blow_out = 10    

    
    # distribute mastermix using distribute command and well referencing
    for ind, d in enumerate(dest_plates):
        pipette_300.pick_up_tip()
        print('Round', ind+1, 'pipetting height', pipette_300.well_bottom_clearance.aspirate)
        pipette_300.distribute(PCR_mastermix_vol,mastermix,d.wells(),
                                #touch_tip=True,
                                #radius=0.8,
                                new_tip='never',
                                blow_out=True,
                                blow_out_location='source well',
                                disposal_volume=2)
        pipette_300.well_bottom_clearance.aspirate = round(initial_mastermix_height-((initial_mastermix_height/steps)*(ind+2)),1)+0.3
        pipette_300.drop_tip()        

    # forward primer distribution
    for ind, primer in enumerate(primers.rows_by_name()['A']):
        dests = [plate.rows_by_name()['A'][ind] for plate in dest_plates]
        pipette_multi10.distribute(primer_vol,
                                   primer,
                                   dests,
                                   touch_tip=False,
                                disposal_volume=1)
        
        
        
        
        
        
        
        