*version 9.1 307979542
u 64
D? 3
V? 2
R? 2
? 5
@libraries
@analysis
.TRAN 1 0 0 0
+0 0ns
+1 5ms
@targets
@attributes
@translators
a 0 u 13 0 0 0 hln 100 PCBOARDS=PCB
a 0 u 13 0 0 0 hln 100 PSPICE=PSPICE
a 0 u 13 0 0 0 hln 100 XILINX=XILINX
@setup
unconnectedPins 0
connectViaLabel 0
connectViaLocalLabels 0
NoStim4ExtIFPortsWarnings 1
AutoGenStim4ExtIFPorts 1
@index
pageloc 1 0 1732 
@status
n 0 124:10:18:08:08:33;1731895713 e 
s 2832 125:00:21:13:18:20;1737443900 e 
*page 1 0 970 720 iA
@ports
port 22 GND_EARTH 380 320 h
@parts
part 5 r 500 240 d
a 0 sp 0 0 0 10 hlb 100 PART=r
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=RC05
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=R1
a 0 ap 9 0 15 0 hln 100 REFDES=R1
part 4 vsin 240 220 h
a 0 a 0:13 0 0 0 hln 100 PKGREF=V1
a 1 ap 9 0 20 10 hcn 100 REFDES=V1
a 1 u 0 0 0 0 hcn 100 DC=0
a 1 u 0 0 0 0 hcn 100 AC=0
a 1 u 0 0 0 0 hcn 100 VOFF=0
a 1 u 0 0 0 0 hcn 100 VAMPL=20
a 1 u 0 0 0 0 hcn 100 FREQ=1K
part 3 D1N4002 360 150 h
a 0 sp 11 0 17 29 hln 100 PART=D1N4002
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=DO-41
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=D2
a 0 ap 9 0 17 4 hln 100 REFDES=D2
part 1 titleblk 970 720 h
a 1 s 13 0 350 10 hcn 100 PAGESIZE=A
a 1 s 13 0 180 60 hcn 100 PAGETITLE=
a 1 s 13 0 340 95 hrn 100 PAGECOUNT=1
a 1 s 13 0 300 95 hrn 100 PAGENO=1
part 53 nodeMarker 240 150 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=3
part 54 nodeMarker 500 150 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=4
@conn
w 19
a 0 up 0:33 0 0 0 hln 100 V=
s 380 320 500 320 23
s 240 320 380 320 20
a 0 up 33 0 310 319 hct 100 V=
s 240 260 240 320 18
s 500 280 500 320 40
w 48
s 240 220 240 150 47
s 240 150 360 150 59
w 27
a 0 up 0:33 0 0 0 hln 100 V=
s 500 150 500 240 36
s 390 150 500 150 61
@junction
j 500 280
+ p 5 2
+ w 19
j 380 320
+ s 22
+ w 19
j 240 260
+ p 4 -
+ w 19
j 500 240
+ p 5 1
+ w 27
j 500 150
+ p 54 pin1
+ w 27
j 240 220
+ p 4 +
+ w 48
j 360 150
+ p 3 1
+ w 48
j 390 150
+ p 3 2
+ w 27
j 240 150
+ p 53 pin1
+ w 48
@attributes
a 0 s 0:13 0 0 0 hln 100 PAGETITLE=
a 0 s 0:13 0 0 0 hln 100 PAGENO=1
a 0 s 0:13 0 0 0 hln 100 PAGESIZE=A
a 0 s 0:13 0 0 0 hln 100 PAGECOUNT=1
@graphics
