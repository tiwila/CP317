from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    
    concerts = db.relationship('Concert', back_populates='organizer', lazy=True)
    seats = db.relationship('Seat', back_populates='user', lazy=True)  # This links the User with their seats

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.String(50), nullable=False)
    comments = db.Column(db.Text, nullable=True)

class Seat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    seat_number = db.Column(db.String(20), nullable=False)
    seat_type = db.Column(db.String(20), nullable=False)
    concert_id = db.Column(db.Integer, db.ForeignKey('concert.id'), nullable=False)
    status = db.Column(db.String(50), default='available')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)  # ForeignKey reference to User model

    concert = db.relationship('Concert', back_populates='seats')
    user = db.relationship('User', back_populates='seats')
class Concert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    vip_tickets = db.Column(db.Integer, nullable=False, default=0)
    economy_tickets = db.Column(db.Integer, nullable=False, default=0)
    regular_tickets = db.Column(db.Integer, nullable=False, default=0)
    tickets_sold_vip = db.Column(db.Integer, nullable=False, default=0)
    tickets_sold_economy = db.Column(db.Integer, nullable=False, default=0)
    tickets_sold_regular = db.Column(db.Integer, nullable=False, default=0)
    organizer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    organizer = db.relationship('User', back_populates='concerts')
    seats = db.relationship('Seat', back_populates='concert', cascade='all, delete-orphan')

    def create_seats(self):
        # Generate seats based on ticket counts
        for i in range(1, self.vip_tickets + 1):
            seat = Seat(seat_number=f"VIP-{i}", seat_type="VIP", concert_id=self.id)
            db.session.add(seat)
        
        for i in range(1, self.economy_tickets + 1):
            seat = Seat(seat_number=f"ECO-{i}", seat_type="Economy", concert_id=self.id)
            db.session.add(seat)

        for i in range(1, self.regular_tickets + 1):
            seat = Seat(seat_number=f"REG-{i}", seat_type="Regular", concert_id=self.id)
            db.session.add(seat)

        db.session.commit()
    
