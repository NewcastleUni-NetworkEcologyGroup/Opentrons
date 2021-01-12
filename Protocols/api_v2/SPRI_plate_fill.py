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
    number_of_destination_plates: int = 5
    if number_of_destination_plates > 5:
        raise Exception('Please specify 5 or fewer destination plates, you cant hold enough SPRI beads in a 2.2ml plate for more.') 

    # labware for protocol
    reservoir = protocol.load_labware('sarstedt_96_wellplate_2200ul',5)
    beads = reservoir.wells('A1')
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
    all_dests = [well for plate in dest_plates for well in plate.rows('A')]
    
    # # set pipetting parameters
    left_pipette.flow_rate.aspirate = 25
    left_pipette.well_bottom_clearance.aspirate = 10
    left_pipette.flow_rate.dispense = 50
    left_pipette.well_bottom_clearance.dispense = 2
    left_pipette.flow_rate.blow_out = 10
    
    # distribute spri mix
    # for d in all_dests:
    #     left_pipette.distribute(spri_vol, beads, d, new_tip='always', touch_tip=True)
    
    spri_dest=['B1','C1','D1','E1','F1','G1','H1']
    
    for plate in dest_plates:
        for idx in spri_dest:
            left_pipette.aspirate(spri_vol,beads)
            left_pipette.dispense(spri_vol,plate.wells(idx))


# Tris_dest=['B1','C1','D1','E1','F1','G1','H1']

# # Get a tip
# pipette1000.pick_up_tip()

# for idx, x in enumerate(Tris_dest):
#    pipette1000.transfer(Tris_vols.__getitem__(idx),
#                      Tris.top(-105),
#                      trough.well(x).bottom(5),
#                      new_tip='never')    

    # # This function will calculate the starting height for any pointy bottomed tube relative to top of the tube.
    # # This requires you to state whether the well is square or round as the tip volume will either be calculated as a cone or a pyramid.
    # def start_height(start_vol, total_length, well_shape, tip_length, width):
    #     # define the volume of the tip of the tube if the tip is a cone
    #     if well_shape == 'round':
    #         vol_tip = 3.14*((width/2)**2)*(tip_length/3)
    #         # if the start volume > tip volume, work out the residual height, add it to the tip height and subrtact it from the total height of the tube
    #         if start_vol > vol_tip:
    #             return -(total_length - (tip_length + (start_vol-vol_tip)/(3.14*((width/2)**2))))
    #         # if the starting volume is less than the tip volume, work out the total height and subrtact it from the total height of the tube
    #         else:
    #             return -(total_length - (3*(start_vol/(3.14*((width/2)**2)))))
    #     # calulate the tip volume if the tip is a pyramid
    #     elif well_shape == "square":
    #         vol_tip = (width*width*tip_length)/3
    #         # if the start volume > tip volume, work out the residual height, add it to the tip height and subrtact it from the total height of the tube
    #         if start_vol > vol_tip:
    #             return -(total_length - (tip_length + (start_vol-vol_tip)/(width*width)))
    #         # if the starting volume is less than the tip volume, work out the total height and subrtact it from the total height of the tube
    #         else:
    #             return -(total_length - ((start_vol/((width*width*tip_length)/3))))
    #     if well_shape != 'round' or 'square':
    #         raise Exception('well_shape must be either \'round\' or \'square\'' )
        
    # # Calculate the distance from the top of the tube to the top of the beads at start
    # inverse_start_height_beads = round(start_height(start_vol = start_vol_beads,
    #                                                     total_length=total_length_deepwell,
    #                                                     well_shape='round',
    #                                                     tip_length = tip_length_deepwell,
    #                                                     width = width_deepwell),1)

    # pipette_height_beads = inverse_start_height_beads
    
    # # The following function creates a tracking value for the liquid height in a well
    # def height_track(transfer_vol):
    #     global remain_vol
    #     remain_vol = remain_vol-transfer_vol # should this be 8*volume_of_mineral_beads_in_ul for a trough?
    #     remain_height = round(start_height(start_vol = remain_vol,
    #                                               total_length=total_length_deepwell,
    #                                               well_shape='round',
    #                                               tip_length = tip_length_deepwell,
    #                                               width = width_deepwell),1)
    #     return remain_height
    
    # # Before starting set the remaining vol of beads to the starting volume
    # remain_vol = start_vol_beads   
  
    # # Get a tip
    # left_pipette.pick_up_tip()
    # #Set a pipette depth using the formula, this is currently done manually as I don't have direct access to the total aspiration volume in a distribute
    # pipette_height_beads = height_track(transfer_vol=300)
    
    # #Transfer the beads
    # for d in all_dests:
    #     if (pipette_height_beads*-1) < total_length_deepwell:
    #         print("Sufficient SPRI beads to proceed")
    #         # Distribute the beads to the plates
    #         left_pipette.well_bottom_clearance.aspirate = pipette_height_beads-1
    #         left_pipette.distribute(spri_vol, beads, d, new_tip='always', touch_tip=True)
    #     if (pipette_height_beads*-1) >= total_length_deepwell:
    #         raise Exception('\n##############################\nInsufficient SybrGreen 1 for protocol!!\n##############################')
