#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 12:02:38 2021

@author: neg
"""
from opentrons import protocol_api

# metadata
metadata = {'apiLevel': '2.8',
            'protocolName': 'SPRI plate fill',
            'author': 'James Kitson <james.kitson@newcastle.ac.uk>',
            'description': 'SPRI plate fill'}

# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions

def run(protocol: protocol_api.ProtocolContext):
   
    # key liquid volumes
    spri_vol = 30
    
    # check for labware space
    available_slots = [1,2,3,4,6,7,8,9]
    number_of_destination_plates: int = 2
    if number_of_destination_plates > 5:
        raise Exception('Please specify 5 or fewer destination plates, you cant hold enough SPRI beads in a 2.2ml plate for more.') 

    # labware for protocol
    reservoir = protocol.load_labware('sarstedt_96_wellplate_2200ul',5)
    beads = reservoir['A1']
    # start_vol_beads = 2000
    tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', 10)
    spri_plate_name = 'sarstedt_96_wellplate_200ul'
    dest_plates = [protocol.load_labware(spri_plate_name, str(slot))
               for slot in [available_slots[i] for i in range(number_of_destination_plates)]]
        
    # # define tube parameters for deepwell tubes - no skirt
    # total_length_deepwell: float = 41.85
    # length_barrel_deepwell: float = 37.7
    # tip_length_deepwell: float = round(total_length_deepwell-length_barrel_deepwell,1)
    # width_deepwell: float = 8.3
    
    # pipettes
    left_pipette = protocol.load_instrument('p300_multi', mount='right', tip_racks=[tiprack_300]) 
    
    #generate a list of detinations to target for the distribute command
    #all_dests = [well for plate in dest_plates for well in plate.rows('A')]
    
    # # set pipetting parameters
    left_pipette.flow_rate.aspirate = 25
    left_pipette.well_bottom_clearance.aspirate = 35
    left_pipette.flow_rate.dispense = 50
    left_pipette.well_bottom_clearance.dispense = 2
    left_pipette.flow_rate.blow_out = 10
    
    steps=len(dest_plates)
 
    # solution with aspirate and dispense
    # for d in dest_plates:
    #     left_pipette.pick_up_tip()
    #     for ind in targets:
    #         print(left_pipette.well_bottom_clearance.aspirate)
    #         left_pipette.aspirate(spri_vol, beads).touch_tip()
    #         left_pipette.dispense(spri_vol,d[ind]).touch_tip()
    #         left_pipette.well_bottom_clearance.aspirate = round(left_pipette.well_bottom_clearance.aspirate-(left_pipette.well_bottom_clearance.aspirate/steps))
    #     left_pipette.drop_tip()
    
    # solution with distribute and well referencing
    for d in dest_plates:
        left_pipette.pick_up_tip()
        print(left_pipette.well_bottom_clearance.aspirate)
        left_pipette.distribute(spri_vol,beads,d.rows_by_name()['A'],
                                touch_tip=True, new_tip='never',
                                blowout_location='source well')
        left_pipette.well_bottom_clearance.aspirate = round(left_pipette.well_bottom_clearance.aspirate-(left_pipette.well_bottom_clearance.aspirate/steps))
        left_pipette.drop_tip()        
        
    