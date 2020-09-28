"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index2.html',
        title=['Police Records', 
               'Birth Certificalte',
               'Marriage Certificate',
               'Citizenship Certificate',
               'Family Status Certificate',
               'Residency Certificate', 
               'Tax code - Codice Fiscale (50)',
               'Companys certificates (70)',
               'Pledges and Liens certificate (70)',
               'Diploma and Academic certificates (80)',
               'Historical Research (160)', 
               'Others'
               ],
        year=datetime.now().year,
    )
