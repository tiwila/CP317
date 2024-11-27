from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from database import db, User, Concert,Seat  # Import your database module
import paypalrestsdk
import os
from dotenv import load_dotenv
from paypalrestsdk import configure

# Load the .env file
load_dotenv()

# Configure PayPal SDK with client ID and secret from .env
configure({
    "mode": "sandbox",  # Use "live" for production
    "client_id": os.getenv("PAYPAL_CLIENT_ID"),
    "client_secret": os.getenv("PAYPAL_CLIENT_SECRET")
})

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Replace with a secure key
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Johnathan81267@localhost/concert_management'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
paypalrestsdk.configure({
    "mode": "sandbox",  # "live" for production
    "client_id": os.getenv('PAYPAL_CLIENT_ID'),
    "client_secret": os.getenv('PAYPAL_CLIENT_SECRET')
})
def get_ticket_price(ticket_type):
    prices = {
        "VIP": 100.00,
        "Regular": 25.00
    }
    return prices.get(ticket_type, 0)

@app.route('/')
def home():
    return render_template('index.html')  # Home page

@app.route('/concerts')
def concerts():
    # Get the user role from session
    user_role = session.get('role', None)

    # Fetch all concerts from the database
    all_concerts = Concert.query.all()  

    # Render concerts for all users, with a specific view for organizers
    return render_template('concert.html', concerts=all_concerts, user_role=user_role)



@app.route('/feedback')
def feedback():
    return render_template('feedback.html')  # Render feedback template

@app.route('/contact')
def contact():
    return render_template('contact.html')  # Render contact template

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']  # Get role from the form

        # Check if the username or email already exists
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            flash('Username or email already exists. Please choose a different one.')
            return redirect(url_for('register'))

        # Create a new user and add it to the database
        new_user = User(username=username, email=email, password=generate_password_hash(password), role=role)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! You can now log in.')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id  # Store the user's ID in the session
            session['username'] = user.username  # Store username for display
            session['role'] = user.role  # Store the user's role

            return redirect(url_for('home'))  # Redirect to the home page instead of dashboard
        flash('Invalid username or password', 'error')

    return render_template('login.html')

@app.route('/profile')
def profile():
    user_id = session.get('user_id')
    user = User.query.get(user_id)
    return render_template('profile.html', user=user)

@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Remove the user ID from the session
    session.pop('role', None)  # Remove the user role from the session
    return redirect(url_for('home'))  # Redirect to the home page





@app.route('/organizer_form', methods=['GET'])
def organizer_form():
    user_id = session.get('user_id')
    user = User.query.get(user_id)

    if user and user.role == 'organizer':
        return render_template('organizer_form.html')  # Render organizer form
    return redirect(url_for('home'))  # Redirect to home if not an organizer




@app.route('/create_concert', methods=['GET', 'POST'])
def create_concert():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        date = request.form['date']
        location = request.form['location']
        vip_tickets = int(request.form['vip_tickets'])
        regular_tickets = int(request.form['regular_tickets'])

        # Assuming the user is already logged in and has an ID of 1
        organizer_id = 1  # Replace with dynamic value as needed

        # Create the concert object
        new_concert = Concert(
            name=name,
            date=date,
            location=location,
            vip_tickets=vip_tickets,
            regular_tickets=regular_tickets,
            organizer_id=organizer_id
        )

        # Add the concert to the session and commit it
        db.session.add(new_concert)
        db.session.commit()

        # Automatically create seats based on ticket numbers
        new_concert.create_seats()

        # Redirect back to the concert list page (or any other page)
        return redirect(url_for('home'))  # Replace 'home' with the appropriate route

    return render_template('create_concert.html')
