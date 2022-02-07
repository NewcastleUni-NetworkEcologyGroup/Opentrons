def get_values(*names):
    import json
    _all_values = json.loads("""{"transfer_csv":"Source Labware,Source Slot,Source Well,Source Aspiration Height Above Bottom (in mm),Dest Labware,Dest Slot,Dest Well,Volume (in ul)\\nnest_12_reservoir_15ml,5,A1,16.6,sarstedt_96_skirted_wellplate_200ul,7,A1,78\\nnest_12_reservoir_15ml,5,A1,16.4,sarstedt_96_skirted_wellplate_200ul,7,A2,65\\nnest_12_reservoir_15ml,5,A1,16.3,sarstedt_96_skirted_wellplate_200ul,7,A3,117\\nnest_12_reservoir_15ml,5,A1,16.1,sarstedt_96_skirted_wellplate_200ul,7,A4,117\\nnest_12_reservoir_15ml,5,A1,16,sarstedt_96_skirted_wellplate_200ul,7,A5,78\\nnest_12_reservoir_15ml,5,A1,15.8,sarstedt_96_skirted_wellplate_200ul,7,A6,91\\nnest_12_reservoir_15ml,5,A1,15.7,sarstedt_96_skirted_wellplate_200ul,7,A7,104\\nnest_12_reservoir_15ml,5,A1,15.5,sarstedt_96_skirted_wellplate_200ul,7,A8,65\\nnest_12_reservoir_15ml,5,A1,15.4,sarstedt_96_skirted_wellplate_200ul,7,A9,104\\nnest_12_reservoir_15ml,5,A1,15.2,sarstedt_96_skirted_wellplate_200ul,7,A10,78\\nnest_12_reservoir_15ml,5,A1,15.1,sarstedt_96_skirted_wellplate_200ul,7,A11,104\\nnest_12_reservoir_15ml,5,A1,14.9,sarstedt_96_skirted_wellplate_200ul,7,A12,91\\nnest_12_reservoir_15ml,5,A1,14.8,sarstedt_96_skirted_wellplate_200ul,7,B1,91\\nnest_12_reservoir_15ml,5,A1,14.6,sarstedt_96_skirted_wellplate_200ul,7,B2,91\\nnest_12_reservoir_15ml,5,A1,14.4,sarstedt_96_skirted_wellplate_200ul,7,B3,65\\nnest_12_reservoir_15ml,5,A1,14.3,sarstedt_96_skirted_wellplate_200ul,7,B4,104\\nnest_12_reservoir_15ml,5,A1,14.1,sarstedt_96_skirted_wellplate_200ul,7,B5,91\\nnest_12_reservoir_15ml,5,A1,14,sarstedt_96_skirted_wellplate_200ul,7,B6,91\\nnest_12_reservoir_15ml,5,A1,13.8,sarstedt_96_skirted_wellplate_200ul,7,B7,91\\nnest_12_reservoir_15ml,5,A1,13.7,sarstedt_96_skirted_wellplate_200ul,7,B8,104\\nnest_12_reservoir_15ml,5,A1,13.5,sarstedt_96_skirted_wellplate_200ul,7,B9,78\\nnest_12_reservoir_15ml,5,A1,13.4,sarstedt_96_skirted_wellplate_200ul,7,B10,65\\nnest_12_reservoir_15ml,5,A1,13.2,sarstedt_96_skirted_wellplate_200ul,7,B11,104\\nnest_12_reservoir_15ml,5,A1,13.1,sarstedt_96_skirted_wellplate_200ul,7,B12,91\\nnest_12_reservoir_15ml,5,A1,12.9,sarstedt_96_skirted_wellplate_200ul,7,C1,104\\nnest_12_reservoir_15ml,5,A1,12.8,sarstedt_96_skirted_wellplate_200ul,7,C2,91\\nnest_12_reservoir_15ml,5,A1,12.6,sarstedt_96_skirted_wellplate_200ul,7,C3,104\\nnest_12_reservoir_15ml,5,A1,12.5,sarstedt_96_skirted_wellplate_200ul,7,C4,104\\nnest_12_reservoir_15ml,5,A1,12.3,sarstedt_96_skirted_wellplate_200ul,7,C5,91\\nnest_12_reservoir_15ml,5,A1,12.1,sarstedt_96_skirted_wellplate_200ul,7,C6,91\\nnest_12_reservoir_15ml,5,A1,12,sarstedt_96_skirted_wellplate_200ul,7,C7,91\\nnest_12_reservoir_15ml,5,A1,11.8,sarstedt_96_skirted_wellplate_200ul,7,C8,91\\nnest_12_reservoir_15ml,5,A1,11.7,sarstedt_96_skirted_wellplate_200ul,7,C9,104\\nnest_12_reservoir_15ml,5,A1,11.5,sarstedt_96_skirted_wellplate_200ul,7,C10,78\\nnest_12_reservoir_15ml,5,A1,11.4,sarstedt_96_skirted_wellplate_200ul,7,C11,65\\nnest_12_reservoir_15ml,5,A1,11.2,sarstedt_96_skirted_wellplate_200ul,7,C12,91\\nnest_12_reservoir_15ml,5,A1,11.1,sarstedt_96_skirted_wellplate_200ul,7,D1,65\\nnest_12_reservoir_15ml,5,A1,10.9,sarstedt_96_skirted_wellplate_200ul,7,D2,78\\nnest_12_reservoir_15ml,5,A1,10.8,sarstedt_96_skirted_wellplate_200ul,7,D3,78\\nnest_12_reservoir_15ml,5,A1,10.6,sarstedt_96_skirted_wellplate_200ul,7,D4,78\\nnest_12_reservoir_15ml,5,A1,10.5,sarstedt_96_skirted_wellplate_200ul,7,D5,91\\nnest_12_reservoir_15ml,5,A1,10.3,sarstedt_96_skirted_wellplate_200ul,7,D6,78\\nnest_12_reservoir_15ml,5,A1,10.1,sarstedt_96_skirted_wellplate_200ul,7,D7,78\\nnest_12_reservoir_15ml,5,A1,10,sarstedt_96_skirted_wellplate_200ul,7,D8,91\\nnest_12_reservoir_15ml,5,A1,9.8,sarstedt_96_skirted_wellplate_200ul,7,D9,78\\nnest_12_reservoir_15ml,5,A1,9.7,sarstedt_96_skirted_wellplate_200ul,7,D10,91\\nnest_12_reservoir_15ml,5,A1,9.5,sarstedt_96_skirted_wellplate_200ul,7,D11,91\\nnest_12_reservoir_15ml,5,A1,9.4,sarstedt_96_skirted_wellplate_200ul,7,D12,78\\nnest_12_reservoir_15ml,5,A1,9.2,sarstedt_96_skirted_wellplate_200ul,7,E1,91\\nnest_12_reservoir_15ml,5,A1,9.1,sarstedt_96_skirted_wellplate_200ul,7,E2,91\\nnest_12_reservoir_15ml,5,A1,8.9,sarstedt_96_skirted_wellplate_200ul,7,E3,91\\nnest_12_reservoir_15ml,5,A1,8.8,sarstedt_96_skirted_wellplate_200ul,7,E4,91\\nnest_12_reservoir_15ml,5,A1,8.6,sarstedt_96_skirted_wellplate_200ul,7,E5,91\\nnest_12_reservoir_15ml,5,A1,8.5,sarstedt_96_skirted_wellplate_200ul,7,E6,78\\nnest_12_reservoir_15ml,5,A1,8.3,sarstedt_96_skirted_wellplate_200ul,7,E7,78\\nnest_12_reservoir_15ml,5,A1,8.1,sarstedt_96_skirted_wellplate_200ul,7,E8,91\\nnest_12_reservoir_15ml,5,A1,8,sarstedt_96_skirted_wellplate_200ul,7,E9,78\\nnest_12_reservoir_15ml,5,A1,7.8,sarstedt_96_skirted_wellplate_200ul,7,E10,91\\nnest_12_reservoir_15ml,5,A1,7.7,sarstedt_96_skirted_wellplate_200ul,7,E11,91\\nnest_12_reservoir_15ml,5,A1,7.5,sarstedt_96_skirted_wellplate_200ul,7,E12,78\\nnest_12_reservoir_15ml,5,A1,7.4,sarstedt_96_skirted_wellplate_200ul,7,F1,78\\nnest_12_reservoir_15ml,5,A1,7.2,sarstedt_96_skirted_wellplate_200ul,7,F2,91\\nnest_12_reservoir_15ml,5,A1,7.1,sarstedt_96_skirted_wellplate_200ul,7,F3,78\\nnest_12_reservoir_15ml,5,A1,6.9,sarstedt_96_skirted_wellplate_200ul,7,F4,78\\nnest_12_reservoir_15ml,5,A1,6.8,sarstedt_96_skirted_wellplate_200ul,7,F5,78\\nnest_12_reservoir_15ml,5,A1,6.6,sarstedt_96_skirted_wellplate_200ul,7,F6,65\\nnest_12_reservoir_15ml,5,A1,6.5,sarstedt_96_skirted_wellplate_200ul,7,F7,91\\nnest_12_reservoir_15ml,5,A1,6.3,sarstedt_96_skirted_wellplate_200ul,7,F8,52\\nnest_12_reservoir_15ml,5,A1,6.1,sarstedt_96_skirted_wellplate_200ul,7,F9,91\\nnest_12_reservoir_15ml,5,A1,6,sarstedt_96_skirted_wellplate_200ul,7,F10,91\\nnest_12_reservoir_15ml,5,A1,5.8,sarstedt_96_skirted_wellplate_200ul,7,F11,78\\nnest_12_reservoir_15ml,5,A1,5.7,sarstedt_96_skirted_wellplate_200ul,7,F12,65\\nnest_12_reservoir_15ml,5,A1,5.5,sarstedt_96_skirted_wellplate_200ul,7,G1,91\\nnest_12_reservoir_15ml,5,A1,5.4,sarstedt_96_skirted_wellplate_200ul,7,G2,104\\nnest_12_reservoir_15ml,5,A1,5.2,sarstedt_96_skirted_wellplate_200ul,7,G3,91\\nnest_12_reservoir_15ml,5,A1,5.1,sarstedt_96_skirted_wellplate_200ul,7,G4,104\\nnest_12_reservoir_15ml,5,A1,4.9,sarstedt_96_skirted_wellplate_200ul,7,G5,91\\nnest_12_reservoir_15ml,5,A1,4.8,sarstedt_96_skirted_wellplate_200ul,7,G6,91\\nnest_12_reservoir_15ml,5,A1,4.6,sarstedt_96_skirted_wellplate_200ul,7,G7,91\\nnest_12_reservoir_15ml,5,A1,4.5,sarstedt_96_skirted_wellplate_200ul,7,G8,78\\nnest_12_reservoir_15ml,5,A1,4.3,sarstedt_96_skirted_wellplate_200ul,7,G9,104\\nnest_12_reservoir_15ml,5,A1,4.2,sarstedt_96_skirted_wellplate_200ul,7,G10,104\\nnest_12_reservoir_15ml,5,A1,4,sarstedt_96_skirted_wellplate_200ul,7,G11,91\\nnest_12_reservoir_15ml,5,A1,3.8,sarstedt_96_skirted_wellplate_200ul,7,G12,78\\nnest_12_reservoir_15ml,5,A1,3.7,sarstedt_96_skirted_wellplate_200ul,7,H1,78\\nnest_12_reservoir_15ml,5,A1,3.5,sarstedt_96_skirted_wellplate_200ul,7,H2,104\\nnest_12_reservoir_15ml,5,A1,3.4,sarstedt_96_skirted_wellplate_200ul,7,H3,91\\nnest_12_reservoir_15ml,5,A1,3.2,sarstedt_96_skirted_wellplate_200ul,7,H4,78\\nnest_12_reservoir_15ml,5,A1,3.1,sarstedt_96_skirted_wellplate_200ul,7,H5,117\\nnest_12_reservoir_15ml,5,A1,2.9,sarstedt_96_skirted_wellplate_200ul,7,H6,78\\nnest_12_reservoir_15ml,5,A1,2.8,sarstedt_96_skirted_wellplate_200ul,7,H7,65\\nnest_12_reservoir_15ml,5,A1,2.6,sarstedt_96_skirted_wellplate_200ul,7,H8,65\\nnest_12_reservoir_15ml,5,A1,2.5,sarstedt_96_skirted_wellplate_200ul,7,H9,91\\nnest_12_reservoir_15ml,5,A1,2.3,sarstedt_96_skirted_wellplate_200ul,7,H10,78\\nnest_12_reservoir_15ml,5,A1,2.2,sarstedt_96_skirted_wellplate_200ul,7,H11,78\\nnest_12_reservoir_15ml,5,A1,2,sarstedt_96_skirted_wellplate_200ul,7,H12,78\\nnest_12_reservoir_15ml,5,A2,16.6,sarstedt_96_skirted_wellplate_200ul,8,A1,104\\nnest_12_reservoir_15ml,5,A2,16.4,sarstedt_96_skirted_wellplate_200ul,8,A2,78\\nnest_12_reservoir_15ml,5,A2,16.3,sarstedt_96_skirted_wellplate_200ul,8,A3,117\\nnest_12_reservoir_15ml,5,A2,16.1,sarstedt_96_skirted_wellplate_200ul,8,A4,78\\nnest_12_reservoir_15ml,5,A2,16,sarstedt_96_skirted_wellplate_200ul,8,A5,117\\nnest_12_reservoir_15ml,5,A2,15.8,sarstedt_96_skirted_wellplate_200ul,8,A6,91\\nnest_12_reservoir_15ml,5,A2,15.7,sarstedt_96_skirted_wellplate_200ul,8,A7,117\\nnest_12_reservoir_15ml,5,A2,15.5,sarstedt_96_skirted_wellplate_200ul,8,A8,117\\nnest_12_reservoir_15ml,5,A2,15.4,sarstedt_96_skirted_wellplate_200ul,8,A9,117\\nnest_12_reservoir_15ml,5,A2,15.2,sarstedt_96_skirted_wellplate_200ul,8,A10,91\\nnest_12_reservoir_15ml,5,A2,15.1,sarstedt_96_skirted_wellplate_200ul,8,A11,104\\nnest_12_reservoir_15ml,5,A2,14.9,sarstedt_96_skirted_wellplate_200ul,8,A12,91\\nnest_12_reservoir_15ml,5,A2,14.8,sarstedt_96_skirted_wellplate_200ul,8,B1,104\\nnest_12_reservoir_15ml,5,A2,14.6,sarstedt_96_skirted_wellplate_200ul,8,B2,117\\nnest_12_reservoir_15ml,5,A2,14.4,sarstedt_96_skirted_wellplate_200ul,8,B3,104\\nnest_12_reservoir_15ml,5,A2,14.3,sarstedt_96_skirted_wellplate_200ul,8,B4,104\\nnest_12_reservoir_15ml,5,A2,14.1,sarstedt_96_skirted_wellplate_200ul,8,B5,117\\nnest_12_reservoir_15ml,5,A2,14,sarstedt_96_skirted_wellplate_200ul,8,B6,117\\nnest_12_reservoir_15ml,5,A2,13.8,sarstedt_96_skirted_wellplate_200ul,8,B7,104\\nnest_12_reservoir_15ml,5,A2,13.7,sarstedt_96_skirted_wellplate_200ul,8,B8,91\\nnest_12_reservoir_15ml,5,A2,13.5,sarstedt_96_skirted_wellplate_200ul,8,B9,65\\nnest_12_reservoir_15ml,5,A2,13.4,sarstedt_96_skirted_wellplate_200ul,8,B10,91\\nnest_12_reservoir_15ml,5,A2,13.2,sarstedt_96_skirted_wellplate_200ul,8,B11,104\\nnest_12_reservoir_15ml,5,A2,13.1,sarstedt_96_skirted_wellplate_200ul,8,B12,26\\nnest_12_reservoir_15ml,5,A2,12.9,sarstedt_96_skirted_wellplate_200ul,8,C1,117\\nnest_12_reservoir_15ml,5,A2,12.8,sarstedt_96_skirted_wellplate_200ul,8,C2,117\\nnest_12_reservoir_15ml,5,A2,12.6,sarstedt_96_skirted_wellplate_200ul,8,C3,78\\nnest_12_reservoir_15ml,5,A2,12.5,sarstedt_96_skirted_wellplate_200ul,8,C4,104\\nnest_12_reservoir_15ml,5,A2,12.3,sarstedt_96_skirted_wellplate_200ul,8,C5,104\\nnest_12_reservoir_15ml,5,A2,12.1,sarstedt_96_skirted_wellplate_200ul,8,C6,104\\nnest_12_reservoir_15ml,5,A2,12,sarstedt_96_skirted_wellplate_200ul,8,C7,104\\nnest_12_reservoir_15ml,5,A2,11.8,sarstedt_96_skirted_wellplate_200ul,8,C8,104\\nnest_12_reservoir_15ml,5,A2,11.7,sarstedt_96_skirted_wellplate_200ul,8,C9,26\\nnest_12_reservoir_15ml,5,A2,11.5,sarstedt_96_skirted_wellplate_200ul,8,C10,104\\nnest_12_reservoir_15ml,5,A2,11.4,sarstedt_96_skirted_wellplate_200ul,8,C11,104\\nnest_12_reservoir_15ml,5,A2,11.2,sarstedt_96_skirted_wellplate_200ul,8,C12,104\\nnest_12_reservoir_15ml,5,A2,11.1,sarstedt_96_skirted_wellplate_200ul,8,D1,91\\nnest_12_reservoir_15ml,5,A2,10.9,sarstedt_96_skirted_wellplate_200ul,8,D2,91\\nnest_12_reservoir_15ml,5,A2,10.8,sarstedt_96_skirted_wellplate_200ul,8,D3,78\\nnest_12_reservoir_15ml,5,A2,10.6,sarstedt_96_skirted_wellplate_200ul,8,D4,104\\nnest_12_reservoir_15ml,5,A2,10.5,sarstedt_96_skirted_wellplate_200ul,8,D5,52\\nnest_12_reservoir_15ml,5,A2,10.3,sarstedt_96_skirted_wellplate_200ul,8,D6,117\\nnest_12_reservoir_15ml,5,A2,10.1,sarstedt_96_skirted_wellplate_200ul,8,D7,91\\nnest_12_reservoir_15ml,5,A2,10,sarstedt_96_skirted_wellplate_200ul,8,D8,78\\nnest_12_reservoir_15ml,5,A2,9.8,sarstedt_96_skirted_wellplate_200ul,8,D9,52\\nnest_12_reservoir_15ml,5,A2,9.7,sarstedt_96_skirted_wellplate_200ul,8,D10,52\\nnest_12_reservoir_15ml,5,A2,9.5,sarstedt_96_skirted_wellplate_200ul,8,D11,65\\nnest_12_reservoir_15ml,5,A2,9.4,sarstedt_96_skirted_wellplate_200ul,8,D12,104\\nnest_12_reservoir_15ml,5,A2,9.2,sarstedt_96_skirted_wellplate_200ul,8,E1,104\\nnest_12_reservoir_15ml,5,A2,9.1,sarstedt_96_skirted_wellplate_200ul,8,E2,104\\nnest_12_reservoir_15ml,5,A2,8.9,sarstedt_96_skirted_wellplate_200ul,8,E3,104\\nnest_12_reservoir_15ml,5,A2,8.8,sarstedt_96_skirted_wellplate_200ul,8,E4,78\\nnest_12_reservoir_15ml,5,A2,8.6,sarstedt_96_skirted_wellplate_200ul,8,E5,104\\nnest_12_reservoir_15ml,5,A2,8.5,sarstedt_96_skirted_wellplate_200ul,8,E6,91\\nnest_12_reservoir_15ml,5,A2,8.3,sarstedt_96_skirted_wellplate_200ul,8,E7,65\\nnest_12_reservoir_15ml,5,A2,8.1,sarstedt_96_skirted_wellplate_200ul,8,E8,91\\nnest_12_reservoir_15ml,5,A2,8,sarstedt_96_skirted_wellplate_200ul,8,E9,91\\nnest_12_reservoir_15ml,5,A2,7.8,sarstedt_96_skirted_wellplate_200ul,8,E10,91\\nnest_12_reservoir_15ml,5,A2,7.7,sarstedt_96_skirted_wellplate_200ul,8,E11,104\\nnest_12_reservoir_15ml,5,A2,7.5,sarstedt_96_skirted_wellplate_200ul,8,E12,91\\nnest_12_reservoir_15ml,5,A2,7.4,sarstedt_96_skirted_wellplate_200ul,8,F1,39\\nnest_12_reservoir_15ml,5,A2,7.2,sarstedt_96_skirted_wellplate_200ul,8,F2,91\\nnest_12_reservoir_15ml,5,A2,7.1,sarstedt_96_skirted_wellplate_200ul,8,F3,78\\nnest_12_reservoir_15ml,5,A2,6.9,sarstedt_96_skirted_wellplate_200ul,8,F4,78\\nnest_12_reservoir_15ml,5,A2,6.8,sarstedt_96_skirted_wellplate_200ul,8,F5,91\\nnest_12_reservoir_15ml,5,A2,6.6,sarstedt_96_skirted_wellplate_200ul,8,F6,91\\nnest_12_reservoir_15ml,5,A2,6.5,sarstedt_96_skirted_wellplate_200ul,8,F7,78\\nnest_12_reservoir_15ml,5,A2,6.3,sarstedt_96_skirted_wellplate_200ul,8,F8,65\\nnest_12_reservoir_15ml,5,A2,6.1,sarstedt_96_skirted_wellplate_200ul,8,F9,39\\nnest_12_reservoir_15ml,5,A2,6,sarstedt_96_skirted_wellplate_200ul,8,F10,78\\nnest_12_reservoir_15ml,5,A2,5.8,sarstedt_96_skirted_wellplate_200ul,8,F11,78\\nnest_12_reservoir_15ml,5,A2,5.7,sarstedt_96_skirted_wellplate_200ul,8,F12,78\\nnest_12_reservoir_15ml,5,A2,5.5,sarstedt_96_skirted_wellplate_200ul,8,G1,65\\nnest_12_reservoir_15ml,5,A2,5.4,sarstedt_96_skirted_wellplate_200ul,8,G2,78\\nnest_12_reservoir_15ml,5,A2,5.2,sarstedt_96_skirted_wellplate_200ul,8,G3,78\\nnest_12_reservoir_15ml,5,A2,5.1,sarstedt_96_skirted_wellplate_200ul,8,G4,78\\nnest_12_reservoir_15ml,5,A2,4.9,sarstedt_96_skirted_wellplate_200ul,8,G5,78\\nnest_12_reservoir_15ml,5,A2,4.8,sarstedt_96_skirted_wellplate_200ul,8,G6,78\\nnest_12_reservoir_15ml,5,A2,4.6,sarstedt_96_skirted_wellplate_200ul,8,G7,104\\nnest_12_reservoir_15ml,5,A2,4.5,sarstedt_96_skirted_wellplate_200ul,8,G8,78\\nnest_12_reservoir_15ml,5,A2,4.3,sarstedt_96_skirted_wellplate_200ul,8,G9,104\\nnest_12_reservoir_15ml,5,A2,4.2,sarstedt_96_skirted_wellplate_200ul,8,G10,78\\nnest_12_reservoir_15ml,5,A2,4,sarstedt_96_skirted_wellplate_200ul,8,G11,91\\nnest_12_reservoir_15ml,5,A2,3.8,sarstedt_96_skirted_wellplate_200ul,8,G12,91\\nnest_12_reservoir_15ml,5,A2,3.7,sarstedt_96_skirted_wellplate_200ul,8,H1,78\\nnest_12_reservoir_15ml,5,A2,3.5,sarstedt_96_skirted_wellplate_200ul,8,H2,91\\nnest_12_reservoir_15ml,5,A2,3.4,sarstedt_96_skirted_wellplate_200ul,8,H3,78\\nnest_12_reservoir_15ml,5,A2,3.2,sarstedt_96_skirted_wellplate_200ul,8,H4,65\\nnest_12_reservoir_15ml,5,A2,3.1,sarstedt_96_skirted_wellplate_200ul,8,H5,104\\nnest_12_reservoir_15ml,5,A2,2.9,sarstedt_96_skirted_wellplate_200ul,8,H6,91\\nnest_12_reservoir_15ml,5,A2,2.8,sarstedt_96_skirted_wellplate_200ul,8,H7,91\\nnest_12_reservoir_15ml,5,A2,2.6,sarstedt_96_skirted_wellplate_200ul,8,H8,78\\nnest_12_reservoir_15ml,5,A2,2.5,sarstedt_96_skirted_wellplate_200ul,8,H9,91\\nnest_12_reservoir_15ml,5,A2,2.3,sarstedt_96_skirted_wellplate_200ul,8,H10,91\\nnest_12_reservoir_15ml,5,A2,2.2,sarstedt_96_skirted_wellplate_200ul,8,H11,104\\nnest_12_reservoir_15ml,5,A2,2,sarstedt_96_skirted_wellplate_200ul,8,H12,91\\n","pipette_type":"p300_single","pipette_mount":"right","tip_type":"filter","tip_reuse":"always"}""")
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
        if tip_reuse == 'always':
            pip.drop_tip()
    if pip.hw_pipette['has_tip']:
        pip.drop_tip()
