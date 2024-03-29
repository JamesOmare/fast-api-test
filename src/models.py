from .database import Base
from sqlalchemy import Column, Integer, Boolean, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    username = Column(String(50), unique = True)
    email = Column(String(100), unique = True)
    password = Column(Text, nullable = False)
    is_staff = Column(Boolean, default = False)
    is_active = Column(Boolean, default = False)
    orders = relationship("Order", back_populates = 'user')

    def __repr__(self):
        return f"=> User {self.username}"

class Order(Base):

    ORDER_STATUSES = (
        ('PENDING', 'pending'),
        ('IN_TRANSIT', 'in-transit'),
        ('DELIVERED', 'delivered'),
    )

    PIZZA_SIZES = (
        ('SMALL', 'small'),
        ('MEDIUM', 'medium'),
        ('LARGE', 'large'),
        ('EXTRA-LARGE', 'extra-large')
    )

    __tablename__ = 'orders'
    id = Column(Integer, primary_key = True)
    quantity = Column(Integer, nullable = False)
    order_status = Column(ChoiceType(choices = ORDER_STATUSES), default = 'PENDING')
    pizza_size = Column(ChoiceType(choices = PIZZA_SIZES), default = 'SMALL')
    flavour = Column(String())
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates = 'orders')

    def __repr__(self):
        return f"=> order id: {self.id}"
