from opentrons.data_storage import database

metadata = {
    'protocolName': 'delete_labware_Starlab',
    'author': 'James Kitson <James.Kitson@ncl.ac.uk>',
    'description': 'A list of the labware delete commands for standard Starlab consumables'
    }

database.delete_container('starlab-E2896-0220')
database.delete_container('starlab-E2896-0600')
