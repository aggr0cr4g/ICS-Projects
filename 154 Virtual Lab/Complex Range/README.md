# ICS Virtual Lab
***Starting point for a virtual range where soldiers can practice TTPs on live data***

This range aims to create a simple ICS enviorment where soldiers can place a tap/span and see live ICS traffic. Also, the ability to emulate simple threats via `pymodbus`, validate detection methods, rules, etc...


## Requirements
  * The following requirements are needed IOT complete setup this range:

    | Requirement | Description |
    | --- | --- |
    | Click C0-10DRE PLC | The PLC used in SANS ICS-612 |
    | CMORE EA3-S3ML-R HMI | Again From ICS-612 |
    | Factory IO Simulation  Software | This is used to replicate a physical enviorment |
    | Laptop | This Laptop will be used to run Factory IO |
    | Gray Switch/TAP (Forgot Model  Number) | This is used to network all the pieces |
    | Server with ESXi/Vcenter (convenience) | You can Skip ESXi for ease of Setup and just use Workstation Pro|


## Usage
- Start buy building the Lab enviorment in ESXi. Helping document here [Building the Lab](https://aj-labz.gitbook.io/aj-labz/building-the-lab/building-the-lab). If you wanted to skip the ESXi part just start workstation and have 3 VMs (engineering workstation ICS612 VM will work, Factory IO VM, and Kali Attack Box)
- Program the PLC with `Click PLC PID using Factory IO.ckp`
- Program the CMORE HMI with `<Insert Filename Here>`
- Configure Factory IO with the `Click PLC PID Level Control.factoryio` Project File/Scene
- Connect everything to Switch

## Exploits
- Coming Soon. Lost old ones. 

## Authors, Licence, Credits
- Factory I/O setup via [CLICK PLC PID USING FACTORY IO (3D)](https://accautomation.ca/click-plc-pid-using-factory-io/)

Additional contributions from: