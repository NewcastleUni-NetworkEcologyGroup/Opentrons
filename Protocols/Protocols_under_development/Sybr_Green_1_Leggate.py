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
pipette10 = instruments.P10_Multi(mount='right', tip_racks=[tips10_1, tips10_2])

# define tube parameters for 50ml tubes - no skirt
total_length_50ml: float = 113.9
length_barrel_50ml: float = 98.0
tip_length_50ml: float = round(total_length_50ml-length_barrel_50ml,1)
width_50ml: float = 27.3

n_controls=24
n_samples=24
assay_vol=200
control_start_conc=5
control_vol=10
sample_vol=5
Sybr_conc=1/2500

def liquid_volumes(n_controls, n_samples, assay_vol, control_start_conc, control_vol, sample_vol, Sybr_conc):
    control_Sybr=(assay_vol-control_vol)*n_controls*1.2
    sample_Sybr=(assay_vol-sample_vol)*n_samples*1.2
    total_Sybr=control_Sybr+sample_Sybr
    conc_Sybr_vol=round(total_Sybr*Sybr_conc,1)
    print("\nThe total volume of "+str(Sybr_conc)+"x SybrGreen1 needed for control wells is " + str(control_Sybr)+"ul")
    print("The total volume of "+str(Sybr_conc)+"x SybrGreen1 needed for sample wells is " + str(sample_Sybr)+"ul")
    print("The total volume of "+str(Sybr_conc)+"x SybrGreen1 needed is " + str(total_Sybr)+"ul")
    print("This is made by mixing "+
          str(conc_Sybr_vol)+"ul of 10,000x SybrGreen 1 with "+
          str(total_Sybr-conc_Sybr_vol)+"ul of TE")
    if total_Sybr < 49000:
        print("Use 50ml falcon tubes for Sybr Green and TE with p1000 single channel")
    elif total_Sybr > 49000:
        print("Use a robotic trough for Sybr Green and a separate TE source with p300 multichannel")
    return(total_Sybr)

# Define liquid locations and volumes
SybrGreen = tubes.wells('A1')
Tris = tubes.wells('A2')
start_vol_SybrGreen=liquid_volumes(n_controls=n_controls,
               n_samples=n_samples,
               assay_vol=assay_vol,
               control_start_conc=control_start_conc,
               control_vol=control_vol,
               sample_vol=sample_vol,
               Sybr_conc=Sybr_conc)
start_vol_Tris: float = 10000

# This function will calculate the starting height for any pointy bottomed tube relative to top of the tube.
# This requires you to state whether the well is square or round as the tip volume will either be calculated as a cone or a pyramid.
def start_height(start_vol, total_length, well_shape, tip_length, width):
    # define the volume of the tip of the tube if the tip is a cone
    if well_shape == 'round':
        vol_tip = 3.14*((width/2)**2)*(tip_length/3)
        # if the start volume > tip volume, work out the residual height, add it to the tip height and subrtact it from the total height of the tube
        if start_vol > vol_tip:
            return -(total_length - (tip_length + (start_vol-vol_tip)/(3.14*((width/2)**2))))
        # if the starting volume is less than the tip volume, work out the total height and subrtact it from the total height of the tube
        else:
            return -(total_length - (3*(start_vol/(3.14*((width/2)**2)))))
    # calulate the tip volume if the tip is a pyramid
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

pipette_height_SybrGreen = inverse_start_height_SybrGreen

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

##################################################################################################### 
### Part 1 - Mix the dilutions series of Lambda DNA
##################################################################################################### 
# Dilution series pipetting steps
# Dispense Tris-HCl into the dilution wells
Tris_vols=[200,200,200,200,200,200,200]
Tris_dest=['B1','C1','D1','E1','F1','G1','H1']

# Get a tip
pipette1000.pick_up_tip()

for idx, x in enumerate(Tris_dest):
   pipette1000.transfer(Tris_vols.__getitem__(idx),
                     Tris.top(-105),
                     trough.well(x).bottom(5),
                     new_tip='never')
