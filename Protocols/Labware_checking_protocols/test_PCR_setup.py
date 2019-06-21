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
PCR1 = labware.load('starlab-E1403-0100','4')
#PCR2 = labware.load('starlab-E1403-5200', '5')
forward_primer = labware.load('starlab-E1403-0100','10')

# set pipettes
pipette300 = instruments.P300_Multi(mount='left', tip_racks=[tips300])
pipette10 = instruments.P10_Multi(mount='right', tip_racks=[tips10])

# Define starting and transfer volumes
start_vol_oil: float = 3000
start_vol_mastermix: float = 2000
vol_transfer_mastermix: float = 18
vol_transfer_oil: float = 20
vol_transfer_primer: float = 1

# Define position of oil and mastermix
mineral_oil = tubes['A1']
mastermix = tubes['A3']

# Define tube parameters
total_length_5ml: float = 65.9
length_barrel_5ml: float = 42.6
length_cone_5ml: float = round(total_length_5ml-length_barrel_5ml,1)
width_5ml: float = 15.3

# This function will calculate the starting height for any cone bottomed tube relative to top of the tube
def start_height(start_vol, total_length, length_cone, width):
    #define the volume of the tip of the tube
    vol_cone = 3.14*((width/2)**2)*(length_cone/3)
    # if the start volume > tip volume, work out the residual height, add it to the tip height and subrtact it from the total height of the tube
    if start_vol > vol_cone:
        return -(total_length - (length_cone + (start_vol-vol_cone)/(3.14*((width/2)**2))))
    # if the starting volume is less than the tip volume, work out the total height and subrtact it from the total height of the tube
    else:
        return -(total_length - (3*(start_vol/(3.14*((width/2)**2)))))

# Calculate the distance from the top of the tube to the top of the mastermix at start
inverse_start_height_mastermix = round(start_height(start_vol = start_vol_mastermix,
                                                    total_length=total_length_5ml,
                                                    length_cone = length_cone_5ml,
                                                    width = width_5ml),1)
# Calculate the distance from the top of the tube to the top of the oil at start
inverse_start_height_oil = round(start_height(start_vol = start_vol_oil,
                                              total_length=total_length_5ml,
                                              length_cone = length_cone_5ml,
                                              width = width_5ml),1)

def height_track(transfer_vol):
    global remain_vol
    remain_vol = remain_vol-transfer_vol # should this be 8*volume_of_mineral_oil_in_ul for a trough?
    remain_height = round(start_height(start_vol = remain_vol,
                                              total_length=total_length_5ml,
                                              length_cone = length_cone_5ml,
                                              width = width_5ml),1)
    return remain_height


remain_vol = start_vol_oil
#pipette_height_oil = height_track(vol_transfer_oil)

# transfer mineral oil
pipette300.set_flow_rate(aspirate=5, dispense=10)
t_count = 0
pipette300.pick_up_tip()
for x in PCR1.wells('A1', to='H4'):
    if t_count == 16:
        pipette300.drop_tip()
        pipette300.pick_up_tip()
        t_count = 1
        
        pipette_height_oil = height_track(vol_transfer_oil)
        pipette300.aspirate(vol_transfer_oil, mineral_oil.top(pipette_height_oil))
        pipette300.delay(seconds=2)
        pipette300.touch_tip(radius = 0.8)
        pipette300.dispense(PCR1.wells(x).bottom(5))
        pipette300.delay(seconds=2)
        pipette300.touch_tip(radius = 0.8)
        t_count += 1
pipette300.drop_tip()


remain_vol = start_vol_mastermix    
#pipette_height_mastermix = height_track(vol_transfer_mastermix)

# transfer mastermix
pipette300.set_flow_rate(aspirate=25, dispense=50)
pipette300.pick_up_tip()
pipette300.distribute(vol_transfer_mastermix, mastermix, PCR1.wells('A1', to='H4'), new_tip='never').touch_tip(radius=0.8)
pipette300.drop_tip()

for x in ['A1','A2','A3','A4']:
    pipette10.pick_up_tip()
    pipette10.aspirate(vol_transfer_primer, forward_primer.well(x).bottom(2))
    pipette10.dispense(PCR1.well(x).bottom(5))
    pipette10.touch_tip(radius = 0.8)
    pipette10.drop_tip()
    