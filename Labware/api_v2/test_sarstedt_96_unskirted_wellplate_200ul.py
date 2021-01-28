import json
from opentrons import protocol_api, types

CALIBRATION_CROSS_COORDS = {
    '1': {
        'x': 12.13,
        'y': 9.0,
        'z': 0.0
    },
    '3': {
        'x': 380.87,
        'y': 9.0,
        'z': 0.0
    },
    '7': {
        'x': 12.13,
        'y': 258.0,
        'z': 0.0
    }
}
CALIBRATION_CROSS_SLOTS = ['1', '3', '7']
TEST_LABWARE_SLOT = '2'

RATE = 0.25  # % of default speeds
SLOWER_RATE = 0.1

PIPETTE_MOUNT = 'right'
PIPETTE_NAME = 'p50_single'

TIPRACK_SLOT = '5'
TIPRACK_LOADNAME = 'opentrons_96_tiprack_300ul'

LABWARE_DEF_JSON = """{"ordering":[["A1","B1","C1","D1","E1","F1","G1","H1"],["A2","B2","C2","D2","E2","F2","G2","H2"],["A3","B3","C3","D3","E3","F3","G3","H3"],["A4","B4","C4","D4","E4","F4","G4","H4"],["A5","B5","C5","D5","E5","F5","G5","H5"],["A6","B6","C6","D6","E6","F6","G6","H6"],["A7","B7","C7","D7","E7","F7","G7","H7"],["A8","B8","C8","D8","E8","F8","G8","H8"],["A9","B9","C9","D9","E9","F9","G9","H9"],["A10","B10","C10","D10","E10","F10","G10","H10"],["A11","B11","C11","D11","E11","F11","G11","H11"],["A12","B12","C12","D12","E12","F12","G12","H12"]],"brand":{"brand":"Sarstedt","brandId":["72.1978.202"]},"metadata":{"displayName":"Sarstedt 96 unskirted wellplate on Starlab E2396-1642","displayCategory":"wellPlate","displayVolumeUnits":"µL","tags":[]},"dimensions":{"xDimension":127,"yDimension":87,"zDimension":35},"wells":{"A1":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":14,"y":75,"z":14},"B1":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":14,"y":66,"z":14},"C1":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":14,"y":57,"z":14},"D1":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":14,"y":48,"z":14},"E1":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":14,"y":39,"z":14},"F1":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":14,"y":30,"z":14},"G1":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":14,"y":21,"z":14},"H1":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":14,"y":12,"z":14},"A2":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":23,"y":75,"z":14},"B2":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":23,"y":66,"z":14},"C2":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":23,"y":57,"z":14},"D2":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":23,"y":48,"z":14},"E2":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":23,"y":39,"z":14},"F2":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":23,"y":30,"z":14},"G2":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":23,"y":21,"z":14},"H2":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":23,"y":12,"z":14},"A3":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":32,"y":75,"z":14},"B3":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":32,"y":66,"z":14},"C3":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":32,"y":57,"z":14},"D3":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":32,"y":48,"z":14},"E3":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":32,"y":39,"z":14},"F3":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":32,"y":30,"z":14},"G3":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":32,"y":21,"z":14},"H3":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":32,"y":12,"z":14},"A4":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":41,"y":75,"z":14},"B4":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":41,"y":66,"z":14},"C4":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":41,"y":57,"z":14},"D4":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":41,"y":48,"z":14},"E4":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":41,"y":39,"z":14},"F4":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":41,"y":30,"z":14},"G4":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":41,"y":21,"z":14},"H4":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":41,"y":12,"z":14},"A5":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":50,"y":75,"z":14},"B5":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":50,"y":66,"z":14},"C5":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":50,"y":57,"z":14},"D5":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":50,"y":48,"z":14},"E5":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":50,"y":39,"z":14},"F5":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":50,"y":30,"z":14},"G5":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":50,"y":21,"z":14},"H5":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":50,"y":12,"z":14},"A6":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":59,"y":75,"z":14},"B6":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":59,"y":66,"z":14},"C6":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":59,"y":57,"z":14},"D6":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":59,"y":48,"z":14},"E6":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":59,"y":39,"z":14},"F6":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":59,"y":30,"z":14},"G6":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":59,"y":21,"z":14},"H6":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":59,"y":12,"z":14},"A7":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":68,"y":75,"z":14},"B7":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":68,"y":66,"z":14},"C7":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":68,"y":57,"z":14},"D7":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":68,"y":48,"z":14},"E7":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":68,"y":39,"z":14},"F7":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":68,"y":30,"z":14},"G7":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":68,"y":21,"z":14},"H7":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":68,"y":12,"z":14},"A8":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":77,"y":75,"z":14},"B8":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":77,"y":66,"z":14},"C8":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":77,"y":57,"z":14},"D8":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":77,"y":48,"z":14},"E8":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":77,"y":39,"z":14},"F8":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":77,"y":30,"z":14},"G8":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":77,"y":21,"z":14},"H8":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":77,"y":12,"z":14},"A9":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":86,"y":75,"z":14},"B9":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":86,"y":66,"z":14},"C9":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":86,"y":57,"z":14},"D9":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":86,"y":48,"z":14},"E9":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":86,"y":39,"z":14},"F9":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":86,"y":30,"z":14},"G9":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":86,"y":21,"z":14},"H9":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":86,"y":12,"z":14},"A10":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":95,"y":75,"z":14},"B10":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":95,"y":66,"z":14},"C10":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":95,"y":57,"z":14},"D10":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":95,"y":48,"z":14},"E10":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":95,"y":39,"z":14},"F10":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":95,"y":30,"z":14},"G10":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":95,"y":21,"z":14},"H10":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":95,"y":12,"z":14},"A11":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":104,"y":75,"z":14},"B11":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":104,"y":66,"z":14},"C11":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":104,"y":57,"z":14},"D11":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":104,"y":48,"z":14},"E11":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":104,"y":39,"z":14},"F11":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":104,"y":30,"z":14},"G11":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":104,"y":21,"z":14},"H11":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":104,"y":12,"z":14},"A12":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":113,"y":75,"z":14},"B12":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":113,"y":66,"z":14},"C12":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":113,"y":57,"z":14},"D12":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":113,"y":48,"z":14},"E12":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":113,"y":39,"z":14},"F12":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":113,"y":30,"z":14},"G12":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":113,"y":21,"z":14},"H12":{"depth":21,"totalLiquidVolume":200,"shape":"circular","diameter":5.5,"x":113,"y":12,"z":14}},"groups":[{"metadata":{"wellBottomShape":"v"},"wells":["A1","B1","C1","D1","E1","F1","G1","H1","A2","B2","C2","D2","E2","F2","G2","H2","A3","B3","C3","D3","E3","F3","G3","H3","A4","B4","C4","D4","E4","F4","G4","H4","A5","B5","C5","D5","E5","F5","G5","H5","A6","B6","C6","D6","E6","F6","G6","H6","A7","B7","C7","D7","E7","F7","G7","H7","A8","B8","C8","D8","E8","F8","G8","H8","A9","B9","C9","D9","E9","F9","G9","H9","A10","B10","C10","D10","E10","F10","G10","H10","A11","B11","C11","D11","E11","F11","G11","H11","A12","B12","C12","D12","E12","F12","G12","H12"]}],"parameters":{"format":"irregular","quirks":[],"isTiprack":false,"isMagneticModuleCompatible":false,"loadName":"sarstedt_96_unskirted_wellplate_200ul"},"namespace":"custom_beta","version":1,"schemaVersion":2,"cornerOffsetFromSlot":{"x":0,"y":0,"z":0}}"""
LABWARE_DEF = json.loads(LABWARE_DEF_JSON)
LABWARE_LABEL = LABWARE_DEF.get('metadata', {}).get(
    'displayName', 'test labware')

