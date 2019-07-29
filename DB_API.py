# Paulo Vasconcelos
# paulobvasconcelos@gmail.com
# 2019 july

import sqlite3

class API:
	
	def __init__(self, pathToDatabase):
		self.connection = sqlite3.connect(pathToDatabase)

	def getBike(self, brand, model):
		cursor = self.connection.cursor()
		instances = cursor.execute("SELECT * FROM Bike WHERE brand=:brand AND model=:model", {"brand": brand, "model": model}).fetchall()
		if(len(instances)==0):
			print("WARNING - {} {} is not present in the database".format(brand, model))
			return
		valuesDict = {
			"brand":			instances[0][0],
			"model":			instances[0][1],
			"image":			instances[0][2],
			"price":			instances[0][3],
			"frame":			instances[0][4],
			"fork":				instances[0][5],
			"rearShock":		instances[0][6],
			"stem":				instances[0][7],
			"handlebars":		instances[0][8],
			"seatpost":			instances[0][9],
			"saddle":			instances[0][10],
			"brakes":			instances[0][11],
			"brakeLevers":		instances[0][12],
			"shifter":			instances[0][13],
			"frontDerailleur":	instances[0][14],
			"rearDerailleur":	instances[0][15],
			"cassette":			instances[0][16],
			"chain":			instances[0][17],
			"crank":			instances[0][18],
			"bottomBracket":	instances[0][19],
			"wheels":			instances[0][20],
			"hubs":				instances[0][21],
			"spokes":			instances[0][22],
			"rims":				instances[0][23],
			"tires":			instances[0][24],
			"wheelSize":		instances[0][25],
			"suspensionType":	instances[0][26],
			"drivetrain":		instances[0][27],
			"brakeType":		instances[0][28],
			"frameMaterial":	instances[0][29],
		}
		temp = cursor.execute("SELECT size FROM BikeSize WHERE brand=:brand AND model=:model", {"brand":instances[0][0], "model":instances[0][1]}).fetchall()
		sizes = []
		for size in temp:
			sizes.extend(size[0])
		valuesDict["sizes"]=sizes
		temp = cursor.execute("SELECT color FROM BikeColor WHERE brand=:brand AND model=:model", {"brand":instances[0][0], "model":instances[0][1]}).fetchall()
		colors = []
		for color in temp:
			colors.extend(color[0])
		valuesDict["colors"]=colors
		return valuesDict


	def getBikeImage(self, brand, model):
		cursor = self.connection.cursor()
		instances = cursor.execute("SELECT *,rowid FROM Bike WHERE brand=:brand AND model=:model", {"brand": brand, "model": model}).fetchall()
		if(len(instances)==0):
			print("WARNING - {} {} is not present in the database".format(brand, model))
		return instances[0][2]


	def insertBike(self, bike):
		cursor = self.connection.cursor()
		instances = cursor.execute("SELECT * FROM Bike WHERE brand=:brand AND model=:model", {"brand": bike.brand, "model": bike.model}).fetchall()
		if(len(instances)>0):
			print("WARNING - There is already an instance of this bike model in the database, do you wish to replace it? (Y/n)")
			answer = input("> ")
			if(answer=='n' or answer=='N'):
				return
			else:
				cursor.execute("DELETE FROM Bike WHERE brand=:brand AND model=:model", {"brand": bike.brand, "model": bike.model})
		insertionCommand =	"""INSERT INTO Bike VALUES (
								:brand,
								:model,
								:image,
								:price,
								:frame,
								:fork,
								:rearShock,

								-- Cockpit
								:stem,
								:handlebars,

								-- Seat
								:seatpost,
								:saddle,

								-- Brakes
								:brakes,
								:brakeLevers,

								-- Shifters and Derailleurs
								:shifter,
								:frontDerailleur,
								:rearDerailleur,

								-- Drivetrain
								:cassette,
								:chain,
								:crank,
								:bottomBracket,

								-- Wheels and Tires
								:wheels,
								:hubs,
								:spokes,
								:rims,
								:tires,

								-- Additional Fitlers
								:wheelSize,
								:suspensionType,
								:drivetrain,
								:brakeType,
								:frameMaterial)
								"""
		valuesDict = {
			"brand":			bike.brand,
			"model":			bike.model,
			"price":			bike.price,
			"image":			bike.image,
			"frame":			bike.frame,
			"fork":				bike.fork,
			"rearShock":		bike.rearShock,
			"stem":				bike.stem,
			"handlebars":		bike.handlebars,
			"seatpost":			bike.seatpost,
			"saddle":			bike.saddle,
			"brakes":			bike.brakes,
			"brakeLevers":		bike.brakeLevers,
			"shifter":			bike.shifter,
			"frontDerailleur":	bike.frontDerailleur,
			"rearDerailleur":	bike.rearDerailleur,
			"cassette":			bike.cassette,
			"chain":			bike.chain,
			"crank":			bike.crank,
			"bottomBracket":	bike.bottomBracket,
			"wheels":			bike.wheels,
			"hubs":				bike.hubs,
			"spokes":			bike.spokes,
			"rims":				bike.rims,
			"tires":			bike.tires,
			"wheelSize":		bike.wheelSize,
			"suspensionType":	bike.suspensionType,
			"drivetrain":		bike.drivetrain,
			"brakeType":		bike.brakeType,
			"frameMaterial":	bike.frameMaterial
		}
		cursor.execute(insertionCommand,valuesDict)
		bikeID = cursor.lastrowid

		# Size
		for size in bike.sizes:
			cursor.execute("INSERT INTO BikeSize VALUES (:brand,:model,:size)", {"brand":bike.brand, "model":bike.model, "size":size})

		# Color
		for color in bike.colors:
			cursor.execute("INSERT INTO BikeColor VALUES (:brand,:model,:color)", {"brand":bike.brand, "model":bike.model, "color":color})
		self.connection.commit()