from flask import current_app as app
import json
from .scraper.scraper import data, retrieve_data

retrieve_data()

@app.route('/latest')
def latest():
    return json.dumps(data)