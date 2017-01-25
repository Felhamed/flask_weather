from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "This is my first flask app!"

@app.route("/contact")
def contact():
	return "This is my contact page!"

@app.route("/employee/<id>")
def employee(id):
	print("Employee - ",type(id))
	return "I passed in {}".format(id)

@app.route("/blog/<int:id>")
def blog(id):
	print("Blog - ",type(id))
	return "I passed in an integer"
	
@app.route("/path/<path:values>")
def path(values):
	return "The entered path is {}".format(values)

if __name__ == "__main__":
	app.run(debug=True)