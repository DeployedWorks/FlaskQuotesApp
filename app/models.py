from app import db

class Quotes(db.Model):
    __tablename__ = 'quotes_table'

    # id = db.Column(db.Integer, primary_key=True)
    quote_id = db.Column(db.String(10), index=True, unique=True, primary_key=True)
    quote_text = db.Column(db.String(300), index=True)
    quote_by = db.Column(db.String(50), index=True)

    def __init__(self, quote_id, quote_text, quote_by):
        self.quote_id = quote_id
        self.quote_text = quote_text
        self.quote_by = quote_by

    def __repr__(self):
        return '<Quote id:{}. {} by {}>'.format(self.quote_id, self.quote_text, self.quote_by)