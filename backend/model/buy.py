from database import db

class Buy(db.Model):
    __tablename__ = 'buy'
    
    buy_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.Text, nullable=False)
    product = db.Column(db.Text, nullable=False)
    price = db.Column(db.Text, nullable=False)
    img = db.Column(db.Text, nullable=False)
    quantity = db.Column(db.Text, nullable=False)
    total = db.Column(db.Text, nullable=False)
    date = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Buy {self.buy_id}>'