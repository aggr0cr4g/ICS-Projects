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
### Turning off the Lights
***Emulation Steps***
- Run `turn-off-power.py`
***Possible Detections***
- A new Modbus TCP/IP communication path previously unseen. Modbus TCP/IP is a common protocol for SCADA systems. Normal Modbus communication is a master, or masters, polling a large number of slaves, the Click PLC. Unless a change occurs in the environment, yhe SRC_IP, DEST_IP, and DEST_PORT tuple would be established and static. A new/unknown tuple would be 
 these communication pairs should be well known and static. The tuple of the Attack_IP, CLICK_PLC, DEST_PORT would be new and should be identified by analysts if proper collection and analysis is occouring.  

### New PLC Program
***Emulation Steps***
- Download Click Software to Attack Box
- Go online with the PLC
- Download a `simple-design.ckp` to the PLC
***Possible Detections***
- PLC State change. Click PLCs are always in remote mode. Meaning software can change the state from RUN to STOP. The Click Programing software will default to change the PLC from RUN to STOP mode before downloading the new program to the PLC. Analysts should be able to navigate to (Click Manual )[https://www.automationdirect.com/microsites/clickplcs/click-help/Content/234.htm] and see that the software operates on port 25425 and that is not configurable. Thus, an analyst should see a new box with Click Software online. 
- PLC behavior change. When you download the new program to the PLC it will now have a JSR that will attempt Modbus Function Code 16 to IP address `192.168.1.2`. If there is no slave active on the .2 then the analyst will only see ARP requests for "who has 192.168.1.131" coming from the PLC which would be new. However, if the host is active they will see TCP SYN requests on port 502. Future work to create a quick pymodbus client with the specified holdier registers so the PLC has something to write to and will give analysts new function codes to see.  


### New Function Code. 

## Authors, Licence, Credits
- 
Additional contributions from: