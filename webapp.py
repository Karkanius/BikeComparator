from DB_API import API
from flask import Flask, render_template, g, send_file
from io import BytesIO

app = Flask(__name__)
DATABASE = 'database.db'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/bike/<brand_model>')
def bike(brand_model):
	api = API(DATABASE)
	temp = brand_model.replace("_"," ")
	temp = temp.split("!", 1)
	brand = temp[0]
	model = temp[1]
	bikeDict = api.getBike(brand, model)
	return render_template('bike.html', bike = bikeDict)

@app.route('/bike/image/<brand_model>')
def bikeimage(brand_model):
	api = API(DATABASE)
	temp = brand_model.replace("_"," ")
	temp = temp.split("!", 1)
	brand = temp[0]
	model = temp[1]
	bikename = brand+" "+model
	image = api.getBikeImage(brand, model)
	return send_file(BytesIO(image), attachment_filename=bikename, as_attachment=True)

if __name__ == '__main__':
	app.run(debug = True)