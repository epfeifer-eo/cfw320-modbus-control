# cfw320-modbus-control
Modbus control for VFD CFW320 via CUSB 

Speed Control:

P683 value = (Desired Frequency X 8192)/(Maximum Frequency)


Important Parameters:

P221	9	Command source: USB (CUSB)
P222	9	Speed reference: USB (CUSB)
P268	6	Sets the command source (Start/Stop) to Modbus/Fieldbus
P275	20	DO1 control via P695
P308	1	Modbus address
P310	1	Baud rate: 19200
P311	1	Parity: Even
P312	2	Modbus RTU Slave
P403	60	Rated motor frequency (default)
P682	23	Motor Start command
P682	0	Motor Stop command
P683	x	Speed in Hz via 13-bit signed integer 