metadata = {'apiLevel': '2.0'}


def uniq(l):
    res = []
    for i in l:
        if i not in res:
            res.append(i)
    return res


def run(protocol: protocol_api.ProtocolContext):
    tiprack = protocol.load_labware(TIPRACK_LOADNAME, TIPRACK_SLOT)
    pipette = protocol.load_instrument(
        PIPETTE_NAME, PIPETTE_MOUNT, tip_racks=[tiprack])

    test_labware = protocol.load_labware_from_definition(
        LABWARE_DEF,
        TEST_LABWARE_SLOT,
        LABWARE_LABEL,
    )

    num_cols = len(LABWARE_DEF.get('ordering', [[]]))
    num_rows = len(LABWARE_DEF.get('ordering', [[]])[0])
    well_locs = uniq([
        'A1',
        '{}{}'.format(chr(ord('A') + num_rows - 1), str(num_cols))])

    pipette.pick_up_tip()

    def set_speeds(rate):
        protocol.max_speeds.update({
            'X': (600 * rate),
            'Y': (400 * rate),
            'Z': (125 * rate),
            'A': (125 * rate),
        })

        speed_max = max(protocol.max_speeds.values())

        for instr in protocol.loaded_instruments.values():
            instr.default_speed = speed_max

    set_speeds(RATE)

    for slot in CALIBRATION_CROSS_SLOTS:
        coordinate = CALIBRATION_CROSS_COORDS[slot]
        location = types.Location(point=types.Point(**coordinate),
                                  labware=None)
        pipette.move_to(location)
        protocol.pause(
            f"Confirm {PIPETTE_MOUNT} pipette is at slot {slot} calibration cross")

    pipette.home()
    protocol.pause(f"Place your labware in Slot {TEST_LABWARE_SLOT}")

    for well_loc in well_locs:
        well = test_labware.well(well_loc)
        all_4_edges = [
            [well._from_center_cartesian(x=-1, y=0, z=1), 'left'],
            [well._from_center_cartesian(x=1, y=0, z=1), 'right'],
            [well._from_center_cartesian(x=0, y=-1, z=1), 'front'],
            [well._from_center_cartesian(x=0, y=1, z=1), 'back']
        ]

        set_speeds(RATE)
        pipette.move_to(well.top())
        protocol.pause("Moved to the top of the well")

        for edge_pos, edge_name in all_4_edges:
            set_speeds(SLOWER_RATE)
            edge_location = types.Location(point=edge_pos, labware=None)
            pipette.move_to(edge_location)
            protocol.pause(f'Moved to {edge_name} edge')

    # go to bottom last. (If there is more than one well, use the last well first
    # because the pipette is already at the last well at this point)
    for well_loc in reversed(well_locs):
        well = test_labware.well(well_loc)
        set_speeds(RATE)
        pipette.move_to(well.bottom())
        protocol.pause("Moved to the bottom of the well")

        pipette.blow_out(well)

    set_speeds(1.0)
    pipette.return_tip()
