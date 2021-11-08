# ICS Virtual Lab
***Starting point for a virtual range where soldiers can practice TTPs on live data***

This range aims to create a simple ICS enviorment where soldiers can place a tap/span and see live ICS traffic. Also, the ability to emulate simple threats via `pymodbus`, validate detection methods, rules, etc...


## Design
This is a simple 2 light design. It uses the C-More to (de)energize a Red/Green light. This is also controlled via the SCADA HMI (`2-light-hmi.py`).

The program is designed to simulate a breaker within a substation or generation facility. The intent is to always be providing power on the grid (Red Light). If the Green Light is energized and there is no ASI then there is an issue on the grid, locally, or an attack.  

## Setup
- Program a ClickPLC with the `simple-design.ckp`
- Program the C-MORE HMI with the `simple-design.mgp`
- Connect the Green Light to Y2
- Connect Red Light to Y3

## Exploits
- Coming Soon. Lost old ones. 

## Authors, Licence, Credits
- 
Additional contributions from: