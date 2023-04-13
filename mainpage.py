from flask import Flask

mainpage = Flask(__name__)


@mainpage.route("/")
def index():
	return "hello world"



if __name__ == "__main__":
	mainpage.run(debug=True)