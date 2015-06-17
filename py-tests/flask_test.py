#intro to flask framework from website example!

from flask import Flask
from flask import render_template
app = Flask(__name__)

# this is the url
@app.route("/hi")
@app.route('/hello/<name>')

# fetch the variable from the url and point towards 'hello.html'
def hello(name=None):
	return render_template('bye.html', name=name)

if __name__ == "__main__":
	app.run()
