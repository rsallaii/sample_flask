def create_players_form(db):

    class PlayersForm(db.Model):
        __tablename__ = 'PlayersForm'

        id = db.Column(db.Integer, primary_key=True)
        Season = db.Column(db.String)
        Team = db.Column(db.String)
        Player = db.Column(db.String)

    return PlayersForm

def create_players(db):

    class Players(db.Model):
        __tablename__ = 'Players'

        id = db.Column(db.Integer, primary_key=True)
        Season = db.Column(db.String)
        Team = db.Column(db.String)
        Player = db.Column(db.String)

    return Players
