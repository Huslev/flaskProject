from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():  # put application's code here
    return render_template("index.html")

@app.route('/')
@app.route('/mainpage')
def mainpage():  # put application's code here
    return render_template("home.html")

@app.route('/')
@app.route('/action')
def actionpage():  # put application's code here
    return render_template("action.html")

@app.route('/')
@app.route('/bees_stat')
def beespage():  # put application's code here
    return render_template("bees_stat.html")

@app.route('/')
@app.route('/product_status')
def productpage():  # put application's code here
    return render_template("product_status.html")


@app.route('/')
@app.route('/documents')
def documentpage():  # put application's code here
    return render_template("documents.html")

@app.route('/')
@app.route('/documents')
def abautpage():  # put application's code here
    return render_template("documents.html")


if __name__ == '__main__':
    app.run()
