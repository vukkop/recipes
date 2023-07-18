from flask_app import app, bcrypt
from flask import render_template,redirect,request,session
from flask_app.models.model_user import User

@app.route("/")
def index():
  if 'user_id' in session:
    return redirect("/recipes")
  return render_template("index.html")



