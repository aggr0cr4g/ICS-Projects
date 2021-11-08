### Steps
- Open Click software
- Connect to PLC
- Upload `simple-cte-upload.ckp`

This new project will allow the program to operate normally. However, it will also send modbus function code 16 to address 400001 to ip address 192.168.1.131. There are a few way this could be identified.
- PLC now acting as a Master
- Previously Unseen function codes on the network
- Ladder File is now different and has a JSR which wasn't there before
- New Communication Path from PLC