*version 9.1 1737012298
u 139
Q? 6
I? 12
V? 4
? 5
@libraries
@analysis
.DC 1 1 0 0 0 0
+ 0 0 Vcb
+ 0 4 0
+ 0 5 10
+ 0 6 0.1
+ 1 0 IE
+ 1 4 0
+ 1 5 1m
+ 1 6 0.2m
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
pageloc 1 0 1487 
@status
n 0 125:00:20:19:06:21;1737378381 e 
s 2832 125:00:20:19:06:21;1737378381 e 
*page 1 0 970 720 iA
@ports
port 117 GND_EARTH 510 280 h
@parts
part 83 VDC 410 200 h
a 0 sp 0 0 22 37 hln 100 PART=VDC
a 0 x 0:13 0 0 0 hln 100 PKGREF=Vcb
a 1 xp 9 0 24 7 hcn 100 REFDES=Vcb
part 84 Q2N2222 510 210 v
a 0 sp 11 0 25 40 hln 100 PART=Q2N2222
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=TO-18
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=Q5
a 0 ap 9 0 5 5 hln 100 REFDES=Q5
part 138 idc 570 200 h
a 0 sp 11 0 0 50 hln 100 PART=idc
a 0 x 0:13 0 0 0 hln 100 PKGREF=IE
a 1 xp 9 0 20 10 hcn 100 REFDES=IE
part 1 titleblk 970 720 h
a 1 s 13 0 350 10 hcn 100 PAGESIZE=A
a 1 s 13 0 180 60 hcn 100 PAGETITLE=
a 1 s 13 0 340 95 hrn 100 PAGECOUNT=1
a 1 s 13 0 300 95 hrn 100 PAGENO=1
@conn
w 110
a 0 up 0:33 0 0 0 hln 100 V=
s 490 190 410 190 109
a 0 up 33 0 450 189 hct 100 V=
s 410 190 410 200 111
w 114
a 0 up 0:33 0 0 0 hln 100 V=
s 410 240 410 280 113
s 510 280 510 210 107
s 410 280 510 280 115
a 0 up 33 0 460 279 hct 100 V=
s 570 280 510 280 105
s 570 240 570 280 128
w 129
a 0 up 0:33 0 0 0 hln 100 V=
s 570 190 570 200 101
s 530 190 570 190 99
a 0 up 33 0 550 189 hct 100 V=
@junction
j 490 190
+ p 84 c
+ w 110
j 510 210
+ p 84 b
+ w 114
j 510 280
+ s 117
+ w 114
j 410 200
+ p 83 +
+ w 110
j 410 240
+ p 83 -
+ w 114
j 530 190
+ p 84 e
+ w 129
j 570 240
+ p 138 -
+ w 114
j 570 200
+ p 138 +
+ w 129
@attributes
a 0 s 0:13 0 0 0 hln 100 PAGETITLE=
a 0 s 0:13 0 0 0 hln 100 PAGENO=1
a 0 s 0:13 0 0 0 hln 100 PAGESIZE=A
a 0 s 0:13 0 0 0 hln 100 PAGECOUNT=1
@graphics
