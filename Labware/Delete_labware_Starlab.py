from opentrons.data_storage import database

metadata = {
    'protocolName': 'delete_labware_Starlab',
    'author': 'James Kitson <James.Kitson@ncl.ac.uk>',
    'description': 'A list of the labware delete commands for standard Starlab consumables'
    }
#Deepwell plates
#database.delete_container('starlab-E2896-0220')
#database.delete_container('starlab-E2896-0600')

#RPT filter tips
database.delete_container('tiprack-starlab-S1181-3810')
#database.delete_container('tiprack-starlab-S1180-3810')
#database.delete_container('tiprack-starlab-S1180-1840')
#database.delete_container('tiprack-starlab-S1180-8810')
#database.delete_container('tiprack-starlab-S1180-9810')
#database.delete_container('tiprack-starlab-S1182-1830')

#Regular filter tips
#database.delete_container('tiprack-starlab-S1121-3810')
#database.delete_container('tiprack-starlab-S1120-3810')
#database.delete_container('tiprack-starlab-S1120-2810')
#database.delete_container('tiprack-starlab-S1123-1840')
#database.delete_container('tiprack-starlab-S1120-8810')
#database.delete_container('tiprack-starlab-S1120-9810')
#database.delete_container('tiprack-starlab-S1122-1830')