from opentrons import labware, instruments

metadata = {
    'protocolName': 'SybrGreen 1 setup',
    'author': 'James Kitson <James.Kitson@ncl.ac.uk>',
    'description': 'A protocol to dilute DNA controls and distribute Sybr Green 1'
    }

# Set labware to use
tips1000 = labware.load('opentrons-tiprack-1000ul', '1', 'for SybrGreen and DNA dilutions')
tips10_1 = labware.load('opentrons-tiprack-10ul', '2', 'for primers')
tips10_2 = labware.load('opentrons-tiprack-10ul', '3', 'for template DNA')
Control_plate = labware.load('Thermo-237108','4', 'lambda DNA controls')
test_DNA = labware.load('Thermo-237108','5', 'template DNA plate')

tubes = labware.load('opentrons-tuberack-50ml', '6', 'Sybr Green 1 in A1')
trough = labware.load('starlab-E2896-0220', '7', 'Control dilutions')

pipette1000 = instruments.P1000_Single(mount='left', tip_racks=[tips1000])
pipette10 = instruments.P10_Multi(mount='right', tip_racks=[tips10_1, tips10_2]) # would be much better with a p50

# =============================================================================
# ### Define tube dimensions for liquid level tracking
# #define deepwell plate parameters for 2.2ml deepwell plates
# total_length_deepwell: float = 37
# length_barrel_deepwell: float = 34
# tip_length_deepwell: float = round(total_length_deepwell-length_barrel_deepwell,1)
# width_deepwell: float = 8
# =============================================================================

#define tube parameters for 50ml tubes - no skirt
total_length_50ml: float = 113.9
length_barrel_50ml: float = 98.0
tip_length_50ml: float = round(total_length_50ml-length_barrel_50ml,1)
width_50ml: float = 27.3

# Define liquid locations and volumes
SybrGreen = tubes.wells('A1')
Tris = tubes.wells('A2')
start_vol_SybrGreen: float = 23040
start_vol_Tris: float = 10000

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
        
# Calculate the distance from the top of the tube to the top of the SybrGreen at start
inverse_start_height_SybrGreen = round(start_height(start_vol = start_vol_SybrGreen,
                                                    total_length=total_length_50ml,
                                                    well_shape='round',
                                                    tip_length = tip_length_50ml,
                                                    width = width_50ml),1)


# The following function creates a tracking value for the liquid height in a well
def height_track(transfer_vol):
    global remain_vol
    remain_vol = remain_vol-transfer_vol # should this be 8*volume_of_mineral_SybrGreen_in_ul for a trough?
    remain_height = round(start_height(start_vol = remain_vol,
                                              total_length=total_length_50ml,
                                              well_shape='round',
                                              tip_length = tip_length_50ml,
                                              width = width_50ml),1)
    return remain_height

# Before starting set the remaining vol of SybrGreen to the starting volume
remain_vol = start_vol_SybrGreen

### Part 1 - Mix the dilutions series of Lambda DNA
# Dilution series pipetting steps
# Dispense Tris-HCl into the dilution wells
Tris_vols=[300,375,500,750,750,750,1500]
Tris_dest=['B1','C1','D1','E1','F1','G1','H1']

# Get a tip
pipette1000.pick_up_tip()

for idx, x in enumerate(Tris_dest):
   pipette1000.transfer(Tris_vols.__getitem__(idx),
                     Tris.top(-105),
                     trough.well(x).bottom(5),
                     new_tip='never')
pipette1000.drop_tip()

# The following code is the 'manual' way of doing the serial dilution
# Get a tip
pipette1000.pick_up_tip()
# perfom dilution 1
pipette1000.transfer(1200, trough.wells('A1').bottom(5), trough.wells('B1').bottom(5), new_tip='never')
pipette1000.mix(5,400,trough.wells('B1').bottom(10))
# perfom dilution 2
pipette1000.transfer(1125, trough.wells('B1').bottom(5), trough.wells('C1').bottom(5), new_tip='never')
pipette1000.mix(5,400,trough.wells('C1').bottom(5))
# perfom dilution 3
pipette1000.transfer(1000, trough.wells('C1').bottom(5), trough.wells('D1').bottom(5), new_tip='never')
pipette1000.mix(5,400,trough.wells('D1').bottom(5))
# perfom dilution 4
pipette1000.transfer(750, trough.wells('D1').bottom(5), trough.wells('E1').bottom(5), new_tip='never')
pipette1000.mix(5,400,trough.wells('E1').bottom(5))
# perfom dilution 5
pipette1000.transfer(750, trough.wells('E1').bottom(5), trough.wells('F1').bottom(5), new_tip='never')
pipette1000.mix(5,400,trough.wells('F1').bottom(5))
# perfom dilution 6
pipette1000.transfer(750, trough.wells('F1').bottom(5), trough.wells('G1').bottom(5), new_tip='never')
pipette1000.mix(5,400,trough.wells('G1').bottom(5))
pipette1000.drop_tip()

# =============================================================================
# # The following code is uses a function to do the calculation - except it doesn't work, just use index positions within lists and a ticker
# start_conc = [10,8,6,4,2,1]
# final_conc = [8,6,4,2,1,0.5]
# target_wells = trough.wells('A1', to = 'G1')
# final_vol: float = 1500
# 
# def dilution_vol(target_vol, target_conc, initial_conc):
#     transfer_vol=(target_vol*target_conc)/initial_conc
#     return transfer_vol
# 
# # transfer primers
# for idx, x in enumerate(target_wells):
#   pipette1000.pick_up_tip()
#   pipette1000.transfer(dilution_vol(target_vol = final_vol,
#                                        target_conc = final_conc.__getitem__(idx),
#                                        initial_conc = start_conc.__getitem__(idx)),
#                         trough.well(target_wells.__getitem__(x)),
#                         trough.well(target_wells.__getitem__(x+1)),
#                         new_tip='never')
#                         
#   
#   pipette10.drop_tip()
# =============================================================================

### Part 2 - Distribute the Syber green 1
# Get a tip
pipette1000.pick_up_tip()
#Set a pipette depth using the formula, this is currently done manually as I don't have direct access to the total aspiration volume in a distribute
pipette_height_SybrGreen = height_track(transfer_vol=9960)
# Distribute the Sybr Green to the control wells
pipette1000.distribute(200, SybrGreen.top(pipette_height_SybrGreen-5),
                       Control_plate.wells('A1', to='H6'),
                       disposal_vol=30,
                       blow_out=SybrGreen.top(-30))
pipette_height_SybrGreen = height_track(transfer_vol=9960)
# Distribute the Sybr Green to the sample wells
pipette1000.distribute(200, SybrGreen.top(pipette_height_SybrGreen-5),
                       Control_plate.wells('A7', to='H12'),
                       disposal_vol=30,
                       blow_out=SybrGreen.top(-30))

### Part 3 - Distribute the DNA
# Distribute the DNA to the control wells
pipette10.transfer(10, trough['A1'].bottom(5), Control_plate.cols('1', to='6'))

# Distribute the DNA to the sample wells as a test - this bit need changed once we're certain it works
pipette10.transfer([5,5,5,10,10,10], trough['A1'].bottom(5), Control_plate.cols('7', to='12'))
