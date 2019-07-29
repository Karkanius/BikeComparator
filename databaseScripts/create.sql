CREATE TABLE Bike (
	-- General Info
	brand				TEXT,
	model				TEXT,
	price				REAL,
	image				BLOB,

	-- Frame and Suspension
	frame				TEXT,
	fork				TEXT,
	rear_shock			TEXT,

	-- Cockpit
	stem				TEXT,
	handlebars			TEXT,

	-- Seat
	seatpost			TEXT,
	saddle				TEXT,

	-- Brakes
	brakes				TEXT,
	brake_levers		TEXT,

	-- Shifters and Derailleurs
	shifter				TEXT,
	front_derailleur	TEXT,
	rear_derailleur		TEXT,

	-- Drivetrain
	cassette			TEXT,
	chain				TEXT,
	crank				TEXT,
	bottom_bracket		TEXT,

	-- Wheels and Tires
	wheels				TEXT,
	hubs				TEXT,
	spokes				TEXT,
	rims				TEXT,
	tires				TEXT,

	-- Additional Fitlers
	wheel_size			TEXT,
	suspension_type		TEXT,
	drivetrain			TEXT,
	brake_type			TEXT,
	frame_material		TEXT	
);

CREATE TABLE BikeSize (
	brand	TEXT,
	model	TEXT,
	size	TEXT
);

CREATE TABLE BikeColor (
	brand	TEXT,
	model	TEXT,
	color	TEXT
);