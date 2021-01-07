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
            'author': 'James Kitson',
            'description': 'SPRI plate fill'}

# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions

def run(protocol: protocol_api.ProtocolContext):

# key liquid volumes
    number_of_destination_plates: int = 8
    spri_vol = 30
    spri_plate_name = 'sarstedt_96_wellplate_200ul'
    available_slots = [1,2,3,4,6,7,8,9]

    # labware for protocol
    reservoir = protocol.load_labware('sarstedt_96_wellplate_2200ul',5)
    beads = reservoir.wells('A1')
    tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', 10)
    dest_plates = [protocol.load_labware(spri_plate_name, str(slot))
               for slot in [available_slots[i] for i in range(0,number_of_destination_plates)]]
        
    # pipettes
    left_pipette = protocol.load_instrument('p300_multi', mount='right', tip_racks=[tiprack_300])

    # check for labware space
    if number_of_destination_plates > 8:
        raise Exception('Please specify 8 or fewer destination plates.')  
    
    
    all_dests = [well for plate in dest_plates for well in plate.rows('A')]
    
    # distribute PCR master mix
  #  left_pipette.set_flow_rate(aspirate=25, dispense=50)
    left_pipette.flow_rate.aspirate = 25
    left_pipette.well_bottom_clearance.aspirate = 10
    left_pipette.flow_rate.dispense = 50
    left_pipette.well_bottom_clearance.dispense = 2
    left_pipette.flow_rate.blow_out = 10
    left_pipette.pick_up_tip()
    for d in all_dests:
        left_pipette.distribute(spri_vol, beads, d, blow_out=True, new_tip='never')
    left_pipette.drop_tip()