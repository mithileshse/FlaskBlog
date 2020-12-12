from flask import Flask , render_template , url_for

app = Flask(__name__)

posts =[
		{
			"author" : "Mahesh",
			"title" : 'Blog Post 1',
			"content" : " Blog post content 1",
			"date_posted" : " April 21 , 2020"
		},
		{
			"author" : "Suresh",
			"title" : 'Blog Post 2',
			"content" : " Blog post content 2",
			"date_posted" : " Sep 29 , 2020"
		}
		] 

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return  render_template("about.html",title="about")


if __name__ == '__main__':	
	app.run(debug=True)