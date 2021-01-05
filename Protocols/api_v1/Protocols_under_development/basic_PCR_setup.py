from opentrons import labware, instruments

metadata = {
    'protocolName': 'Temp gradient PCR set up',
    'author': 'James Kitson',
        'description': 'A protocol to set up PCRs in a variable number of columns on a plate, all with the same primer combination'
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

# set PCR parameters
mastermix_vol: float = 18.5
DNA_vol: float = 1.5
sample_num: float = 85
neg_num: float = 1

# distribute mastermix
pipette50.pick_up_tip()
for idx, x in enumerate(range(0, sample_num+neg_num)):
    pipette50.transfer(mastermix_vol,
                       mastermix('A1').bottom(round(35-(idx*(34/(sample_num+neg_num))))),
                       PCR_plate(x).bottom(1),
                       blow_out=True,
                       new_tip='never')
pipette50.drop_tip()

# distribute DNA (the 0.49 just ensures that you will always include a partially filled row at the end)
for x in range(0, (round((sample_num/8)+0.49))):
    pipette10.transfer(DNA_vol,
                       DNA_plate.cols(x).bottom(1),
                       PCR_plate.cols(x).bottom(1),
                       blow_out=True)

# distribute the negative 'sample' from a tube
for x in range(sample_num, sample_num+neg_num):
    pipette10.pick_up_tip(tips_10['H12'])
    pipette10.aspirate(DNA_vol,mastermix('A2').top(-10))
    pipette10.dispense(DNA_vol,PCR_plate(x).bottom(1)).blow_out()
    pipette10.drop_tip()
                       


#for idx, x in enumerate(range(0, sample_num+neg_num)):
#    print(round(37-(idx*(36/(sample_num+neg_num)))))