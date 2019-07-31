from opentrons import labware, instruments

metadata = {
    'protocolName': 'Cherrypicking CSV',
    'author': 'James Kitson',
    'source': 'modified from Protocol Library'
    }

# =============================================================================
# example_csv (Slot, Well, Volume)
# 
# 2, A1, 20
# 4, A3, 10
# 8, B2, 15
# 
# =============================================================================

input_file_path = './cherrypicking.csv'
volumes_csv = open(input_file_path, 'r').read()
pipette_model = 'p50'
source_plate_type = 'starlab-E1403-0100'
destination_plate_type = 'starlab-E1403-0100'
tip_reuse = 'new tip each time'
tip_type = 'tiprack-starlab-S1120-9810'
number_of_source_plates = 2

pipette_max_vol = int(pipette_model[1:])

tiprack_slots = ['10']
dest_plate = labware.load(destination_plate_type, '11')

if pipette_max_vol == 300:
    tipracks = [
        labware.load(tip_type, slot) for slot in tiprack_slots]
    pipette = instruments.P300_Single(mount='left', tip_racks=tipracks)
elif pipette_max_vol == 50:
    tipracks = [
        labware.load(tip_type, slot) for slot in tiprack_slots]
    pipette = instruments.P50_Single(mount='left', tip_racks=tipracks)
elif pipette_max_vol == 10:
    tipracks = [
        labware.load(tip_type, slot) for slot in tiprack_slots]
    pipette = instruments.P10_Single(mount='left', tip_racks=tipracks)
elif pipette_max_vol == 1000:
    tipracks = [
        labware.load(tip_type, slot) for slot in tiprack_slots]
    pipette = instruments.P1000_Single(mount='left', tip_racks=tipracks)

data = [
    [plate, well, vol]
    for plate, well, vol in
    [row.split(',') for row in volumes_csv.strip().splitlines() if row]
]

# =============================================================================
# #source_plate = labware.load(source_plate_type, '2')
# source_plates = [labware.load(source_plate_type, str(slot), 'source plate')
#              for slot in range(2, 2+(number_of_source_plates-1))]
# =============================================================================

plate1 = labware.load(source_plate_type, '1', 'source plate')
plate2 = labware.load(source_plate_type, '2', 'source plate')

# =============================================================================
# # set a source desitination with negatives in and a fancy pattern of destination wells
# dest_plates=[PCR1,PCR2]
# all_dests = [well for plate in dest_plates for well in plate.rows('A')]
# =============================================================================

tip_strategy = 'always' if tip_reuse == 'new tip each time' else 'once'

for well_idx, (source_plate, source_well, vol) in enumerate(data):
    if source_well and vol:
        vol = float(vol)
        pipette.transfer(
            vol,
            vars()[source_plate].wells(source_well).bottom(3),
            dest_plate.wells(well_idx).bottom(3),
            new_tip=tip_strategy)
