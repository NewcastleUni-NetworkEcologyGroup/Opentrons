def get_values(*names):
    import json
    _all_values = json.loads("""{"transfer_csv":"Source Labware,Source Slot,Source Well,Source Aspiration Height Above Bottom (in mm),Dest Labware,Dest Slot,Dest Well,Volume (in ul)\\nnest_12_reservoir_15ml,5,A1,16.6,sarstedt_96_skirted_wellplate_200ul,7,A1,78\\nnest_12_reservoir_15ml,5,A1,16.4,sarstedt_96_skirted_wellplate_200ul,7,A2,91\\nnest_12_reservoir_15ml,5,A1,16.3,sarstedt_96_skirted_wellplate_200ul,7,A3,91\\nnest_12_reservoir_15ml,5,A1,16.1,sarstedt_96_skirted_wellplate_200ul,7,A4,91\\nnest_12_reservoir_15ml,5,A1,16,sarstedt_96_skirted_wellplate_200ul,7,A5,52\\nnest_12_reservoir_15ml,5,A1,15.8,sarstedt_96_skirted_wellplate_200ul,7,A6,91\\nnest_12_reservoir_15ml,5,A1,15.7,sarstedt_96_skirted_wellplate_200ul,7,A7,78\\nnest_12_reservoir_15ml,5,A1,15.5,sarstedt_96_skirted_wellplate_200ul,7,A8,91\\nnest_12_reservoir_15ml,5,A1,15.4,sarstedt_96_skirted_wellplate_200ul,7,A9,78\\nnest_12_reservoir_15ml,5,A1,15.1,sarstedt_96_skirted_wellplate_200ul,7,A11,78\\nnest_12_reservoir_15ml,5,A1,14.9,sarstedt_96_skirted_wellplate_200ul,7,A12,78\\nnest_12_reservoir_15ml,5,A1,14.8,sarstedt_96_skirted_wellplate_200ul,7,B1,78\\nnest_12_reservoir_15ml,5,A1,14.6,sarstedt_96_skirted_wellplate_200ul,7,B2,91\\nnest_12_reservoir_15ml,5,A1,14.4,sarstedt_96_skirted_wellplate_200ul,7,B3,91\\nnest_12_reservoir_15ml,5,A1,14.3,sarstedt_96_skirted_wellplate_200ul,7,B4,78\\nnest_12_reservoir_15ml,5,A1,14.1,sarstedt_96_skirted_wellplate_200ul,7,B5,78\\nnest_12_reservoir_15ml,5,A1,14,sarstedt_96_skirted_wellplate_200ul,7,B6,78\\nnest_12_reservoir_15ml,5,A1,13.8,sarstedt_96_skirted_wellplate_200ul,7,B7,78\\nnest_12_reservoir_15ml,5,A1,13.7,sarstedt_96_skirted_wellplate_200ul,7,B8,26\\nnest_12_reservoir_15ml,5,A1,13.5,sarstedt_96_skirted_wellplate_200ul,7,B9,91\\nnest_12_reservoir_15ml,5,A1,13.4,sarstedt_96_skirted_wellplate_200ul,7,B10,91\\nnest_12_reservoir_15ml,5,A1,13.2,sarstedt_96_skirted_wellplate_200ul,7,B11,104\\nnest_12_reservoir_15ml,5,A1,13.1,sarstedt_96_skirted_wellplate_200ul,7,B12,91\\nnest_12_reservoir_15ml,5,A1,12.9,sarstedt_96_skirted_wellplate_200ul,7,C1,104\\nnest_12_reservoir_15ml,5,A1,12.8,sarstedt_96_skirted_wellplate_200ul,7,C2,91\\nnest_12_reservoir_15ml,5,A1,12.6,sarstedt_96_skirted_wellplate_200ul,7,C3,65\\nnest_12_reservoir_15ml,5,A1,12.5,sarstedt_96_skirted_wellplate_200ul,7,C4,65\\nnest_12_reservoir_15ml,5,A1,12.3,sarstedt_96_skirted_wellplate_200ul,7,C5,26\\nnest_12_reservoir_15ml,5,A1,12.1,sarstedt_96_skirted_wellplate_200ul,7,C6,78\\nnest_12_reservoir_15ml,5,A1,12,sarstedt_96_skirted_wellplate_200ul,7,C7,91\\nnest_12_reservoir_15ml,5,A1,11.8,sarstedt_96_skirted_wellplate_200ul,7,C8,91\\nnest_12_reservoir_15ml,5,A1,11.7,sarstedt_96_skirted_wellplate_200ul,7,C9,78\\nnest_12_reservoir_15ml,5,A1,11.5,sarstedt_96_skirted_wellplate_200ul,7,C10,91\\nnest_12_reservoir_15ml,5,A1,11.4,sarstedt_96_skirted_wellplate_200ul,7,C11,91\\nnest_12_reservoir_15ml,5,A1,11.2,sarstedt_96_skirted_wellplate_200ul,7,C12,91\\nnest_12_reservoir_15ml,5,A1,11.1,sarstedt_96_skirted_wellplate_200ul,7,D1,26\\nnest_12_reservoir_15ml,5,A1,10.9,sarstedt_96_skirted_wellplate_200ul,7,D2,78\\nnest_12_reservoir_15ml,5,A1,10.8,sarstedt_96_skirted_wellplate_200ul,7,D3,78\\nnest_12_reservoir_15ml,5,A1,10.3,sarstedt_96_skirted_wellplate_200ul,7,D6,13\\nnest_12_reservoir_15ml,5,A1,10.1,sarstedt_96_skirted_wellplate_200ul,7,D7,26\\nnest_12_reservoir_15ml,5,A1,9.8,sarstedt_96_skirted_wellplate_200ul,7,D9,52\\nnest_12_reservoir_15ml,5,A1,9.4,sarstedt_96_skirted_wellplate_200ul,7,D12,78\\nnest_12_reservoir_15ml,5,A1,9.2,sarstedt_96_skirted_wellplate_200ul,7,E1,65\\nnest_12_reservoir_15ml,5,A1,9.1,sarstedt_96_skirted_wellplate_200ul,7,E2,91\\nnest_12_reservoir_15ml,5,A1,8.9,sarstedt_96_skirted_wellplate_200ul,7,E3,65\\nnest_12_reservoir_15ml,5,A1,8.8,sarstedt_96_skirted_wellplate_200ul,7,E4,26\\nnest_12_reservoir_15ml,5,A1,8.5,sarstedt_96_skirted_wellplate_200ul,7,E6,39\\nnest_12_reservoir_15ml,5,A1,8.3,sarstedt_96_skirted_wellplate_200ul,7,E7,65\\nnest_12_reservoir_15ml,5,A1,8.1,sarstedt_96_skirted_wellplate_200ul,7,E8,13\\nnest_12_reservoir_15ml,5,A1,8,sarstedt_96_skirted_wellplate_200ul,7,E9,78\\nnest_12_reservoir_15ml,5,A1,7.8,sarstedt_96_skirted_wellplate_200ul,7,E10,65\\nnest_12_reservoir_15ml,5,A1,7.7,sarstedt_96_skirted_wellplate_200ul,7,E11,78\\nnest_12_reservoir_15ml,5,A1,7.5,sarstedt_96_skirted_wellplate_200ul,7,E12,91\\nnest_12_reservoir_15ml,5,A1,7.2,sarstedt_96_skirted_wellplate_200ul,7,F2,91\\nnest_12_reservoir_15ml,5,A1,7.1,sarstedt_96_skirted_wellplate_200ul,7,F3,78\\nnest_12_reservoir_15ml,5,A1,6.9,sarstedt_96_skirted_wellplate_200ul,7,F4,39\\nnest_12_reservoir_15ml,5,A1,6.8,sarstedt_96_skirted_wellplate_200ul,7,F5,13\\nnest_12_reservoir_15ml,5,A1,6.1,sarstedt_96_skirted_wellplate_200ul,7,F9,13\\nnest_12_reservoir_15ml,5,A1,6,sarstedt_96_skirted_wellplate_200ul,7,F10,13\\nnest_12_reservoir_15ml,5,A1,5.7,sarstedt_96_skirted_wellplate_200ul,7,F12,91\\nnest_12_reservoir_15ml,5,A1,5.5,sarstedt_96_skirted_wellplate_200ul,7,G1,78\\nnest_12_reservoir_15ml,5,A1,5.4,sarstedt_96_skirted_wellplate_200ul,7,G2,78\\nnest_12_reservoir_15ml,5,A1,5.2,sarstedt_96_skirted_wellplate_200ul,7,G3,78\\nnest_12_reservoir_15ml,5,A1,5.1,sarstedt_96_skirted_wellplate_200ul,7,G4,65\\nnest_12_reservoir_15ml,5,A1,4.9,sarstedt_96_skirted_wellplate_200ul,7,G5,65\\nnest_12_reservoir_15ml,5,A1,4.8,sarstedt_96_skirted_wellplate_200ul,7,G6,65\\nnest_12_reservoir_15ml,5,A1,4.6,sarstedt_96_skirted_wellplate_200ul,7,G7,52\\nnest_12_reservoir_15ml,5,A1,4.5,sarstedt_96_skirted_wellplate_200ul,7,G8,78\\nnest_12_reservoir_15ml,5,A1,4.3,sarstedt_96_skirted_wellplate_200ul,7,G9,39\\nnest_12_reservoir_15ml,5,A1,4.2,sarstedt_96_skirted_wellplate_200ul,7,G10,78\\nnest_12_reservoir_15ml,5,A1,4,sarstedt_96_skirted_wellplate_200ul,7,G11,39\\nnest_12_reservoir_15ml,5,A1,3.8,sarstedt_96_skirted_wellplate_200ul,7,G12,91\\nnest_12_reservoir_15ml,5,A1,3.7,sarstedt_96_skirted_wellplate_200ul,7,H1,78\\nnest_12_reservoir_15ml,5,A1,3.5,sarstedt_96_skirted_wellplate_200ul,7,H2,78\\nnest_12_reservoir_15ml,5,A1,3.4,sarstedt_96_skirted_wellplate_200ul,7,H3,78\\nnest_12_reservoir_15ml,5,A1,3.2,sarstedt_96_skirted_wellplate_200ul,7,H4,65\\nnest_12_reservoir_15ml,5,A1,3.1,sarstedt_96_skirted_wellplate_200ul,7,H5,78\\nnest_12_reservoir_15ml,5,A1,2.9,sarstedt_96_skirted_wellplate_200ul,7,H6,52\\nnest_12_reservoir_15ml,5,A1,2.8,sarstedt_96_skirted_wellplate_200ul,7,H7,65\\nnest_12_reservoir_15ml,5,A1,2.6,sarstedt_96_skirted_wellplate_200ul,7,H8,52\\nnest_12_reservoir_15ml,5,A1,2.5,sarstedt_96_skirted_wellplate_200ul,7,H9,78\\nnest_12_reservoir_15ml,5,A1,2.3,sarstedt_96_skirted_wellplate_200ul,7,H10,78\\nnest_12_reservoir_15ml,5,A1,2.2,sarstedt_96_skirted_wellplate_200ul,7,H11,26\\nnest_12_reservoir_15ml,5,A1,2,sarstedt_96_skirted_wellplate_200ul,7,H12,91\\nnest_12_reservoir_15ml,5,A2,16.4,sarstedt_96_skirted_wellplate_200ul,8,A2,91\\nnest_12_reservoir_15ml,5,A2,16.3,sarstedt_96_skirted_wellplate_200ul,8,A3,91\\nnest_12_reservoir_15ml,5,A2,16.1,sarstedt_96_skirted_wellplate_200ul,8,A4,78\\nnest_12_reservoir_15ml,5,A2,16,sarstedt_96_skirted_wellplate_200ul,8,A5,78\\nnest_12_reservoir_15ml,5,A2,15.8,sarstedt_96_skirted_wellplate_200ul,8,A6,65\\nnest_12_reservoir_15ml,5,A2,15.7,sarstedt_96_skirted_wellplate_200ul,8,A7,91\\nnest_12_reservoir_15ml,5,A2,15.5,sarstedt_96_skirted_wellplate_200ul,8,A8,39\\nnest_12_reservoir_15ml,5,A2,15.4,sarstedt_96_skirted_wellplate_200ul,8,A9,78\\nnest_12_reservoir_15ml,5,A2,15.2,sarstedt_96_skirted_wellplate_200ul,8,A10,91\\nnest_12_reservoir_15ml,5,A2,15.1,sarstedt_96_skirted_wellplate_200ul,8,A11,65\\nnest_12_reservoir_15ml,5,A2,14.9,sarstedt_96_skirted_wellplate_200ul,8,A12,91\\nnest_12_reservoir_15ml,5,A2,14.8,sarstedt_96_skirted_wellplate_200ul,8,B1,104\\nnest_12_reservoir_15ml,5,A2,14.6,sarstedt_96_skirted_wellplate_200ul,8,B2,91\\nnest_12_reservoir_15ml,5,A2,14.4,sarstedt_96_skirted_wellplate_200ul,8,B3,65\\nnest_12_reservoir_15ml,5,A2,14.3,sarstedt_96_skirted_wellplate_200ul,8,B4,91\\nnest_12_reservoir_15ml,5,A2,14,sarstedt_96_skirted_wellplate_200ul,8,B6,65\\nnest_12_reservoir_15ml,5,A2,13.8,sarstedt_96_skirted_wellplate_200ul,8,B7,91\\nnest_12_reservoir_15ml,5,A2,13.7,sarstedt_96_skirted_wellplate_200ul,8,B8,78\\nnest_12_reservoir_15ml,5,A2,13.5,sarstedt_96_skirted_wellplate_200ul,8,B9,13\\nnest_12_reservoir_15ml,5,A2,13.4,sarstedt_96_skirted_wellplate_200ul,8,B10,104\\nnest_12_reservoir_15ml,5,A2,13.2,sarstedt_96_skirted_wellplate_200ul,8,B11,52\\nnest_12_reservoir_15ml,5,A2,12.9,sarstedt_96_skirted_wellplate_200ul,8,C1,91\\nnest_12_reservoir_15ml,5,A2,12.8,sarstedt_96_skirted_wellplate_200ul,8,C2,91\\nnest_12_reservoir_15ml,5,A2,12.6,sarstedt_96_skirted_wellplate_200ul,8,C3,78\\nnest_12_reservoir_15ml,5,A2,12.3,sarstedt_96_skirted_wellplate_200ul,8,C5,78\\nnest_12_reservoir_15ml,5,A2,12.1,sarstedt_96_skirted_wellplate_200ul,8,C6,78\\nnest_12_reservoir_15ml,5,A2,12,sarstedt_96_skirted_wellplate_200ul,8,C7,91\\nnest_12_reservoir_15ml,5,A2,11.8,sarstedt_96_skirted_wellplate_200ul,8,C8,104\\nnest_12_reservoir_15ml,5,A2,11.7,sarstedt_96_skirted_wellplate_200ul,8,C9,52\\nnest_12_reservoir_15ml,5,A2,11.5,sarstedt_96_skirted_wellplate_200ul,8,C10,91\\nnest_12_reservoir_15ml,5,A2,11.4,sarstedt_96_skirted_wellplate_200ul,8,C11,78\\nnest_12_reservoir_15ml,5,A2,11.2,sarstedt_96_skirted_wellplate_200ul,8,C12,78\\nnest_12_reservoir_15ml,5,A2,11.1,sarstedt_96_skirted_wellplate_200ul,8,D1,26\\nnest_12_reservoir_15ml,5,A2,10.9,sarstedt_96_skirted_wellplate_200ul,8,D2,78\\nnest_12_reservoir_15ml,5,A2,10.6,sarstedt_96_skirted_wellplate_200ul,8,D4,39\\nnest_12_reservoir_15ml,5,A2,10.1,sarstedt_96_skirted_wellplate_200ul,8,D7,39\\nnest_12_reservoir_15ml,5,A2,10,sarstedt_96_skirted_wellplate_200ul,8,D8,39\\nnest_12_reservoir_15ml,5,A2,9.7,sarstedt_96_skirted_wellplate_200ul,8,D10,13\\nnest_12_reservoir_15ml,5,A2,9.5,sarstedt_96_skirted_wellplate_200ul,8,D11,52\\nnest_12_reservoir_15ml,5,A2,9.2,sarstedt_96_skirted_wellplate_200ul,8,E1,78\\nnest_12_reservoir_15ml,5,A2,9.1,sarstedt_96_skirted_wellplate_200ul,8,E2,78\\nnest_12_reservoir_15ml,5,A2,8.9,sarstedt_96_skirted_wellplate_200ul,8,E3,52\\nnest_12_reservoir_15ml,5,A2,8.8,sarstedt_96_skirted_wellplate_200ul,8,E4,26\\nnest_12_reservoir_15ml,5,A2,8.6,sarstedt_96_skirted_wellplate_200ul,8,E5,39\\nnest_12_reservoir_15ml,5,A2,8.5,sarstedt_96_skirted_wellplate_200ul,8,E6,52\\nnest_12_reservoir_15ml,5,A2,8.3,sarstedt_96_skirted_wellplate_200ul,8,E7,13\\nnest_12_reservoir_15ml,5,A2,8.1,sarstedt_96_skirted_wellplate_200ul,8,E8,52\\nnest_12_reservoir_15ml,5,A2,8,sarstedt_96_skirted_wellplate_200ul,8,E9,26\\nnest_12_reservoir_15ml,5,A2,7.8,sarstedt_96_skirted_wellplate_200ul,8,E10,78\\nnest_12_reservoir_15ml,5,A2,7.7,sarstedt_96_skirted_wellplate_200ul,8,E11,78\\nnest_12_reservoir_15ml,5,A2,7.5,sarstedt_96_skirted_wellplate_200ul,8,E12,91\\nnest_12_reservoir_15ml,5,A2,7.4,sarstedt_96_skirted_wellplate_200ul,8,F1,39\\nnest_12_reservoir_15ml,5,A2,7.2,sarstedt_96_skirted_wellplate_200ul,8,F2,78\\nnest_12_reservoir_15ml,5,A2,7.1,sarstedt_96_skirted_wellplate_200ul,8,F3,26\\nnest_12_reservoir_15ml,5,A2,6.9,sarstedt_96_skirted_wellplate_200ul,8,F4,39\\nnest_12_reservoir_15ml,5,A2,6.5,sarstedt_96_skirted_wellplate_200ul,8,F7,13\\nnest_12_reservoir_15ml,5,A2,6,sarstedt_96_skirted_wellplate_200ul,8,F10,91\\nnest_12_reservoir_15ml,5,A2,5.8,sarstedt_96_skirted_wellplate_200ul,8,F11,78\\nnest_12_reservoir_15ml,5,A2,5.5,sarstedt_96_skirted_wellplate_200ul,8,G1,91\\nnest_12_reservoir_15ml,5,A2,5.4,sarstedt_96_skirted_wellplate_200ul,8,G2,91\\nnest_12_reservoir_15ml,5,A2,5.2,sarstedt_96_skirted_wellplate_200ul,8,G3,78\\nnest_12_reservoir_15ml,5,A2,5.1,sarstedt_96_skirted_wellplate_200ul,8,G4,65\\nnest_12_reservoir_15ml,5,A2,4.9,sarstedt_96_skirted_wellplate_200ul,8,G5,26\\nnest_12_reservoir_15ml,5,A2,4.8,sarstedt_96_skirted_wellplate_200ul,8,G6,65\\nnest_12_reservoir_15ml,5,A2,4.6,sarstedt_96_skirted_wellplate_200ul,8,G7,65\\nnest_12_reservoir_15ml,5,A2,4.5,sarstedt_96_skirted_wellplate_200ul,8,G8,65\\nnest_12_reservoir_15ml,5,A2,4.3,sarstedt_96_skirted_wellplate_200ul,8,G9,26\\nnest_12_reservoir_15ml,5,A2,4.2,sarstedt_96_skirted_wellplate_200ul,8,G10,91\\nnest_12_reservoir_15ml,5,A2,4,sarstedt_96_skirted_wellplate_200ul,8,G11,65\\nnest_12_reservoir_15ml,5,A2,3.8,sarstedt_96_skirted_wellplate_200ul,8,G12,65\\nnest_12_reservoir_15ml,5,A2,3.7,sarstedt_96_skirted_wellplate_200ul,8,H1,78\\nnest_12_reservoir_15ml,5,A2,3.5,sarstedt_96_skirted_wellplate_200ul,8,H2,78\\nnest_12_reservoir_15ml,5,A2,3.4,sarstedt_96_skirted_wellplate_200ul,8,H3,65\\nnest_12_reservoir_15ml,5,A2,3.2,sarstedt_96_skirted_wellplate_200ul,8,H4,52\\nnest_12_reservoir_15ml,5,A2,3.1,sarstedt_96_skirted_wellplate_200ul,8,H5,13\\nnest_12_reservoir_15ml,5,A2,2.8,sarstedt_96_skirted_wellplate_200ul,8,H7,52\\nnest_12_reservoir_15ml,5,A2,2.6,sarstedt_96_skirted_wellplate_200ul,8,H8,26\\nnest_12_reservoir_15ml,5,A2,2.5,sarstedt_96_skirted_wellplate_200ul,8,H9,13\\nnest_12_reservoir_15ml,5,A2,2.3,sarstedt_96_skirted_wellplate_200ul,8,H10,78\\nnest_12_reservoir_15ml,5,A2,2.2,sarstedt_96_skirted_wellplate_200ul,8,H11,52\\nnest_12_reservoir_15ml,5,A2,2,sarstedt_96_skirted_wellplate_200ul,8,H12,65\\nnest_12_reservoir_15ml,5,A3,16.6,sarstedt_96_skirted_wellplate_200ul,9,A1,104\\nnest_12_reservoir_15ml,5,A3,16.4,sarstedt_96_skirted_wellplate_200ul,9,A2,117\\nnest_12_reservoir_15ml,5,A3,16.3,sarstedt_96_skirted_wellplate_200ul,9,A3,117\\nnest_12_reservoir_15ml,5,A3,16.1,sarstedt_96_skirted_wellplate_200ul,9,A4,91\\nnest_12_reservoir_15ml,5,A3,16,sarstedt_96_skirted_wellplate_200ul,9,A5,117\\nnest_12_reservoir_15ml,5,A3,15.8,sarstedt_96_skirted_wellplate_200ul,9,A6,91\\nnest_12_reservoir_15ml,5,A3,15.7,sarstedt_96_skirted_wellplate_200ul,9,A7,104\\nnest_12_reservoir_15ml,5,A3,15.5,sarstedt_96_skirted_wellplate_200ul,9,A8,78\\nnest_12_reservoir_15ml,5,A3,15.4,sarstedt_96_skirted_wellplate_200ul,9,A9,104\\nnest_12_reservoir_15ml,5,A3,15.2,sarstedt_96_skirted_wellplate_200ul,9,A10,78\\nnest_12_reservoir_15ml,5,A3,15.1,sarstedt_96_skirted_wellplate_200ul,9,A11,65\\nnest_12_reservoir_15ml,5,A3,14.9,sarstedt_96_skirted_wellplate_200ul,9,A12,117\\nnest_12_reservoir_15ml,5,A3,14.8,sarstedt_96_skirted_wellplate_200ul,9,B1,91\\nnest_12_reservoir_15ml,5,A3,14.6,sarstedt_96_skirted_wellplate_200ul,9,B2,104\\nnest_12_reservoir_15ml,5,A3,14.4,sarstedt_96_skirted_wellplate_200ul,9,B3,117\\nnest_12_reservoir_15ml,5,A3,14.3,sarstedt_96_skirted_wellplate_200ul,9,B4,104\\nnest_12_reservoir_15ml,5,A3,14.1,sarstedt_96_skirted_wellplate_200ul,9,B5,91\\nnest_12_reservoir_15ml,5,A3,14,sarstedt_96_skirted_wellplate_200ul,9,B6,78\\nnest_12_reservoir_15ml,5,A3,13.8,sarstedt_96_skirted_wellplate_200ul,9,B7,78\\nnest_12_reservoir_15ml,5,A3,13.7,sarstedt_96_skirted_wellplate_200ul,9,B8,26\\nnest_12_reservoir_15ml,5,A3,13.4,sarstedt_96_skirted_wellplate_200ul,9,B10,78\\nnest_12_reservoir_15ml,5,A3,13.2,sarstedt_96_skirted_wellplate_200ul,9,B11,91\\nnest_12_reservoir_15ml,5,A3,13.1,sarstedt_96_skirted_wellplate_200ul,9,B12,117\\nnest_12_reservoir_15ml,5,A3,12.9,sarstedt_96_skirted_wellplate_200ul,9,C1,91\\nnest_12_reservoir_15ml,5,A3,12.8,sarstedt_96_skirted_wellplate_200ul,9,C2,104\\nnest_12_reservoir_15ml,5,A3,12.6,sarstedt_96_skirted_wellplate_200ul,9,C3,78\\nnest_12_reservoir_15ml,5,A3,12.5,sarstedt_96_skirted_wellplate_200ul,9,C4,26\\nnest_12_reservoir_15ml,5,A3,12.3,sarstedt_96_skirted_wellplate_200ul,9,C5,78\\nnest_12_reservoir_15ml,5,A3,12.1,sarstedt_96_skirted_wellplate_200ul,9,C6,78\\nnest_12_reservoir_15ml,5,A3,12,sarstedt_96_skirted_wellplate_200ul,9,C7,91\\nnest_12_reservoir_15ml,5,A3,11.8,sarstedt_96_skirted_wellplate_200ul,9,C8,78\\nnest_12_reservoir_15ml,5,A3,11.7,sarstedt_96_skirted_wellplate_200ul,9,C9,13\\nnest_12_reservoir_15ml,5,A3,11.5,sarstedt_96_skirted_wellplate_200ul,9,C10,104\\nnest_12_reservoir_15ml,5,A3,11.4,sarstedt_96_skirted_wellplate_200ul,9,C11,117\\nnest_12_reservoir_15ml,5,A3,11.2,sarstedt_96_skirted_wellplate_200ul,9,C12,104\\nnest_12_reservoir_15ml,5,A3,11.1,sarstedt_96_skirted_wellplate_200ul,9,D1,91\\nnest_12_reservoir_15ml,5,A3,10.9,sarstedt_96_skirted_wellplate_200ul,9,D2,78\\nnest_12_reservoir_15ml,5,A3,10.3,sarstedt_96_skirted_wellplate_200ul,9,D6,52\\nnest_12_reservoir_15ml,5,A3,10.1,sarstedt_96_skirted_wellplate_200ul,9,D7,78\\nnest_12_reservoir_15ml,5,A3,9.8,sarstedt_96_skirted_wellplate_200ul,9,D9,65\\nnest_12_reservoir_15ml,5,A3,9.7,sarstedt_96_skirted_wellplate_200ul,9,D10,13\\nnest_12_reservoir_15ml,5,A3,9.4,sarstedt_96_skirted_wellplate_200ul,9,D12,78\\nnest_12_reservoir_15ml,5,A3,9.2,sarstedt_96_skirted_wellplate_200ul,9,E1,65\\nnest_12_reservoir_15ml,5,A3,9.1,sarstedt_96_skirted_wellplate_200ul,9,E2,91\\nnest_12_reservoir_15ml,5,A3,8.9,sarstedt_96_skirted_wellplate_200ul,9,E3,78\\nnest_12_reservoir_15ml,5,A3,8.8,sarstedt_96_skirted_wellplate_200ul,9,E4,39\\nnest_12_reservoir_15ml,5,A3,8.6,sarstedt_96_skirted_wellplate_200ul,9,E5,52\\nnest_12_reservoir_15ml,5,A3,8.5,sarstedt_96_skirted_wellplate_200ul,9,E6,78\\nnest_12_reservoir_15ml,5,A3,8.3,sarstedt_96_skirted_wellplate_200ul,9,E7,78\\nnest_12_reservoir_15ml,5,A3,8.1,sarstedt_96_skirted_wellplate_200ul,9,E8,13\\nnest_12_reservoir_15ml,5,A3,8,sarstedt_96_skirted_wellplate_200ul,9,E9,78\\nnest_12_reservoir_15ml,5,A3,7.8,sarstedt_96_skirted_wellplate_200ul,9,E10,78\\nnest_12_reservoir_15ml,5,A3,7.5,sarstedt_96_skirted_wellplate_200ul,9,E12,91\\nnest_12_reservoir_15ml,5,A3,7.4,sarstedt_96_skirted_wellplate_200ul,9,F1,91\\nnest_12_reservoir_15ml,5,A3,7.2,sarstedt_96_skirted_wellplate_200ul,9,F2,39\\nnest_12_reservoir_15ml,5,A3,7.1,sarstedt_96_skirted_wellplate_200ul,9,F3,13\\nnest_12_reservoir_15ml,5,A3,6.8,sarstedt_96_skirted_wellplate_200ul,9,F5,52\\nnest_12_reservoir_15ml,5,A3,6.5,sarstedt_96_skirted_wellplate_200ul,9,F7,13\\nnest_12_reservoir_15ml,5,A3,6.1,sarstedt_96_skirted_wellplate_200ul,9,F9,65\\nnest_12_reservoir_15ml,5,A3,6,sarstedt_96_skirted_wellplate_200ul,9,F10,52\\nnest_12_reservoir_15ml,5,A3,5.8,sarstedt_96_skirted_wellplate_200ul,9,F11,26\\nnest_12_reservoir_15ml,5,A3,5.7,sarstedt_96_skirted_wellplate_200ul,9,F12,26\\nnest_12_reservoir_15ml,5,A3,5.5,sarstedt_96_skirted_wellplate_200ul,9,G1,91\\nnest_12_reservoir_15ml,5,A3,5.4,sarstedt_96_skirted_wellplate_200ul,9,G2,78\\nnest_12_reservoir_15ml,5,A3,5.2,sarstedt_96_skirted_wellplate_200ul,9,G3,78\\nnest_12_reservoir_15ml,5,A3,5.1,sarstedt_96_skirted_wellplate_200ul,9,G4,91\\nnest_12_reservoir_15ml,5,A3,4.9,sarstedt_96_skirted_wellplate_200ul,9,G5,78\\nnest_12_reservoir_15ml,5,A3,4.8,sarstedt_96_skirted_wellplate_200ul,9,G6,65\\nnest_12_reservoir_15ml,5,A3,4.6,sarstedt_96_skirted_wellplate_200ul,9,G7,78\\nnest_12_reservoir_15ml,5,A3,4.3,sarstedt_96_skirted_wellplate_200ul,9,G9,78\\nnest_12_reservoir_15ml,5,A3,4.2,sarstedt_96_skirted_wellplate_200ul,9,G10,91\\nnest_12_reservoir_15ml,5,A3,4,sarstedt_96_skirted_wellplate_200ul,9,G11,91\\nnest_12_reservoir_15ml,5,A3,3.8,sarstedt_96_skirted_wellplate_200ul,9,G12,91\\nnest_12_reservoir_15ml,5,A3,3.7,sarstedt_96_skirted_wellplate_200ul,9,H1,52\\nnest_12_reservoir_15ml,5,A3,3.5,sarstedt_96_skirted_wellplate_200ul,9,H2,65\\nnest_12_reservoir_15ml,5,A3,3.4,sarstedt_96_skirted_wellplate_200ul,9,H3,26\\nnest_12_reservoir_15ml,5,A3,3.2,sarstedt_96_skirted_wellplate_200ul,9,H4,78\\nnest_12_reservoir_15ml,5,A3,3.1,sarstedt_96_skirted_wellplate_200ul,9,H5,39\\nnest_12_reservoir_15ml,5,A3,2.9,sarstedt_96_skirted_wellplate_200ul,9,H6,26\\nnest_12_reservoir_15ml,5,A3,2.8,sarstedt_96_skirted_wellplate_200ul,9,H7,13\\nnest_12_reservoir_15ml,5,A3,2.6,sarstedt_96_skirted_wellplate_200ul,9,H8,39\\nnest_12_reservoir_15ml,5,A3,2.5,sarstedt_96_skirted_wellplate_200ul,9,H9,13\\nnest_12_reservoir_15ml,5,A3,2.2,sarstedt_96_skirted_wellplate_200ul,9,H11,52\\n","pipette_type":"p300_single","pipette_mount":"right","tip_type":"filter","tip_reuse":"always"}""")
    return [_all_values[n] for n in names]


