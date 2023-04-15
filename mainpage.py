from flask import Flask, render_template, url_for

mainpage = Flask(__name__)


@mainpage.route("/")
@mainpage.route("/mainpage")
def index():
	return render_template("mainpage.html")

@mainpage.route("/about")
def about():
	return render_template("about.html")

@mainpage.route("/user/<string:name>/<int:id>")
def user(name, id):
	return "User: " + name + "-" + str(id)

if __name__ == "__main__":
	mainpage.run(debug=True)