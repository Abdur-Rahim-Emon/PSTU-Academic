*version 9.1 3747211633
u 63
D? 5
V? 2
R? 2
? 4
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
pageloc 1 0 2980 
@status
n 0 124:10:18:07:58:32;1731895112 e 
s 2832 125:00:21:12:48:06;1737442086 e 
*page 1 0 970 720 iA
@ports
port 44 GND_EARTH 470 240 h
@parts
part 2 D1N4002 410 150 v
a 0 sp 11 0 17 29 hln 100 PART=D1N4002
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=DO-41
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=D1
a 0 ap 9 0 17 4 hln 100 REFDES=D1
part 3 D1N4002 530 150 v
a 0 sp 11 0 17 29 hln 100 PART=D1N4002
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=DO-41
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=D2
a 0 ap 9 0 17 4 hln 100 REFDES=D2
part 46 r 690 180 d
a 0 sp 0 0 0 10 hlb 100 PART=r
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=RC05
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=R1
a 0 ap 9 0 15 0 hln 100 REFDES=R1
part 4 D1N4002 410 240 v
a 0 sp 11 0 17 29 hln 100 PART=D1N4002
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=DO-41
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=D3
a 0 ap 9 0 17 4 hln 100 REFDES=D3
part 5 D1N4002 530 240 v
a 0 sp 11 0 17 29 hln 100 PART=D1N4002
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=DO-41
a 0 s 0:13 0 0 0 hln 100 GATE=
a 0 a 0:13 0 0 0 hln 100 PKGREF=D4
a 0 ap 9 0 17 4 hln 100 REFDES=D4
part 37 vsin 180 160 h
a 0 a 0:13 0 0 0 hln 100 PKGREF=V1
a 1 ap 9 0 20 10 hcn 100 REFDES=V1
a 1 u 0 0 0 0 hcn 100 DC=0
a 1 u 0 0 0 0 hcn 100 AC=0
a 1 u 0 0 0 0 hcn 100 VOFF=0
a 1 u 0 0 0 0 hcn 100 VAMPL=20
a 1 u 0 0 0 0 hcn 100 FREQ=1k
part 1 titleblk 970 720 h
a 1 s 13 0 350 10 hcn 100 PAGESIZE=A
a 1 s 13 0 180 60 hcn 100 PAGETITLE=
a 1 s 13 0 340 95 hrn 100 PAGECOUNT=1
a 1 s 13 0 300 95 hrn 100 PAGENO=1
part 60 nodeMarker 690 100 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=1
part 61 nodeMarker 180 160 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=2
@conn
w 55
a 0 up 0:33 0 0 0 hln 100 V=
s 690 220 690 230 54
s 690 230 470 230 56
a 0 up 33 0 580 229 hct 100 V=
s 410 240 470 240 24
s 470 240 530 240 45
s 470 230 470 240 58
w 32
a 0 up 0:33 0 0 0 hln 100 V=
s 530 120 470 120 22
s 470 120 410 120 49
s 470 120 470 100 47
s 470 100 690 100 50
a 0 up 33 0 580 99 hct 100 V=
s 690 100 690 180 52
w 7
a 0 up 0:33 0 0 0 hln 100 V=
s 410 150 410 160 33
s 410 160 410 210 40
s 180 160 410 160 38
a 0 up 33 0 295 159 hct 100 V=
w 15
a 0 up 0:33 0 0 0 hln 100 V=
s 530 150 530 200 35
s 530 200 530 210 43
s 180 200 530 200 41
a 0 up 33 0 355 199 hct 100 V=
@junction
j 530 210
+ p 5 2
+ w 15
j 530 120
+ p 3 2
+ w 32
j 410 210
+ p 4 2
+ w 7
j 410 120
+ p 2 2
+ w 32
j 410 150
+ p 2 1
+ w 7
j 530 150
+ p 3 1
+ w 15
j 410 160
+ w 7
+ w 7
j 530 200
+ w 15
+ w 15
j 470 120
+ w 32
+ w 32
j 690 180
+ p 46 1
+ w 32
j 690 220
+ p 46 2
+ w 55
j 410 240
+ p 4 1
+ w 55
j 530 240
+ p 5 1
+ w 55
j 470 240
+ s 44
+ w 55
j 690 100
+ p 60 pin1
+ w 32
j 180 160
+ p 61 pin1
+ w 7
j 180 160
+ p 37 +
+ w 7
j 180 200
+ p 37 -
+ w 15
j 180 160
+ p 61 pin1
+ p 37 +
@attributes
a 0 s 0:13 0 0 0 hln 100 PAGETITLE=
a 0 s 0:13 0 0 0 hln 100 PAGENO=1
a 0 s 0:13 0 0 0 hln 100 PAGESIZE=A
a 0 s 0:13 0 0 0 hln 100 PAGECOUNT=1
@graphics
