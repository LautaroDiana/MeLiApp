from flask import Flask, jsonify, request
from mutant import *

app = Flask(__name__)

@app.route('/')
def home():
	return "Meli Application - Lautaro Diana", 200

@app.route('/mutant', methods = ['POST'])
def mutant_post():
	dna = request.get_json()
	dna = dna['dna']
	# return str(is_mutant(dna))
	output = is_mutant(dna)
	if output == True:
		return "Success", 200
	else:
		return "Failed", 403

if __name__ == '__main__':
	app.run(debug=True)