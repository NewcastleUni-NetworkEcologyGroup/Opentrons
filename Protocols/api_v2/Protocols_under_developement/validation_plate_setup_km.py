#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 12:02:38 2021

@author: neg
"""
from opentrons import protocol_api

# metadata
metadata = {'apiLevel': '2.8',
            'protocolName': 'OPM_DNA multiplate dispense',
            'author': 'James Kitson <james.kitson@newcastle.ac.uk>',
            'description': 'A protocol to distribute OPM_DNA beads to multiple PCR plates'}



# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions

def run(protocol: protocol_api.ProtocolContext):
      
    # key labware dimensions
    tip_height = 3.5
    well_width =8.3
    well_length = 8.3
    
    # key liquid volumes
    OPM_vol = 10
    
    # Set the initial DNA volumes in 2ml tubes
    OPM_start_vol = 1000
    Carcelia_start_vol = 1000
       
    # create a function that works out the starting liquid height
    def start_height(OPM_start_vol, tip_height, well_width, well_length):
        # define the volume of the tip of the well tip
        #tip_vol = ((tip_height*well_width)/2)*well_length
        tip_vol = (2/3)*3.14159*tip_height**3
        # if the start volume > tip volume, work out the residual height, add it to the tip height and subrtact it from the total height of the tube
        if OPM_start_vol > tip_vol:
            return round(tip_height+((OPM_start_vol-tip_vol)/(well_width*well_length)),1)
        # if the starting volume is less than the tip volume, work out the total height and subrtact it from the total height of the tube
        else:
            return (3*OPM_start_vol/(2*3.14159))**(1/3)
        
    # calculate the initial liquid heights
    initial_OPM_height = start_height(OPM_start_vol, tip_height, well_width, well_length)
    initial_Carcelia_height = start_height(Carcelia_start_vol, tip_height, well_width, well_length)
  
    print("The initial OPM_DNA volume is: ", OPM_start_vol)
    print("The initial OPM_DNA height is: ", initial_OPM_height)
    print("The initial OPM_DNA volume is: ", Carcelia_start_vol)
    print("The initial OPM_DNA height is: ", initial_Carcelia_height)
    

    # set up the source DNA locations
    reservoir = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap',9)
    OPM_DNA = reservoir['A1']
    Carcelia_DNA = reservoir['A2']
    
    # set up destination plates
    low = protocol.load_labware('sarstedt_96_skirted_wellplate_200ul',1, 'Low incidence plate')
    med = protocol.load_labware('sarstedt_96_skirted_wellplate_200ul',4, 'Medium incidence plate')
    high = protocol.load_labware('sarstedt_96_skirted_wellplate_200ul',7, 'High incidence plate')
    
    platelist=[low,med,high]
    
    # set up tip locations
    tiprack_1 = protocol.load_labware('opentrons_96_filtertiprack_200ul', 3)
    tiprack_2 = protocol.load_labware('opentrons_96_filtertiprack_200ul', 6)
    
    # set up pipette
    pipette_300 = protocol.load_instrument('p300_single', mount='left', tip_racks=[tiprack_1,tiprack_2]) 
    ticker = 0
    steps=11*len(platelist)
    
    # distribute OPM_DNA using distribute command and well referencing - may need replacing with aspirate and dispense if I need waiting times etc
    for plate in platelist:
        pipette_300.pick_up_tip()
        for col in [0,1,2,3,4,5,6,7,8,9,10]:
            print('Round', ticker, 'pipetting height', pipette_300.well_bottom_clearance.aspirate)
            pipette_300.aspirate((OPM_vol*12)+5, OPM_DNA)
            for well in plate.columns()[col]:
                pipette_300.dispense(OPM_vol,
                                     well)    
            pipette_300.blow_out(OPM_DNA.top(-2))
            # tasks done so add one to the ticker to calulate new pipette heights.
            ticker = ticker+1
                      
            # change the aspirate height on the OPM_DNA to move down a bit, if it is the last step, set a special heigh that isn't zero and slow the aspirate right down
            if ticker < steps:
                pipette_300.well_bottom_clearance.aspirate = round((initial_OPM_height)-((initial_OPM_height/steps)*(ticker*0.9)),1)
            elif ticker == steps:
                pipette_300.well_bottom_clearance.aspirate = round((initial_OPM_height)-((initial_OPM_height/steps)*(ticker*0.9)),1)
                pipette_300.flow_rate.aspirate = 5
        pipette_300.drop_tip()
        
        
    ##Carcelia spiking
    
    # File path on robot
    #input_file_path = '/Python_files/Input/validation_spiked_Wells_csv_ot.csv'
    # File path on local machine for simulation
    input_file_path = './validation_spiked_wells_csv_ot.csv'
    status_csv = open(input_file_path, 'r').read()
            
    # Sort the raw data into a list
    #data = [
     #           [slot, source_plate, source_well, vol]
      #          for slot, source_plate, source_well, vol in
       #         [row.split(',') for row in status_csv.strip().splitlines() if row]
        #        ]      
    data = [ 
            [Wells, Plate, Volume]
            for Wells, Plate, Volume in
            [row.split(',') for row in status_csv.strip().splitlines() if row]
            ]
            # Make the transfers using the nested values in the data list
    #for well_idx, (slot, source_plate, source_well, vol) in enumerate(data):
     #   vol = float(vol)
      #  pipette.transfer(
       #                 vol,
        #                vars()[source_plate].wells(source_well).bottom(3),
         #               dest_plate.wells(well_idx).bottom(3),
          #              new_tip=tip_strategy,
           #             blow_out=True)
    
    # for well_idx, (Wells, Plate, Volume) in enumerate(data):
    #     print(vars()[Plate][[Wells]])
      
    # for well_idx, (Wells, Plate, Volume) in enumerate(data):
    #      pipette_300.transfer(
    #                      vars()[Volume],
    #                      Carcelia_DNA,
    #                      vars()[Plate][Wells].bottom(3),
    #                      new_tip='once',
    #                      blow_out=False)
    
    for well_idx, (Wells, Plate, Volume) in enumerate(data):
         pipette_300.transfer(
                         Volume,
                         Carcelia_DNA,
                         vars()[Plate].wells(Wells),
                         new_tip='once',
                         blow_out=False)
        
        
    # MAKE THIS TARGET CORRECTLY
    #MAKE THIS STEP DOWN WITH EACH PIPETTING