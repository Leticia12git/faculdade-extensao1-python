from flask import render_template, request, redirect, url_for
from app import app, db
from models import Donation

@app.route('/')
def index():
    donations = Donation.query.all()
    return render_template('index.html', donations=donations)

@app.route('/add', methods=['POST'])
def add_donation():
    item = request.form['item']
    quantity = request.form['quantity']
    donor = request.form['donor']
    
    new_donation = Donation(item=item, quantity=int(quantity), donor=donor)
    db.session.add(new_donation)
    db.session.commit()
    
    return redirect(url_for('index'))