@app.route('/submit_concert', methods=['GET', 'POST'])
def submit_concert():
    if request.method == 'POST':
        concert_name = request.form.get('name')
        concert_date = request.form.get('date')
        concert_location = request.form.get('location')

        # Get the number of tickets for each type
        vip_tickets = request.form.get('vip_tickets', type=int)  # Ensure it is an integer
        regular_tickets = request.form.get('regular_tickets', type=int)

        # Retrieve organizer_id from session (assuming the user is logged in and their ID is stored in session)
        organizer_id = session.get('user_id')  # Replace 'user_id' with the correct key based on your user session management

        if organizer_id is None:
            flash('You must be logged in to submit a concert!', 'error')
            return redirect(url_for('login'))  # Redirect to login or another appropriate page

        # Create a new concert entry in the database
        new_concert = Concert(
            name=concert_name,
            date=concert_date,
            location=concert_location,
            vip_tickets=vip_tickets,
            regular_tickets=regular_tickets,
            tickets_sold_vip=0,  # Initialize tickets sold
            tickets_sold_regular=0,
            organizer_id=organizer_id  # Set the organizer_id
        )

        # Add to the database session and commit
        db.session.add(new_concert)
        db.session.commit()
        new_concert.create_seats()
        flash('Concert submitted successfully!', 'success')
        return redirect(url_for('my_concerts'))  # Redirect to my_concerts instead of a non-existing route

    return render_template('organizer_form.html')
@app.route('/dashboard')
def dashboard():
    user_id = session.get('user_id')
    user = User.query.get(user_id)

    if user:
        return render_template('dashboard.html', user=user)  # Render the dashboard for the user
    return redirect(url_for('login'))  # Redirect to login if not authenticated

@app.route('/my_concerts')
def my_concerts():
    user_id = session.get('user_id')
    user = User.query.get(user_id)

    if user and user.role == 'organizer':
        concerts = Concert.query.filter_by(organizer_id=user.id).all()  # Get concerts organized by the user
        return render_template('submitted_concerts.html', concerts=concerts)  # Render submitted concerts page

    return redirect(url_for('home'))  # Redirect to home if not an organizer

@app.route('/delete_concert/<int:concert_id>', methods=['POST'])
def delete_concert(concert_id):
    user_id = session.get('user_id')
    concert_to_delete = Concert.query.get(concert_id)

    if concert_to_delete and concert_to_delete.organizer_id == user_id:  # Ensure the concert belongs to the user
        db.session.delete(concert_to_delete)
        db.session.commit()
        flash('Concert deleted successfully!')
    else:
        flash('Concert not found or you do not have permission to delete it.')

    return redirect(url_for('view_submitted_concerts'))  # Redirect back to the submitted concerts page

@app.route('/view_submitted_concerts')
def view_submitted_concerts():
    user_id = session.get('user_id')
    user = User.query.get(user_id)

    if user:
        concerts = Concert.query.filter_by(organizer_id=user.id).all()  # Fetch concerts submitted by the organizer
        return render_template('submitted_concerts.html', concerts=concerts)  # Render submitted concerts page

    return redirect(url_for('login'))  # Redirect to login if not authenticated

@app.route('/tickets/<int:concert_id>', methods=['GET', 'POST'])
def tickets(concert_id):
    # Check if the user is logged in and is an attendee
    user_role = session.get('role', None)
    if user_role != 'attendee':
        flash('You must be logged in as an attendee to purchase tickets.', 'error')
        return redirect(url_for('login'))  # Redirect non-attendees to the login page

    # Fetch the concert by ID
    concert = Concert.query.get_or_404(concert_id)

    if request.method == 'POST':
        ticket_type = request.form['ticket_type']  # This could be VIP or Regular
        available_seat = None

        # Check if tickets are available for the selected type
        if ticket_type == 'VIP':
            available_seat = Seat.query.filter_by(concert_id=concert_id, seat_type='VIP', status='available').first()
        elif ticket_type == 'Regular':
            available_seat = Seat.query.filter_by(concert_id=concert_id, seat_type='Regular', status='available').first()

        # Check if tickets are available for the selected type before proceeding to PayPal
        if available_seat:
            if ticket_type == 'VIP' and concert.vip_tickets > 0:
                return redirect(url_for('payment', concert_id=concert_id, ticket_type='VIP'))  # Redirect to PayPal payment
            elif ticket_type == 'Regular' and concert.regular_tickets > 0:
                return redirect(url_for('payment', concert_id=concert_id, ticket_type='Regular'))  # Redirect to PayPal payment
            else:
                flash('Sorry, no available tickets for that type or tickets are sold out.', 'error')
                return redirect(url_for('tickets', concert_id=concert_id))  # Redirect to ticket selection page
        else:
            flash('Sorry, no available seats for that type or tickets are sold out.', 'error')
            return redirect(url_for('tickets', concert_id=concert_id))  # Redirect to ticket selection page

    return render_template('tickets.html', concert=concert)



