#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 11:53:00 2019

@author: neg
"""

from opentrons import protocol_api

# metadata
metadata = {'apiLevel': '2.0',
            'protocolName': 'SPRI Sanger cleanup',
            'author': 'James Kitson',
            'description': 'SPRI cleanups for Sanger Seq'}

# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions

def run(protocol: protocol_api.ProtocolContext):

    # labware for protocol
    reservoir = protocol.load_labware('starlab-E2896-0220',2)
    tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', 3)
    tiprack_200 = protocol.load_labware('opentrons_96_tiprack_300ul', 6)
    
    # module and labware on it
    module = protocol.load_module('magdeck', 1)
    magplate = module.load_labware('sarsteadt_96_wellplate_200ul',
                                      label='Samples')
    
    # pipettes
    left_pipette = protocol.load_instrument('p50_single', mount='left', tip_racksacks=[tiprack])
    right_pipette = protocol.load_instrument('p300_multi', mount='right', tip_racksacks=[tiprack])
    
    # commands
    left_pipette.pick_up_tip()
    left_pipette.distribute(30,
                            reservoir.wells_by_name()['A1'],
                            magplate.rows_by_name()['A'])
    