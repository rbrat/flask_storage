from flask import render_template, jsonify
from app import app, db


@app.errorhandler(400)
def bad_request(error):
    return jsonify(error=400, text=str(error)), 400

@app.errorhandler(404)
def not_found_error(error):
    return jsonify(error=404, text=str(error)), 404
