from flask import Flask , render_template
app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("main-page.html")

@app.route("/main-page.html")
def HomeA():
    return render_template("main-page.html")

@app.route("/FAQ.html")
def Faq():
    return render_template("FAQ.html")

@app.route("/About-Us.html")
def About():
    return render_template("About-Us.html")


if __name__ == "__main__" :
  app.run(debug=True , port=9000)
