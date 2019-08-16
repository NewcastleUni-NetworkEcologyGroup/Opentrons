from opentrons import labware, instruments

metadata = {
    'protocolName': 'Tissue lysate into PDB+EtOH then into spin column',
    'author': 'James Kitson',
    'description': 'a series of commands that will transfer tissue lysate from a deepwell plate into mixing plates and then on to spin columns' 
    }

# get the plates loaded in the middle of the deck so we can do fancy multichannel pickups
lysate_plate1 = labware.load('starlab-E1403-0100', '4', 'input lysate plate')
lysate_plate2 = labware.load('starlab-E1403-0100', '5', 'input lysate plate')

mix_plate1 = labware.load('starlab-E1403-0100', '7', 'mixing plate')
mix_plate2 = labware.load('starlab-E1403-0100', '8', 'mixing plate')

spin_cols1 = labware.load('spin_cols_96', '10', 'mixing plate')
spin_cols2 = labware.load('spin_cols_96', '11', 'mixing plate')


tips_300 = [labware.load('tiprack-starlab-S1120-9810', str(slot))
             for slot in [1,2]]

# set pipettes
pipette300 = instruments.P300_Multi(mount='left', tip_racks=tips_300)

lysate_volume: float=200
denature_volume: float=400

# =============================================================================
# for well in ['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12']:
#     pipette300.pick_up_tip()
#     pipette300.aspirate(lysate_volume, lysate_plate1[well].top(-20))
#     pipette300.dispense(lysate_volume, mix_plate1[well].bottom(3))
#     pipette300.mix(5,lysate_volume)
#     pipette300.transfer(lysate_volume+denature_volume,
#                         mix_plate1[well].bottom(0.5),
#                         spin_cols1[well].top(-4),
#                         new_tip='never').blow_out()
#     pipette300.drop_tip()
#     
# for well in ['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12']:
#     pipette300.pick_up_tip()
#     pipette300.aspirate(lysate_volume, lysate_plate2[well].top(-20))
#     pipette300.dispense(lysate_volume, mix_plate2[well].bottom(3))
#     pipette300.mix(5,lysate_volume)
#     pipette300.transfer(lysate_volume+denature_volume,
#                         mix_plate2[well].bottom(0.5),
#                         spin_cols2[well].top(-4),
#                         new_tip='never').blow_out()
#     pipette300.drop_tip()
# =============================================================================

lysates=[lysate_plate1,lysate_plate2]
mixes=[mix_plate1,mix_plate2]
spins=[spin_cols1,spin_cols2]

for idx, plate in enumerate(lysates):
    for well in ['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12']:
        pipette300.pick_up_tip()
        pipette300.aspirate(lysate_volume, plate[well].top(-20))
        pipette300.dispense(lysate_volume, mixes[idx][well].bottom(3))
        pipette300.mix(5,lysate_volume)
        pipette300.transfer(lysate_volume+denature_volume,
                            mixes[idx][well].bottom(0.5),
                            spins[idx][well].top(-4),
                            air_gap=20,
                            touch_tip=True,
                            new_tip='never').blow_out(spins[idx][well].top(-4))
        pipette300.drop_tip()
        

