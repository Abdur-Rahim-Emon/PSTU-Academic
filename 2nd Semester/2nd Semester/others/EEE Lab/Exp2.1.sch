*version 9.1 906663851
u 38
I? 2
Q? 3
V? 2
? 3
@libraries
@analysis
.AC 0 1 0
+0 101
+1 10
+2 1.00K
.DC 1 1 0 0 0 0
+ 0 0 Vce
+ 0 4 0
+ 0 5 10
+ 0 6 0.1
+ 1 0 IB
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
pageloc 1 0 1498 
@status
n 0 125:00:20:14:55:58;1737363358 e 
s 2832 125:00:21:09:03:37;1737428617 e 
c 125:00:20:14:55:55;1737363355
*page 1 0 970 720 iA
@ports
port 6 GND_EARTH 280 260 h
@parts
part 2 idc 160 200 u
a 0 sp 11 0 0 50 hln 100 PART=idc
a 0 x 0:13 0 0 0 hln 100 PKGREF=IB
a 1 xp 9 0 20 10 hcn 100 REFDES=IB
part 3 Q2N2222 260 130 h
a 0 sp 11 0 25 40 hln 100 PART=Q2N2222
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=TO-18
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=Q1
a 0 ap 9 0 5 5 hln 100 REFDES=Q1
part 5 VDC 410 160 h
a 0 sp 0 0 22 37 hln 100 PART=VDC
a 0 x 0:13 0 0 0 hln 100 PKGREF=Vce
a 1 xp 9 0 24 7 hcn 100 REFDES=Vce
a 1 u 13 0 -11 18 hcn 100 DC=0V
part 1 titleblk 970 720 h
a 1 s 13 0 350 10 hcn 100 PAGESIZE=A
a 1 s 13 0 180 60 hcn 100 PAGETITLE=
a 1 s 13 0 340 95 hrn 100 PAGECOUNT=1
a 1 s 13 0 300 95 hrn 100 PAGENO=1
@conn
w 25
a 0 up 0:33 0 0 0 hln 100 V=
s 160 160 160 130 7
s 260 130 160 130 20
a 0 up 33 0 210 129 hct 100 V=
w 14
a 0 up 0:33 0 0 0 hln 100 V=
s 160 200 160 260 13
s 160 260 280 260 15
s 280 260 410 260 17
a 0 up 33 0 345 259 hct 100 V=
s 410 260 410 200 18
s 280 150 280 260 32
w 27
a 0 up 0:33 0 0 0 hln 100 V=
s 280 110 280 30 26
s 280 30 410 30 28
s 410 30 410 160 30
a 0 up 33 0 412 95 hlt 100 V=
@junction
j 160 160
+ p 2 -
+ w 25
j 160 200
+ p 2 +
+ w 14
j 280 260
+ s 6
+ w 14
j 410 200
+ p 5 -
+ w 14
j 260 130
+ p 3 b
+ w 25
j 280 150
+ p 3 e
+ w 14
j 280 110
+ p 3 c
+ w 27
j 410 160
+ p 5 +
+ w 27
@attributes
a 0 s 0:13 0 0 0 hln 100 PAGETITLE=
a 0 s 0:13 0 0 0 hln 100 PAGENO=1
a 0 s 0:13 0 0 0 hln 100 PAGESIZE=A
a 0 s 0:13 0 0 0 hln 100 PAGECOUNT=1
@graphics
