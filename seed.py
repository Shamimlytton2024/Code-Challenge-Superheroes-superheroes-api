from app import app
from models import db, Hero, Power

with app.app_context():
    db.drop_all()
    db.create_all()

    h1 = Hero(name="Kamala Khan", super_name="Ms. Marvel")
    h2 = Hero(name="Doreen Green", super_name="Squirrel Girl")
    h3 = Hero(name="Gwen Stacy", super_name="Spider-Gwen")

    p1 = Power(name="super strength", description="gives the wielder super-human strengths")
    p2 = Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed")

    db.session.add_all([h1, h2, h3, p1, p2])
    db.session.commit()
