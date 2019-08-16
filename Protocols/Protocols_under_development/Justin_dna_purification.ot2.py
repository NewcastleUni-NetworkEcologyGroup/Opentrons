from opentrons import labware, instruments, modules

metadata = {
    'protocolName': 'SPRI Bead Normalisation and size selection',
    'author': 'Kitson, James J., Byrne, Justin G. D. '
    }

mag_deck = modules.load('magdeck', '10')
mag_plate = labware.load('starlab-E1403-5200', '10', share=True)
output_plate = labware.load('starlab-E1403-0100', '6')
ethanol_plate = labware.load('starlab-E2896-0220', '4')
elution_buffer = labware.load('starlab-E2896-0220', '1') 

# add an empty p1000 box as a waste bucket

waste_plate = labware.load('trash-starlab-S1182-1830', '8')

# define a pipetting location for the waste_plate
waste = waste_plate.wells('A6').top(-30)

# Define reagents locations in a loop Or maybe can be done more simply

# Ethanol Location
# Here we need a loop specifying where to take ethanol from
# something like:   e_col = ['A1', 'A2', 'A3']
#                   if e_ticker == 8,
#                       e_index = e_index + 1
#                       ethanol = ethanol_plate.wells(e_col[e_index])


ethanol = ethanol_plate.wells('A1', 'A2', 'A3') 

# Elution buffer needs to be done in the same way

tris = elution_buffer.wells('A1')

# Specify sample well

#def run_custom_protocol(
pipette_type: 'StringSelection...'='p300_Multi'
pipette_mount: 'StringSelection...'='right'
sample_number: int=96
sample_volume: float=15
bead_ratio: float=0.8
elution_buffer_volume: float=30
incubation_time: float=5
settling_time: float=5
drying_time: float=15

## We'll need to work out how many tips are needed !!!!!!

total_tips = 40
tiprack_num = total_tips//96 + (1 if total_tips % 96 > 0 else 0)
slots = ['2', '3', '5', '7', '8'][:tiprack_num]

tipracks = [labware.load('tiprack-starlab-S1120-9810', slot) for slot in slots]
pipette = instruments.P300_Multi(
mount=pipette_mount,
tip_racks=tipracks)

#    mode = pipette_type.split('_')[1] # this is 'Multi'

### Here I'm not really sure whats going on. I think that this is is recording
  # the potential locations for pipetting out from and to 

col_num = sample_number // 8 + (1 if sample_number % 8 > 0 else 0)
samples = [col for col in mag_plate.cols()[:col_num]]
output = [col for col in output_plate.cols()[:col_num]]

# total_vol still needs to be specified
bead_volume = sample_volume*bead_ratio
total_vol = bead_volume + sample_volume + 5 # = 15ul of samples + 12 ul of beads + 5ul of excess

# =============================================================================
#       This Section will be done by hand prior to running the protocol to save 1600 tips
#
#     # Define bead and mix volume ##Justin: Consider moving to seperate script
#     bead_volume = sample_volume*bead_ratio
#     if bead_volume/2 > pipette.max_volume:
#         mix_vol = pipette.max_volume
#     else:
#         mix_vol = bead_volume/2
#     total_vol = bead_volume + sample_volume + 5
# 
#     # Mix beads and PCR samples ##Justin: Consider removing an doing by hand
#     for target in samples:
#         pipette.pick_up_tip()
#         pipette.mix(5, mix_vol, beads)
#         pipette.transfer(bead_volume, beads, target, new_tip='never')
#         pipette.mix(10, mix_vol, target)
#         pipette.blow_out()
#         pipette.drop_tip()
# 
#     # Incubate beads and PCR product at RT for 5 minutes ##Justin: Consider doing by hand
#     pipette.delay(minutes=incubation_time)
# =============================================================================

### Workflow:

# Engagae MagDeck and incubate
mag_deck.engage(height = 18)
########################################    pipette.delay(minutes=settling_time)

# Remove supernatant from magnetic beads - this bit has been changed by james!!
pipette.set_flow_rate(aspirate=25, dispense=150)
pipette.pick_up_tip()
for target in samples:
    pipette.transfer(total_vol, target, waste, new_tip='never')
    pipette.blow_out(waste)
pipette.drop_tip()
# Wash beads twice with 70% ethanol
air_vol = 15
pipette.pick_up_tip()
for cycle in range(2):
    ticker = 0
    for target in ['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12']:
        ethanol_source = ticker//4
        pipette.transfer(185, ethanol[ethanol_source], mag_plate[target].top(-1),
                         air_gap=air_vol,
                         new_tip='never')
        ticker += 1
        
    #########################################################################pipette.delay(minutes=1)

    for target in ['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12']:
        pipette.transfer(195, mag_plate[target], waste, air_gap=air_vol,
                         new_tip = 'never')
    
pipette.drop_tip()

# Dry at RT
######################## #####################################################   pipette.delay(minutes=drying_time)

# Disengage MagDeck
mag_deck.disengage()

### Do the bead and elution buffer need mixing? Probably

# Mix beads with elution buffer

mix_vol = elution_buffer_volume

# =============================================================================
#     pipette.pick_up_tip()
#     for target in samples:
#         pipette.transfer(
#             elution_buffer_volume, tris, target.top(), new_tip='never')
#         pipette.mix(15, mix_vol, target)
#         pipette.move_to(target.top(-1))
#         pipette.blow_out()
#     pipette.drop_tip()
# =============================================================================
# =============================================================================
#     pipette.pick_up_tip()
# 
#     
#     for target in samples:
#         pipette.transfer(
#                 elution_buffer_volume, tris, samples.top(-1), new_tip='never')
#         
#     for target in samples:
#         pipette.mix(6, mix_vol, samples)   #less because it takes such a long time...
#         pipette.move_to(target.top(-1))
#         pipette.blow_out()
#     pipette.drop_tip()
#     
#     
#         pipette.pick_up_tip()
# =============================================================================

### Bit added by James to directly target a list of wells instead of making the list a well series in an object   
pipette.pick_up_tip()
# =============================================================================
# 
# for target in ['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12']:
#     pipette.transfer(
#         elution_buffer_volume, tris, mag_plate[target].top(-1), new_tip='never')
# =============================================================================
    
pipette.distribute(elution_buffer_volume, tris, mag_plate.cols('1', to = str(col_num)), new_tip = 'never')

for target in ['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12']:
    pipette.mix(6, mix_vol, mag_plate[target])   #less because it takes such a long time...
    pipette.move_to(mag_plate[target].top(-1))
    pipette.blow_out()
pipette.drop_tip()
# Incubate at RT for 5 minutes
#############################################################################    pipette.delay(minutes=5)

# Engagae MagDeck for 1 minute and remain engaged for DNA elution
mag_deck.engage(height = 16)
###############################################################################    pipette.delay(minutes=settling_time)

# Transfer clean PCR product to a new well
pipette.pick_up_tip()
for target, dest in zip(samples, output):
    pipette.transfer(
            elution_buffer_volume, target, dest, blow_out=True, new_tip = 'never')
pipette.drop_tip()

#run_custom_protocol(**{'pipette_type': 'p300_Multi', 'pipette_mount': 'right', 'sample_number': 96, 'sample_volume': 15.0, 'bead_ratio': 0.8, 'elution_buffer_volume': 30.0, 'incubation_time': 5.0, 'settling_time': 5.0, 'drying_time': 15.0})
