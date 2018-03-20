import os
from flask import Flask, render_template
application = Flask(__name__)

@application.route("/")
def hello():
    return render_template("index.html")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    application.run('0.0.0.0', port=port, debug=os.environ.get('FLASK_DEBUG', False))