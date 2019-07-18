from opentrons import labware, instruments

metadata = {
    'protocolName': 'Justin PCR setup',
    'author': 'James Kitson <James.Kitson@ncl.ac.uk>',
    'description': 'Justin PCR plate setup protocol for HiSeq runs'
    }

# Set labware to use
tips10_1 = labware.load('tiprack-starlab-S1180-3810', '1', 'for primers')
tips10_2 = labware.load('tiprack-starlab-S1180-3810', '2', 'for template DNA')
tips300 = labware.load('opentrons-tiprack-300ul', '3', 'for oil and mastermix')
trough = labware.load('starlab-E2896-0220', '4', 'oil trough')
PCR1 = labware.load('starlab-E1403-0100','5', 'output plate')
primer_mix = labware.load('starlab-E1403-0100','6', 'primer plate')
PCR2 = labware.load('starlab-E1403-0100','8', 'output plate')

# set pipettes
pipette300 = instruments.P300_Multi(mount='left', tip_racks=[tips300])
pipette10 = instruments.P10_Multi(mount='right', tip_racks=[tips10_1, tips10_2])

# Define starting and transfer volumes
start_vol_oil: float = 1500
start_vol_mastermix: float = 530.4
vol_transfer_mastermix: float = 17
vol_transfer_oil: float = 20
vol_transfer_primer: float = 1

# Define position of oil and mastermix
mineral_oil = trough['A1']
mastermix = trough['A3']

#define deepwell plate parameters for 2.2ml deepwell plates
total_length_deepwell: float = 37
length_barrel_deepwell: float = 34
tip_length_deepwell: float = round(total_length_deepwell-length_barrel_deepwell,1)
width_deepwell: float = 8

# This function will calculate the starting height for any pointy bottomed tube relative to top of the tube.
# This requires you to state whether the well is square or round as the tip volume will either be calculated as a cone or a pyramid.
def start_height(start_vol, total_length, well_shape, tip_length, width):
    #define the volume of the tip of the tube if the tip is a cone
    if well_shape == 'round':
        vol_tip = 3.14*((width/2)**2)*(tip_length/3)
        # if the start volume > tip volume, work out the residual height, add it to the tip height and subrtact it from the total height of the tube
        if start_vol > vol_tip:
            return -(total_length - (tip_length + (start_vol-vol_tip)/(3.14*((width/2)**2))))
        # if the starting volume is less than the tip volume, work out the total height and subrtact it from the total height of the tube
        else:
            return -(total_length - (3*(start_vol/(3.14*((width/2)**2)))))
    #calulate the tip volume if the tip is a pyramid
    elif well_shape == "square":
        vol_tip = (width*width*tip_length)/3
        # if the start volume > tip volume, work out the residual height, add it to the tip height and subrtact it from the total height of the tube
        if start_vol > vol_tip:
           return -(total_length - (tip_length + (start_vol-vol_tip)/(width*width)))
        # if the starting volume is less than the tip volume, work out the total height and subrtact it from the total height of the tube
        else:
           return -(total_length - ((start_vol/((width*width*tip_length)/3))))
    if well_shape != 'round' or 'square':
        raise Exception('well_shape must be either \'round\' or \'square\'' )


# =============================================================================
# # Calculate the distance from the top of the tube to the top of the mastermix at start
# inverse_start_height_mastermix = round(start_height(start_vol = start_vol_mastermix,
#                                                     total_length=total_length_5ml,
#                                                     well_shape='round',
#                                                     tip_length = tip_length_5ml,
#                                                     width = width_5ml),1)
# # Calculate the distance from the top of the tube to the top of the oil at start
# inverse_start_height_oil = round(start_height(start_vol = start_vol_oil,
#                                               total_length=total_length_5ml,
#                                               well_shape='round',
#                                               tip_length = tip_length_5ml,
#                                               width = width_5ml),1)
# =============================================================================

# Calculate the distance from the top of the tube to the top of the mastermix at start
inverse_start_height_mastermix = round(start_height(start_vol = start_vol_mastermix,
                                                    total_length=total_length_deepwell,
                                                    well_shape='square',
                                                    tip_length = tip_length_deepwell,
                                                    width = width_deepwell),1)
# Calculate the distance from the top of the tube to the top of the oil at start
inverse_start_height_oil = round(start_height(start_vol = start_vol_oil,
                                              total_length=total_length_deepwell,
                                              well_shape='square',
                                              tip_length = tip_length_deepwell,
                                              width = width_deepwell),1)

# The following function creates a tracking value for the liquid height in a well
def height_track(transfer_vol):
    global remain_vol
    remain_vol = remain_vol-transfer_vol # should this be 8*volume_of_mineral_oil_in_ul for a trough?
    remain_height = round(start_height(start_vol = remain_vol,
                                              total_length=total_length_deepwell,
                                              well_shape='square',
                                              tip_length = tip_length_deepwell,
                                              width = width_deepwell),1)
    return remain_height

# Before starting set the remaining vol of oil to the starting volume
remain_vol = start_vol_oil

# transfer mineral oil
pipette300.set_flow_rate(aspirate=5, dispense=5)
#t_count = 0
pipette300.pick_up_tip()
for dest_col in range(12):
    pipette_height_oil = height_track(vol_transfer_oil)
    pipette300.aspirate(vol_transfer_oil, mineral_oil.top(pipette_height_oil-5))
    pipette300.move_to(mineral_oil.top(-1)) 
    pipette300.delay(seconds=2)
    pipette300.touch_tip(radius = 0.8)
    pipette300.dispense(PCR1.cols(dest_col).bottom(5)).blow_out()
    pipette300.move_to(PCR1.cols(dest_col).top(-1)) 
    pipette300.delay(seconds=2)
    pipette300.touch_tip(radius = 0.8)
pipette300.drop_tip()

pipette300.pick_up_tip()
for dest_col in range(12):
    pipette_height_oil = height_track(vol_transfer_oil)
    pipette300.aspirate(vol_transfer_oil, mineral_oil.top(pipette_height_oil-5))
    pipette300.move_to(mineral_oil.top(-1)) 
    pipette300.delay(seconds=2)
    pipette300.touch_tip(radius = 0.8)
    pipette300.dispense(PCR2.cols(dest_col).bottom(5)).blow_out()
    pipette300.move_to(PCR2.cols(dest_col).top(-1)) 
    pipette300.delay(seconds=2)
    pipette300.touch_tip(radius = 0.8)
pipette300.drop_tip()

# set a source desitination with negatives in and a fancy pattern of destination wells
dest_plates=[PCR1,PCR2]
all_dests = [well for plate in dest_plates for well in plate.rows('A')]

remain_vol = start_vol_mastermix    
#pipette_height_mastermix = height_track(vol_transfer_mastermix)

# distribute PCR master mix
pipette300.set_flow_rate(aspirate=25, dispense=50)
pipette300.pick_up_tip()
for d in all_dests:
    pipette300.transfer(vol_transfer_mastermix, mastermix, d.bottom(2), blow_out=True, new_tip='never')
pipette300.drop_tip()

# forward primer distribution
for ind, primer in enumerate(primer_mix.rows('A')):
    dests = [plate.rows('A')[ind] for plate in dest_plates]
    pipette10.distribute(1, primer, dests)


