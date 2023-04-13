from flask import Flask

mainpage = Flask(__name__)


@mainpage.route("/")
@mainpage.route("/mainpage")
def index():
	return "Hello world"

@mainpage.route("/about")
def about():
	return "About"

@mainpage.route("/user/<string:name>/<int:id>")
def user(name, id):
	return "User: " + name + "-" + id

if __name__ == "__main__":
	mainpage.run(debug=True)