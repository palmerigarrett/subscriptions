from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import cross_origin
from sqlalchemy import or_, asc, desc
import uuid
import string
import logging

from models import *
from db_funcs import *
from initialize import create_app

logging.basicConfig(level=logging.DEBUG)
app = create_app()

@app.route('/')
@app.route('/api/subscription', methods=['POST', 'PUT'])
def update_subscriptions():
  if (request.method == 'POST'):
    request_body = request.get_json()
    email = request_body.get('email')
    first_name = request_body.get('first_name')
    last_name = request_body.get('last_name')
    address_1 = request_body.get('address_1')
    address_2 = request_body.get('address_2')
    city = request_body.get('city')
    state = request_body.get('state')
    postal_code = request_body.get('postal_code')
    subscription_id = request_body.get('subscription_id')
    gifts = request_body.get('gifts')

    customer = check_user_exists(Customer, email)
    sub_exists = check_subscription(Subscription, subscription_id)
    if (customer):
      return jsonify({'error': 'Customer already exists.'})
    elif (not sub_exists):
      return jsonify({'error': 'Subscription selected does not exist.'})
    else:
      customer_id = uuid.uuid4()
      new_customer = create_item(Customer, email=email, first_name=first_name, last_name=last_name, address_1=address_1, address_2=address_2, city=city, state=state, postal_code=postal_code, uuid=customer_id, subscription_id=subscription_id)
      if (len(gifts) > 0):
        handled_gifts = handle_create_gift(Gift, gifts)
        if (not handled_gifts):
          return jsonify({"error": "There was an issue gifting subscriptions."}), 200
      return jsonify({"success": "New customer created successfully"}), 200

  if (request.method == 'PUT'):
    request_body = request.get_json()
    email = request_body.get('email')
    first_name = request_body.get('first_name')
    last_name = request_body.get('last_name')
    address_1 = request_body.get('address_1')
    address_2 = request_body.get('address_2')
    city = request_body.get('city')
    state = request_body.get('state')
    postal_code = request_body.get('postal_code')
    subscription_id = request_body.get('subscription_id')

    customer = check_user_exists(Customer, email)
    sub_exists = check_subscription(Subscription, subscription_id)
    if (not customer):
      return jsonify({'error': 'Customer does not exists.'})
    elif (not sub_exists):
      return jsonify({'error': 'Subscription selected does not exist.'})
    else:
      updated_customer = update_customer(Customer, email=email, first_name=first_name, last_name=last_name, address_1=address_1, address_2=address_2, city=city, state=state, subscription_id=subscription_id)
      return jsonify({"customer": updated_customer}), 200

@app.route('/api/gift', methods=['POST', 'PUT'])
def update_gifts():
  if (request.method == 'POST'):
    request_body = request.get_json()
    gifter_email = request_body.get('gifter_email')
    recipient_email = request_body.get('recipient_email')
    subscription_id = request_body.get('subscription_id')

    sub_exists = check_subscription(Subscription, subscription_id)
    if (not sub_exists):
      return jsonify({'error': 'Subscription selected does not exist.'})
    else:
      customer_id = uuid.uuid4()
      new_customer = create_item(Gift, gifter_email=gifter_email, recipient_email=recipient_email, subscription_id=subscription_id)
      return jsonify({"customer": new_customer}), 200

