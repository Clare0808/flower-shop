from database import db

class User(db.Model):
    __tablename__ = 'user'
    
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    birthday = db.Column(db.Text, nullable=False)
    number = db.Column(db.Text, nullable=False)
    img = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<User {self.user_id}>'