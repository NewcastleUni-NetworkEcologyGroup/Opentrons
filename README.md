<p align="center">
<img src="https://github.com/NewcastleUni-NetworkEcologyGroup/Opentrons/blob/master/images/droctocat.png">
</p>

# Newcastle University Network Ecology Group Opentrons repository.

This repository contains the custom protocols and labware used by the Network Ecology Group at Newcastle University on their Opentrons OT-2 robots.
***

## Important considerations working with the OT-2
Here are a few points to keep note of when getting used to the OT-2. If you are coming here with a fair amount of Python knowlege then this probably isn't for you. Rather, this is intended to help novice users climb the learning curve and get working with the OT-2 rapidly.

* For short protocols (e.g. setting up a single PCR plate) you're much faster than the OT-2, this machine is for bulk PCR setups and performinf setups that are difficult to track in your head.
* Install Anaconda and use Spyder to write your code to help with debugging, don't use the OT-2 app errors, they are too cryptic.
* Install the opentrons package into Python/Ananconda, you can't do any debugging if your python doesn't understand the data objects.
    + `python -m pip install opentrons` in your linux or OSX command line to install the opentrons package.
