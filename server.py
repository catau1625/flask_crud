from flask import render_template
from __init__ import app
from controllers import usuarios

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)