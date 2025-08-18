from database import db

class Cart(db.Model):
    __tablename__ = 'cart'
    
    cart_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False)
    price = db.Column(db.Text, nullable=False)
    img = db.Column(db.Text, nullable=False)
    quantity = db.Column(db.Text, nullable=False)
    total = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Cart {self.cart_id}>'