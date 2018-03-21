from . import db


class UserProfile(db.Model):
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    gender =  db.Column(db.String(1))
    email = db.Column(db.String(255), unique=True)
    location = db.Column(db.String(80))
    biography = db.Column(db.Text)
    photo = db.Column(db.String(255))
    userid = db.Column(db.Integer, primary_key=True, autoincrement=False)
    created_on = db.Column(db.String(80))



    def __init__(self, first_name, last_name, gender,email,location,biography,photo,userid,created_on):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.email = email
        self.location = location
        self.biography = biography
        self.photo = photo
        self.userid = userid
        self.created_on = created_on

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
