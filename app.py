from flask import Flask, jsonify, render_template, request, redirect, url_for
import paypalrestsdk
import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

app = Flask(__name__)

# PayPal Configuration
paypalrestsdk.configure({
    "mode": "sandbox",  # Change to "live" for real transactions
    "client_id": os.getenv("PAYPAL_CLIENT_ID"),
    "client_secret": os.getenv("PAYPAL_CLIENT_SECRET")
})

# Stripe Configuration
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

@app.route('/')
def home():
    return render_template('index.html')

# PayPal Payment Route
@app.route('/pay', methods=['POST'])
def pay():
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {"payment_method": "paypal"},
        "redirect_urls": {
            "return_url": url_for('payment_success', _external=True),
            "cancel_url": url_for('payment_cancel', _external=True),
        },
        "transactions": [{
            "amount": {"total": "100.00", "currency": "USD"},
            "description": "Payment for a product"
        }]
    })

    if payment.create():
        for link in payment.links:
            if link.rel == "approval_url":
                return redirect(link.href)
    return render_template('payment_cr.html')

# Stripe Checkout Session
@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {'name': 'Test Product'},
                    'unit_amount': 1000,  # Amount in cents (100.00 USD)
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=url_for('payment_success', _external=True),
            cancel_url=url_for('payment_cancel', _external=True),
        )
        return jsonify({'id': session.id})
    except Exception as e:
        return str(e), 400

# Handle Payment Success
@app.route('/success')
def payment_success():
    return render_template('payment_successful.html')

# Handle Payment Cancellation
@app.route('/cancel')
def payment_cancel():
    return render_template('payment_cancelled.html')

# Error handling & Display Payment Buttons on 404 Page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('page-404.html', stripe_public_key=os.getenv("STRIPE_PUBLIC_KEY"))

if __name__ == "__main__":
    app.run(debug=True)
