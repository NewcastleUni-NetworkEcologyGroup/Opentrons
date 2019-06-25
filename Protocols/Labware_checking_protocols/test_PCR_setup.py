from opentrons import labware, instruments

metadata = {
    'protocolName': 'Test PCR setup',
    'author': 'James Kitson <James.Kitson@ncl.ac.uk>',
    'description': 'The first PCR setup on the OT-2, just one plate that will be run and gelled'
    }

# Set labware to use
trough = labware.load('starlab-E2896-0220', '5')
tips300 = labware.load('opentrons-tiprack-300ul', '2')
tips10 = labware.load('tiprack-starlab-S1181-3810', '3')
PCR1 = labware.load('starlab-E1403-0100','4')
#PCR2 = labware.load('starlab-E1403-5200', '5')
forward_primer = labware.load('starlab-E1403-0100','10')

# set pipettes
pipette300 = instruments.P300_Multi(mount='left', tip_racks=[tips300])
pipette10 = instruments.P10_Multi(mount='right', tip_racks=[tips10])

# Define starting and transfer volumes
start_vol_oil: float = 1500
start_vol_mastermix: float = 500
vol_transfer_mastermix: float = 18
vol_transfer_oil: float = 20
vol_transfer_primer: float = 1

# Define position of oil and mastermix
#mineral_oil = tubes['A1']
#mastermix = tubes['C1']

# Define position of oil and mastermix
mineral_oil = trough['A3']
mastermix = trough['A1']


# Define tube parameters
total_length_5ml: float = 65.9
length_barrel_5ml: float = 42.6
tip_length_5ml: float = round(total_length_5ml-length_barrel_5ml,1)
width_5ml: float = 15.3

total_length_deepwell: float = 37
length_barrel_deepwell: float = 34
tip_length_deepwell: float = round(total_length_deepwell-length_barrel_deepwell,1)
width_deepwell: float = 8

# This function will calculate the starting height for any pointy bottomed tube relative to top of the tube
def start_height(start_vol, total_length, tip_type, tip_length, width):
    #define the volume of the tip of the tube
    if tip_type == 'round':
        vol_tip = 3.14*((width/2)**2)*(tip_length/3)
        # if the start volume > tip volume, work out the residual height, add it to the tip height and subrtact it from the total height of the tube
        if start_vol > vol_tip:
            return -(total_length - (tip_length + (start_vol-vol_tip)/(3.14*((width/2)**2))))
        # if the starting volume is less than the tip volume, work out the total height and subrtact it from the total height of the tube
        else:
            return -(total_length - (3*(start_vol/(3.14*((width/2)**2)))))
    elif tip_type == "pyramid":
        vol_tip = (width*width*tip_length)/3
        # if the start volume > tip volume, work out the residual height, add it to the tip height and subrtact it from the total height of the tube
        if start_vol > vol_tip:
           return -(total_length - (tip_length + (start_vol-vol_tip)/(width*width)))
        # if the starting volume is less than the tip volume, work out the total height and subrtact it from the total height of the tube
        else:
           return -(total_length - ((start_vol/((width*width*tip_length)/3))))
    if tip_type != 'round' or 'pyramid':
        raise Exception('tip_type must be either \'round\' or \'pyramid\'' )


# Calculate the distance from the top of the tube to the top of the mastermix at start
#inverse_start_height_mastermix = round(start_height(start_vol = start_vol_mastermix,
#                                                    total_length=total_length_5ml,
#                                                    tip_type='round',
#                                                    tip_length = tip_length_5ml,
#                                                    width = width_5ml),1)
# Calculate the distance from the top of the tube to the top of the oil at start
#inverse_start_height_oil = round(start_height(start_vol = start_vol_oil,
#                                              total_length=total_length_5ml,
#                                              tip_type='round',
#                                              tip_length = tip_length_5ml,
#                                              width = width_5ml),1)

# Calculate the distance from the top of the tube to the top of the mastermix at start
inverse_start_height_mastermix = round(start_height(start_vol = start_vol_mastermix,
                                                    total_length=total_length_deepwell,
                                                    tip_type='pyramid',
                                                    tip_length = tip_length_deepwell,
                                                    width = width_deepwell),1)
# Calculate the distance from the top of the tube to the top of the oil at start
inverse_start_height_oil = round(start_height(start_vol = start_vol_oil,
                                              total_length=total_length_deepwell,
                                              tip_type='pyramid',
                                              tip_length = tip_length_deepwell,
                                              width = width_deepwell),1)


def height_track(transfer_vol):
    global remain_vol
    remain_vol = remain_vol-transfer_vol # should this be 8*volume_of_mineral_oil_in_ul for a trough?
    remain_height = round(start_height(start_vol = remain_vol,
                                              total_length=total_length_deepwell,
                                              tip_type='pyramid',
                                              tip_length = tip_length_deepwell,
                                              width = width_deepwell),1)
    return remain_height


remain_vol = start_vol_oil
#pipette_height_oil = height_track(vol_transfer_oil)

# transfer mineral oil
pipette300.set_flow_rate(aspirate=5, dispense=5)
#t_count = 0
pipette300.pick_up_tip()
for dest_col in ['A5','A6','A7','A8']:
    pipette_height_oil = height_track(vol_transfer_oil)
    pipette300.aspirate(vol_transfer_oil, mineral_oil.top(pipette_height_oil-5))
    pipette300.move_to(mineral_oil.top(-1)) 
    pipette300.delay(seconds=2)
    pipette300.touch_tip(radius = 0.8)
    pipette300.dispense(PCR1.wells(dest_col).bottom(5)).blow_out()
    pipette300.move_to(PCR1.wells(dest_col).top(-1)) 
    pipette300.delay(seconds=2)
    pipette300.touch_tip(radius = 0.8)
    #t_count += 1
pipette300.drop_tip()


remain_vol = start_vol_mastermix    
#pipette_height_mastermix = height_track(vol_transfer_mastermix)

# transfer mastermix
pipette300.set_flow_rate(aspirate=25, dispense=25)
pipette300.pick_up_tip()
pipette300.distribute(vol_transfer_mastermix,
                      mastermix.bottom(2),
                      PCR1.cols('1', to ='4'))

# transfer primers
for x in ['A5','A6','A7','A8']:
    pipette10.pick_up_tip()
    pipette10.aspirate(vol_transfer_primer, forward_primer.well(x).bottom(2))
    pipette10.dispense(vol_transfer_primer, PCR1.well(x).bottom(2)).blow_out()
    pipette10.touch_tip(radius = 0.8)
    pipette10.drop_tip()
    