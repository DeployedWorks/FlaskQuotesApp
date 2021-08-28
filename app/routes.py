from flask import render_template, request, flash, url_for, redirect, get_flashed_messages
from .models import Quotes
import datetime
from app import app, db

@app.route('/')
@app.route('/home')
def home():
    quotes = Quotes.query.all()
    quotes_ids = []
    quotes_texts = []
    quotes_bys = []
    data={                
        'qids' : '',
        'qts' : '',
        'qbs' : '',
    }
    if quotes is not []:
        for q in quotes:
            quotes_ids.append(q.quote_id)
            quotes_texts.append(q.quote_text)
            quotes_bys.append(q.quote_by)

            data = {
                'qids' : quotes_ids,
                'qts' : quotes_texts,
                'qbs' : quotes_bys,
            }
    return render_template('home.html', title='Home', data=data, n=len(quotes_ids))

@app.route('/submit', methods=['POST','GET'])
def submit():
    if request.method == 'GET':
        quote_id = 'qid'+str(datetime.datetime.now().timestamp()).split('.')[0][:5]+str(datetime.datetime.now().timestamp()).split('.')[1][:2]
        quote_text = request.args.get("quotetext", False)
        quote_by = request.args.get("quoteby", False)
        print("QT",quote_text)
        new_quote = Quotes(quote_id=quote_id, quote_text=quote_text, quote_by=quote_by)
        db.session.add(new_quote)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        flash('Not able to add new quote.')
        redirect(url_for('home'))
        