from database import db

class Like(db.Model):
    __tablename__ = 'like'
    
    like_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.Text, nullable=False)
    product = db.Column(db.Text, nullable=False)
    price = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Like {self.like_id}>'