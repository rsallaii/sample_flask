# import necessary libraries
import os
from models import create_players, create_players_form
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pandas as pd

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite" # os.environ.get('DATABASE_URL', '') or

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

engine = db.get_engine(app)

Players = create_players(db)
PlayersForm = create_players_form(db)

# create route that renders index.html template
@app.route("/")
def home():    
    return render_template("index.html")


# Query the database and send the jsonified results
@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        print(request.form)
        season = request.form["season"]
        team = request.form["team"]
        player = request.form["player"]
        print(season)

        p = PlayersForm(Season=season,
                    Team=team,
                    Player=player)

        db.session.add(p)
        db.session.commit()

        return redirect("/", code=302)

    return render_template("index.html")


@app.route("/api/get_players_all")
def get_players_all():
    q = "Select * from PlayersForm"
    df = pd.read_sql_query(q, con=engine)
    
    print(df)

    return df.to_json(orient="records")


@app.route("/api/get_players_form")
def get_players_form():
    q = "Select * from PlayersForm order by id desc limit 1"
    df = pd.read_sql_query(q, con=engine)

    q2 = f'''
        Select * 
        from Players 
        where 1=1
        and Season = {df["Season"][0]} 
        and Team = {df["Team"][0]} 
        and Player = {df["Player"][0]}
    '''
    df2 = pd.read_sql_query(q2, con=engine)
    
    print(df2)

    return df2.to_json(orient="records")


if __name__ == "__main__":
    app.run(debug=True)
