*version 9.1 3997703397
u 41
R? 5
V? 2
Q? 4
@libraries
@analysis
.TEMP 1 27
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
pageloc 1 0 2315 
@status
n 0 125:00:20:17:08:01;1737371281 e 
s 2832 125:00:20:17:08:28;1737371308 e 
c 125:00:20:17:07:56;1737371276
*page 1 0 970 720 iA
@ports
port 33 GND_EARTH 590 210 h
port 6 GND_EARTH 430 300 h
@parts
part 7 VDC 590 170 h
a 0 sp 0 0 22 37 hln 100 PART=VDC
a 0 x 0:13 0 0 0 hln 100 PKGREF=VCC
a 1 xp 9 0 24 7 hcn 100 REFDES=VCC
a 1 u 13 0 -11 18 hcn 100 DC=10V
part 3 r 430 110 v
a 0 sp 0 0 0 10 hlb 100 PART=r
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=RC05
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 u 13 0 15 25 hln 100 VALUE=3.3K
a 0 x 0:13 0 0 0 hln 100 PKGREF=RC
a 0 xp 9 0 15 0 hln 100 REFDES=RC
part 5 r 280 260 v
a 0 sp 0 0 0 10 hlb 100 PART=r
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=RC05
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=R4
a 0 ap 9 0 15 0 hln 100 REFDES=R4
a 0 u 13 0 15 25 hln 100 VALUE=22K
part 2 r 280 150 v
a 0 sp 0 0 0 10 hlb 100 PART=r
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=RC05
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=R1
a 0 ap 9 0 15 0 hln 100 REFDES=R1
a 0 u 13 0 15 25 hln 100 VALUE=228K
part 40 Q2N3904 410 190 h
a 0 sp 11 0 25 40 hln 100 PART=Q2N3904
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=TO-92
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=Q3
a 0 ap 9 0 5 5 hln 100 REFDES=Q3
part 1 titleblk 970 720 h
a 1 s 13 0 350 10 hcn 100 PAGESIZE=A
a 1 s 13 0 180 60 hcn 100 PAGETITLE=
a 1 s 13 0 340 95 hrn 100 PAGECOUNT=1
a 1 s 13 0 300 95 hrn 100 PAGENO=1
@conn
w 10
a 0 up 0:33 0 0 0 hln 100 V=
s 280 110 280 70 9
s 280 70 430 70 11
s 430 70 590 70 29
a 0 up 33 0 510 69 hct 100 V=
s 590 70 590 170 31
w 18
a 0 up 0:33 0 0 0 hln 100 V=
s 280 150 280 190 17
s 280 190 280 220 36
s 280 190 410 190 34
a 0 up 33 0 345 189 hct 100 V=
w 26
a 0 up 0:33 0 0 0 hln 100 V=
s 280 260 280 300 19
s 280 300 430 300 21
a 0 up 33 0 355 299 hct 100 V=
s 430 210 430 300 38
a 0 up 33 0 432 220 hlt 100 V=
w 28
a 0 up 0:33 0 0 0 hln 100 V=
s 430 170 430 110 27
a 0 up 33 0 432 140 hlt 100 V=
@junction
j 280 110
+ p 2 2
+ w 10
j 430 70
+ p 3 2
+ w 10
j 280 150
+ p 2 1
+ w 18
j 280 220
+ p 5 2
+ w 18
j 430 110
+ p 3 1
+ w 28
j 590 170
+ p 7 +
+ w 10
j 590 210
+ s 33
+ p 7 -
j 280 190
+ w 18
+ w 18
j 280 260
+ p 5 1
+ w 26
j 430 300
+ s 6
+ w 26
j 410 190
+ p 40 b
+ w 18
j 430 210
+ p 40 e
+ w 26
j 430 170
+ p 40 c
+ w 28
@attributes
a 0 s 0:13 0 0 0 hln 100 PAGETITLE=
a 0 s 0:13 0 0 0 hln 100 PAGENO=1
a 0 s 0:13 0 0 0 hln 100 PAGESIZE=A
a 0 s 0:13 0 0 0 hln 100 PAGECOUNT=1
@graphics
