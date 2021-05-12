from flask_sqlalchemy import SQLAlchemy
from models import db
import uuid

def check_user_exists(model, email):
  item = model.query.filter_by(email=email).first()
  return item

def check_subscription(model, sub_id):
  item = model.query.filter_by(uuid=sub_id).first()
  return item

def create_item(model, **kwargs):
  item = model(**kwargs)
  db.session.add(item)
  commit_changes()
  # item = item.serialize

  item_res = {"item": item, "submitted": True}
  return item_res

def update_customer(model, **kwargs):
  item = model(**kwargs)
  for attr, updated_val in kwargs.items():
    if (updated_val):
      setattr(item, attr, updated_value)
  db.session.add(item)
  commit_changes()
  # item = item.serialize
  return item

def handle_create_gift(model, gifts):
  for gift in gifts:
    gift_id = uuid.uuid4()
    gifter_email = gift['gifter_email']
    recipient_email = gift['recipient_email']
    subscription_id = gift['subscription_id']
    item = model(uuid=gift_id, gifted_by=gifter_email, recipient_email=recipient_email, subscription_id=subscription_id)
    db.session.add(item)
    commit_changes()
  return True

def commit_changes():
  db.session.commit()