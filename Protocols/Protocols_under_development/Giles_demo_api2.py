#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 11:53:00 2019

@author: neg
"""

from opentrons import protocol_api

# metadata
metadata = {'apiLevel': '2.0',
            'protocolName': 'My Protocol',
            'author': 'Name <email@address.com>',
            'description': 'Pipetteing out some blue and yellow dye for Giles and Nicola'}

# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions

def run(protocol: protocol_api.ProtocolContext):

    # labware
    plate = protocol.load_labware('starlab-E1403-0100', 3)
    reservoir = protocol.load_labware('starlab-E2896-0220',2)
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', 1)
    
    # pipettes
    left_pipette = protocol.load_instrument('p300_multi', mount='left', tip_racksacks=[tiprack])
    
    # commands
    left_pipette.pick_up_tip()
    left_pipette.distribute(30,
                            reservoir.wells_by_name()['A1'],
                            plate.rows_by_name()['A'])
    
    left_pipette.distribute(30,
                       reservoir.wells_by_name['A2'],
                       [plate.wells_by_name()[well_name] for well_name in ['A1', 'A3', 'A5', 'A7', 'A9', 'A11']])
