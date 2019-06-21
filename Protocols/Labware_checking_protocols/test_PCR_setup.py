from opentrons import labware, instruments

metadata = {
    'protocolName': 'Test PCR setup',
    'author': 'James Kitson <James.Kitson@ncl.ac.uk>',
    'description': 'The first PCR setup on the OT-2, just one plate that will be run and gelled'
    }

# Set labware to use
tubes = labware.load('opentrons-tuberack-15ml', '1')
tips300 = labware.load('opentrons-tiprack-300ul', '2')
tips10 = labware.load('tiprack-starlab-S1181-3810', '3')
PCR1 = labware.load('starlab-E1403-5200', '4')
PCR2 = labware.load('starlab-E1403-5200', '5')
forward_primer = labware.load('starlab-E1403-0100','10')

# set pipettes
pipette300 = instruments.P300_Single(mount='left', tip_racks=[tips300])
pipette10 = instruments.P10_Multi(mount='right', tip_racks=[tips10])

# Define starting and transfer volumes
start_vol_oil: float = 2000
start_vol_mastermix: float = 2000
vol_transfer_mastermix: float = 18
vol_transfer_oil: float = 20

# Define tube parameters
total_length_5ml: float = 65.9
length_barrel_5ml: float = 42.6
length_cone_5ml: float = total_length_5ml-length_barrel_5ml
width_5ml: float = 15.3

### DO THIS FOR DEPTH!!!###
# This function will calculate the starting height for any cone bottomed tube
def start_height(start_vol, length_cone, width):
    #define the volume of the tip of the tube
    vol_cone = 3.14*((width/2)**2)*(length_cone/3)
    # if the start volume > tip volume, work out the residual height and add it to the tip height
    if start_vol > vol_cone:
        return length_cone + (start_vol-vol_cone)/(3.14*((width/2)**2))
    # if the starting volume is less than the tip volume, work out the total height
    else:
        return 3*(start_vol/(3.14*((width/2)**2)))

# Calculate the distance from the top of the tube to the top of the mastermix at start
inverse_start_height_mastermix = round(total_length_5ml - start_height(start_vol = start_vol_mastermix,
                                                                      length_cone = length_cone_5ml,
                                                                      width = width_5ml),1)
# Calculate the distance from the top of the tube to the top of the oil at start
inverse_start_height_oil = round(total_length_5ml - start_height(start_vol = start_vol_oil,
                                                                 length_cone = length_cone_5ml,
                                                                 width = width_5ml),1)

# variables for liquid height track
h_liquid_oil = -(distance_from_surface_to_opening_of_trough_in_mm_oil + 5)
h_liquid_mastermix = -(distance_from_surface_to_opening_of_trough_in_mm_mastermix + 5)

def height_track():
    global h_liquid
    dh = vol_transfer/(length*width) # should this be 8*volume_of_mineral_oil_in_ul for a trough?
    h_liquid -= dh
    
height_track()