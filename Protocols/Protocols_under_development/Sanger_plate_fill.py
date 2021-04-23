from opentrons import protocol_api

metadata = {'apiLevel': '2.0',
            'protocolName': 'Sanger_plate_fill',
            'author': 'James Kitson',
            'description': 'A basic protcol to get used to API v2 that just fills a PCR plate with premade mastermix'}

def run(protocol: protocol_api.ProtocolContext):
    