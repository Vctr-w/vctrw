from flask import Flask, render_template, flash, redirect, session, url_for, request, g
import config

app = Flask(__name__)
app.config.from_object('config')

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
	return render_template('index.html', 
				title='Home')

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run()
