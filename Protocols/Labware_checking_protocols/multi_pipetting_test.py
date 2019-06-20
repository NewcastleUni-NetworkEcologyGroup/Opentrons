from opentrons import labware, instruments

metadata = {
    'protocolName': 'Test multiplate',
    'author': 'James Kitson <James.Kitson@ncl.ac.uk>',
    'description': 'A simple test protocol that checks I can pipette into the same target well on multiple plates'
    }

# Set labware to use
trough = labware.load('starlab-E2310-1200', '1')
#tips300 = labware.load('opentrons-tiprack-300ul', '2')
tips10 = labware.load('tiprack-starlab-S1181-3810', '2')
tips10L = labware.load('tiprack-starlab-S1120-3810', '3')
PCR1 = labware.load('starlab-E1403-5200', '4')
PCR2 = labware.load('starlab-E1403-5200', '5')
forward_primer = labware.load('starlab-E1403-0100','10')

# set pipettes
pipette10 = instruments.P10_Multi(mount='right', tip_racks=[tips10, tips10L])
#pipette300 = instruments.P300_Multi(mount='left', tip_racks=[tips300])

master_mix = trough.wells('A3')

dest_plates = [PCR1,PCR2]

all_dests = [well for plate in dest_plates for well in plate.rows('A')]

# 
#for d in all_dests:
#    pipette300.transfer(30, master_mix, d.top(), blow_out=True, new_tip='never')
#pipette300.drop_tip()

# forward primer distribution
for ind, primer in enumerate(forward_primer.rows('A')):
    dests = [plate.rows('A')[ind] for plate in dest_plates]
    pipette10.distribute(1, primer, dests,
                         air_gap=5,
                         trash=False)

# forward primer distribution
for ind, primer in enumerate(forward_primer.rows('A')):
    dests = [plate.rows('A')[ind] for plate in dest_plates]
    pipette10.distribute(1, primer, dests,
                         air_gap=5,
                         trash=False)