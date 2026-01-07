from flask import flask, render_template

app = flask(__name__)

@app.route("/")
def inicio():
	return render_template("estatico.html")
	
if __name__ == "__main__":
	app.run(debug=True)
