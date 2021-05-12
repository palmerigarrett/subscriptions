from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Customer(db.Model):
  __tablename__ = 'customer'
  uuid = db.Column(db.String(50), primary_key=True, unique=True)
  email = db.Column(db.String(50), nullable=False, unique=True)
  first_name = db.Column(db.String(50), nullable=False)
  last_name = db.Column(db.String(50), nullable=False)
  address_1 = db.Column(db.String(50), nullable=False)
  address_2 = db.Column(db.String(50))
  city = db.Column(db.String(50), nullable=False)
  state = db.Column(db.String(2), nullable=False)
  postal_code = db.Column(db.String(5), nullable=False)
  subscription_id = db.Column(db.String(100), db.ForeignKey('subscription.uuid', onupdate="CASCADE", ondelete="SET NULL"),  nullable=True)

  def serialize(self):
    return {
      "email": self.email,
      "first_name": self.first_name,
      "last_name": self.last_name,
      "address_1": self.address_1,
      "address_2": self.address_2,
      "city": self.city,
      "state": self.state,
      "postal_code": self.postal_code,
      "subscription_id": self.subscription_id,
    }


class Subscription(db.Model):
  __tablename__ = 'subscription'
  uuid = db.Column(db.String(50), primary_key=True, unique=True)
  plan_name = db.Column(db.String(50), nullable=False)
  price = db.Column(db.String(5), nullable=False)

  gift = db.relationship("Gift", cascade="all, delete", passive_deletes=True)

class Gift(db.Model):
  __tablename__ = 'gift'
  uuid = db.Column(db.String(50), primary_key=True, unique=True)
  recipient_email = db.Column(db.String(50), nullable=False)
  subscription_id = db.Column(db.String(100), db.ForeignKey('subscription.uuid', onupdate="CASCADE", ondelete="SET NULL"),  nullable=True)
  gifted_by = db.Column(db.String(100), nullable=False)

  gifted_subscription = db.relationship("Subscription", back_populates="gift")

  def serialize(self):
    return {
      "recipient_email": self.recipient_email,
      "gifted_by": self.gifted_by,
      "last_name": self.last_name,
      "address_1": self.address_1,
    }