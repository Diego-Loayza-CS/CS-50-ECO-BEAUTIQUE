from flask_bootstrap import Bootstrap5
from flask import Flask, request, redirect, render_template
import json
import requests
import urllib.parse

app = Flask(__name__)

bootstrap = Bootstrap5(app)
title = "Ecolocation"

API = {
	'apiKey': 'RPEubPergx2M2VmDgKadX6iorC1Y7PN4IihZrf0Bn7Y',
}

@app.route('/')
def map():
	with open('./items.json') as items_file:
		item_list = json.load(items_file)['list']

	category = request.args.get('category')
	if category:
		filtered_list = [item for item in item_list if item['string'] == category]
	else:
		filtered_list = item_list

	return render_template("index.html", list=filtered_list, title=title)

@app.route('/api/places')
def get_places():
	latitude = request.args.get('latitude')
	longitude = request.args.get('longitude')
	query = request.args.get('query')
	radius = request.args.get('radius')

	# URL encode the query
	encoded_query = urllib.parse.quote(query)

	url = f"https://places.api.here.com/places/v1/discover/search?at={latitude},{longitude}&q={encoded_query}&radius={radius}&apiKey={API['apiKey']}"

	print("\nLA URL: " + url + "\n")

	response = requests.get(url)
	data = response.json()

	return data

@app.route('/map')
def map_page():
	return render_template("map.html", title=title)

@app.errorhandler(404)
def page_not_found(e):
	return redirect('/')

if __name__ == "__main__":
	app.run(debug=True)
