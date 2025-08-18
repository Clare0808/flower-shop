from database import db

class Review(db.Model):
    __tablename__ = 'review'
    
    review_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    img = db.Column(db.Text, nullable=False)
    date = db.Column(db.Text, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Review {self.review_id}>'