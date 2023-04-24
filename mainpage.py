from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


mainpage = Flask(__name__)
mainpage.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
mainpage.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db = SQLAlchemy(mainpage)


class Article(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	intro = db.Column(db.String(300), nullable=False)
	text = db.Column(db.Text, nullable=False)
	date = db.Column(db.DateTime(300), default=datetime.utcnow)

	def __repr__(self):
		return "<Article %r>" %self.id


@mainpage.route("/")
@mainpage.route("/mainpage")
def index():
	return render_template("mainpage.html")

@mainpage.route("/about")
def about():
	return render_template("about.html")

@mainpage.route("/create-article", methods=["POST", "GET"])
#@mainpage.route("/create-article.html")
def create_article():
	if request.method == "POST":
		title = request.form["title"]
		intro = request.form["intro"]
		text = request.form["text"]

		article = Article(title=title, intro=intro, text=text)

		try:
			db.session.add(article)
			db.session.commit()
			return redirect("/")

		except:
			return "Error."
	else:
		return render_template("create-article.html")


@mainpage.route("/posts")
def posts():
	articles = Article.query.order_by(Article.date.desc()).all()
	return render_template("posts.html", articles=articles)


@mainpage.route("/posts/<int:id>")
def post_content(id):
	article = Article.query.get(id)
	return render_template("post-content.html", article=article)


@mainpage.route("/posts/<int:id>/del")
def post_del(id):
	article = Article.query.get_or_404(id)

	try:
		db.session.delete(article)
		db.session.commit()
		return redirect("/")
	except:
		return "Error."


@mainpage.route("/user/<string:name>/<int:id>")
def user(name, id):
	return "User: " + name + "-" + str(id)

if __name__ == "__main__":
	mainpage.run(debug=True)