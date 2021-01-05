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
#elution_tube = labware.load('opentrons_24_tuberack_generic_2ml_screwcap')

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

tris = elution_buffer.wells('A5').bottom(3)

# Specify sample well

#def run_custom_protocol(
p300_type: 'StringSelection...'='p300_Multi'
p300_mount: 'StringSelection...'='right'
sample_number: int=96
sample_volume: float=15
bead_ratio: float=0.8
elution_buffer_volume: float=30
incubation_time: float=5
settling_time: float=5
drying_time: float=4

p50_type: 'StringSelection...'='p50_Single'
p50_mount: 'StringSelection...'='left'

tipracks = labware.load('tiprack-starlab-S1120-9810', slot = 2)
p50_tips = labware.load('tiprack-starlab-S1120-2810', slot = 3)

p300 = instruments.P300_Multi(
mount=p300_mount,
tip_racks=[tipracks])

p50 = instruments.P50_Single(
mount=p50_mount,
tip_racks=[p50_tips])

#    mode = p300_type.split('_')[1] # this is 'Multi'

### Here I'm not really sure whats going on. I think that this is is recording
  # the potential locations for pipetting out from and to 

col_num = sample_number // 8 + (1 if sample_number % 8 > 0 else 0)
samples = [col for col in mag_plate.cols()[:col_num]]
output = [col for col in output_plate.cols()[:col_num]]

# Make a list for wells to collect elution from
output_wells = list(range(0,96))
#output_wells.remove(95)
#output_wells.remove(87)


# total_vol still needs to be specified
bead_volume = sample_volume*bead_ratio
total_vol = bead_volume + sample_volume + 4 # = 15ul of samples + 12 ul of beads + 5ul of excess


### Workflow:

# Engagae MagDeck and incubate
mag_deck.engage(height = 17)

p300.delay(minutes=settling_time)

# Remove supernatant from magnetic beads - this bit has been changed by james!!
p300.set_flow_rate(aspirate=25, dispense=150)
p300.pick_up_tip()
for target in ['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12']:
    p300.transfer(total_vol, mag_plate[target].bottom(0.9), waste,
                     new_tip='never')
    p300.blow_out(waste)
    p300.touch_tip(waste_plate.wells('A6'), radius =0.8, v_offset=30)
p300.drop_tip()

# Wash beads twice with 70% ethanol
air_vol = 10
p300.pick_up_tip()
for cycle in range(2):
    ticker = 0
    for target in ['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12']:
        ethanol_source = ticker//4
        p300.transfer(165, ethanol[ethanol_source], mag_plate[target].top(-1),
                         air_gap=air_vol,
                         new_tip='never')
        ticker += 1
        
    for target in ['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12']:
        p300.transfer(185, mag_plate[target].bottom(1), waste, air_gap=air_vol,
                         new_tip = 'never')
        p300.blow_out(waste)
    
p300.drop_tip()

p50.set_flow_rate(aspirate = 10)

p50.pick_up_tip()
for x in range(0,96):
    p50.transfer(20, mag_plate.wells(x).bottom(0.1), waste, new_tip = 'never')
p50.drop_tip()

p50.set_flow_rate(aspirate = 25)

# Dry at RT
p300.delay(minutes=drying_time)

# Disengage MagDeck
mag_deck.disengage()

# Mix beads with elution buffer

mix_vol = elution_buffer_volume

### Bit added by James to directly target a list of wells instead of making the list a well series in an object   
p300.pick_up_tip()
# =============================================================================
# 
# for target in ['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12']:
#     p300.transfer(
#         elution_buffer_volume, tris, mag_plate[target].top(-1), new_tip='never')
# =============================================================================
    
p300.distribute(elution_buffer_volume, tris, mag_plate.cols('1', to = str(col_num)), new_tip = 'never')

for target in ['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12']:
    p300.mix(6, mix_vol, mag_plate[target])   #less because it takes such a long time...
    p300.move_to(mag_plate[target].top(-1))
    p300.blow_out()
p300.drop_tip()

# Incubate at RT for 5 minutes
p300.delay(minutes=2)


# Engagae MagDeck for 1 minute and remain engaged for DNA elution
mag_deck.engage(height = 16)

p300.delay(minutes=settling_time)

# Transfer clean PCR product to a new well
# =============================================================================
# p300.pick_up_tip()
# for target, dest in zip(samples, output):
#     p300.transfer(
#             20, target, dest, blow_out=True, new_tip = 'never')
# p300.drop_tip()
# =============================================================================

#### Consolidating all
p50.pick_up_tip()
for x in output_wells:
    p50.transfer(15, mag_plate.wells(x).bottom(0.5), output_plate(x).top(-5), new_tip = 'never')
p50.drop_tip()


#p50.pick_up_tip()
#p50.consolidate(10, mag_plate, elutiontube(1), new_tip = 'never')
#for x in range(0,96):
#    p50.transfer(10, mag_plate.wells(x).bottom(0.3), elution_tube.wells('A1').top(-5), new_tip = 'never')
#p50.drop_tip()

#run_custom_protocol(**{'p300_type': 'p300_Multi', 'p300_mount': 'right', 'sample_number': 96, 'sample_volume': 15.0, 'bead_ratio': 0.8, 'elution_buffer_volume': 30.0, 'incubation_time': 5.0, 'settling_time': 5.0, 'drying_time': 15.0})
