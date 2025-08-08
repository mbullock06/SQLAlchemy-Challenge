# 🌦️ SQLAlchemy Climate Analysis API & Data Visualization

This project analyzes historical climate data from Hawaii using Python, SQLAlchemy, and Flask. It includes:

- 📊 A Jupyter Notebook (`climate_cleaned.ipynb`) for exploratory data analysis and visualizations.
- 🔌 A Flask API (`app.py`) that serves precipitation, temperature, and station data from a SQLite database.

---

## 📁 Project Structure
├── Resources

├── hawaii.sqlite # SQLite database with climate & station data

├── app.py # Flask API for climate endpoints

├── climate_cleaned.ipynb # Jupyter Notebook for EDA and visualization

├── README.md # You're here!


---

## ⚙️ Technologies Used

- Python 3.8+
- Flask
- SQLAlchemy ORM
- SQLite
- Pandas
- Matplotlib
- Jupyter Notebook

---

## 📊 Climate Data Visualizations (`climate_cleaned.ipynb`)

- **Precipitation over the past 12 months**
- **Station activity overview**
- **Temperature distribution** from the most active station
- Uses Pandas and Matplotlib for clear, accessible plotting

📌 Run this notebook to explore and understand the raw climate data before building the API.

---

## 🔌 API Endpoints (`app.py`)

| Endpoint                          | Description |
|----------------------------------|-------------|
| `/`                              | Welcome message + list of routes |
| `/api/v1.0/precipitation`        | JSON of precipitation by date (last 12 months) |
| `/api/v1.0/stations`             | List of weather stations |
| `/api/v1.0/tobs`                 | Daily temps from the most active station (last 12 months) |
| `/api/v1.0/<start>`              | Min, Max, Avg temps from a start date |
| `/api/v1.0/<start>/<end>`        | Min, Max, Avg temps for a date range |

All date inputs must follow the format: `YYYY-MM-DD`

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/mbullock06/SQLAlchemy-Challenge.git
cd SQLAlchemy-Challenge
```

### 2. Set Up the Environment
```bash
pip install -r requirements.txt
```

### 3. Run the Flask API
```bash
python app.py
Open your browser to: http://localhost:5000
```

### 4. Run the Jupyter Notebook
```bash
jupyter notebook climate_cleaned.ipynb
```

---

📌 Sample API Output

Example: http://localhost:5000/api/v1.0/precipitation
```jsonc
[
  { "date": "2016-08-23", "precip": 0.00 },
  { "date": "2016-08-24", "precip": 0.08 },
  // ... more results
]
```

---

📄 License<br>
This project is for educational/demo purposes and is open for personal or professional portfolio use.

---

🙌 Acknowledgments & References

- Hawaii Climate Station (https://www.ncdc.noaa.gov/cdo-web/), via Vanderbilt Data Vizualization and Analysis Bootcamp

- Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, https://journals.ametsoc.org/view/journals/atot/29/7/jtech-d-11-00103_1.xml
