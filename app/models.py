from app import db
import datetime

class User(db.Model):
    """Model for the users table"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.Text())
    lastname = db.Column(db.Text())
    email = db.Column(db.Text())
    password = db.Column(db.Text())


class Category(db.Model):
    """Model for the categories table"""
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    def __init__(self, title):
        """initialize with name."""
        self.title = title

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Category.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Category: {}>".format(self.title)


class Recipe(db.Model):
    """Model for recipe table"""
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    recipename = db.Column(db.Text())
    contents = db.Column(db.Text())
    instructions = db.Column(db.Text())
