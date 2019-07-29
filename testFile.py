# Paulo Vasconcelos
# paulobvasconcelos@gmail.com
# 2019 july

# Test File

from DB_API import API
from Bike import Bike

api = API("database.db")

with open('bikeImages/Giant_Glory1.jpg', 'rb') as f:
	img = f.read()

giant_glory1 = Bike(
	"Giant",
	"Glory 1",
	img,
	4499.0,
	["S","M","L"],
	["Silver","Black","Metallic Green"],
	"ALUXX SL-Grade Aluminum",
	"DVO custom-tuned Onyx DC WC",
	"DVO custom-tuned Jade coil",
	"TruVativ Descendent, direct mount",
	"TruVativ Descendent DH, 800 x 35mm, 25mm rise",
	"Giant Contact SL, zero offset, 30.9mm",
	"Giant Contact (forward)",
	"SRAM Code R, [F] 200mm [R] 200mm, hydraulic disc",
	"SRAM Code R",
	"SRAM GX DH, 1x7",
	None,
	"SRAM GX DH",
	"SRAM XG795-DH, 10x24",
	"X11EL-1",
	"SRAM Descendant DH, 34",
	"SRAM GXP",
	None,
	"[F] Giant PDH 20mm thru axle Boost DH, sealed bearing [R] DT 240 12x150mm, sealed bearing",
	"DT",
	"DT Swiss EX 471, tubeless ready",
	"[F] Maxxis Minion DHF 27.5x2.5 WT, 60 tpi DW, 3C, TR DH [R] Maxxis Minion DHRII 27.5x2.4 WT, 60tpi DH, 3C, TR DH, tubeless",
	"27.5",
	"Front and Rear",
	"Rear Derailleur",
	"Disc",
	"Aluminum")

with open('bikeImages/Trek_TopFuel8.jpeg', 'rb') as f:
	img = f.read()

trek_topfuel8 = Bike(
	"Trek",
	"Top Fuel 8",
	img,
	2999.0,
	["S","M","M/L","L","XL","XXL"],
	["Matte Trek Black/Gloss Viper Red"],
	"Alpha Platinum Aluminium, tapered head tube, Knock Block, Control Freak internal routing, downtube guard, magnesium rocker link, Mino Link, ABP, Boost148, 115 mm travel",
	"RockShox Recon RL, Solo Air spring, Motion Control damper, TwistLoc remote, tapered steerer, 46 mm offset, Boost110, 15 mm Maxle Stealth, 120 mm travel",
	"Fox Performance Float, 2-position DPS damper, TwistLoc remote, tuned by Trek Suspension Lab, 190x45 mm",
	"Bontrager Rhythm Comp, Knock Block, 31.8 mm, 0-degree",
	"Bontrager Comp, alloy, 31.8 mm, 15mm rise",
	"Bontrager Line Dropper, 150 mm travel, internal routing, 31.6 mm",
	"Bontrager Arvada, steel rails",
	"Shimano hydraulic disc, MT500 caliper",
	"MT501 lever",
	"SRAM NX Eagle, 12-speed",
	None,
	"SRAM NX Eagle",
	"SRAM PG-1230 Eagle, 11-50, 12-speed",
	"SRAM NX Eagle, 12-speed",
	"SRAM NX Eagle, DUB, 32T steel ring, Boost",
	"SRAM DUB, 92 mm, PressFit",
	"Bontrager Kovee Comp 23, Tubeless Ready, 6-bolt, Boost110 front, Boost148 rear",
	"",
	"",
	"",
	"Bontrager XR3 Team Issue, Tubeless Ready, Inner Strength sidewall, aramid bead, 120 tpi, 29x2.40",
	"29",
	"Front and Rear",
	"Rear Derailleur",
	"Disc",
	"Aluminum")


# INSERT
api.insertBike(giant_glory1)
api.insertBike(trek_topfuel8)

# READ
api.getBike("Giant","Glory 1")