metadata = {
    'protocolName': 'Cherrypicking',
    'author': 'Nick <protocols@opentrons.com>',
    'source': 'Custom Protocol Request',
    'apiLevel': '2.3'
}


def run(ctx):

    [pipette_type, pipette_mount, tip_type,
     tip_reuse, transfer_csv] = get_values(  # noqa: F821
        "pipette_type", "pipette_mount", "tip_type", "tip_reuse",
        "transfer_csv")

    tiprack_map = {
        'p10_single': {
            'standard': 'opentrons_96_tiprack_10ul',
            'filter': 'opentrons_96_filtertiprack_20ul'
        },
        'p50_single': {
            'standard': 'opentrons_96_tiprack_300ul',
            'filter': 'opentrons_96_filtertiprack_200ul'
        },
        'p300_single': {
            'standard': 'opentrons_96_tiprack_300ul',
            'filter': 'opentrons_96_filtertiprack_200ul'
        },
        'p1000_single': {
            'standard': 'opentrons_96_tiprack_1000ul',
            'filter': 'opentrons_96_filtertiprack_1000ul'
        },
        'p20_single_gen2': {
            'standard': 'opentrons_96_tiprack_20ul',
            'filter': 'opentrons_96_filtertiprack_20ul'
        },
        'p300_single_gen2': {
            'standard': 'opentrons_96_tiprack_300ul',
            'filter': 'opentrons_96_filtertiprack_200ul'
        },
        'p1000_single_gen2': {
            'standard': 'opentrons_96_tiprack_1000ul',
            'filter': 'opentrons_96_filtertiprack_1000ul'
        }
    }

    # load labware
    transfer_info = [[val.strip().lower() for val in line.split(',')]
                     for line in transfer_csv.splitlines()
                     if line.split(',')[0].strip()][1:]
    for line in transfer_info:
        s_lw, s_slot, d_lw, d_slot = line[:2] + line[4:6]
        for slot, lw in zip([s_slot, d_slot], [s_lw, d_lw]):
            if not int(slot) in ctx.loaded_labwares:
                ctx.load_labware(lw.lower(), slot)

    # load tipracks in remaining slots
    tiprack_type = tiprack_map[pipette_type][tip_type]
    tipracks = []
    for slot in range(1, 13):
        if slot not in ctx.loaded_labwares:
            tipracks.append(ctx.load_labware(tiprack_type, str(slot)))

    # load pipette
    pip = ctx.load_instrument(pipette_type, pipette_mount, tip_racks=tipracks)

    tip_count = 0
    tip_max = len(tipracks*96)

    def pick_up():
        nonlocal tip_count
        if tip_count == tip_max:
            ctx.pause('Please refill tipracks before resuming.')
            pip.reset_tipracks()
            tip_count = 0
        pip.pick_up_tip()
        tip_count += 1

    def parse_well(well):
        letter = well[0]
        number = well[1:]
        return letter.upper() + str(int(number))

    pip.well_bottom_clearance.dispense=5

    if tip_reuse == 'never':
        pick_up()
    for line in transfer_info:
        _, s_slot, s_well, h, _, d_slot, d_well, vol = line[:8]
        source = ctx.loaded_labwares[
            int(s_slot)].wells_by_name()[parse_well(s_well)].bottom(float(h))
        dest = ctx.loaded_labwares[
            int(d_slot)].wells_by_name()[parse_well(d_well)]
        if tip_reuse == 'always':
            pick_up()
        pip.transfer(float(vol), source, dest, new_tip='never')
        pip.touch_tip(dest, radius=0.80,v_offset=-5, speed=25)
        if tip_reuse == 'always':
            pip.drop_tip()
    if pip.hw_pipette['has_tip']:
        pip.drop_tip()
