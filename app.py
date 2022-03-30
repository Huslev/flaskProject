from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")

@app.route('/homepage')
def homepage():  # put application's code here
    return render_template("home.html")


@app.route('/action')
def actionpage():  # put application's code here
    return render_template("action.html")


@app.route('/bees_stat')
def beespage():  # put application's code here
    return render_template("bees_stat.html")


@app.route('/product_status')
def productpage():  # put application's code here
    return render_template("product_status.html")


@app.route('/documents')
def documentpage():  # put application's code here
    return render_template("documents.html")

@app.route('/about')
def abautpage():  # put application's code here
    return render_template("about.html")


# Route for handling the login page logic
@app.route('/mainpage', methods=['GET', 'POST'])
def mainpage():
    error = None
    if request.method == 'POST':
        # print(request)
        # print(str(request.form))
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('homepage'))
    return render_template('index.html', error=error)


if __name__ == '__main__':
    app.run()
