from database import db

class Login(db.Model):
    __tablename__ = 'login'
    
    login_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Login {self.login_id}>'