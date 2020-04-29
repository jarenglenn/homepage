from flask import Flask, render_template, url_for
from flask_assets import Environment, Bundle

app = Flask(__name__)

assets = Environment(app)
assets.url = app.static_url_path

scss = Bundle(
  'main.scss', 
  filters='pyscss', 
  output='css/main.css', 
  depends=("*.scss", "utilities/*.scss")) 

assets.register('scss_all', scss)

@app.route("/")
def home():
    return render_template("index.html")
