##!/usr/bin/env python3
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

    tiprack_3 = protocol.load_labware('opentrons_96_filtertiprack_20ul', 9, "Tips for PCR product transfer")
    source_plate = protocol.load_labware('sarstedt_96_skirted_wellplate_200ul', 8, "PCRs to be cleaned")
    target_plate = protocol.load_labware('sarstedt_96_skirted_wellplate_200ul', 5, "SPRI to mix with PCR")

    # pipettes
    pipette_10 = protocol.load_instrument('p10_multi', mount='left', tip_racks=[tiprack_3])
    
    ticker=0

    ##### Step 1 - Transfer PCR products to magdeck and mix ####
    # Using a loop pick up PCR products and mix 
    for source_well in source_plate.rows_by_name()['A']:
        pipette_10.pick_up_tip()
        pipette_10.flow_rate.aspirate = 5
        # pipette off most of the ethanol
        pipette_10.aspirate(10, source_well.bottom(z=0.3))
        # step up releasing any blockages and giving liquid time to flow into the pipette
        protocol.delay(seconds = 1)
        pipette_10.move_to(source_well.bottom(z=0.5))
        protocol.delay(seconds = 1)
        pipette_10.move_to(source_well.bottom(z=0.7))
        protocol.delay(seconds = 1)
        pipette_10.move_to(source_well.bottom(z=0.9))
        protocol.delay(seconds = 1)
        pipette_10.move_to(source_well.bottom(z=1.1))
        protocol.delay(seconds = 1)
        pipette_10.move_to(source_well.top(-2))
        protocol.delay(seconds = 2)
        pipette_10.touch_tip(source_well, radius=0.75,v_offset=-2, speed=25)
        
        # make the pipetting faster and mix PCR products with SPRI beads
        pipette_10.flow_rate.aspirate = 50
        pipette_10.flow_rate.dispense = 50
        pipette_10.dispense(10, target_plate.rows_by_name()['A'][ticker].bottom(2))
        for iter in range(10):
            pipette_10.aspirate(10, target_plate.rows_by_name()['A'][ticker].bottom(2))
            pipette_10.dispense(10, target_plate.rows_by_name()['A'][ticker].bottom(z=10))
            pipette_10.aspirate(10, target_plate.rows_by_name()['A'][ticker].bottom(4))
            pipette_10.dispense(10, target_plate.rows_by_name()['A'][ticker].bottom(z=12))
        pipette_10.touch_tip(target_plate.rows_by_name()['A'][ticker], radius=0.75,v_offset=-8, speed=25)
        pipette_10.drop_tip()
        ticker = ticker+1
    
    
