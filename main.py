from flask import Flask, request, redirect, render_template
import json

app = Flask(__name__)
if __name__ == "__main__":
	app.run()

@app.route('/')
def map():
	with open('static/items.json') as items:
		list = json.load(items)['list']

	category = request.args.get('type')
	try:
		category
	except NameError:
		category = None

	if category == None:
		#index
		return render_template("inicio.html", list=list)

	else:
		#map
		return render_template("map.html", list=list, category=category)

@app.errorhandler(404)
def page_not_found(e):
  return redirect('/')
