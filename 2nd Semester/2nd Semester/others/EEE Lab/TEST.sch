*version 9.1 670993205
u 24
V? 2
D? 2
R? 2
? 3
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
pageloc 1 0 1683 
@status
n 0 124:10:18:07:25:33;1731893133 e 
s 2832 124:10:18:07:25:38;1731893138 e 
*page 1 0 970 720 iA
@ports
port 22 GND_EARTH 450 300 h
@parts
part 3 D1N4002 450 130 h
a 0 sp 11 0 17 29 hln 100 PART=D1N4002
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=DO-41
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=D1
a 0 ap 9 0 17 4 hln 100 REFDES=D1
part 4 r 590 210 d
a 0 sp 0 0 0 10 hlb 100 PART=r
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=RC05
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=R1
a 0 ap 9 0 15 0 hln 100 REFDES=R1
part 2 vsin 330 200 h
a 0 a 0:13 0 0 0 hln 100 PKGREF=V1
a 1 ap 9 0 20 10 hcn 100 REFDES=V1
a 1 u 0 0 0 0 hcn 100 DC=0
a 1 u 0 0 0 0 hcn 100 AC=0
a 1 u 0 0 0 0 hcn 100 VOFF=0
a 1 u 0 0 0 0 hcn 100 VAMPL=20
a 1 u 0 0 0 0 hcn 100 FREQ=2k
part 1 titleblk 970 720 h
a 1 s 13 0 350 10 hcn 100 PAGESIZE=A
a 1 s 13 0 180 60 hcn 100 PAGETITLE=
a 1 s 13 0 300 95 hrn 100 PAGENO=1
a 1 s 13 0 340 95 hrn 100 PAGECOUNT=1
part 20 nodeMarker 330 130 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=1
part 21 nodeMarker 590 130 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=2
@conn
w 6
s 330 210 330 200 5
s 330 200 330 130 7
s 330 130 450 130 8
s 450 130 480 130 10
s 480 130 590 130 11
s 590 130 590 210 12
s 590 250 590 300 14
s 590 210 590 250 15
s 590 300 450 300 16
s 330 300 330 240 18
s 450 300 330 300 23
@junction
j 330 200
+ p 2 +
+ w 6
j 450 130
+ p 3 1
+ w 6
j 480 130
+ p 3 2
+ w 6
j 590 250
+ p 4 2
+ w 6
j 590 210
+ p 4 1
+ w 6
j 330 240
+ p 2 -
+ w 6
j 330 130
+ p 20 pin1
+ w 6
j 590 130
+ p 21 pin1
+ w 6
j 450 300
+ s 22
+ w 6
@attributes
a 0 s 0:13 0 0 0 hln 100 PAGETITLE=
a 0 s 0:13 0 0 0 hln 100 PAGENO=1
a 0 s 0:13 0 0 0 hln 100 PAGESIZE=A
a 0 s 0:13 0 0 0 hln 100 PAGECOUNT=1
@graphics
