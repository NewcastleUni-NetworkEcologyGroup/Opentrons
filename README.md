<p align="center">
<img src="https://github.com/NewcastleUni-NetworkEcologyGroup/Opentrons/blob/master/images/droctocat.png">
</p>

# Newcastle University Network Ecology Group Opentrons repository.

This repository contains the custom protocols and labware used by the Network Ecology Group at Newcastle University on their Opentrons OT-2 robots.
***

## Important considerations working with the OT-2
Here are a few points to keep note of when getting used to the OT-2. If you are coming here with a fair amount of Python knowlege then this probably isn't for you. Rather, this is intended to help novice users climb the learning curve and get working with the OT-2 rapidly.

* **Don't expect this machine to replacing all your pipetting!** For short protocols (e.g. setting up a single PCR plate) you are probably much faster than the OT-2. This machine is for bulk PCR setups and performing setups that are difficult to track in your head. 
    + e.g. reordering wells on a plate or combining failed samples into a rerun plate.
* Install [Anaconda](https://www.anaconda.com/) and use [Spyder](https://www.spyder-ide.org/) to write your code to help with debugging, don't use the OT-2 app errors, they are too cryptic.
    + sometimes no error will appear at all in the OT-2 app but you will have missing labware.
    + Check this in Spyder and you will often find that you've forgotten to do something that permits an otherwise correctly written command e.g. pick up some tips before distributing
* Install the opentrons package into Python/Ananconda, you can't do any debugging if your python doesn't understand the data objects.
    + `python -m pip install opentrons` in your linux or OSX command line to install the opentrons package.
