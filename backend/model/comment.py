from database import db

class Comment(db.Model):
    __tablename__ = 'comment'
    
    comment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    number = db.Column(db.Text, nullable=False)
    date = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Comment {self.comment_id}>'