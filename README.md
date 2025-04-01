# cfw320-modbus-control
Modbus control for VFD CFW320 via CUSB 

****SET COM PORT***

Speed Control:

P683 value = (Desired Frequency X 8192)/(Maximum Frequency)


Important Parameters:

P221	9	Command source: USB 
P222	9	Speed reference: USB 
P224	2	Local Run/Stop Select: USB
P308	1	Modbus address
P310	1	Baud rate: 19200
P311	1	Parity: Even
P312	2	Modbus RTU Slave
P403	60	Rated motor frequency (default)
P682	23	Motor Start command (0x0017)
P682	0	Motor Stop command
P683	x	Speed in Hz via 13-bit signed integer 