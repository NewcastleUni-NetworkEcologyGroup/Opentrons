from opentrons import labware, instruments

metadata = {
    'protocolName': 'Temp gradient PCR set up',
    'author': 'James Kitson',
        'description': 'A protocol to set up PCRs on specific columns of a plate for temperature gradients'
    }


# get the plates loaded in the middle of the deck so we can do fancy multichannel pickups
DNA_plate = labware.load('starlab-E1403-0100', '4', 'input DNA plate')
PCR_plate = labware.load('starlab-E1403-0100', '5', 'PCR plate')
mastermix = labware.load('opentrons_24_tuberack_generic_2ml_screwcap', '6', 'tube of mastermix')

# load the tips at the top of the deck
tips_50 = labware.load('tiprack-starlab-S1120-2810', '10', 'mastermix tips')
tips_10 = labware.load('tiprack-starlab-S1121-3810', '11', 'DNA tips')

# set pipettes
pipette50 = instruments.P50_Single(mount='left', tip_racks=[tips_50])
pipette10 = instruments.P10_Multi(mount='right', tip_racks=[tips_10])

# distribute the mastermix
pipette50.pick_up_tip()
for x in ['1','6','9','12']:
    for y in ['C','D','E','F']:
        pipette50.transfer(18.5,
                           mastermix('A1').bottom(1),
                           PCR_plate(y+x).bottom(1),
                           touch_tip=False,
                           new_tip='never')
pipette50.drop_tip()

#Distribute the DNA
for x in ['1','6','9','12']:
    for y in ['C']:
        pipette10.pick_up_tip(tips_10('F'+x))
        pipette10.transfer(1.5,
                           DNA_plate('F1').bottom(1),
                           PCR_plate(y+x).bottom(1),
                           touch_tip=False,
                           blow_out=True)
        
# =============================================================================
# #Distribute the water for the negative
# pipette10.pick_up_tip(tips_10('H2'))
# pipette10.distribute(1.5,
#                    mastermix('A2').bottom(1),
#                    PCR_plate('F1','F6','F9','F12').bottom(1),
#                    touch_tip=False,
#                    new_tip='never')
# pipette10.drop_tip()
#         
# =============================================================================
        
        