# pipette1000.drop_tip()

# The following code is the 'manual' way of doing the serial dilution
# perfom dilution 1
pipette1000.transfer(400, trough.wells('A1').bottom(5), trough.wells('B1').bottom(5), new_tip='never')
pipette1000.mix(5,400,trough.wells('B1').bottom(10))
# perfom dilution 2
pipette1000.transfer(400, trough.wells('B1').bottom(5), trough.wells('C1').bottom(5), new_tip='never')
pipette1000.mix(5,400,trough.wells('C1').bottom(5))
# perfom dilution 3
pipette1000.transfer(400, trough.wells('C1').bottom(5), trough.wells('D1').bottom(5), new_tip='never')
pipette1000.mix(5,400,trough.wells('D1').bottom(5))
# perfom dilution 4
pipette1000.transfer(400, trough.wells('D1').bottom(5), trough.wells('E1').bottom(5), new_tip='never')
pipette1000.mix(5,400,trough.wells('E1').bottom(5))
# perfom dilution 5
pipette1000.transfer(400, trough.wells('E1').bottom(5), trough.wells('F1').bottom(5), new_tip='never')
pipette1000.mix(5,400,trough.wells('F1').bottom(5))
# perfom dilution 6
pipette1000.transfer(400, trough.wells('F1').bottom(5), trough.wells('G1').bottom(5), new_tip='never')
pipette1000.mix(5,400,trough.wells('G1').bottom(5))
pipette1000.drop_tip()


##################################################################################################### 
### Part 2 - Distribute the Syber green 1
##################################################################################################### 
# We're dispensing large volumes a bit rapidly so slow down the dispense rate
pipette1000.set_flow_rate(aspirate=500, dispense=200)
# Get a tip
pipette1000.pick_up_tip()
#Set a pipette depth using the formula, this is currently done manually as I don't have direct access to the total aspiration volume in a distribute
pipette_height_SybrGreen = height_track(transfer_vol=4710)

#Transfer the control SybrGreen
if (pipette_height_SybrGreen*-1) < total_length_50ml:
    print("Sufficient SybrGreen to proceed")
    # Distribute the Sybr Green to the control wells
    pipette1000.distribute(190, SybrGreen.top(pipette_height_SybrGreen-5),
                           Control_plate.wells('A1', to='H3'),
                           disposal_vol=30,
                           blow_out=SybrGreen)
if (pipette_height_SybrGreen*-1) >= total_length_50ml:
    raise Exception('\n##############################\nInsufficient SybrGreen 1 for protocol!!\n##############################')

# Set a pipette depth AGAIN using the formula, this is currently done manually as I don't have direct access to the total aspiration volume in a distribute
pipette_height_SybrGreen = height_track(transfer_vol=4860)

if (pipette_height_SybrGreen*-1) < total_length_50ml:
    print("Sufficient SybrGreen to proceed")
    # Distribute the Sybr Green to the sample wells
    pipette1000.distribute(195, SybrGreen.top(pipette_height_SybrGreen-5),
                           Control_plate.wells('A7', to='H9'),
                           disposal_vol=30,
                           blow_out=SybrGreen,)
if (pipette_height_SybrGreen*-1) >= total_length_50ml:
    raise Exception('\n##############################\nInsufficient SybrGreen 1 for protocol!!\n##############################')

#####################################################################################################
### Part 3 - Distribute the DNA
#####################################################################################################
    
# Distribute the DNA to the control wells
pipette10.transfer(10, 
                   trough['A1'].bottom(2), 
                   Control_plate.cols('1', to='3'), 
                   mix_after=(5,5))

# Distribute the DNA to the sample wells as a test - this bit needs changed once we're certain it works
pipette10.transfer([5,5,5], 
                   trough['A1'].bottom(2), 
                   Control_plate.cols('7', to='9'), 
                   mix_after=(5,5))
