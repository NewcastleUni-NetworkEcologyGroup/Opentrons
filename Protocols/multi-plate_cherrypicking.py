from opentrons import labware, instruments

metadata = {
    'protocolName': 'Cherrypicking CSV',
    'author': 'James Kitson',
    'source': 'modified from Protocol Library'
    }

# =============================================================================
# example_csv (Slot, Plate name, Well, Volume)
# 
# 1, plate2, A1, 20
# 2, plate4, A3, 10
# 3, plate8, B2, 15
# 
# =============================================================================

# File path on robot
input_file_path = '/data/custom_input_data/cherrypicking.csv'
# File path on local machine for simulation
#input_file_path = '/home/neg/Documents/Projects/Cratopus/Cratopus-chrysochlorus-diet/Output_files/cherrypicking.csv'
volumes_csv = open(input_file_path, 'r').read()

# Set up other parameters for the code to follow
pipette_model = 'p50'
source_plate_type = 'starlab-E1403-0100'
destination_plate_type = 'starlab-E1403-0100'
tip_reuse = 'new tip each time'
tip_type = 'tiprack-starlab-S1120-2810'

# Set a max volume of pipette based on the selcted model to automatically load the correct pipette - can probably simplify this a lot
pipette_max_vol = int(pipette_model[1:])

# Assign slots for tips and destination plate
tiprack_slots = ['10']
dest_plate = labware.load(destination_plate_type, '11')

# Set pipette type based on maximum volume
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

# Sort the raw data into a list
data = [
    [slot, source_plate, source_well, vol]
    for slot, source_plate, source_well, vol in
    [row.split(',') for row in volumes_csv.strip().splitlines() if row]
]

# Create a list to keep track of slots we've already used, incuding slots preallocated to tips and output plate
slot_list=['10','11']

for idx, (slot, source_plate, source_well, vol) in enumerate(data):
    # Check we've not already filled the slot
    if slot not in slot_list:
        # Create the labware and add the slot to slot_list
        vars()[source_plate]=labware.load(source_plate_type, str(slot), str(source_plate))
        slot_list.append(slot)

# Set how you want to use tips
tip_strategy = 'always' if tip_reuse == 'new tip each time' else 'once'

# Make the transfers using the nested values in the data list
for well_idx, (slot, source_plate, source_well, vol) in enumerate(data):
    vol = float(vol)
    pipette.transfer(
                    vol,
                    vars()[source_plate].wells(source_well).bottom(3),
                    dest_plate.wells(well_idx).bottom(3),
                    new_tip=tip_strategy,
                    blow_out=True)