@app.route('/pay/<int:concert_id>/<string:ticket_type>', methods=['POST'])
def pay(concert_id, ticket_type):
    concert = Concert.query.get_or_404(concert_id)
    ticket_price = get_ticket_price(ticket_type)  # Define a function that gets the price based on ticket type
    
    # Check if ticket price is 0 and bypass PayPal if true
    if ticket_price == 0:
        # Mark the seat as purchased without PayPal
        available_seat = Seat.query.filter_by(concert_id=concert_id, seat_type=ticket_type, status='available').first()
        
        if available_seat:
            available_seat.status = 'purchased'
            db.session.commit()
            flash("Ticket has been successfully reserved for free!", 'success')
            return redirect(url_for('tickets', concert_id=concert_id))
        else:
            flash("No available seats for this ticket type.", 'error')
            return redirect(url_for('tickets', concert_id=concert_id))

    # Create PayPal payment object if ticket price is not 0
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"},
        "redirect_urls": {
            "return_url": url_for('payment_execute', concert_id=concert_id, ticket_type=ticket_type, _external=True),
            "cancel_url": url_for('payment_cancel', _external=True)},
        "transactions": [{
            "amount": {
                "total": str(ticket_price),
                "currency": "USD"},
            "description": f"{ticket_type} ticket for concert: {concert.name}"
        }]
    })

    if payment.create():
        for link in payment.links:
            if link.rel == "approval_url":
                return redirect(link.href)  # Redirect to PayPal approval URL
    else:
        flash("An error occurred with PayPal. Please try again later.", 'error')
        return redirect(url_for('tickets', concert_id=concert_id))


@app.route('/execute/<int:concert_id>/<string:ticket_type>', methods=['GET'])
def payment_execute(concert_id, ticket_type):
    payment_id = request.args.get('paymentId')
    payer_id = request.args.get('PayerID')
    
    payment = paypalrestsdk.Payment.find(payment_id)
    
    if payment.execute({"payer_id": payer_id}):
        # Mark the ticket as sold in your database
        available_seat = Seat.query.filter_by(concert_id=concert_id, seat_type=ticket_type, status='available').first()
        if available_seat:
            user_id = session.get('user_id')
            # Update the seat status to 'sold'
            available_seat.status = 'sold'
            available_seat.user_id = user_id
            # Get the concert
            concert = Concert.query.get(concert_id)
            if concert:
                # Update the tickets sold for the specific type
                if ticket_type == 'VIP':
                    concert.tickets_sold_vip += 1
                elif ticket_type == 'Regular':
                    concert.tickets_sold_regular += 1
                db.session.commit()  # Commit both the seat update and concert update
            flash('Payment successful! Your ticket has been purchased.', 'success')
        else:
            flash('No available seats for that ticket type.', 'error')
        return redirect(url_for('concerts'))
    else:
        flash('Payment failed.', 'error')
        return redirect(url_for('tickets', concert_id=concert_id))

@app.route('/cancel')
def payment_cancel():
    flash('Payment canceled.', 'warning')
    return redirect(url_for('concerts'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist
    app.run(debug=True)  # Run the Flask app
     
