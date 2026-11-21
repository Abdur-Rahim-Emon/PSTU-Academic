*version 9.1 1070209927
u 27
Q? 2
@libraries
@analysis
.DC 1 1 2 2 2 1
+ 0 0 IB
+ 0 4 100u
+ 0 5 1m
+ 0 6 20
+ 1 0 IB
+ 1 4 1
+ 1 5 25
+ 1 6 10
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
pageloc 1 0 1440 
@status
n 0 125:00:20:15:36:25;1737365785 e 
s 2832 125:00:20:15:36:29;1737365789 e 
*page 1 0 970 720 iA
@ports
port 26 GND_EARTH 490 360 h
@parts
part 23 idc 370 300 u
a 0 sp 11 0 0 50 hln 100 PART=idc
a 0 x 0:13 0 0 0 hln 100 PKGREF=IB
a 1 xp 9 0 20 10 hcn 100 REFDES=IB
part 24 Q2N2222 470 230 h
a 0 sp 11 0 25 40 hln 100 PART=Q2N2222
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=TO-18
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 ap 9 0 5 5 hln 100 REFDES=Q1
a 0 a 0:13 0 0 0 hln 100 PKGREF=Q1
part 25 VDC 620 260 h
a 0 sp 0 0 22 37 hln 100 PART=VDC
a 0 x 0:13 0 0 0 hln 100 PKGREF=Vce
a 1 xp 9 0 24 7 hcn 100 REFDES=Vce
a 1 u 13 0 -11 18 hcn 100 DC=5V
part 1 titleblk 970 720 h
a 1 s 13 0 350 10 hcn 100 PAGESIZE=A
a 1 s 13 0 180 60 hcn 100 PAGETITLE=
a 1 s 13 0 300 95 hrn 100 PAGENO=1
a 1 s 13 0 340 95 hrn 100 PAGECOUNT=1
@conn
w 3
s 370 260 370 230 2
s 470 230 370 230 4
a 0 up 33 0 420 229 hct 100 V=
w 7
s 370 300 370 360 6
s 370 360 490 360 10
a 0 up 33 0 555 359 hct 100 V=
s 620 360 620 300 12
s 490 360 620 360 16
s 490 250 490 360 14
w 18
s 490 210 490 130 17
s 490 130 620 130 19
s 620 130 620 260 21
a 0 up 33 0 622 195 hlt 100 V=
@junction
j 490 360
+ w 7
+ w 7
j 370 260
+ p 23 -
+ w 3
j 370 300
+ p 23 +
+ w 7
j 470 230
+ p 24 b
+ w 3
j 490 250
+ p 24 e
+ w 7
j 490 210
+ p 24 c
+ w 18
j 620 300
+ p 25 -
+ w 7
j 620 260
+ p 25 +
+ w 18
j 490 360
+ s 26
+ w 7
@attributes
a 0 s 0:13 0 0 0 hln 100 PAGETITLE=
a 0 s 0:13 0 0 0 hln 100 PAGENO=1
a 0 s 0:13 0 0 0 hln 100 PAGESIZE=A
a 0 s 0:13 0 0 0 hln 100 PAGECOUNT=1
@graphics
