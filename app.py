# app.py

# ======================================
# Import Dependencies
# ======================================
import numpy as np
import datetime as dt

from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

from flask import Flask, jsonify

# ======================================
# Database Setup
# ======================================
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(autoload_with=engine)

Measurement = Base.classes.measurement
Station = Base.classes.station

# ======================================
# Flask App Setup
# ======================================
app = Flask(__name__)

# ======================================
# Helper Function: Create DB session
# ======================================
def get_session():
    return Session(engine)

# ======================================
# Routes
# ======================================

@app.route("/")
def welcome():
    """List all available API routes."""
    return (
        f"<h2>Available API Routes</h2>"
        f"<ul>"
        f"<li>/api/v1.0/precipitation</li>"
        f"<li>/api/v1.0/stations</li>"
        f"<li>/api/v1.0/tobs</li>"
        f"<li>/api/v1.0/&lt;start&gt;</li>"
        f"<li>/api/v1.0/&lt;start&gt;/&lt;end&gt;</li>"
        f"</ul>"
        f"<p><strong>Date format:</strong> YYYY-MM-DD</p>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return precipitation data for the last 12 months."""
    session = get_session()
    last_date = dt.datetime(2017, 8, 23)
    one_year_ago = last_date - dt.timedelta(days=365)

    results = session.query(Measurement.date, Measurement.prcp)\
                     .filter(Measurement.date >= one_year_ago)\
                     .order_by(Measurement.date).all()
    session.close()

    data = [{ "date": date, "precip": prcp } for date, prcp in results]
    return jsonify(data)

@app.route("/api/v1.0/stations")
def stations():
    """Return list of all weather stations."""
    session = get_session()
    results = session.query(Station.station, Station.id).all()
    session.close()

    data = [{ "station": station, "id": id_ } for station, id_ in results]
    return jsonify(data)

@app.route("/api/v1.0/tobs")
def tobs():
    """Return temperature observations for the most active station over the past year."""
    session = get_session()
    one_year_ago = dt.datetime(2017, 8, 23) - dt.timedelta(days=365)

    most_active = session.query(Measurement.station)\
                         .group_by(Measurement.station)\
                         .order_by(func.count().desc())\
                         .first()[0]

    results = session.query(Measurement.date, Measurement.tobs)\
                     .filter(Measurement.station == most_active)\
                     .filter(Measurement.date >= one_year_ago).all()
    session.close()

    data = [{ "date": date, "tobs": tobs } for date, tobs in results]
    return jsonify(data)

@app.route("/api/v1.0/<start>")
def start_date(start):
    """Return min, max, and avg temps from start date to end of dataset."""
    session = get_session()
    results = session.query(
        func.min(Measurement.tobs),
        func.max(Measurement.tobs),
        func.avg(Measurement.tobs)
    ).filter(Measurement.date >= start).all()
    session.close()

    min_temp, max_temp, avg_temp = results[0]
    return jsonify({
        "start_date": start,
        "min_temp": min_temp,
        "max_temp": max_temp,
        "avg_temp": avg_temp
    })

@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    """Return min, max, and avg temps between given start and end dates."""
    session = get_session()
    results = session.query(
        func.min(Measurement.tobs),
        func.max(Measurement.tobs),
        func.avg(Measurement.tobs)
    ).filter(Measurement.date >= start)\
     .filter(Measurement.date <= end).all()
    session.close()

    min_temp, max_temp, avg_temp = results[0]
    return jsonify({
        "start_date": start,
        "end_date": end,
        "min_temp": min_temp,
        "max_temp": max_temp,
        "avg_temp": avg_temp
    })

# ======================================
# App Runner
# ======================================
if __name__ == "__main__":
    app.run(debug=False)
