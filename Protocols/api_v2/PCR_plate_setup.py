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
    PCR_matermix_vol = 7
    primer_vol = 1
    
    # check for labware space
    available_slots = [1,2,3,4,7,8,9]
    number_of_destination_plates: int = 2
    if number_of_destination_plates > 4:
        raise Exception('Please specify 4 or fewer destination plates, you dont have enough cold plates.')
    

    # set up the reagent locations
    primers = protocol.load_labware('sarstedt_96_skirted_wellplate_200ul',5)
    reservoir = protocol.load_labware('nest_12_reservoir_15ml',6)
    mastermix = reservoir['A1']
    
    # set up tip locations
    tiprack_200 = protocol.load_labware('opentrons_96_filtertiprack_200ul', 10)
    tiprack_10 = protocol.load_labware('opentrons_96_filtertiprack_20ul', 11)
    
    # set up the destination PCR plates
    PCR_plate_name = 'sarstedt_96_skirted_wellplate_200ul'
    dest_plates = [protocol.load_labware(PCR_plate_name, str(slot))
               for slot in [available_slots[i] for i in range(number_of_destination_plates)]]
    
    # generate a list of detinations to target for the primer distribute command
    #all_dests = [well for plate in dest_plates for well in plate.rows('A')] 

    # calculate a step number for pipette changes and aspirate heights
    steps=len(dest_plates)      
    
    # set up pipettes
    pipette_multi50 = protocol.load_instrument('p50_multi', mount='left', tip_racks=[tiprack_200]) 
    pipette_multi10 = protocol.load_instrument('p10_multi', mount='right', tip_racks=[tiprack_10]) 
    
    # set pipetting parameters for mastermix distribution
    pipette_multi50.flow_rate.aspirate = 25
    pipette_multi50.well_bottom_clearance.aspirate = 35
    pipette_multi50.flow_rate.dispense = 50
    pipette_multi50.well_bottom_clearance.dispense = 2
    pipette_multi50.flow_rate.blow_out = 10

    # set pipetting parameters for primer distribution
    pipette_multi10.flow_rate.aspirate = 25
    pipette_multi10.well_bottom_clearance.aspirate = 35
    pipette_multi10.flow_rate.dispense = 50
    pipette_multi10.well_bottom_clearance.dispense = 2
    pipette_multi10.flow_rate.blow_out = 10    

    
    # distributemastermix using distribute command and well referencing
    for d in dest_plates:
        pipette_multi50.pick_up_tip()
        print(pipette_multi50.well_bottom_clearance.aspirate)
        pipette_multi50.distribute(PCR_matermix_vol,mastermix,d.rows_by_name()['A'],
                                touch_tip=True,
                                new_tip='never',
                                blow_out=True,
                                blow_out_location='source well')
        pipette_multi50.well_bottom_clearance.aspirate = round(pipette_multi50.well_bottom_clearance.aspirate-(pipette_multi50.well_bottom_clearance.aspirate/steps))
        pipette_multi50.drop_tip()        

    # forward primer distribution
    for ind, primer in enumerate(primers.rows_by_name()['A']):
        dests = [plate.rows_by_name()['A'][ind] for plate in dest_plates]
        pipette_multi10.distribute(primer_vol,
                                   primer,
                                   dests,
                                   touch_tip=True)
        
        
        
        
        
        
        
        